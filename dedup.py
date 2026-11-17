#!/usr/bin/env python3
from __future__ import annotations

"""
Moodle HTML mentések deduplikálója.
Használat:
  1. Tedd a lementett .html oldalakat az `input_html/` mappába (almappákban is lehet).
  2. Futtasd: python3 dedup.py
"""

import hashlib
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input_html"
OUT_JSON = BASE_DIR / "osszes_egyedi_kerdes.json"
OUT_MD = BASE_DIR / "osszes_egyedi_kerdes.md"
OUT_HTML = BASE_DIR / "osszes_egyedi_kerdes.html"


def clean_text(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def strip_option_prefix(text: str) -> str:
    return re.sub(r"^[a-dA-D]\.\s*", "", text).strip()


class MoodleParser(HTMLParser):
    """Kinyeri a Moodle .que blokkokból a kérdés szövegét és a válaszlehetőségeket."""

    def __init__(self) -> None:
        super().__init__()
        self.questions = []
        self._in_que = False
        self._que_depth = 0
        self._in_qtext = False
        self._qtext_depth = 0
        self._in_answer = False
        self._answer_depth = 0
        self._in_opt = False
        self._opt_depth = 0
        self._current_qtext = []
        self._current_opts = []
        self._current_opt_buf = []
        self._skip_tags = {"script", "style"}
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in self._skip_tags:
            self._skip_depth += 1
            return
        if self._skip_depth > 0:
            return

        attr_dict = dict(attrs)
        classes = set((attr_dict.get("class") or "").split())

        if tag == "div" and "que" in classes and not self._in_que:
            self._in_que = True
            self._que_depth = 1
            self._current_qtext = []
            self._current_opts = []
            return

        if not self._in_que:
            return

        if tag == "div":
            self._que_depth += 1

        if tag == "div" and "qtext" in classes and not self._in_qtext:
            self._in_qtext = True
            self._qtext_depth = 1
            return

        if self._in_qtext:
            if tag == "div":
                self._qtext_depth += 1
            return

        if tag == "div" and "answer" in classes and not self._in_answer:
            self._in_answer = True
            self._answer_depth = 1
            return

        if self._in_answer:
            if tag == "div":
                self._answer_depth += 1
            if (tag == "div" and ("r0" in classes or "r1" in classes)) or tag == "label":
                if not self._in_opt:
                    self._in_opt = True
                    self._opt_depth = 1
                    self._current_opt_buf = []
                    return
            if self._in_opt and tag in ("div", "label"):
                self._opt_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in self._skip_tags:
            self._skip_depth = max(0, self._skip_depth - 1)
            return
        if self._skip_depth > 0 or not self._in_que:
            return

        if self._in_qtext:
            if tag == "div":
                self._qtext_depth -= 1
                if self._qtext_depth == 0:
                    self._in_qtext = False

        if self._in_opt:
            if tag in ("div", "label"):
                self._opt_depth -= 1
                if self._opt_depth == 0:
                    opt_txt = clean_text("".join(self._current_opt_buf))
                    opt_txt = strip_option_prefix(opt_txt)
                    if opt_txt and opt_txt.lower() != "clear my choice":
                        self._current_opts.append(opt_txt)
                    self._in_opt = False

        if self._in_answer and tag == "div":
            self._answer_depth -= 1
            if self._answer_depth == 0:
                self._in_answer = False

        if tag == "div":
            self._que_depth -= 1
            if self._que_depth == 0:
                qtext = clean_text("".join(self._current_qtext))
                if qtext:
                    self.questions.append(
                        {
                            "question": qtext,
                            "options": self._current_opts,
                        }
                    )
                self._in_que = False

    def handle_data(self, data: str) -> None:
        if self._skip_depth > 0 or not self._in_que:
            return
        if self._in_qtext:
            self._current_qtext.append(data)
        elif self._in_opt:
            self._current_opt_buf.append(data)


def question_key(question: str) -> str:
    """Egyedi azonosító kulcs a kérdés szövege alapján."""
    return hashlib.sha256(question.lower().encode("utf-8")).hexdigest()[:16]


def load_existing_questions(json_path: Path) -> dict[str, dict]:
    """Betölti a korábban elmentett egyedi kérdéseket a JSON fájlból."""
    if not json_path.exists():
        return {}
    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}

    unique: dict[str, dict] = {}
    for item in data.get("questions", []):
        qtext = item.get("question")
        if not qtext:
            continue
        key = question_key(qtext)
        if key not in unique:
            unique[key] = {
                "id": item.get("id", len(unique) + 1),
                "question": qtext,
                "options": list(item.get("options", [])),
                "sources": list(item.get("sources", [])),
            }
    return unique


def main() -> None:
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    html_files = sorted(
        list(INPUT_DIR.rglob("*.html")) + list(INPUT_DIR.rglob("*.htm"))
    )

    unique = load_existing_questions(OUT_JSON)
    existing_count = len(unique)

    if not html_files:
        print(f"Nincs .html fájl itt: {INPUT_DIR}")
        if existing_count:
            print(f"A meglévő adatbázisban továbbra is {existing_count} db egyedi kérdés található.")
        print("Mentsd el a Moodle oldalakat (Cmd+S -> Webpage, HTML Only) ebbe a mappába, majd futtasd újra!")
        return

    total_seen = 0
    next_id = max((q["id"] for q in unique.values()), default=0) + 1

    for path in html_files:
        content = path.read_text(encoding="utf-8", errors="replace")
        parser = MoodleParser()
        parser.feed(content)
        for item in parser.questions:
            total_seen += 1
            key = question_key(item["question"])
            if key not in unique:
                unique[key] = {
                    "id": next_id,
                    "question": item["question"],
                    "options": item["options"],
                    "sources": [path.name],
                }
                next_id += 1
            else:
                if path.name not in unique[key]["sources"]:
                    unique[key]["sources"].append(path.name)

    items = list(unique.values())
    new_added = len(items) - existing_count

    OUT_JSON.write_text(
        json.dumps({"count": len(items), "questions": items}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    md_lines = [f"# Összegyűjtött egyedi kérdések ({len(items)} db)\n"]
    html_cards = []
    labels = ["a", "b", "c", "d", "e", "f"]

    for q in items:
        md_lines.append(f"**{q['id']}.** {q['question']}")
        opt_lis = []
        for idx, opt in enumerate(q["options"]):
            prefix = labels[idx] if idx < len(labels) else str(idx + 1)
            md_lines.append(f"- {prefix}. {opt}")
            opt_lis.append(f"<li><strong>{prefix}.</strong> {html.escape(opt)}</li>")
        md_lines.append("")
        html_cards.append(
            f"<article class='card'><h3>{q['id']}. kérdés</h3>"
            f"<p>{html.escape(q['question'])}</p>"
            f"<ul>{''.join(opt_lis)}</ul></article>"
        )

    OUT_MD.write_text("\n".join(md_lines), encoding="utf-8")

    html_doc = f"""<!DOCTYPE html>
<html lang="hu"><head><meta charset="UTF-8"><title>Egyedi kérdések ({len(items)})</title>
<style>
  @page {{ size: A4; margin: 14mm; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; line-height: 1.45; color: #111827; }}
  .card {{ border: 1px solid #d1d5db; border-radius: 6px; padding: 10px 12px; margin-bottom: 10px; break-inside: avoid; }}
  h3 {{ margin: 0 0 4px; color: #162a4d; font-size: 11pt; }}
  p {{ margin: 0 0 6px; font-weight: 500; }}
  ul {{ margin: 0; padding-left: 18px; }}
</style></head>
<body><h1>Összegyűjtött egyedi kérdések ({len(items)} db)</h1>{''.join(html_cards)}</body></html>"""
    OUT_HTML.write_text(html_doc, encoding="utf-8")

    pct_650 = round(len(items) / 650 * 100, 1)
    print(f"Feldolgozott HTML fájlok: {len(html_files)} db")
    print(f"Fájlokban talált kérdés:  {total_seen} db")
    print(f"Újonnan hozzáadott:       {new_added} db")
    print(f"Összes egyedi kérdés:     {len(items)} db (~{pct_650}% a 650-es bankból)")
    print(f"Kimenetek:\n  - {OUT_MD}\n  - {OUT_HTML}\n  - {OUT_JSON}")


if __name__ == "__main__":
    main()
