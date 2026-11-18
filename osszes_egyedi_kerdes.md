# Összegyűjtött egyedi kérdések (380 db)

**1.** Miért lehet félrevezető a napi átlagos válaszidő önmagában?
- a. Az átlagból közvetlenül meghatározható a gyökérok.
- b. Elfödheti a rövid csúcsokat vagy a felhasználók egy részének hosszú várakozását.
- c. Az átlagos válaszidő nem kapcsolódhat felhasználói tapasztalathoz.
- d. A válaszidő kizárólag a compute kihasználtságát jelenti.

**2.** Mit fejez ki az error budget?
- a. A következő kiadás automatikus engedélyét.
- b. A hibaelhárításra elkülönített pénzügyi keretet.
- c. A nem használt compute-kapacitás mennyiségét.
- d. Az SLO által megengedett eltérés keretét.

**3.** Egy háromrétegű portál webes felülete működik, de az adatlekérés sikertelen. A DNS és az útvonal helyes; az alkalmazási réteg nem érheti el az adatbázis célportját. Melyik beavatkozás a legszűkebb?
- a. Az adatbázis minden portjának internetes megnyitása.
- b. A webes belépési pont megszüntetése.
- c. A helyes DNS véletlenszerű módosítása.
- d. Az alkalmazási réteg → adatbázis szükséges portjának célzott engedélyezése.

**4.** Melyik következtetés helyes, ha két szolgáltató hasonló célú compute-szolgáltatást kínál?
- a. Közös döntési szempontok alkalmazhatók, de a hosting, integráció és felelősség külön ellenőrzendő.
- b. A szolgáltatásnevek alapján minden működési feltétel levezethető.
- c. A konfigurációk és jogosultságok változtatás nélkül felcserélhetők.
- d. A hasonló cél azonos költségmodellt bizonyít.

**5.** Egy webáruház cache-e kiesik. Az adatbázis működik, de korábban a legtöbb olvasást a cache szolgálta ki. A terv minden kérést korlátozás nélkül az adatbázisra irányítana. Melyik felülvizsgálat indokolt?
- a. A cache kiesése miatt az adatbázist is feltétlenül le kell állítani.
- b. Csak azt kell ellenőrizni, hogy a cache-szolgáltatás managed-e.
- c. A fallback adatút és a megnövekedő adatbázis-terhelés együtt vizsgálandó.
- d. A cache tartalmát kell hitelesnek nyilvánítani, elérhetőségtől függetlenül.

**6.** Egy vállalat legfeljebb négyórás szolgáltatáskimaradást fogad el. Melyik célérték kapcsolódik közvetlenül ehhez?
- a. RPO = 4 óra
- b. Mentési gyakoriság = 4 óra
- c. RTO = 4 óra
- d. Retention = 4 óra

**7.** Melyik megfogalmazás különíti el helyesen a cache-aside vezérlését és a konzisztenciagaranciát?
- a. Az alkalmazás vezérli az adatlekérést és feltöltést, de a minta önmagában nem garantál teljes konzisztenciát.
- b. Az adatbázis vezérli minden cache-bejegyzés frissítését, ezért invalidálás nem szükséges.
- c. A cache vezérli az adatlekérést, ezért az alkalmazás minden esetben a legfrissebb adatot kapja.
- d. Az alkalmazás csak cache hit esetén vesz részt, a TTL pedig tranzakciós konzisztenciát biztosít.

**8.** Egy autoscaling-szabály a terhelés változására reagál, de nincs meghatározva a végrehajtandó kapacitásművelet. Mi hiányzik a szabályból?
- a. A beavatkozás során végrehajtandó kapacitásváltozás
- b. A guest OS neve
- c. A forráskód programozási nyelve
- d. Az image tárolási helye

**9.** Miért fontos a measured service a gazdasági működésben?
- a. Kizárólag a hálózati sebességet méri
- b. Láthatóvá teszi a fogyasztást, ami támogatja az elszámolást és az elemzést
- c. Megszünteti a költségkeretek szükségességét
- d. Automatikusan ingyenessé teszi a szolgáltatást

**10.** Három spoke hálózat ugyanahhoz a hubhoz kapcsolódik, de az egyik spoke nem éri el a másikat. Melyik értelmezés indokolt?
- a. A spoke–spoke forgalom továbbítását és szabályait külön kell ellenőrizni.
- b. A hub minden esetben automatikusan továbbít.
- c. A spoke-ok csak publikus címen kapcsolódhatnak.
- d. A DNS automatikusan létrehozza a hiányzó útvonalat.

**11.** Melyik kifejezés jelöli a tervezett pénzügyi keretet?
- a. Forecast.
- b. Right-sizing.
- c. Budget.
- d. Tagging.

**12.** Egy csapat váratlan cloudköltség-növekedést észlel. Mi legyen az első vizsgálati lépés?
- a. A hálózati kapcsolat lekapcsolása
- b. Minden jogosultság megszüntetése
- c. A teljes naplózás törlése
- d. A fogyasztási adatok, futó erőforrások és skálázási szabályok áttekintése

**13.** Melyik fogalom jelöli a korábbi adatállapot visszaállítására szolgáló mentési képességet?
- a. Load balancing
- b. Autoscaling
- c. Backup
- d. Failover

**14.** Egy trace-ben az API a függőségi hívás befejezésére vár. Mi indokolja, hogy a két span időtartamát ne kezeljük független, összeadható szakaszként?
- a. A span időtartama kizárólag a CPU-futás ideje.
- b. A függőségi span minden esetben a hívó után kezdődik.
- c. A hívó időtartama tartalmazhatja a függő művelet idejét.
- d. A trace összes spanadata mindig egymást kizáró időszakot jelöl.

**15.** Egy szervezet csökkenteni akarja az üzemeltetési terhet, megtartani a kritikus adatok feletti kontrollt, és gyorsan fejleszteni új funkciókat. Mi a legjobb architekturális elv?
- a. A komponensek követelményei alapján kombinálni a megfelelő telepítési és szolgáltatási modelleket
- b. Minden komponenst azonos szolgáltató legmagasabb szintű szolgáltatására helyezni
- c. Az egész szervezet számára egyetlen modellt előírni
- d. A költséget és felelősségi határokat nem vizsgálni

**16.** Egy vállalat külön szeretné választani az éles és fejlesztési AWS-környezet erőforrásait, hozzáféréseit és költségeit. Melyik megoldás alkalmazza legjobban az előadásban bemutatott modellt?
- a. Az erőforrások azonos néven történő létrehozása
- b. Az összes erőforrás elhelyezése egyetlen Availability Zone-ban
- c. Külön AWS accountok használata
- d. Egyetlen közös ARN használata

**17.** Egy cache-aside olvasásnál az adat nincs a cache-ben. Melyik műveletsor felel meg a bemutatott mintának?
- a. A cache lekéri az adatbázist, az alkalmazás csak a végleges cache-értéket olvassa.
- b. Az alkalmazás lekéri az adatbázist, választ ad, és feltöltheti a cache-t.
- c. A kliens közvetlenül az adatbázistól kér választ, az alkalmazási réteg kihagyásával.
- d. Az alkalmazás megvárja a TTL lejáratát, amely automatikusan feltölti az adatot.

**18.** Egy Azure Blob-adatkörhöz archive osztályt és zónaredundanciát terveznek. Mi legyen a következő lépés?
- a. A kapacitás nullára csökkentése
- b. A konfiguráció automatikus elfogadása
- c. A tier és redundancia kombináció támogatottságának ellenőrzése
- d. A Blob Storage lecserélése VM-memóriára

**19.** Egy AWS privát subnetből kimenő IPv4-forgalmat terveznek. Melyik útvonal illik a bemutatott NAT-mintához?
- a. A DNS-rekord lesz az útvonaltábla.
- b. A Security Group hozza létre a NAT-szolgáltatást.
- c. A privát subnet útvonala a megfelelő publikus NAT Gateway felé mutat.
- d. Minden privát példány közvetlenül internet gateway felé kap publikus címet.

**20.** Egy kritikus alkalmazás több régióban fut, de minden régió ugyanattól az egyetlen identitáskomponenstől függ. Mi a következő tervezési feladat?
- a. Az identitáskomponens hibahatásának és redundanciájának vizsgálata
- b. A kapacitás végleges rögzítése
- c. A measured service kikapcsolása
- d. További alkalmazáspéldányok indítása ugyanazzal a függőséggel

**21.** Mire szolgál a Continuous Re-evaluation?
- a. A monitoring megszüntetésére
- b. A munkamenet hozzáférési feltételeinek megváltozott jelek alapján történő újraértékelésére
- c. Minden token korlátlan érvényesítésére
- d. Új Permissionök automatikus létrehozására

**22.** Egy Azure-ban futó alkalmazás tartós alkalmazássecret nélkül szeretne hozzáférni egy Azure-erőforráshoz. Melyik identitásmegoldás megfelelő?
- a. Anonymous Access
- b. Managed Identity
- c. AWS IAM Group
- d. Megosztott felhasználói jelszó

**23.** Egy nem compliant eszközről érkező munkamenetnél melyik lehet adaptív hozzáférési eredmény?
- a. Minden policy végleges törlése
- b. Automatikus adminisztrátori Permission
- c. Az eszközállapot figyelmen kívül hagyása
- d. Böngészőalapú megtekintés engedélyezése, letöltés blokkolása

**24.** Melyik állítás helyes a PaaS és a serverless kapcsolatáról?
- a. A PaaS nem feltétlenül serverless, a konkrét csomag feltételei számítanak.
- b. A serverless kizárólag saját kezelésű VM-et jelent.
- c. A két fogalom minden szolgáltatásnál azonos felelősségi határt ad.
- d. Minden PaaS-csomag kizárólag végrehajtásalapú számlázású.

**25.** Egy magasabb Azure governance-scope-on alkalmazott kontroll befolyásolhatja az alárendelt erőforrások földrajzi telepítési lehetőségeit, miközben maga a governance-hierarchia nem földrajzi struktúra.
- a. True
- b. False

**26.** Egy Pilot Light környezetben az adatbázis és a minimális infrastruktúra rendelkezésre áll, de a teljes alkalmazási kapacitás aktiválása hosszabb időt igényel. Melyik követelmény teljesülése kerülhet veszélybe?
- a. A mentések megőrzési ideje.
- b. A mentési fájlok tömörítési aránya.
- c. A snapshotok száma.
- d. A szolgáltatás RTO-célja.

**27.** Az Evidence egy kontroll kialakításának, működésének vagy ellenőrzésének visszakövethető bizonyítéka lehet.
- a. True
- b. False

**28.** Melyik azonosító kapcsolódik egy container image konkrét manifestjéhez, szemben egy később átállítható taggel?
- a. Digest
- b. Podnév
- c. Namespace
- d. VM-méret

**29.** Miért változhat meg egy AWS accountra alkalmazandó szervezeti kontrollok köre, ha az accountot másik Organizational Unitba helyezik?
- a. Mert az OU áthelyezése minden IAM-policy-t automatikusan töröl.
- b. Mert az account elveszíti az Account ID-ját.
- c. Mert az account az új OU hierarchiájában érvényesülő, örökölt policy-k hatálya alá kerülhet.
- d. Mert az account összes erőforrása automatikusan másik Regionbe kerül.

**30.** Melyik meghatározás különíti el helyesen az adatrezidenciát az adatszuverenitástól?
- a. A két fogalom minden esetben teljesen azonos jelentésű.
- b. Az adatrezidencia a hálózati késleltetést, az adatszuverenitás a szolgáltatás listaárát jelenti.
- c. Az adatrezidencia kizárólag Azure-, az adatszuverenitás kizárólag AWS-fogalom.
- d. Az adatrezidencia az adat földrajzi helyére, az adatszuverenitás az alkalmazható joghatóságra és állami kontrollokra is vonatkozik.

**31.** Melyik fogalom tartozik a futás közben alkalmazott Kubernetes-erőforráskorláthoz?
- a. Limit
- b. Request
- c. Registry
- d. Fault Domain

**32.** Egy Azure-rendszerben a forgalmat hálózati szinten több célhoz kell elosztani, egy másik rendszerben webes kérésjellemzők alapján kell irányítani. Melyik párosítás megfelelő?
- a. Private Endpoint, illetve NAT Gateway.
- b. Load Balancer, illetve Application Gateway.
- c. VNet, illetve subnet.
- d. NSG, illetve VNet-peering.

**33.** Egy platformjelölt várható futtatási díja kedvező, de nem ismert, hogy teljesíti-e a workload kötelező megfelelőségi követelményét. Hogyan használandó a döntési mátrix?
- a. A mátrixból a megfelelőségi sort törölni kell, mert nem futtatási szempont.
- b. A kedvező díj alapján a jelölt automatikusan megfelelő.
- c. A megfelelőségi cellát minden platformnál előre „igen”-re kell állítani.
- d. A konkrét követelményt és a jelölt tényleges képességeit előbb ellenőrizni kell; a költséget ezután lehet a többi szemponttal együtt mérlegelni.

**34.** Egy Azure-alkalmazás támogatott szolgáltatást Private Endpointon ér el. Mit kell a végpont mellett összehangolni?
- a. A privát névfeloldást.
- b. A webes load balancer célpéldányait.
- c. A publikus adatbázisportot.
- d. Az összes VNet automatikus peeringjét.

**35.** Egy vállalat alacsonyabb RTO-t szeretne, és vállalja a tartalék alkalmazáskörnyezet folyamatos működtetésének többletköltségét. Melyik DR-modell lehet megfelelőbb a kizárólag mentésből történő helyreállításnál?
- a. Warm Standby.
- b. Kizárólag lokális snapshot.
- c. Hosszabb backup retention.
- d. Ritkább teljes mentés.

**36.** Melyik mentéstípus tartalmazza az utolsó teljes mentés óta történt változásokat?
- a. Folyamatos replikáció
- b. Teljes mentés
- c. Inkrementális mentés
- d. Differenciális mentés

**37.** Miért nem bizonyít teljes biztonságot egy sikeres compliance-ellenőrzés?
- a. Mert a compliance kizárólag Authenticationt jelent
- b. Mert meghatározott követelményeket, Scope-ot, kontrollokat és időszakot értékel
- c. Mert a compliance minden biztonsági kontroll használatát tiltja
- d. Mert audit során nem használható Evidence

**38.** Egy compliant eszközről induló munkamenetben érzékeny adat exportja kezdődik, miközben magas identity risk jelenik meg. Melyik rendszerreakció megfelelő?
- a. Feltétel nélküli engedélyezés a korábbi bejelentkezés miatt
- b. Automatikus új Permission kiosztása
- c. A Risk figyelmen kívül hagyása a compliant eszköz miatt
- d. Újraértékelés, export-Permission ellenőrzése, további Authentication vagy munkamenet-korlátozás

**39.** Miért fontos a DR-próbán mért eredményeket a meghatározott üzleti célértékekhez viszonyítani?
- a. Mert az üzleti követelmények csak a teszt után határozhatók meg.
- b. Mert az RPO/RTO kizárólag dokumentációs mező, amelyet nem lehet mérni.
- c. Mert a DR-próba kizárólag a mentési fájlok épségét ellenőrzi.
- d. Mert a technikai siker nem bizonyítja automatikusan az üzletileg elfogadható helyreállítást.

**40.** Egy támogatott API PaaS-ra költözik. Melyik feladat marad biztosan releváns az ügyfél számára?
- a. Az alkalmazás konfigurációjának és hozzáféréseinek ellenőrzése
- b. A platform minden hostjának kézi frissítése
- c. Az összes infrastrukturális feladat átvétele
- d. A szolgáltató fizikai tápellátásának karbantartása

**41.** Mitől függ, hogy a felhasználó elérheti-e a webalkalmazást?
- a. A megfelelő belépési ponttól, útvonaltól és szabályoktól.
- b. Kizárólag a subnet nevétől.
- c. Attól, hogy minden réteg publikus IP-t kap.
- d. Kizárólag attól, hogy az adatbázis fut.

**42.** Melyik folyamat határozza meg, hogy egy igazolt identitás milyen műveletet hajthat végre?
- a. Encryption at Rest
- b. Authorization
- c. Threat Detection
- d. Authentication

**43.** Miért nem feltétlenül megfelelő egy hagyományos fájlszerver object storage-ra történő közvetlen cseréje?
- a. Mert az alkalmazás fájlrendszer-műveleteket várhat az objektum-API helyett
- b. Mert object storage nem használ hálózatot
- c. Mert object storage-ban nem lehet dokumentumot tárolni
- d. Mert a fájlszerver kizárólag memóriában működik

**44.** Egy szervezet speciális helyi integrációt tart meg, de globális analitikát public cloudban végez. Mi indokolja leginkább a kombinált megoldást?
- a. A cloudban nem lehet adatot tárolni
- b. Az, hogy minden szolgáltatási modell azonos
- c. Az on-premises mindig olcsóbb
- d. A komponensek eltérő késleltetési, integrációs és skálázási követelményei

**45.** Egy gyártó saját környezetben tartja a vezérlést, public cloudban futtat analitikát, és egy másik public szolgáltatónál AI-képességet használ. Hogyan jellemezhető a teljes környezet?
- a. Egyszerű on-premises hosting
- b. Kizárólag private cloud
- c. Kizárólag SaaS
- d. Egyszerre hybrid és multi-cloud

**46.** Melyik állítás jellemzi az aszinkron replikációt?
- a. A primer és a szekunder minden pillanatban garantáltan azonos
- b. Nem készül adatmásolat
- c. Csak ugyanazon memórián belül használható
- d. A szekunder másolat frissítése késhet a primerhez képest

**47.** Egy portál gyakran olvasott tájékoztató szövegeket cache-el. A tartalom időnként változik. Melyik kiegészítő feladat szükséges a gyorsítótár használatához?
- a. Az élettartam és az invalidálás megtervezése.
- b. Minden cache-bejegyzés korlátlan megőrzése.
- c. Minden olvasás írási tranzakcióvá alakítása.
- d. A hiteles adattár hozzáférésének megszüntetése.

**48.** Miért használhat ugyanazon a fizikai hoston két VM eltérő guest operációs rendszert?
- a. Mert mindkét VM közvetlenül átírja a fizikai processzor működését.
- b. Mert az operációs rendszer az image registryben fut.
- c. Mert a virtualizáció elkülönített virtuális hardverkörnyezetet biztosít számukra.
- d. Mert a két VM kötelezően ugyanazt a guest kernelt használja.

**49.** Melyik állítás írja le legpontosabban az AWS Organizations Root szerepét?
- a. Az AWS-erőforrások egyedi azonosítására szolgáló objektum.
- b. Az Organization accountjainak és Organizational Unitjainak legfelső konténere.
- c. Egy adott AWS account teljes hozzáférésű identitása.
- d. Egy AWS Region valamennyi Availability Zone-jának közös fizikai helyszíne.

**50.** Egy alkalmazásnak részletes Kubernetes-workloadkonfigurációra és közvetlen Kubernetes API-hozzáférésre van szüksége. A csapat menedzselt megoldást is vizsgál. Melyik kérdés dönti el legközvetlenebbül, hogy a jelölt platform alkalmas-e?
- a. Alacsonyabb-e a listaára minden más platforménál?
- b. Szerepel-e a szolgáltatás nevében a „cloud” szó?
- c. Biztosítja-e a szükséges Kubernetes-kontrollt, miközben világos, mely platform- és workloadfeladatok maradnak a csapatnál?
- d. Megszünteti-e automatikusan az alkalmazás adatkezelési felelősségét?

**51.** Egy rendszer 10 perces RPO-t követel meg. A backup 30 percenként készül, a replikáció viszont folyamatos. Melyik értékelési megközelítés helyes?
- a. A retention növelése önmagában biztosítja a 10 perces RPO-t.
- b. A folyamatos replikáció miatt az RPO minden hibamodellre automatikusan teljesül.
- c. A backup gyakorisága miatt az RPO biztosan teljesül.
- d. A releváns hibamodellben elérhető és visszaállítható adatállapotot kell ellenőrizni.

**52.** Egy vállalat public cloudban futtat ügyfélportált, saját adatközpontban gyártási rendszert, és a két környezet között adatkapcsolat működik. Melyik modell írja le ezt?
- a. Community cloud
- b. Kizárólag SaaS
- c. Kizárólag multi-cloud
- d. Hybrid cloud

**53.** Egy IaC-definíció alapján két környezetet telepítenek. A telepítés után az egyik környezetben hiányzik egy szükséges erőforráskapcsolat. Melyik eljárás felel meg a tanult modellnek?
- a. Az alkalmazás működését ellenőrzés nélkül megfelelőnek minősítik.
- b. Az IaC helyett kizárólag a container nevét változtatják meg.
- c. Összevetik a kívánt és a tényleges környezetet, feltárják az eltérést, majd a szükséges módosítás után újra ellenőriznek.
- d. A definíció létezését a tényleges kapcsolat bizonyítékának tekintik.

**54.** Miért nem teszi a kimenő internetkapcsolat automatikusan publikussá a privát szervert?
- a. Mert a NAT DNS-szolgáltatás.
- b. Mert minden internetes útvonal tiltott.
- c. Mert a szerver nem fogadhat választ.
- d. Mert a kifelé indított és a kívülről indított új kapcsolat különböző.

**55.** A sikeres mentések arányát ténylegesen megmérjük. Melyik fogalom alá tartozik ez a mérőszám?
- a. SLO.
- b. Error budget.
- c. SLI.
- d. SLA.

**56.** Egy kérés portálon, API-n és adatbázishíváson halad át. Melyik nézőpontot választanád az út összekapcsolásához?
- a. Budget.
- b. Trace.
- c. Költségcímke.
- d. SLA.

**57.** Miért nem automatikusan biztonságosabb minden customer-managed key konfiguráció?
- a. Mert megszünteti az audit lehetőségét
- b. Mert a nagyobb kontroll hibás kulcsjogosultság vagy kulcséletciklus esetén működési kockázatot is okozhat
- c. Mert a kulcs minden adatot publikussá tesz
- d. Mert a customer-managed key nem használható titkosításhoz

**58.** Egy háromrétegű alkalmazás webes oldala megnyílik, de az adatokat nem jeleníti meg. Melyik következtetés indokolt?
- a. Az adatbázist azonnal publikálni kell.
- b. A teljes alkalmazási út már igazolt.
- c. A DNS minden esetben hibás.
- d. A belső alkalmazás–adatbázis kapcsolatot is ellenőrizni kell.

**59.** Melyik megállapítás jellemzi legjobban a Fault Tolerance és a High Availability viszonyát?
- a. A Fault Tolerance meghatározott hibák mellett megszakításmentes működést céloz, ami szigorúbb követelmény lehet.
- b. A High Availability minden esetben nulla megszakítást garantál.
- c. A Fault Tolerance kizárólag mentési pontok megőrzését jelenti.
- d. A két fogalom között kizárólag a használt cloud szolgáltató jelent különbséget.

**60.** Két hibaarányt hasonlítasz össze. Melyik feltételt ellenőriznéd az értelmezéshez?
- a. Csak a hibás műveletek darabszámát, a teljes forgalom nélkül.
- b. A releváns műveletek definícióját és az időablakot.
- c. Csak az átlagos CPU-terhelést, a műveletdefiníció nélkül.
- d. Csak a napi összes forgalmat, az időablak egyeztetése nélkül.

**61.** Miben különbözik a subnetekre tagolás a hálózati forgalom tiltásától?
- a. A tagolás automatikusan minden portot lezár.
- b. A subnet csak publikus szolgáltatásokhoz használható.
- c. A tagolás önmagában nem bizonyítja, hogy a rétegek közötti forgalom tiltott.
- d. A tiltás kizárólag DNS-sel történik.

**62.** Miért nem tekinthető egy budgetriasztás általános költési plafonnak?
- a. A budget létrehozása automatikusan leállít minden erőforrást.
- b. A budget és a forecast ugyanazt jelenti.
- c. Az értesítéshez vagy művelethez konkrét platformbeállítás tartozik.
- d. A budgetriasztás csak a CPU-terhelést figyeli.

**63.** Melyik állítás írja le pontosan a telepítési és szolgáltatási modell kapcsolatát?
- a. Külön döntési dimenziók: az egyik a környezetet és irányítást, a másik a felelősségi rétegeket írja le
- b. A szolgáltatási modell csak a földrajzi helyet határozza meg
- c. A két fogalom azonos
- d. A telepítési modell kizárólag a számlázást írja le

**64.** Egy csapatnak egy VM súlyos tárolóhibája után elkülönítetten megőrzött másolatból kell adatokat helyreállítania. Melyik párosítás felel meg a feladatnak?
- a. Container tag és podcsere.
- b. VM-image és automatikus alkalmazáskód-javítás.
- c. Snapshot mint minden körülmények között független, hosszú távú mentés.
- d. Backup mint helyreállítási forrás, majd restore mint végrehajtott művelet.

**65.** Egy többzónás alkalmazás webes rétege működőképes marad zónakiesés után, de az adatbázis csak a kiesett zónában volt elérhető. Melyik tervezési hiányosság a meghatározó?
- a. A webes réteg nem használhat többzónás kialakítást.
- b. A mentések túl hosszú ideig maradnak meg.
- c. A webes réteg túl sok példányt használ.
- d. A kritikus adatréteg nem rendelkezik megfelelő zónaszintű védelemmel.

**66.** Két storage-jelölt kapacitásdíja hasonló, de egyiknél magasabb a műveleti és adatátviteli díj. Hogyan kell összehasonlítani őket?
- a. Kizárólag a szolgáltatás nevét összevetve
- b. Mindig a több funkciót tartalmazó terméket választva
- c. Csak a maximális kapacitást vizsgálva
- d. Azonos workloadra és megőrzési időre számított teljes költséggel

**67.** Melyik adatmodellben elsőrendű elemek a csomópontok és a közöttük lévő élek?
- a. Széles oszlopos modell.
- b. Dokumentummodell.
- c. Kulcs-érték modell.
- d. Gráfmodell.

**68.** Miért kell block storage esetén a VM és a lemez teljesítménykorlátait együtt vizsgálni?
- a. Mert bármelyik réteg szűk keresztmetszetté válhat
- b. Mert a lemeznek nincs saját teljesítményjellemzője
- c. Mert a két erőforrás mindig azonos kapacitású
- d. Mert a VM mérete minden esetben meghatározza a tárolt adatok formátumát

**69.** Egy VM kisebb konfigurációra vált, a példányok száma nem változik. Hogyan nevezzük ezt?
- a. Scale down
- b. Deployment
- c. Scale out
- d. Scale in

**70.** Miért nem elég egy helyes útvonal a működő kapcsolathoz?
- a. Mert csak publikus subnetben létezhet útvonal.
- b. Mert az útvonaltábla nem használ célcímet.
- c. Mert az útvonal mindig titkosítást igényel.
- d. Mert a szabályozás és a céloldali szolgáltatás állapota is számít.

**71.** Mit nevezünk forró partíciónak az előadás fogalmi modelljében?
- a. Olyan partíciót, amelyben kizárólag frissen létrehozott rekordok vannak.
- b. Olyan partíciót, amely több adatmodellt kezel egyszerre.
- c. Olyan partíciót, amelyre aránytalanul nagy kérésterhelés koncentrálódik.
- d. Olyan partíciót, amelynek adatait a cache már betöltötte.

**72.** Egy alkalmazás egyetlen Availability Zone-ban működik. Melyik módosítás csökkenti az adott zóna kiesésének kockázatát?
- a. Az alkalmazás több Availability Zone-ban történő telepítése
- b. Az alkalmazás átnevezése
- c. Az internetes cím hosszabbra módosítása
- d. Új számlázási fiók létrehozása

**73.** Miért nem elegendő a PostgreSQL motorvonal egyezése a migráció jóváhagyásához?
- a. Mert az azonos motorvonal minden esetben eltérő adatmodellt jelent.
- b. Mert a motorvonal csak a szolgáltatás hálózati végpontját határozza meg.
- c. Mert managed szolgáltatások között nincs lehetőség adatmozgatásra.
- d. Mert a verziók, bővítmények és alkalmazási viselkedés kompatibilitását is ellenőrizni kell.

**74.** Mit jelent a storage redundancia hibahatára?
- a. A titkosítási kulcs lejárati idejét
- b. Azt az infrastruktúra-egységet, amelynek meghibásodása közösen érintheti a másolatokat
- c. A fájlrendszerben létrehozható könyvtárak számát
- d. Az objektumkulcs maximális hosszát

**75.** Melyik tárolási modell használ tipikusan bucketet vagy containert?
- a. File storage
- b. Object storage
- c. Memória
- d. Block storage

**76.** Egy szervezet szabályozni szeretné az engedélyezett régiókat és erőforrástípusokat. Melyik megoldás a legcélszerűbb?
- a. A naplózás kikapcsolása
- b. Minden felhasználónak rendszergazdai jog adása
- c. Policy-alapú governance
- d. A szolgáltatási limitek figyelmen kívül hagyása

**77.** Miért növeli a több storage-modell együttes használata az üzemeltetési összetettséget?
- a. Mert egy alkalmazás nem használhat több storage-modellt
- b. Mert minden adatot többször kötelező tárolni
- c. Mert megszűnik a titkosítás lehetősége
- d. Mert több eltérő interfészt, jogosultságot, életciklust és megfigyelési pontot kell kezelni

**78.** Miért egészíti ki egymást a Conditional Access és az Azure RBAC?
- a. Mindkettő kizárólag költségriportokat készít
- b. Az egyik a hozzáférési feltételeket, a másik az Azure-erőforráson végrehajtható műveleteket szabályozza
- c. Mindkettő kizárólag jelszavakat tárol
- d. Az egyik automatikusan megszünteti a másikat

**79.** Egy titkosított storage-hoz túl széles törlési jogosultságot kap egy alkalmazás. Melyik változtatás indokolt?
- a. A jogosultság szűkítése a szükséges adatkörre és műveletekre
- b. A régió átnevezése
- c. A kapacitás növelése
- d. A titkosítás kikapcsolása

**80.** Miért nem emelhető át automatikusan egy komponens SLA-ja a teljes alkalmazásra?
- a. A komponens SLA-ja minden üzleti műveletet azonosan lefed.
- b. Az alkalmazás SLA-ját kizárólag a CPU-átlag határozza meg.
- c. A teljes szolgáltatás több függőségből áll, és eltérhet a hatókör és a feltétel.
- d. Az SLA kizárólag belső mérési cél.

**81.** Miért kell egy file storage szolgáltatásnál a protokollt is ellenőrizni?
- a. Mert protokoll nélkül nem lehet adatot titkosítani
- b. Mert nem minden szolgáltatás és kliens támogatja ugyanazt az SMB- vagy NFS-elérést
- c. Mert az SMB és az NFS tárolási osztály
- d. Mert a protokoll határozza meg az adat üzleti értékét

**82.** Melyik FinOps-fázis építi a döntéseket a működésbe és méri vissza a hatásukat?
- a. Inform.
- b. Deployment.
- c. Operate.
- d. Optimize.

**83.** Egy adminisztrátori szerepkör csak ritka karbantartások idején szükséges. Melyik hozzáférési modell megfelelő?
- a. Állandó aktív hozzáférés lejárat nélkül
- b. Minden felhasználó teljes hozzáférése
- c. Közös adminisztrátori credential
- d. Eligible, időben korlátozott aktiválás fokozott Authenticationnel

**84.** Melyik meghatározás írja le legpontosabban a vendor lock-in fogalmát az előadás döntési modelljében?
- a. A több Availability Zone használatából eredő hálózati késleltetés.
- b. A szolgáltatóspecifikus API-kból, adatmodellekből, menedzselt szolgáltatásokból vagy automatizációból kialakuló függőség, amely növelheti a későbbi migráció nehézségét.
- c. A kiválasztott régióban érvényes erőforráskvóta.
- d. A szolgáltató által garantált fizikai kapacitás.

**85.** Egy rendszer több alkalmazáspéldánnyal működik, de egyetlen adatbázist használ tartalék nélkül. Mi a fő kockázat?
- a. A költségmérés lehetetlenné válik
- b. Az adatbázis egyetlen hibapont marad
- c. A több alkalmazáspéldány megszünteti az összes hibát
- d. A rendszer automatikusan multi-cloud lesz

**86.** Egy eseményt három üzleti ág kap meg. Mindegyik ágban több worker dolgozik, de egy ágon belül egy feladatot valamelyik workernek kell átvennie. Melyik kombináció illik ehhez?
- a. Egyetlen cache, amelyből minden worker ugyanazt a bejegyzést törli.
- b. Egyetlen közös queue az összes üzleti ágnak, külön előfizetések nélkül.
- c. Külön szinkron kérés minden workerhez, közös állapotkövetés nélkül.
- d. Pub/sub az ágak szétválasztására, áganként saját queue és versengő workerek.

**87.** Miért nem bizonyítja egy egyszerű lekérdezés sikeres migrációs tesztje a teljes alkalmazás kompatibilitását?
- a. Mert a kompatibilitás kizárólag az alapár összehasonlításával állapítható meg.
- b. Mert a tényleges bővítmények, SQL-funkciók és alkalmazási műveletek további vizsgálatot igényelnek.
- c. Mert a sikeres lekérdezés bizonyítja, hogy az adatmodell megváltozott.
- d. Mert a managed működésben nem tesztelhető alkalmazási viselkedés.

**88.** Miért lehet tudatos kompromisszum a vendor lock-in?
- a. Mert kizárólag hibás architektúra okozza
- b. Mert minden függőség automatikusan megszűnik
- c. Mert nincs hatása a migrációra
- d. A szolgáltatóspecifikus képesség üzleti előnye nagyobb lehet a hordozhatóság értékénél

**89.** Oktatási trace-ben az API-span 900 ms, és teljesen tartalmaz egy 700 ms-os függőségi hívást. Melyik következtetés indokolt?
- a. A két idő összege nem az API végponttól végpontig mért ideje; a várakozás okát tovább vizsgáljuk.
- b. Az API teljes ideje biztosan 1600 ms.
- c. A 700 ms önmagában bizonyítja az adatbázis kapacitáshiányát.
- d. A 900 ms kizárólag az API CPU-futási ideje.

**90.** Miért nem tekinthető egy zónaredundáns tároló önmagában teljes alkalmazási magas rendelkezésre állásnak?
- a. Mert az alkalmazás hálózati, identitási, compute- és egyéb függőségei ettől még meghibásodhatnak
- b. Mert zónaredundancia esetén nincs adatmásolat
- c. Mert a storage nem befolyásolja az alkalmazást
- d. Mert a zónák mindig külön régióban vannak

**91.** Menedzselt PaaS-szolgáltatás használatakor az ügyfél minden identitás- és hozzáférés-kezelési felelőssége megszűnik.
- a. True
- b. False

**92.** Egy alkalmazás naponta készít mentést, de a mentési pontokat csak három napig őrzi meg. Egy hibás adatváltoztatást tíz nap után észlelnek. Mi a legfontosabb hiányosság?
- a. A megőrzési idő nem biztosít elegendő történeti visszaállítási pontot.
- b. A szolgáltatásnak több aktív alkalmazáspéldányra van szüksége.
- c. A mentési műveletek között túl hosszú idő telik el.
- d. A mentések kizárólag teljes mentésként készülhettek.

**93.** Egy webalkalmazás két zónában fut. Az egyik zóna kiesik, a másikban maradó példányok azonban nem tudják kezelni a teljes terhelést. Melyik feltétel hiányzik?
- a. Több alkalmazásverzió egyidejű használata
- b. Elegendő megmaradó kiszolgálási kapacitás
- c. Azonos image-név minden példányon
- d. A load balancer átnevezése

**94.** Egy cloudbeli ügyfélportál helyi identitásszolgáltatást használ. A webes célok egészségesek, de a bejelentkezés időnként sikertelen. Melyik vizsgálat fedi le a teljes függőséget?
- a. A hibrid kapcsolat kizárása, mert a webes célok egészségesek.
- b. Kizárólag a webes célok egészségének újbóli megtekintése.
- c. Az adatbázis publikus címének kötelezővé tétele.
- d. A helyi szolgáltatás, a hibrid út, a DNS és az engedélyezett forgalom együttes ellenőrzése.

**95.** Mit jelent a desired state a deklaratív infrastruktúra-leírásban?
- a. A létrehozni kívánt erőforrások és beállítások leírt célállapotát.
- b. A futó alkalmazás hibamentességének automatikus bizonyítékát.
- c. A cloudszolgáltató által minden workloadhoz kötelezően kiválasztott platformot.
- d. A kézi telepítési lépések utólagos naplóját.

**96.** Melyik besorolás helyes az AWS konténeres compute-példáinál?
- a. ECS: compute-kapacitás; EKS: függvényfuttatás; Fargate: Kubernetes API.
- b. ECS és EKS: eltérő orkesztrációs modellek; Fargate: compute-kapacitásmodell.
- c. ECS és EKS: azonos orkesztrátor; Fargate: registry.
- d. ECS: image-formátum; EKS: VM-image; Fargate: batch-ütemező.

**97.** Egy csapat kizárólag egyetlen projekt erőforrásait kezelheti. Hol célszerű megadni a szükséges Role Assignmentet?
- a. A lehető legszűkebb, projektet lefedő Scope-ban
- b. Minden felhasználó valamennyi erőforrásán
- c. A teljes szervezet legmagasabb Scope-ján
- d. Scope alkalmazása nélkül

**98.** Méretcsökkentés után a számla kisebb, de a csúcsidős mentési sikeresség nem teljesíti a változatlan célt. Hogyan értékelnéd?
- a. A csúcsidős adatot kihagyjuk az összehasonlításból.
- b. Az optimalizálás sikeres, mert a számla csökkent.
- c. Az SLO-t utólag a romló működéshez igazítjuk, és lezárjuk az értékelést.
- d. A megtakarítás nem bizonyít követelményt teljesítő optimalizálást; a kapacitást és visszaállást felülvizsgáljuk.

**99.** Egy API-kérést a megfelelő háttérszolgáltatáshoz kell továbbítani. Melyik gateway-képesség szükséges ehhez?
- a. Tokenellenőrzés.
- b. Auditnapló-megőrzés.
- c. Routing.
- d. Kvóta.

**100.** Miért nem bizonyítja a sok különböző partíciókulcs az egyenletes terheléseloszlást?
- a. Mert a forgalom néhány népszerű kulcsra koncentrálódhat.
- b. Mert a kulcsok száma csak relációs adatbázisban értelmezhető.
- c. Mert a különböző kulcsok minden esetben ugyanazt a rekordot jelölik.
- d. Mert az egyenletes terhelést kizárólag a titkosítás határozza meg.

**101.** Mi a customer-managed key legfontosabb sajátossága?
- a. Nagyobb ügyfélkontrollt és kulcskezelési felelősséget ad
- b. Storage-modellt vált blockról objectre
- c. Automatikusan publikus hozzáférést ad
- d. Megszünteti a titkosítás szükségességét

**102.** Egy globális portál gyors növekedést vár, érzékeny adatokat kezel, és több ország szabályozásának kell megfelelnie. Mi a legjobb régióválasztási megközelítés?
- a. Mindig a földrajzilag legtávolabbi régió használata
- b. A régiók közötti különbségek figyelmen kívül hagyása
- c. A késleltetés, adatrezidencia, szolgáltatás-elérhetőség, költség és megfelelőség együttes értékelése
- d. Kizárólag a legalacsonyabb egységár választása

**103.** Egy vállalat második régióban tart fenn replikált adatokat és alkalmazáskapacitást. A primer régió kiesése után a felhasználói kérések továbbra is a kiesett régióba érkeznek. Melyik helyreállítási lépés hiányossága merül fel?
- a. A primer régió kapacitásának növelése.
- b. A replikációs naplók archiválása.
- c. A forgalom átirányítása a működő régióba.
- d. A mentési pontok megőrzése.

**104.** Egy tartósan elérhető alkalmazásnál a csapat a Kubernetes API közvetlen kezelését nem igényli, viszont csökkentené a platformüzemeltetési feladatokat. Melyik döntési irány megalapozott?
- a. VM-snapshot választása futtatási platformként.
- b. Saját Kubernetes-klaszter választása további vizsgálat nélkül.
- c. Menedzselt alkalmazásplatform mérlegelése, az alkalmazás követelményeinek és a platform képességeinek összevetésével.
- d. Serverless függvény kötelező választása, mert minden tartós alkalmazás csak így működhet.

**105.** Egy dokumentált szabály előírja a privilegizált hozzáférések negyedéves felülvizsgálatát, de a végrehajtásról nincs napló vagy jóváhagyási eredmény. Mi hiányzik?
- a. Cloud régió
- b. A kontroll működését igazoló Evidence
- c. Workload Identity
- d. Titkosítási algoritmus

**106.** A visszaállítás után a mentés ismét működik, a kódhiba oka még vizsgálat alatt áll. Mi a helyes értelmezés?
- a. A működés helyreállt, de a tartós hibajavítás külön feladat.
- b. A gyökérok megszűnése már bizonyított.
- c. A további tanulságvizsgálat szükségtelen.
- d. A helyreállítás sikertelen, amíg minden kódrészletet nem elemeztek.

**107.** Egy médiaplatform felhasználói több kontinensen találhatók. A forgalomirányítás globális, az alkalmazáskiszolgálók két régióban működnek, az egyes kiszolgálók pedig meghatározott zónákhoz kötődnek. Melyik értelmezés helyes?
- a. A megoldás globális, regionális és zonális komponenseket egyaránt tartalmaz.
- b. A globális forgalomirányítás miatt a zónák már nem jelentenek hibatartományt.
- c. Két régió használata automatikusan megszünteti az alkalmazásszintű hibakezelés szükségességét.
- d. A teljes megoldás kizárólag globális scope-pal rendelkezik.

**108.** Egy meglévő SQL Server-alkalmazáshoz keresnek Azure- és AWS-jelölteket. Melyik összehasonlítás illeszkedik az előadás motorvonal-alapú megközelítéséhez?
- a. Cosmos DB for NoSQL és Amazon Neptune, az SQL Server-verzió figyelmen kívül hagyásával.
- b. Azure SQL Database / Managed Instance és RDS for SQL Server, külön kompatibilitásvizsgálattal.
- c. Azure Database for MySQL és Aurora PostgreSQL, kizárólag ár alapján.
- d. Azure Managed Redis és Amazon ElastiCache, tranzakciós elsődleges adattárként.

**109.** Egy worker végrehajtotta a feladatot, de a sikeres visszaigazolás elmaradt. Ugyanaz az üzenet újra kézbesíthető. Melyik tervezési követelmény válik fontossá?
- a. A cache-bejegyzések korlátlan megőrzése.
- b. Minden újrakézbesített üzenet feltétel nélküli eldobása.
- c. Idempotens feldolgozás az ismételt üzleti hatás kezelésére.
- d. Az adatbázis-tranzakciók megszüntetése.

**110.** Egy konfigurációs értéket mindig az ismert konfigurációazonosító alapján kérnek le, egész értékként. Melyik adatmodell természetes első jelölt?
- a. Relációs modell többtáblás kapcsolatokkal.
- b. Kulcs-érték modell.
- c. Dokumentummodell mezőalapú kereséssel.
- d. Gráfmodell.

**111.** Egy munkakörváltás során a Mover folyamatnak a már nem szükséges hozzáféréseket is kezelnie kell.
- a. True
- b. False

**112.** Miért nem oldja meg önmagában a gateway throttling a háttérszolgáltatás minden skálázási problémáját?
- a. Mert throttling mellett a háttérszolgáltatás nem kaphat kéréseket.
- b. Mert a throttling minden átengedett kérés üzleti eredményét megőrzi.
- c. Mert a throttling kizárólag naplózási funkció.
- d. Mert a forgalom korlátozása nem helyettesíti a háttérszolgáltatás megfelelő kialakítását.

**113.** Miért nem biztosít minden hibamodell ellen védelmet a többzónás kialakítás?
- a. Mert a többzónás működés kizárja az adatreplikációt.
- b. Mert a zónák kizárólag mentési pontokat tárolnak.
- c. Mert a zónák mindig külön szolgáltatókhoz tartoznak.
- d. Mert a teljes régiót érintő kiesés több zónát is érinthet.

**114.** Egy Azure-workload Kubernetes API-ra és orkesztrációs modellre épül. Melyik szolgáltatás illeszkedik ehhez közvetlen jelöltként?
- a. App Service kizárólag a webes elérés miatt
- b. Functions kizárólag a kód futtatása miatt
- c. AKS
- d. Batch kizárólag a párhuzamosság miatt

**115.** Egy esemény három előfizetőhöz jutott el. Két feldolgozás sikeres, a harmadik tartósan hibás. Melyik következtetés indokolt?
- a. A harmadik ág hibája automatikusan visszavonja a másik két ág eredményét.
- b. A topic a hibás ág üzleti logikáját automatikusan kijavítja.
- c. A harmadik ág állapotát és hibakezelését külön kell vizsgálni.
- d. A publisher sikeres küldése bizonyítja mindhárom üzleti feldolgozás sikerét.

**116.** Melyik DR-stratégia tart fenn minimális működő magot, amelyhez kieséskor további komponenseket kell aktiválni?
- a. Warm Standby
- b. Pilot Light
- c. Backup and Restore
- d. Active-Active

**117.** Egy dokumentumfeldolgozó feladat csak új fájl érkezésekor fut. Melyik elszámolási és futtatási irány lehet hatékony?
- a. Eseményvezérelt, használatalapú serverless működés
- b. Folyamatosan maximális méretű szerver
- c. Évekre előre rögzített kapacitás
- d. SaaS levelezési szolgáltatás

**118.** Melyik állítás írja le a pay-as-you-go működést?
- a. A költség a tényleges vagy elszámolt használathoz kapcsolódik
- b. A szolgáltatás minden esetben fix beruházási költségű
- c. A használat nem mérhető
- d. Minden kapacitást évekre előre meg kell vásárolni

**119.** Miért növelheti az automatizáció a működési kockázatot is?
- a. A hibás konfigurációt gyorsan és nagy léptékben terjesztheti
- b. Megakadályoz minden változtatást
- c. Kikapcsolja a monitoringot
- d. Megszünteti a szabályozást

**120.** Egy AWS Organization production OU-jára olyan SCP vonatkozik, amely tilt egy magas kockázatú műveletet. Egy production accountban egy IAM-policy kifejezetten engedélyezi ugyanezt a műveletet. Mi történik a művelet végrehajtási kísérletekor?
- a. A művelet nem hajtható végre, mert az SCP korlátozza, hogy az accountban mi lehet engedélyezhető.
- b. A művelet végrehajtható, mert az accounton belüli IAM-policy specifikusabb.
- c. Az account automatikusan kikerül a production OU-ból.
- d. A művelet automatikusan másik Regionben hajtódik végre.

**121.** Melyik szerepet töltheti be az Identity Provider a hozzáférési folyamatban?
- a. Minden Permission automatikus engedélyezése
- b. Identitás ellenőrzése és identitásra vonatkozó állítás vagy token biztosítása
- c. Fizikai adatközpont építése
- d. Kizárólag cloud erőforrások számlázása

**122.** Az automatizált beavatkozás előfeltétele nem teljesül. Mi a megfelelő döntés?
- a. Nincs automatikus beavatkozás; szükség szerint emberi vizsgálat következik.
- b. A műveletet korlátlanul újrapróbáljuk.
- c. A műveletet az előfeltétel figyelmen kívül hagyásával végrehajtjuk.
- d. Az esetet sikeresen lezárjuk, mert a riasztás megérkezett.

**123.** Egy globálisan elérhető webalkalmazás adatbázisa egyetlen régióban működik. Melyik következtetés helyes?
- a. A regionális adatbázis csak az adott régió felhasználói számára érhető el.
- b. Az alkalmazás globális elérhetősége nem változtatja automatikusan globálissá a regionális adatbázis scope-ját.
- c. Az adatbázis globális scope-pal rendelkezik, mert az alkalmazás világszerte elérhető.
- d. Az adatbázis automatikusan minden régióba replikálódik.

**124.** Melyik állítás különíti el legpontosabban a High Availability és a Disaster Recovery célját?
- a. A HA kizárólag adatmentést, a DR kizárólag forgalomelosztást jelent.
- b. A HA a szolgáltatás magas rendelkezésre állását, a DR a súlyos kiesés utáni helyreállítást célozza.
- c. A HA minden hibát megszüntet, a DR csak alkalmazásfrissítéskor használható.
- d. A HA kizárólag egy régióban, a DR kizárólag két aktív régióban működhet.

**125.** A tesztkapacitás ütemezése csökkentette a számlát, de a tesztelési igény megváltozott. Mi következik?
- a. Az Operate fázist lezárjuk, mert már volt megtakarítás.
- b. Csak a korábbi megtakarítást jelentjük, az új igényt kizárjuk.
- c. Új információ alapján ismét értékeljük az ütemezést és a használhatóságot.
- d. A korábbi döntést véglegesnek tekintjük.

**126.** Miért nem elegendő egy távoli szerver használata ahhoz, hogy cloudszolgáltatásról beszéljünk?
- a. A cloud kizárólag SaaS lehet
- b. Cloudban nem használhatók szerverek
- c. A távoli szerver nem kapcsolódhat hálózathoz
- d. A cloud működéséhez további alapjellemzők is szükségesek

**127.** Egy portál eredeti dokumentumokat fogad felhasználóktól. Az alkalmazáspéldányok rendszeresen cserélődnek. Hol célszerű megőrizni az eredeti dokumentumokat?
- a. A compute-tól elválasztott tartós tárolásban
- b. Kizárólag a helyi ideiglenes lemezen
- c. A böngésző gyorsítótárában
- d. Kizárólag az alkalmazáspéldány memóriájában

**128.** A kedvezményes konstrukció stabil alapigényre alkalmasnak látszik, de a tesztterhelés jövője bizonytalan. Mi a megfelelő döntési alap?
- a. A jelenlegi teljes kapacitás lekötése kizárólag a kedvezmény alapján.
- b. A műszaki kihasználtsági adat automatikus kereskedelmi jóváhagyásként kezelése.
- c. Elkülönített használati előrejelzés, méretezésvizsgálat, konstrukciós feltételek és külön pénzügyi jóváhagyás.
- d. A tesztterhelés bizonytalanságának elhagyása az értékelésből.

**129.** Egy gyakran használt objektumhoz melyik általános tárolási osztály illeszkedik?
- a. Törölt állapot
- b. Deep Archive
- c. Archive
- d. Hot

**130.** Mi a Health Check szerepe a magas rendelkezésre állású alkalmazáskörnyezetben?
- a. A mentési pontok automatikus archiválása.
- b. Az alkalmazáspéldány kiszolgálási állapotának ellenőrzése.
- c. Az alkalmazás teljes adatállapotának replikálása.
- d. A szolgáltatás helyreállítási idejének garantálása.

**131.** Egy Azure VM DR-tervében a célrégióban nincs elegendő alkalmazáskapacitás. Melyik területet kell rendezni a helyreállítás előtt?
- a. A célkörnyezet erőforrás- és kapacitástervezését.
- b. Kizárólag a mentések megőrzési idejét.
- c. Kizárólag a forrás VM elnevezését.
- d. A helyreállítási tesztek teljes megszüntetését.

**132.** Két peerelt hálózat egyikéből egy harmadik hálózatot is elérnének. Melyik terv kerülheti el a hibás feltételezést?
- a. A peering automatikus transzitivitásának feltételezése.
- b. A harmadik célhoz szükséges továbbítás külön megtervezése és ellenőrzése.
- c. A harmadik hálózat minden erőforrásának publikálása.
- d. A DNS útvonaltáblaként használata.

**133.** Miért nem elegendő annyit mondani, hogy egy tárolási rendszer geo-redundáns?
- a. Mert geo-redundancia esetén nincs adatmásolat
- b. Mert geo-redundancia csak fájlneveket tárol
- c. Mert minden geo-redundáns rendszer aktív-aktív
- d. Mert a másolat frissességét, hozzáférhetőségét és helyreállítási módját is ismerni kell

**134.** Egy AWS Role permissions policy-ja engedélyezi az adatolvasást. A target account trust kapcsolata megfelelő, de egy alkalmazandó policy explicit Deny szabályt tartalmaz ugyanarra a műveletre. Mi a végső döntés?
- a. Allow
- b. Automatikus step-up Authentication
- c. Deny
- d. Új IAM User létrehozása

**135.** Melyik meghatározás felel meg a right-sizing fogalmának?
- a. A költségek címkék alapján történő hozzárendelése.
- b. A kapacitás igazítása a mért igényhez és az elvárt működéshez.
- c. A legkisebb elérhető példány választása.
- d. Az egységár csökkentése változatlan használat mellett.

**136.** Ugyanazt az infrastruktúra-leírást teszt- és éles környezethez alkalmazzuk. Mit kell a leírás mellett kontrollálni a reprodukálhatósághoz?
- a. A paramétereket, image-eket és függőségeket
- b. Csak a fájl megjelenített nevét
- c. Csak az első deployment időpontját
- d. Kizárólag a dokumentáció oldalszámát

**137.** Melyik fogalom jelöli a meghibásodás által együttesen érinthető infrastruktúraelemek körét?
- a. Backup chain
- b. Failure domain
- c. Recovery point
- d. Retention period

**138.** Melyik tartozik a Zero Trust három alapelve közé?
- a. Unlimited Privilege
- b. Verify Explicitly
- c. Trust Every Network
- d. Disable Monitoring

**139.** Melyik fogalom jelöli az összetartozó container image-változatokat csoportosító egységet egy registryben?
- a. Hypervisor
- b. Pod
- c. Trigger
- d. Repository

**140.** Miért nem azonos az API adatbázisfüggőségi telemetriája az adatbázis teljes belső naplózásával?
- a. Az adatbázis saját metrikái nem használhatók monitoringra.
- b. Az API instrumentációja minden belső adatbáziseseményt automatikusan rögzít.
- c. Az előbbi az alkalmazás hívását figyeli; a platformadatok külön gyűjtést igényelhetnek.
- d. A függőségi telemetria kizárólag pénzügyi adat.

**141.** Egy szolgáltatóspecifikus menedzselt képesség használata elfogadható döntés lehet, ha az üzleti és működési előnye tudatosan meghaladja a későbbi hordozhatóság csökkenésének kockázatát.
- a. True
- b. False

**142.** Egy EBS-alapú EC2 példány stopped állapotban van, az EBS-lemezek megmaradtak. Melyik költségértelmezés helyes?
- a. A futó példánykapacitás nem fogy, de a megmaradó erőforrások költsége fennmaradhat.
- b. A megmaradó lemezek automatikusan törlődnek.
- c. Minden kapcsolódó költség szükségszerűen megszűnt.
- d. A stopped állapot minden platformon a terminated szinonimája.

**143.** Egy archive osztály kapacitásdíja alacsony, de az adatot naponta visszaolvassák. Mit kell újraértékelni?
- a. Csak a titkosítási kulcs nevét
- b. A teljes költséget és az elérési osztály illeszkedését
- c. Kizárólag a fájl nevét
- d. A compute-példány háttérszínét

**144.** Egy menedzselt alkalmazásplatformra telepített szolgáltatás hibás alkalmazáskonfigurációval indul. Melyik feladat marad a csapatnál?
- a. Az összes alkalmazásadat figyelmen kívül hagyása.
- b. A hiba automatikus áthárítása a fizikai szerver gyártójára.
- c. Az alkalmazás konfigurációjának javítása és működésének ellenőrzése.
- d. A platform PaaS-jellegének megszüntetése.

**145.** A CPU és a memória mellett a tárolási teljesítmény bizonyul meghatározónak. Melyik instance-kategória vizsgálata indokolt?
- a. GPU-alapú konfiguráció szoftvervizsgálat nélkül
- b. Storage Optimized
- c. General Purpose kizárólag a neve alapján
- d. Memory Optimized kizárólag a RAM alapján

**146.** A Device Trust és a workload security posture azonos fogalom, ezért minden hozzáférési helyzetben változtatás nélkül felcserélhetők.
- a. True
- b. False

**147.** Mire szolgálhat az Azure Private Endpoint az előadásban bemutatott helyzetben?
- a. Támogatott szolgáltatás privát IP-n történő elérésére.
- b. A DNS szükségességének megszüntetésére.
- c. Kizárólag a webes terhelés elosztására.
- d. Minden VNet automatikus összekapcsolására.

**148.** Egy Azure Storage Account törlését erőforrászár védi, de egy jogosult alkalmazás továbbra is törölhet blobokat. Mi ennek a magyarázata?
- a. Az erőforrászár csak throughputot növel
- b. A kezelési sík erőforrászára és az adatszintű jogosultság külön kontroll
- c. A titkosítás kikapcsolta az erőforrászárat
- d. A blobok nem tartoznak tároláshoz

**149.** Mit jelöl a `/24` a CIDR-jelölésben?
- a. Huszonnégy hálózatközi kapcsolatot.
- b. A hálózati előtag hosszát.
- c. Huszonnégy subnetet.
- d. Huszonnégy engedélyezett portot.

**150.** Melyik funkció szolgálhat egy objektum korábbi változatának megőrzésére?
- a. Verziózás
- b. DNS-konfiguráció
- c. Kizárólag helyi redundancia
- d. Throughput-növelés

**151.** Egy vállalat külön Azure subscriptiont használ production és development környezethez. Mindkét subscription eltérő régiókban tartalmaz erőforrásokat. Melyik állítás helyes?
- a. Minden régióhoz kötelező külön Microsoft Entra tenant.
- b. A production és development subscription csak azonos régióban működhet.
- c. A subscription elkülönítés alkalmazható governance- és elszámolási célra, és nem követeli meg, hogy a subscription erőforrásai egyetlen régióban legyenek.
- d. Egy subscription kizárólag egyetlen Availability Zone erőforrásait tartalmazhatja.

**152.** Miért kell a hibakeret fogyását ugyanazon műveletdefinícióval és időablakkal értékelni?
- a. Más hatókörrel a felhasznált és megengedett hibák nem lennének összehasonlíthatók.
- b. A hibakeret kizárólag a kiadások számától függ.
- c. Az időablak csak a pénzügyi előrejelzésnél fontos.
- d. A megengedett hibák száma független a releváns műveletek számától.

**153.** Miért kell managed adatbázisnál is foglalkozni a lekérdezések és jogosultságok kialakításával?
- a. Mert a managed szolgáltató kizárólag fizikai tárhelyet biztosít.
- b. Mert a platformfeladatok átvétele nem szünteti meg az ügyfél adat- és alkalmazásfelelősségét.
- c. Mert a managed adatbázis csak ügyfél által üzemeltetett operációs rendszeren működik.
- d. Mert a managed működésben minden lekérdezést a szolgáltató ír meg.

**154.** Egy adatbázishiba több komponens riasztását váltja ki. Hogyan csökkentenéd a zajt?
- a. Minden érintett riasztást tartósan elnémítanék.
- b. A kapcsolódó jelzéseket együtt értelmezném, és ellenőrizném a fontos eset észlelhetőségét.
- c. Minden jelzést külön, azonos prioritású incidenssé alakítanék.
- d. Kizárólag a riasztások számából határoznám meg az üzleti hatást.

**155.** Miért nem egyenértékű a régióközi backup egy előkészített DR-környezettel?
- a. Mert a régióközi mentési pontok nem állíthatók vissza.
- b. Mert a mentési másolat mellett az alkalmazást és függőségeit is helyre kell állítani.
- c. Mert a másodlagos régióban nem működhetnek alkalmazások.
- d. Mert a mentési másolat minden esetben nulla adatvesztést garantál.

**156.** Melyik állítás írja le az AWS Security Groupot?
- a. Kizárólag névfeloldási szolgáltatás.
- b. Központi hálózatközi tranzitmodell.
- c. Erőforráshoz kapcsolódó, állapottartó forgalmi kontroll.
- d. Subnet szintű, állapotmentes kontroll.

**157.** Melyik állítás különíti el helyesen az IaC-t és a Kubernetes folyamatos állapotegyeztetését?
- a. Az IaC csak műveleti sorrendet írhat le, kívánt állapotot nem.
- b. Rokon gondolatokra épülhetnek, de nem minden IaC-eszköz működik folyamatos állapotvezérlőként.
- c. Minden deklaratív leírás folyamatosan futó vezérlőt jelent.
- d. A Kubernetes deklarációja önmagában garantálja a szükséges fizikai kapacitást.

**158.** Egy automatizált alkalmazás saját nevében fér hozzá egy cloud szolgáltatáshoz. Melyik identitástípus illeszkedik ehhez?
- a. Workload Identity
- b. Naming Convention
- c. Human Identity
- d. IAM Group

**159.** Melyik állítás határozza meg helyesen a Risk-based Access korlátját?
- a. Bármilyen hiányzó Permissiont pótolhat
- b. Szabályozhatja a meglévő Authorization használatát, de nem hoz létre hiányzó Permissiont
- c. Minden alacsony Risk értéknél teljes adminisztrátori hozzáférést ad
- d. Kizárólag költséganalízist végez

**160.** Miért nem tekinthető egy SCP-ben megengedett művelet automatikusan végrehajthatónak egy AWS accountban?
- a. Mert SCP csak root userrel rendelkező accountban használható.
- b. Mert az SCP csak azt határozza meg, hogy mi lehet legfeljebb engedélyezhető; a tényleges hozzáférési policy-nak is engedélyeznie kell a műveletet.
- c. Mert az SCP minden accounton belüli engedélyt automatikusan töröl.
- d. Mert az SCP kizárólag Region és Availability Zone kiválasztására használható.

**161.** Miért lehet a multi-cloud egyszerre előny és hátrány?
- a. Csökkenthet bizonyos függőségeket, de növelheti az üzemeltetési összetettséget
- b. Kizárja a governance szükségességét
- c. Megszüntet minden biztonsági feladatot
- d. Mindig olcsóbbá teszi a működést

**162.** Melyik elem segíti két AWS account között ugyanannak a fizikai Availability Zone-nak a következetes azonosítását?
- a. Amazon Resource Name
- b. Account ID
- c. Service Control Policy
- d. Availability Zone ID

**163.** Egy ritkán olvasott dokumentumra kérés esetén azonnal szükség van. Mi a helyes megközelítés?
- a. A dokumentum törlése
- b. Kötelező offline archive használata
- c. Kizárólag helyi VM-lemez használata
- d. Olyan ritka elérésű osztály választása, amely azonnali hozzáférést támogat

**164.** AWS-ben konténeres alkalmazást szeretnénk orkesztrálni, Kubernetes-követelmény nélkül. Melyik bemutatott szolgáltatás lehet jelölt?
- a. Amazon ECS
- b. AWS Lambda kizárólag a csomag formátuma miatt
- c. AMI mint önálló orkesztrátor
- d. Amazon EKS kizárólag a konténeres csomag miatt

**165.** Melyik állítás különíti el a Kubernetes reconciliation és a deklaratív IaC szerepét anélkül, hogy azonos működést feltételezne minden eszköznél?
- a. Egy IaC-fájl puszta mentése bizonyítja, hogy az infrastruktúra és az alkalmazás hibamentesen működik.
- b. Az IaC leírhatja és telepítheti a kívánt infrastruktúrát; a Kubernetes vezérlési folyamatai a kezelt clusterobjektumok tényleges állapotát folyamatosan a deklarált állapot felé terelik.
- c. Mindkettő szükségszerűen folyamatosan javítja az alkalmazás üzleti logikáját.
- d. Az IaC csak a futó podok hálózati elérését adja, a Kubernetes pedig kizárólag VM-eket hoz létre.

**166.** Egy munkatárs korábbi projektjeinek minden jogosultságát megtartotta, miközben új szerepköröket is kapott. Melyik folyamat működött hiányosan?
- a. Encryption at Rest
- b. Threat Detection
- c. Network Routing
- d. Mover és Reviewer

**167.** Egy Azure VM operációs rendszerének tárolásához melyik szolgáltatás a megfelelő első jelölt?
- a. Blob lifecycle policy
- b. Azure Files
- c. Azure Managed Disks
- d. Azure Blob Storage

**168.** Egy adatplatform teljes kapacitását növelték, de a népszerű kulcshoz tartozó kérések továbbra is lassúak. Más kulcsok kiszolgálása megfelelő. Mi a leginkább indokolt következő vizsgálat?
- a. A motorverzió módosítása a hozzáférési minta vizsgálata nélkül.
- b. A teljes adatplatform lecserélése cache-re.
- c. A kulcsok és a kérésterhelés eloszlásának elemzése.
- d. A titkosítás kikapcsolása minden adaton.

**169.** Melyik következtetés helyes a hagyományos VM- és containerarchitektúra összehasonlításakor?
- a. A VM és a container izolációs határa szükségszerűen azonos.
- b. A VM saját guest operációs rendszert futtathat, míg a hagyományos container a host kernelére épül.
- c. A VM-nek nincs szüksége futtató infrastruktúrára.
- d. A container minden esetben saját guest kernelt futtat.

**170.** Egy AWS-alkalmazás privát API-t használna egy másik környezetből. A csapat teljes VPC-peeringet javasol, noha csak az API szolgáltatáselérése szükséges. Melyik döntési kérdés a legfontosabb?
- a. Hogyan helyettesíthető a DNS Network ACL-lel?
- b. Hogyan nyitható meg minden port a két VPC között?
- c. Hogyan tehető mindkét adatbázis publikussá?
- d. Elég-e a meghatározott szolgáltatás PrivateLink-alapú privát elérése a teljes hálózatközi kapcsolat helyett?

**171.** Miért nem garantálja egy zónákkal rendelkező Azure-régió önmagában, hogy egy kiválasztott szolgáltatás zónaredundánsan használható?
- a. Mert az Azure Availability Zone-ok kizárólag management groupokhoz használhatók.
- b. Mert a zónaredundancia csak globális szolgáltatásoknál értelmezhető.
- c. Mert egy Azure-régió legfeljebb egy zónát tartalmazhat.
- d. Mert a konkrét szolgáltatás, feature vagy konfiguráció zónatámogatását külön is ellenőrizni kell.

**172.** Miért szükséges a DR-teszt során az alkalmazási függőségek működését is ellenőrizni?
- a. Mert az alkalmazási függőségek nem befolyásolják az RTO-t.
- b. Mert a DR-terv nem tartalmazhat infrastruktúra-helyreállítást.
- c. Mert a működő infrastruktúra nem bizonyítja önmagában a használható üzleti szolgáltatást.
- d. Mert a DR-teszt kizárólag az alkalmazáskonfigurációt vizsgálja.

**173.** Melyik fogalom kapcsolódik az időegység alatt átvitt adatmennyiséghez?
- a. Redundancia
- b. Metadata
- c. Availability
- d. Throughput

**174.** Egy fejlesztő saját alkalmazást készít, de nem akar operációs rendszert frissíteni. Melyik modell a legkézenfekvőbb?
- a. Community cloud
- b. SaaS
- c. PaaS
- d. IaaS

**175.** Egy Kubernetes Deployment új podot hoz létre a kiesett példány helyett, de az új pod is ugyanazzal a hibás alkalmazáskonfigurációval indul. Mit mutat ez?
- a. A platform helyreállíthatja a deklarált példányszámot, miközben a hibás konfiguráció külön javítást igényel.
- b. A Service automatikusan kijavítja majd az alkalmazás konfigurációját.
- c. A kívánt példányszám szükségszerűen nullára változott.
- d. A reconciliation nem működik, mert új pod nem jött létre.

**176.** Egy vállalat Pilot Light DR-modellt használ. A DR-próbán a replikált adatok rendelkezésre állnak, de az alkalmazás indításához szükséges hálózati és jogosultsági konfigurációk kézi létrehozása jelentős késést okoz. Melyik fejlesztési irány indokolható?
- a. A replikáció teljes megszüntetése.
- b. Az aktiválási és konfigurációs lépések előkészítése, automatizálása és újratesztelése.
- c. A mentések megőrzési idejének kizárólagos növelése.
- d. A hálózati és jogosultsági függőségek kihagyása a DR-tervből.

**177.** Egy hoston több, egymástól elkülönített VM fut. Miért nem következik az elkülönítésből, hogy a host fizikai kapacitása és hibája többé nem közös szempont?
- a. Mert egy fizikai hoston legfeljebb egy VM működhet.
- b. Mert a VM-ek valójában ugyanazt a guest operációs rendszert használják.
- c. Mert a virtualizáció megszünteti a hoston lévő fizikai memóriát.
- d. Mert a VM-ek mögött közös fizikai erőforrások állnak, amelyek kapacitását és rendelkezésre állását továbbra is kezelni kell.

**178.** Egy alkalmazás egyetlen virtuális gépe több CPU-t és memóriát kap. Milyen változtatás történt?
- a. Horizontális skálázás
- b. Resource pooling
- c. Vertikális skálázás
- d. Multi-cloud

**179.** Egy PaaS-alkalmazásban hibás üzleti logika rosszul kezeli az adatokat. Melyik fél felelősségi körébe tartozik elsődlegesen a hiba?
- a. Az ügyfél alkalmazásfejlesztési felelősségébe
- b. Az internetszolgáltató felelősségébe
- c. A fizikai adatközpont őrzésébe
- d. A szolgáltató hűtési rendszerébe

**180.** Mit kapcsol össze a Role Assignment az RBAC-modellben?
- a. Password, Token és Encryption Key
- b. Requirement, Audit és Invoice
- c. Identity, Role és Scope
- d. Region, Zone és Data Center

**181.** Miért nem lehet az Availability Setet többzónás architektúraként értelmezni?
- a. Mert az Availability Zone kizárólag karbantartási csoport.
- b. Mert a logikai VM-csoportosítás és a régión belüli fizikai zónaelkülönítés eltérő fogalom.
- c. Mert a Fault Domain és a zóna minden esetben ugyanaz.
- d. Mert az Availability Set nem kapcsolódik VM-ekhez.

**182.** Miért csökkenti az MFA egy megszerzett jelszó önálló felhasználhatóságát?
- a. Mert további, eltérő hitelesítési tényezőt követelhet meg
- b. Mert automatikusan eltávolítja az összes Permissiont
- c. Mert minden felhasználót adminisztrátorrá tesz
- d. Mert letiltja az Identity Providert

**183.** Miért nem garantálja a cloud infrastruktúra önmagában az alkalmazás magas rendelkezésre állását?
- a. Az ügyfél nem tervezhet architektúrát
- b. A cloudban nem létezik redundancia
- c. Az alkalmazás redundanciáját, adatvédelmét és hibakezelését is meg kell tervezni
- d. A rendelkezésre állás kizárólag az ártól függ

**184.** Megfelelő Allow hiányában a hozzáférési kérés implicit Deny eredményt kaphat akkor is, ha nincs explicit Deny.
- a. True
- b. False

**185.** Mit jelent a CapEx?
- a. Beruházási kiadás
- b. Használatalapú elszámolás
- c. Szolgáltatói kötöttség
- d. Automatikus skálázás

**186.** Melyik párosítás helyes?
- a. Skálázhatóság: a többleterőforrásból elérhető többletteljesítmény; rugalmasság: a kapacitás igényhez igazítása.
- b. Skálázhatóság: kizárólag VM-méretváltás; rugalmasság: kizárólag backup.
- c. Skálázhatóság: a platform neve; rugalmasság: a runtime verziója.
- d. Skálázhatóság: az image tárolása; rugalmasság: az OS indulása.

**187.** Egy privát gépnek frissítést kell letöltenie. Melyik kapcsolati mintát vizsgálnád?
- a. A DNS letiltása.
- b. Privát erőforrás kimenete NAT-on keresztül.
- c. Közvetlen adatbázis-publikálás.
- d. Kizárólag bejövő load balancing.

**188.** Miért lehet hibás következtetés, hogy a private cloud mindig biztonságosabb a public cloudnál?
- a. A private cloud nem használhat titkosítást
- b. A public cloudban nincs megosztott infrastruktúra
- c. A biztonságot az architektúra, konfiguráció, kontrollok és üzemeltetési fegyelem határozza meg
- d. A biztonság kizárólag a tulajdonjogtól függ

**189.** Egy régió teljesíti a compliance-követelményt és rendelkezik a szükséges szolgáltatással, de a szükséges erőforrásmennyiség kvótája alacsony. Mi a helyes következő lépés?
- a. Új Organizational Unit létrehozása a kvóta növeléséhez.
- b. A szolgáltatás globálisnak nyilvánítása.
- c. A régió automatikus kizárása anélkül, hogy a kvótát megvizsgálnák.
- d. A kvóta növelhetőségének és a tényleges regionális kapacitásnak a külön ellenőrzése.

**190.** Egy szervezet kizárólag jóváhagyott régióban és kötelező biztonsági baseline-nal enged erőforrást létrehozni. Melyik megoldás alkalmazza legközvetlenebbül ezt az elvet?
- a. Dokumentált szabályokhoz kapcsolt technikai policy enforcement
- b. Önkéntes elnevezési javaslat kontroll nélkül
- c. Minden felhasználónak teljes hozzáférés
- d. Auditnaplók törlése

**191.** Egy alkalmazás adatainak RPO-célja 15 perc, de csak óránként készül használható mentési pont. Melyik megállapítás indokolt?
- a. A retention növelése önmagában megoldja az eltérést.
- b. A jelenlegi mentési pontok sűrűsége önmagában nem biztosítja a 15 perces RPO-t.
- c. Az RTO-t kell 15 percre módosítani.
- d. Az RPO automatikusan teljesül, mert a mentések rendszeresek.

**192.** Melyik állítás írja le helyesen a PaaS absztrakciójának kompromisszumát?
- a. Kevesebb platformmunka mellett minden OS-beállítás korlátlanul elérhető.
- b. Több alkalmazásfelelősség kerül a szolgáltatóhoz, ezért tesztelés nem kell.
- c. A támogatott runtime-verzió nem befolyásolja a kompatibilitást.
- d. Kevesebb infrastruktúra-kezelésért cserébe a támogatott platformkeretekhez kell illeszkedni.

**193.** Egy szabály jelenleg minden forrásnak minden portot megenged az adatréteg felé. Mi a célzott módosítás?
- a. A DNS eltávolítása.
- b. A szükséges alkalmazási forrásra és célportra szűkítés.
- c. Az adatbázis publikus címének kötelezővé tétele.
- d. Minden további port megnyitása.

**194.** Melyik állítás írja le a Kubernetes pod és Deployment kapcsolatát?
- a. A Deployment image-eket tárol, a pod kizárólag tageket rendel hozzájuk.
- b. A pod és a Deployment egyaránt VM-backupot jelent.
- c. A pod futtatási egység; a Deployment a hozzá tartozó podpéldányok kívánt állapotának kezelésére használható.
- d. A pod a teljes cluster, a Deployment egy fizikai szerver.

**195.** Egy rendelés sikeresen véglegesült az adatbázisban. A hozzá tartozó esemény publikálása sikertelen, ezért az értesítés nem indul el. A csapat a sikeres commit alapján teljesen sikeresnek minősítené a folyamatot. Melyik értékelés helyes?
- a. Az eseményküldési hiba automatikusan visszavonta a rendelést.
- b. Az eseményküldés hibája kizárólag a cache élettartamának módosításával kezelhető.
- c. A commit minden kapcsolódó szolgáltatás sikerét bizonyítja.
- d. A helyi adatbázis-tranzakció sikeres, de a komponenseken átívelő folyamat nem igazoltan teljes; az összehangolást külön kell megtervezni.

**196.** Egy AWS privát subnet példányának van kimenő Security Group-engedélye, de nincs megfelelő útja a publikus NAT Gateway felé. Melyik módosítás kezeli a megadott hiányt?
- a. A privát subnet megfelelő kimenő útvonalának kialakítása.
- b. A Security Group átnevezése.
- c. Minden példány közvetlen publikálása.
- d. A DNS-zóna törlése.

**197.** Miért szükséges felelőst megadni egy riasztáshoz?
- a. A riasztás ettől automatikusan bizonyítja a gyökérokot.
- b. A riasztás ettől minden naplóadatot összegyűjt.
- c. A riasztás ettől automatikusan teljesíti az SLO-t.
- d. A jelzésből koordinált vizsgálat és reagálás legyen.

**198.** Egy teszt-VM törlésekor az üzleti adatokat tartalmazó kapcsolt lemezt meg szeretnénk őrizni. Mit kell ellenőrizni?
- a. Kizárólag az alkalmazásverzió nevét
- b. Csak a VM eredeti indulási idejét
- c. Kizárólag a CPU-kategóriát
- d. A kapcsolt lemez megőrzési vagy törlési konfigurációját

**199.** Melyik következtetés indokolt, ha egy alkalmazás átlagos CPU-terhelése alacsony?
- a. Biztosan túlméretezett, ezért azonnal csökkenteni kell a méretét.
- b. További erőforrások, csúcsok és szolgáltatási követelmények vizsgálata szükséges.
- c. Biztosan nincs teljesítményproblémája.
- d. A memória- és I/O-adatok már nem befolyásolják a döntést.

**200.** Egy vállalat Azure management group szintjén korlátozza a használható régiókat. Egy alárendelt subscription tulajdonosa megfelelő RBAC-jogosultsággal rendelkezik új erőforrás létrehozására, de nem engedélyezett régiót választ. Melyik eredmény illeszkedik a governance-modellhez?
- a. Az erőforrás létrehozását a felsőbb scope-on alkalmazott kontroll megakadályozhatja.
- b. A subscription automatikusan másik management groupba kerül.
- c. Az RBAC-jogosultság automatikusan felülírja a felsőbb policy-korlátozást.
- d. Az erőforrás automatikusan a resource group régiójába kerül.

**201.** A jelentkezési portál kezdőoldala betöltődik, de a mentés hibát jelez. Melyik következtetés indokolt?
- a. A hibát biztosan a compute leállása okozza.
- b. A kezdőoldal elérhetősége nem bizonyítja a mentési funkció működését.
- c. Az adatbázis biztosan kapacitáshiányos.
- d. A teljes szolgáltatás működik, mert a kezdőoldal elérhető.

**202.** Melyik állítás mutatja meg helyesen az idempotencia és a visszaállíthatóság különbségét?
- a. Az idempotens művelet minden korábbi üzleti adatot automatikusan visszaállít.
- b. A verziózott leírás miatt minden változtatás kockázatmentes.
- c. Az ismételt alkalmazás stabil végállapota nem garantálja egy adatot módosító változás veszteségmentes visszafordítását.
- d. Az idempotencia csak akkor létezik, ha minden alkalmazás új erőforrásmásolatot készít.

**203.** Egy dokumentum téves felülírása után korábbi állapotot kell visszaállítani. Melyik funkció lehet megfelelő jelölt?
- a. Kizárólag aktuális állapotú replikáció
- b. A VM újraindítása
- c. Verziózás vagy megfelelő backup
- d. Throughput-növelés

**204.** Miért nem elegendő a running erőforrásállapot a szolgáltatás ellenőrzéséhez?
- a. Az üzleti művelet függőségek miatt ettől még hibás lehet.
- b. A running állapot kizárólag a költségkeretet mutatja.
- c. A running állapot kizárólag a naplómegőrzést mutatja.
- d. A running állapot a szerződéses vállalás teljesítését jelzi.

**205.** Miért kell külön vizsgálni a tranzakciós képességeket egy NoSQL-szolgáltatásnál?
- a. Mert a képességek és a tranzakciós határok szolgáltatásfüggők.
- b. Mert a dokumentumformátum önmagában teljes ACID-garanciát ad.
- c. Mert a managed működés minden szolgáltatásban azonos tranzakciós határt biztosít.
- d. Mert NoSQL esetén minden tranzakciós művelet tiltott.

**206.** Egy rendelési rendszer két régióban működik. A primer régió kiesésekor a másodlagos régió 20 perc alatt átveszi a forgalmat. Az üzleti RTO 15 perc, az RPO 10 perc, a tényleges adatvesztés 5 perc. Melyik értékelés helyes?
- a. Az RTO teljesült, az RPO nem.
- b. Mindkét cél teljesült.
- c. Egyik cél sem teljesült.
- d. Az RPO teljesült, az RTO nem.

**207.** Miért vezethet vissza a validáció a követelményprofilhoz, nem csak a szolgáltatás kiválasztásához?
- a. Mert a validáció célja kizárólag a korábban kiválasztott jelölt megerősítése.
- b. Mert a mért eredmények feltárhatják a korábbi feltételezések pontatlanságát.
- c. Mert a szolgáltatásnév alapján minden követelmény automatikusan újradefiniálódik.
- d. Mert a teszt után az adatmodell és a működési követelmény már nem számít.

**208.** Melyik leírás különíti el helyesen a Type 1 és Type 2 hypervisort?
- a. A Type 1 közvetlenül a fizikai hardveren, a Type 2 hagyományos host operációs rendszer fölött működik.
- b. A Type 1 csak egy VM-et, a Type 2 több VM-et futtathat.
- c. A Type 1 container image-eket, a Type 2 VM-image-eket tárol.
- d. A Type 2 működéséhez nincs szükség fizikai erőforrásokra.

**209.** Melyik meghatározás illik a Fargate előadásban bemutatott szerepéhez?
- a. Konténerimage-ek tárolási helye
- b. Az EKS control plane-jének szinonimája
- c. Menedzselt compute-kapacitásmodell, nem önálló orkesztrátor
- d. Az ECS másik neve

**210.** Egy konténeres API saját VM-ről menedzselt hostingra kerül, az image változatlan. Melyik megállapítás helyes?
- a. Az alkalmazásnak többé nincs hálózati vagy adatfüggősége.
- b. A konténeres csomagolás megszűnik.
- c. Az image-ben lévő minden függőség frissítése automatikusan szolgáltatói feladat lesz.
- d. A hostfeladatok megosztása változhat, az image és alkalmazás kezelése megmaradhat.

**211.** Egy fájlmegosztást több alkalmazáspéldány elér, de két példány ugyanazt a fájlt egyszerre módosítja, és hibás állapot keletkezik. Mi hiányzik leginkább?
- a. Több boot disk
- b. Nagyobb object storage-bucket
- c. Megfelelő alkalmazási koordináció vagy zárolási mechanizmus
- d. Offline archiválás

**212.** Miért kell külön kezelni az availability és durability fogalmát?
- a. Mert az adat megmaradhat akkor is, amikor átmenetileg nem érhető el
- b. Mert a két fogalom minden esetben ellentétes
- c. Mert availability kizárólag a kapacitást jelenti
- d. Mert durability csak memóriánál értelmezhető

**213.** Melyik állítás írja le helyesen az Amazon Aurora helyét az előadás szolgáltatási térképén?
- a. Az RDS része, minden SQL Server-funkciót változtatás nélkül megvalósító motor.
- b. Az RDS része, cloudra épített, MySQL- és PostgreSQL-kompatibilis relációs motor.
- c. Az RDS-től független, kizárólag gráfadatokat kezelő szolgáltatás.
- d. Az RDS mellett működő, kizárólag memóriabeli cache-szolgáltatás.

**214.** Melyik fogalom fejezi ki, hogy a rendszer hibák mellett vagy azok után is képes megfelelően működni és helyreállni?
- a. CapEx
- b. Availability
- c. Reliability
- d. Resource pooling

**215.** Melyik állítás írja le helyesen a storage snapshot fogalmát?
- a. Minden alkalmazási komponenst automatikusan konzisztens állapotba hoz
- b. Kizárólag földrajzi redundanciát biztosít
- c. Automatikusan eltávolít minden korábbi verziót
- d. Egy meghatározott tárolási egység pont-időbeli állapotát őrizheti

**216.** Miért igényelhet a differenciális mentés nagyobb adatmennyiséget a teljes mentések közötti idő előrehaladtával?
- a. Mert a mentés automatikusan növeli a kijelölt adatkört.
- b. Mert minden differenciális mentés teljes rendszerképet tartalmaz.
- c. Mert minden korábbi differenciális mentést külön újra tárol.
- d. Mert a mentett változások az utolsó teljes mentés óta halmozódnak.

**217.** Melyik megfogalmazás írja le helyesen a Recovery Point Objective és a Recovery Time Objective kapcsolatát?
- a. Az RTO automatikusan teljesül, ha az RPO nulla.
- b. Az RPO adatvesztési, az RTO helyreállítási időcél; egyik teljesülése nem bizonyítja a másikét.
- c. Az RPO kizárólag mentési gyakoriság, az RTO kizárólag backup retention.
- d. Az RPO és az RTO mindig azonos értékű, mert ugyanazt a kiesést mérik.

**218.** Egy VM-nél a mért CPU-terhelés tartósan magas. A csapat nagyobb méretet fontolgat. Melyik döntés a leginkább megalapozott?
- a. A mérés figyelmen kívül hagyása és a VM azonnali törlése.
- b. Annak feltételezése, hogy minden magas CPU-terhelést a hálózat okoz.
- c. A backupfájl átnevezése nagyobb VM-méretre.
- d. A terhelés okának vizsgálata, a kapacitásmódosítás megtervezése és az eredmény ellenőrzése.

**219.** Egy szerepkör-hozzárendelés továbbra is aktív, de a felhasználó feladata megváltozott. Melyik kontroll támogatja a hozzáférés indokoltságának újbóli értékelését?
- a. Access Review
- b. Naming Convention
- c. Availability Zone
- d. Encryption in Transit

**220.** Egy workload váratlanul új erőforrásokhoz és szokatlan mennyiségű adathoz próbál hozzáférni. Melyik kontrollkombináció megfelelő?
- a. A workload emberi identitássá alakítása
- b. Authorization ellenőrzése, threat detection és szükség esetén response-folyamat
- c. Automatikus Permission-bővítés
- d. A naplózás megszüntetése

**221.** Mi a REST API alapgondolata az előadásban?
- a. Gyakran olvasott adatok memóriabeli tárolása.
- b. Adatbázistáblák közvetlen megosztása a klienssel.
- c. Erőforrások elérése szabványos HTTP-műveletekkel.
- d. Háttérfeladatok kiosztása versengő feldolgozóknak.

**222.** Két alkalmazás külön VPC-ben fut. Csak egy meghatározott API-t kell privát módon elérni, teljes VPC-kapcsolat nem követelmény. Melyik AWS-megoldás illik a vizsgált feladathoz?
- a. Automatikus VPC-összeolvasztás.
- b. PrivateLink.
- c. Network ACL mint DNS-szerver.
- d. Internet Gateway minden példányhoz.

**223.** Miért maradhat kiesési pont egy közös adatbázis két redundáns webkiszolgáló mellett?
- a. Mert két webkiszolgáló nem használhat közös adatbázist.
- b. Mert a webkiszolgálók csak felváltva működhetnek.
- c. Mert az adatbázis kiesése mindkét webkiszolgáló működését érintheti.
- d. Mert a közös adatbázis automatikusan letiltja a failovert.

**224.** Egy AWS-vállalati környezetben külön account szolgál a központi naplózásra. A naplózási account a security OU-ban található. A szervezet korlátozni szeretné azokat a magas kockázatú műveleteket, amelyek szervezeti szinten sem lehetnek engedélyezhetők. Melyik kontroll illeszkedik legjobban a követelményhez?
- a. A security OU-ra alkalmazott Service Control Policy.
- b. Az account Availability Zone-nevének megváltoztatása.
- c. A security account másik Regionben történő megnyitása.
- d. A naplózási erőforrások közös ARN-re átnevezése.

**225.** Mit jelent egy cache-bejegyzés invalidálása?
- a. A bejegyzés titkosítási kulcsának cseréjét.
- b. A bejegyzés eltávolítását vagy érvénytelenítését.
- c. A bejegyzés hozzáférési jogosultságának kibővítését.
- d. A bejegyzés elsődleges adatbázisba másolását.

**226.** A portál lassú, a CPU alacsony, a trace-ben hosszú adatbázishívás látszik. Mi az indokolt következő lépés?
- a. A szolgáltatás hibamentesnek minősítése az alacsony CPU miatt.
- b. A függőségi várakozás okának célzott vizsgálata kapcsolódó adatokkal.
- c. A VM automatikus bővítése kizárólag a lassulás alapján.
- d. Az adatbázis erőforráshiányának végleges megállapítása.

**227.** Egy kis alkalmazás egyetlen relációs adatbázissal teljesíti a jelenlegi követelményeket. A csapat dokumentumtárat, gráfadatbázist, cache-t és messaginget vezetne be a cloud-native jelleg erősítésére. Melyik döntési megközelítés illeszkedik az előadáshoz?
- a. Minden új komponensnél konkrét követelményt és igazolható előnyt kell kimutatni, a hozzáadott teherrel együtt.
- b. Minden elérhető szolgáltatást be kell vezetni, hogy az architektúra teljes legyen.
- c. Kizárólag a komponensek számát kell összevetni más alkalmazásokéval.
- d. Az egyszerűbb megoldást a követelmények vizsgálata nélkül el kell vetni.

**228.** Egy alkalmazás az eszközazonosítóhoz tartozó, időrendben érkező méréseket kérdezi le. Nagy adathalmaz és előre ismert hozzáférési minta jellemzi. Melyik modell vizsgálata indokolt elsőként?
- a. Gráfmodell, mert minden mérés kapcsolódik egy eszközhöz.
- b. Széles oszlopos modell, megfelelő partíció- és lekérdezéstervezéssel.
- c. Dokumentummodell, a hozzáférési minta vizsgálata nélkül.
- d. Kulcs-érték modell, kizárólag egész adathalmazok lekérésével.

**229.** Mi marad jellemzően az ügyfél feladata IaaS esetén?
- a. A vendég operációs rendszer kezelése
- b. A fizikai szerverek javítása
- c. A fizikai adatközpont hűtése
- d. A virtualizációs réteg üzemeltetése

**230.** Egy webalkalmazás minden példánya ugyanabban a zónában fut. Az üzleti követelmény egyetlen zóna hibájának túlélése. Melyik megoldás teljesíti legjobban a követelményt?
- a. Az alkalmazás nevének módosítása
- b. Több példány ugyanabban a zónában
- c. Példányok telepítése több zónába, megfelelő forgalomelosztással
- d. Új resource group létrehozása

**231.** Egy customer-managed key törlését kezdeményezik, miközben a hozzá kapcsolódó storage-adatot még meg kell őrizni. Mi a helyes döntési szempont?
- a. A storage automatikusan szolgáltatói kulcsra vált
- b. A kulcs törlésének adat-hozzáférési következményét és visszaállíthatóságát előbb értékelni kell
- c. A kulcs azonnal törölhető, mert az adat ettől biztosan olvasható marad
- d. A kulcstörlés csak throughputot befolyásol

**232.** Miért nem bizonyít megtakarítást önmagában a kedvezményes egységár?
- a. A díjazási konstrukció minden szolgáltatásnál azonos.
- b. A tényleges használat és a vállalás kihasználtsága is számít.
- c. A kedvezmény automatikusan megszünteti a felesleges kapacitást.
- d. A használati profil nem kapcsolódik a teljes költséghez.

**233.** Melyik kontroll alkalmas az erőforrás tulajdonosának és költséghelyének strukturált nyilvántartására?
- a. Authentication kikapcsolása
- b. Közös adminisztrátori jelszó
- c. Kötelező tagek
- d. Nyilvános hálózati hozzáférés

**234.** Egy lifecycle-szabály csak a „lezárt-exportok” adatkörre vonatkozhat. Mit kell pontosan beállítani?
- a. A szabály hatókörét vagy szűrését
- b. A felhasználó monitorának felbontását
- c. A VM CPU-számát
- d. A fájlrendszer IOPS-értékét

**235.** Egy csapat az infrastruktúra-definíció módosításával új tárolóerőforrást kér a tesztkörnyezethez. Mi szükséges a módosítás alkalmazása után?
- a. Annak kijelentése, hogy az alkalmazás minden funkciója automatikusan hibamentes.
- b. Annak ellenőrzése, hogy a kívánt erőforrás és kapcsolat ténylegesen létrejött-e.
- c. A Kubernetes folyamatos állapotkezelésének minden IaC-eszközre való automatikus feltételezése.
- d. A definíció törlése, mert a létrejött környezet már nem ellenőrizhető.

**236.** Miért nem tekinthető az Azure resource group földrajzi konténernek?
- a. Mert minden resource group automatikusan globális erőforrás.
- b. Mert a benne található erőforrások saját régióval és szolgáltatási scope-pal rendelkezhetnek.
- c. Mert a resource group kizárólag felhasználókat tartalmaz.
- d. Mert a resource group nem rendelkezhet névvel.

**237.** Melyik tulajdonság jellemzi az IAM Role-t?
- a. Kizárólag storage-erőforráshoz kapcsolható tag
- b. Saját tartós jelszóval kötelezően rendelkező emberi identitás
- c. Kizárólag IAM User objektumokat tartalmazó csoport
- d. Felvehető identitás, amely role sessionben ideiglenes credentialöket használhat

**238.** A Kubernetesben melyik objektum írhatja le a kívánt podpéldányokat és azok frissítését?
- a. Container tag
- b. Deployment
- c. VM-snapshot
- d. Registry

**239.** Hétfőn teljes mentés készült, kedden és szerdán differenciális mentés. Mely mentések szükségesek a szerdai állapot klasszikus visszaállításához?
- a. Kizárólag a szerdai differenciális mentés.
- b. A keddi és szerdai differenciális mentés.
- c. A hétfői teljes és a szerdai differenciális mentés.
- d. A hétfői teljes és mindkét differenciális mentés.

**240.** Melyik felsorolás tartalmazza az Azure API Management előadásban bemutatott három fő elemét?
- a. HTTP backend, relációs motor és auditadatbázis.
- b. API gateway, management plane és developer portal.
- c. Authorizer, adatbázisséma és partíciókulcs.
- d. Adatbázismotor, cache és queue.

**241.** Egy alkalmazás VM-en fut, és a csapat containerbe csomagolná a gyorsabb alkalmazástelepítés érdekében. A tervező szerint a containerizáció után a VM azonnal feleslegessé válik. Melyik állítás pontos?
- a. A VM csak container image-ek tárolására használható.
- b. A containerizáció automatikusan megszünteti a host üzemeltetését.
- c. A container VM-en is futhat; a két réteg eltérő feladatot láthat el.
- d. A container kizárólag fizikai szerveren működhet.

**242.** Miért nem következik univerzális kiadási tilalom a hibakeret kimerüléséből?
- a. A policy és a változtatás kockázata is számít; egy javítás eltérhet egy új funkciótól.
- b. A kimerült hibakeret minden esetben jó szolgáltatási állapotot jelent.
- c. A hibakeret csak naplómegőrzési adat.
- d. A kimerült keret tetszőleges összeggel azonnal feltölthető.

**243.** Miért nem biztosít önmagában friss adatot egy cache hit?
- a. Mert a cache hit kizárólag írási műveletnél fordulhat elő.
- b. Mert a cache hit azt jelenti, hogy az adat hiányzik.
- c. Mert a megtalált másolat a hiteles adatforrás korábbi állapotát is tartalmazhatja.
- d. Mert a cache hit minden esetben új adatbázis-lekérdezést indít.

**244.** Egy korábban engedélyezett munkamenetben magas Risk jelenik meg. Melyik reakció illeszkedik az adaptív modellhez?
- a. Új Permission automatikus létrehozása
- b. Az összes napló törlése
- c. A hozzáférés újraértékelése és szükség esetén szigorítása vagy megszakítása
- d. A Risk figyelmen kívül hagyása a korábbi Authentication miatt

**245.** Egy szolgáltatás több azonos alkalmazáspéldány indításával kezeli a növekvő forgalmat. Milyen változtatás történt?
- a. CapEx-optimalizálás
- b. Vertikális skálázás
- c. Horizontális skálázás
- d. Community cloud

**246.** Egy alkalmazás deployment-folyamata személyes felhasználói fiókot használ, subscription szintű adminisztrátori hozzáféréssel. Nincs lejárat vagy rendszeres felülvizsgálat. Melyik átalakítás a legmegfelelőbb?
- a. A naplózás kikapcsolása
- b. Saját Workload Identity, feladathoz igazított Role, szűk Scope, időbeli korlátozás és rendszeres review
- c. A credential megosztása a teljes csapattal
- d. További adminisztrátori Permissionök a személyes fióknak

**247.** Egy felhasználó megfelelően hitelesített, de a szükséges Azure-műveletet nem hajthatja végre. A Conditional Access feltételei teljesültek. Mit kell következőként vizsgálni?
- a. Az erőforrás megjelenítési színét
- b. A régió földrajzi távolságát
- c. A szükséges Role Assignmentet és annak Scope-ját
- d. Egy AWS IAM Group tagságát

**248.** Miért lehet túlzott egy egyébként megfelelő Permissionöket tartalmazó Role Assignment?
- a. Mert az RBAC nem használ identitásokat
- b. Mert a Scope kizárólag Authenticationt jelent
- c. Mert minden Role Assignment automatikusan Deny eredményt ad
- d. Mert a hozzárendelés Scope-ja szélesebb lehet a tényleges feladatnál

**249.** Egy AWS Organization security OU-jában szigorúbb szervezeti korlátozásokat kell alkalmazni, mint a development OU-ban. Melyik megoldás illeszkedik a bemutatott governance-modellhez?
- a. Az összes account ugyanabba az Availability Zone-ba helyezése.
- b. Eltérő SCP-k alkalmazása a két OU-ra.
- c. A security OU accountjainak minden Regionben történő automatikus lemásolása.
- d. Az accountok ARN-jének azonosra módosítása.

**250.** Miért nem szünteti meg az önállóan telepíthető mikroszolgáltatások használata a rendszer egészének felügyeleti igényét?
- a. Mert a szolgáltatások nem kommunikálhatnak egymással.
- b. Mert minden mikroszolgáltatásnak kötelezően ugyanazon a VM-en kell futnia.
- c. Mert a szolgáltatások közötti kapcsolatokban részleges hibák léphetnek fel, amelyek az üzleti folyamatot is érinthetik.
- d. Mert az önálló telepítés automatikusan kikapcsolja a naplózást.

**251.** Melyik megfogalmazás írja le helyesen a Warm Standby működési modelljét?
- a. Csökkentett kapacitású, működő tartalék alkalmazáskörnyezet.
- b. Teljes kapacitású, párhuzamos aktív kiszolgálás minden régióban.
- c. Kizárólag mentési fájlok tárolása egy másik régióban.
- d. A primer alkalmazás teljes újraépítése minden kiesés után.

**252.** Egy AWS-szolgáltatásnak meghatározott műveleteket kell végrehajtania a szervezet nevében. Melyik objektum illeszkedik ehhez?
- a. Közös root credential
- b. Human Identity
- c. IAM Group
- d. Service Role

**253.** Egy Azure resource groupban két különböző régió erőforrásai találhatók. Melyik állítás helyes?
- a. Ez nem lehetséges, mert a resource group mindig egyetlen Availability Zone.
- b. A resource group kizárólag globális erőforrásokat tartalmazhat.
- c. Ez lehetséges, mert a resource group logikai és menedzsment-scope.
- d. A második régió erőforrása automatikusan átkerül az első régióba.

**254.** Egy gateway ellenőrzi a tokent, majd a rendelési szolgáltatáshoz továbbítja a kérést. Hol kell eldönteni, hogy a felhasználó jogosult-e az adott rendelés üzleti műveletére?
- a. Kizárólag az auditnapló utólagos elemzésekor.
- b. Kizárólag a cache-kulcs kialakításakor.
- c. Az alkalmazási szolgáltatás megfelelő üzleti jogosultság-ellenőrzésében.
- d. Kizárólag a hálózati tűzfalban.

**255.** Egy webes API és egy éjszakai feldolgozás hasonló CPU-igényű. Az API-nál a válaszidő, a feldolgozásnál a befejezési határidő fontos. Hogyan értelmezzük őket?
- a. A CPU-igény alapján az állapot és függőség figyelmen kívül hagyható.
- b. Azonos workloadok, ezért minden futtatási feltételük azonos.
- c. Mindkettő kizárólag folyamatos webes kiszolgálás.
- d. Eltérő működési és teljesítménykövetelményű workloadok.

**256.** Egy serverless szolgáltatás automatikusan skálázódik. Miért nem állítható ebből, hogy tétlenségkor biztosan nullára csökken a példányszáma?
- a. Mert a serverless szolgáltatások nem fogadnak eseményeket.
- b. Mert az automatikus skálázás kizárólag fizikai szervereken lehetséges.
- c. Mert a nullára skálázás a konkrét szolgáltatás és futtatási csomag feltételeitől függ.
- d. Mert a scale to zero a VM-backup másik neve.

**257.** Egy csapat ritkán érkező eseményeket feldolgozó komponenst és tartósan elérhető webalkalmazást üzemeltetne. Mindkettőnél csökkentené a közvetlen infrastruktúra-kezelést, de a költség és a skálázás még nem ismert. Melyik döntési terv a leginkább megalapozott?
- a. Komponensenként összevetik a menedzselt alkalmazásplatform és az eseményvezérelt futtatás alkalmasságát, majd ellenőrzik a konkrét skálázási és díjazási feltételeket.
- b. Kizárólag a szolgáltatások marketingelnevezése alapján döntenek.
- c. Mindkét komponenst kötelezően ugyanabba a serverless függvénybe helyezik, mert az biztosan nullára skálázódik.
- d. Mindkét komponenst saját VM-re helyezik, mert különböző futtatási modellek nem kombinálhatók.

**258.** Miért szükséges Authorization és Key Management az Encryption at Rest mellett?
- a. Mert a titkosítás automatikusan minden identitást töröl
- b. Mert az Encryption at Rest csak hálózati forgalmat véd
- c. Mert a jogosult alkalmazások az adatot működés közben használhatják, a kulcsokat pedig védeni kell
- d. Mert Key Management nélkül minden felhasználó implicit Allow döntést kap

**259.** Miért nem következik a nagyobb platformabsztrakcióból automatikusan jobb biztonság vagy rosszabb biztonság?
- a. Mert az absztrakció minden jogosultságot eltávolít.
- b. Mert más felelősségi határt ad, de minden modell helyes konfigurációt és alkalmazáskezelést igényel.
- c. Mert a menedzselt platformon nem létezhet hibás kód.
- d. Mert a közvetlen OS-kontroll minden esetben kivédi az alkalmazáshibát.

**260.** A Kubernetesben több podot deklarálunk, de egyik meglévő node sem teljesíti az új podok feltételeit. Melyik beavatkozási irány megalapozott?
- a. Csak a podszám további növelése
- b. A requestek ellenőrzés nélküli eltávolítása
- c. A scheduler eredményének figyelmen kívül hagyása, mert a deklaráció kapacitásgarancia
- d. A deklarált igények, elhelyezési feltételek és node-kapacitás együttes vizsgálata

**261.** Egy vállalat két régiót vizsgál. Mindkettő teljesíti az adatrezidencia-követelményt. Az első olcsóbb, de nem támogatja a kívánt zónaredundáns konfigurációt. A második drágább, de támogatja a szükséges rendelkezésre állási modellt. Ha a zónaredundancia kötelező követelmény, melyik megközelítés helyes?
- a. A zónaredundancia helyettesítése egy új subscription vagy account létrehozásával.
- b. Az első régió választása, mert alacsonyabb a listaára.
- c. A második régió továbbértékelése, mert az első nem teljesíti a kötelező technikai feltételt.
- d. Mindkét régió automatikus elfogadása, mert teljesítik az adatrezidenciát.

**262.** Egy vállalat cloudbeli alkalmazása helyi rendszerből kér adatot. A cloudbeli példányok egészségesek, az adatlekérés mégis hibás. Melyik vizsgálat indokolt?
- a. Kizárólag a webes példányok számának növelése.
- b. A cloud–helyi kapcsolat, DNS, útvonal és szabályok ellenőrzése.
- c. A helyi függőség figyelmen kívül hagyása.
- d. Minden adatbázis publikus elérésének engedélyezése.

**263.** Miért nem elegendő a listaárak összehasonlítása a régióválasztás gazdasági értékelésénél?
- a. Mert a cloud szolgáltatásoknak nincs meghatározható ára.
- b. Mert az adatforgalom, a licencek, a támogatás, a helyreállítás, a migráció és az üzemeltetési szakértelem is befolyásolhatja a teljes költséget.
- c. Mert a költséget kizárólag az Availability Zone neve határozza meg.
- d. Mert gazdasági szempontokat csak a telepítés után lehet vizsgálni.

**264.** Egy Kubernetes-workloadból jelenleg két pod fut, de a csapat négy példányt szeretne fenntartani. Melyik beállítás módosítása illeszkedik a bemutatott működési modellhez?
- a. A Service átnevezése négyesre.
- b. A workload kívánt podpéldányszámának négyre állítása.
- c. A registryben tárolt image-ek számának négyre korlátozása.
- d. Négy külön fizikai szerver kötelező létrehozása.

**265.** Melyik Azure-szint fog össze több subscriptiont közös governance-célból?
- a. Availability Zone
- b. Resource group
- c. Resource
- d. Management group

**266.** Melyik sorrend fejezi ki helyesen a compliance működési logikáját?
- a. Audit → Permission → Identity → Requirement
- b. Requirement → Control → Evidence → Audit
- c. Control → Availability Zone → Tag → Authentication
- d. Evidence → Region → Password → Cost

**267.** Melyik állítás választja szét pontosan az SLI, SLO és SLA szerepét?
- a. Az SLO teljesítése minden esetben bizonyítja az SLA teljesítését.
- b. Az SLI célérték, az SLO szerződés, az SLA tényleges mérés.
- c. Az SLI mérőszám, az SLO cél és időablak, az SLA feltételekkel rögzített szolgáltatási megállapodás.
- d. Az SLI és SLO ugyanaz; az SLA a hibakeret számszerű értéke.

**268.** Miért nem tekinthető a virtuális lemez önmagában fájlrendszernek?
- a. Mert a fájlrendszert a hálózati végpont hozza létre
- b. Mert a virtuális lemez csak objektumokat kezel
- c. Mert virtuális lemezen nem lehet adatot tárolni
- d. Mert a fájlokat és könyvtárakat egy külön fájlrendszerréteg szervezi

**269.** Egy közös szolgáltatás költségét több termék között kell megosztani. Mi szükséges lehet a címkézésen túl?
- a. A megosztott tétel kihagyása a költségértékelésből.
- b. Dokumentált allokációs szabály.
- c. Minden költség hozzárendelése az első címkézett erőforráshoz.
- d. A termékek SLO-jának azonos értékre állítása.

**270.** Melyik állítás helyes a cloud compute és a fizikai erőforrások kapcsolatáról?
- a. A cloudban kizárólag szoftveres erőforrások léteznek.
- b. A fizikai erőforrások megmaradnak, de más kezelési felületen érhetők el.
- c. A függvényfuttatás megszünteti a memóriaigényt.
- d. A menedzselt platformok nem használnak processzort.

**271.** Egy VM törlése után az adatlemez is eltűnt, pedig az eredményeket meg kellett volna őrizni. Melyik döntést kellett volna korábban ellenőrizni?
- a. A dokumentum fájlnevét
- b. A kapcsolt lemez törlési és megőrzési beállítását
- c. A prezentáció diaszámát
- d. A felhasználói böngésző típusát

**272.** A felhasználó hibát jelzett, de a naplólekérdezés üres. Mit ellenőriznél a következtetés előtt?
- a. Az időablakot, adatgyűjtést, táblát és hozzáférést.
- b. Csak a jelenlegi erőforrásállapotot; a korábbi időablakot nem vizsgálnám.
- c. Csak a lekérdezés szintaxisát; az adatgyűjtést megfelelőnek tekinteném.
- d. Az esemény hiányát véglegesnek tekinteném.

**273.** Mi a dead-letter kezelés szerepe a bemutatott üzenetfeldolgozási modellben?
- a. Az ismételten sikertelen üzenetek elkülönítése és kivizsgálásuk támogatása.
- b. Az üzenet üzleti tartalmának automatikus kijavítása.
- c. A sikeresen feldolgozott üzenetek gyorsítótárazása.
- d. Az üzenet adatbázis-tranzakcióvá alakítása.

**274.** Miért nem oldja meg önmagában a közös fájlmegosztás a párhuzamos módosítások problémáját?
- a. Mert a jogosultságok, zárolás és alkalmazási koordináció továbbra is szükséges lehet
- b. Mert file storage-on nem módosítható fájl
- c. Mert a fájlmegosztás csak objektumokon működik
- d. Mert a több kliens automatikusan külön másolatot kap

**275.** Melyik meghatározás különíti el helyesen a skálázhatóságot az elasztikusságtól?
- a. A skálázhatóság kizárólag fizikai szerverekre vonatkozik
- b. A két fogalom minden esetben azonos
- c. Az elasztikusság csak kapacitásnövelést jelent
- d. A skálázhatóság a kapacitás változtathatósága, az elasztikusság annak dinamikus igazítása

**276.** Miért nem elég a control plane elérhetősége az alkalmazás teljes elérhetőségének igazolására?
- a. Mert a menedzselt control plane megszünteti a node-kapacitást.
- b. Mert az elérhető control plane automatikusan kijavít minden image-et.
- c. Mert az alkalmazás kizárólag a control plane-ben tárolja minden adatát.
- d. Mert a workload kapacitása, elhelyezése, állapota és függőségei külön is szükségesek.

**277.** Melyik meghatározás különíti el helyesen a span és a trace fogalmát?
- a. A span eseménynapló, a trace annak megőrzési ideje.
- b. A span számlázási egység, a trace a költség-előrejelzés.
- c. A span a teljes szolgáltatás SLO-ja, a trace a mért SLI.
- d. A span részműveletet, a trace az összekapcsolt kérésvégrehajtást írja le.

**278.** Miért nem elegendő a replikált adatbázis megléte egy logikai adattörlés elleni védelem igazolásához?
- a. Mert a törlési művelet a replikált példányra is átkerülhet.
- b. Mert a replikáció kizárólag zónák között működik.
- c. Mert a replikált adatbázis nem fogadhat olvasási kéréseket.
- d. Mert a replikáció mindig teljes adatvesztést eredményez.

**279.** Miért kell az RPO és az RTO teljesülését külön vizsgálni?
- a. Mert mindkettő kizárólag az adatvesztést méri.
- b. Mert az RTO kizárólag a mentések megőrzésére vonatkozik.
- c. Mert az adatvesztési időablak és a helyreállítási idő külön célérték.
- d. Mert mindkettő kizárólag a szolgáltatás kiesési idejét méri.

**280.** Egy szolgáltatás neve helyes címre oldódik, de a cél felé nincs útvonal. Melyik feltételt kell javítani?
- a. A forgalom továbbítását.
- b. A célpéldányok számát.
- c. A név írásmódját.
- d. A válaszlehetőségek sorrendjét.

**281.** Egy vállalat mentésből állítja helyre a rendelési adatbázist. Az adatok rendelkezésre állnak, de az alkalmazás hálózati kapcsolata még hiányzik. Mikor tekinthető helyreállítottnak az üzleti szolgáltatás?
- a. Amikor a helyreállítási folyamat elindult.
- b. Amikor az adatbázis virtuális gépe elindult.
- c. Amikor a mentési fájl másolása befejeződött.
- d. Amikor az alkalmazás szükséges üzleti funkciói ismét használhatók.

**282.** Egy AWS-erőforrás publikus subnetben van, de külső kliens nem éri el. Melyik megállapítás helyes?
- a. Minden privát subnetet törölni kell.
- b. A publikus subnet önmagában bizonyítja az elérhetőséget.
- c. A DNS szükségszerűen hibás.
- d. A címzést, az útvonalat, a szabályokat és a céloldali szolgáltatást is ellenőrizni kell.

**283.** Miért nem helyettesíti a privát hálózati elérés a jogosultságkezelést?
- a. Mert a jogosultságkezelés csak nyilvános végpontnál értelmezhető.
- b. Mert a privát elérés kizárólag a titkosítást szabályozza.
- c. Mert privát hálózaton minden művelet automatikusan tiltott.
- d. Mert az elérési út és az engedélyezett műveletek külön kontrollterületek.

**284.** Miért különbözik a self-healing a tartós hibajavítástól?
- a. A működési állapot helyreállítása nem feltétlenül szünteti meg a kiváltó hibát.
- b. A két fogalom csak kézi és automatikus naplózást különít el.
- c. A self-healing kizárólag költség-hozzárendelést végez.
- d. A tartós hibajavítás kizárólag a példányszámot állítja helyre.

**285.** Melyik állítás különíti el helyesen a requestet, limitet és tényleges fogyasztást?
- a. A tényleges fogyasztás automatikusan felülír minden deklarált elhelyezési feltételt.
- b. A request elhelyezési igény, a limit futási korlát, a tényleges fogyasztás pedig eltérhet ezektől.
- c. Mindhárom ugyanannak a folyamatosan mért értéknek más neve.
- d. A limit választ node-ot, a request pedig a futás közbeni maximális fogyasztás.

**286.** Egy CPU-intenzív feldolgozás nem párhuzamosítható jól. Több példány indítása nem hoz érdemi gyorsulást. Melyik vizsgálat illeszkedik a tananyaghoz?
- a. Az adatmegőrzés lecserélése image-verziózásra
- b. További példányok korlátlan indítása az alkalmazás vizsgálata nélkül
- c. A horizontális skálázás eredményének automatikus kétszeresnek minősítése
- d. A vertikális kapacitásváltozás tesztelése, a kód korlátainak és teljes feladatköltségnek a figyelembevételével

**287.** Miért nem elegendő a JSON-formátum ismerete egy adatmodell kiválasztásához?
- a. Mert a JSON csak relációs adatbázisban használható.
- b. Mert a JSON használata kizárja a kulcsalapú elérést.
- c. Mert az is számít, hogy egész értéket vagy belső mezőket akarunk elérni.
- d. Mert minden JSON-adatot gráfmodellben kell tárolni.

**288.** Egy IaaS virtuális gépnél a szolgáltató kezeli a fizikai hostot. Miért nem tekinthető emiatt automatikusan naprakésznek a VM-en futó rendszer?
- a. Mert a fizikai host és a VM szükségszerűen ugyanaz az operációs rendszer.
- b. Mert a guest operációs rendszer karbantartása külön feladat marad.
- c. Mert az IaaS VM-en nem telepíthetők frissítések.
- d. Mert a hypervisor nem használ fizikai erőforrásokat.

**289.** Egy Amazon Resource Name minden esetben kötelezően tartalmaz kitöltött Region és Account ID mezőt.
- a. True
- b. False

**290.** Miért nem következtethetünk két peeringkapcsolatból automatikus elérésre egy harmadik hálózat felé?
- a. Mert a peering mindig megszünteti a DNS-t.
- b. Mert egy VNetben csak egy subnet lehet.
- c. Mert a peeringből általános transzitivitás nem feltételezhető.
- d. Mert peering kizárólag interneten keresztül működik.

**291.** Melyik leírás illik az observability fogalmához?
- a. A belső működés értelmezése az elérhető külső jelekből és kapcsolatokból.
- b. A naplóadatok megőrzése értelmezés nélkül.
- c. Kizárólag előre rögzített küszöbök ellenőrzése.
- d. Az erőforrások szerződéses rendelkezésre állási vállalása.

**292.** Egy adatbázis megfelelő Encryption at Rest védelme önmagában kompenzálja a túl széles alkalmazás-Permissiont és a hiányzó monitoringot.
- a. True
- b. False

**293.** Egy konténeres alkalmazás új példányt kap telepítéskor. A felhasználók által feltöltött fájloknak a régi példány eltávolítása után is meg kell maradniuk. Hová kerüljenek a megőrzendő fájlok?
- a. A példány életciklusától független tartós tárolásba.
- b. Kizárólag a régi container saját írható rétegébe.
- c. Az image tagjének szövegébe.
- d. A containerpéldány nevébe.

**294.** Egy szolgáltatóspecifikus menedzselt adatplatform jelentősen csökkenti a fejlesztési és üzemeltetési munkát, de növeli a migrációs függőséget. Melyik döntés követi az előadás logikáját?
- a. A szolgáltatás automatikus elutasítása minden vendor lock-in miatt.
- b. A migrációs kockázat figyelmen kívül hagyása, mert menedzselt szolgáltatásról van szó.
- c. Az üzleti és működési előny, valamint a hordozhatósági és migrációs kockázat dokumentált összevetése.
- d. Multi-cloud környezet kötelező kialakítása a workload követelményeitől függetlenül.

**295.** Egy konténeres rendelésfeldolgozó alkalmazásnál a pod kiesése után a Kubernetes új podot indít. A szolgáltatás mégsem tudja folytatni a munkát, mert a korábbi példány saját írható rétegében voltak a feldolgozandó adatok. Melyik következtetés a legpontosabb?
- a. A podpótlás a futtatási állapotot célozza; a megőrzendő adatokat a cserélhető példánytól függetlenül kell kezelni.
- b. A Service nevét kell módosítani, mert az tárolja a feldolgozandó adatokat.
- c. A container image tagje önmagában visszaállítja a feldolgozatlan üzleti adatokat.
- d. A Kubernetesnek az új pod helyett automatikusan vissza kellett volna állítania a régi írható réteget.

**296.** A VM életciklusában melyik művelet hozza létre elsősorban a virtuális processzort, memóriát, hálózati kapcsolatot és tárolót tartalmazó alap-erőforráskonfigurációt?
- a. Snapshot
- b. Provisioning
- c. Monitoring
- d. Restore

**297.** Melyik Azure-objektum szolgál kapcsolódó erőforrások logikai és életciklus-alapú csoportosítására?
- a. Microsoft Entra tenant
- b. Azure geography
- c. Management group
- d. Resource group

**298.** Egy folyamatosan nagy terhelésű, állapottartó feldolgozásnál a serverless költsége és futási korlátai kedvezőtlenek. Mi a helyes döntési elv?
- a. A szolgáltatási limiteket figyelmen kívül kell hagyni
- b. Más futtatási modellt is értékelni kell a workload jellemzői alapján
- c. A monitoringot ki kell kapcsolni
- d. A serverless minden esetben kötelező

**299.** Egy webáruház óránként készít mentést. Az üzlet legfeljebb 20 perc adatvesztést fogad el. A legrosszabb vizsgált esetben 55 percnyi rendelés veszne el. Mi a helyes következtetés?
- a. A mentési retention növelése önmagában megoldja a problémát.
- b. Az adatvédelmi kialakítás nem teljesíti a 20 perces RPO-célt.
- c. A mentési gyakoriság megfelel, mert óránként készül mentés.
- d. Az RTO teljesülése automatikusan biztosítja az RPO-t.

**300.** Miért nem jelent a rapid elasticity korlátlan kapacitást?
- a. Kvóták, technikai limitek, régiós kapacitás és költségkeretek korlátozhatják
- b. Mert kizárólag tárhelyre alkalmazható
- c. Mert csak on-premises környezetben működik
- d. Mert a kapacitás soha nem növelhető

**301.** Miért lehet hibás a Kubernetes-elhelyezést kizárólag pillanatnyi gépterhelés alapján értelmezni?
- a. A scheduler kizárólag az image nevét vizsgálja.
- b. A request mindig azonos a pillanatnyi fogyasztással.
- c. A scheduler a deklarált igényeket, hozzárendelhető kapacitást és elhelyezési feltételeket is figyelembe veszi.
- d. A pod deklarációja automatikusan új fizikai kapacitást hoz létre.

**302.** Egy függvényhosting megfelelőségét vizsgáljuk. Melyik ellenőrzési csomag releváns?
- a. Kizárólag a trigger megnevezése
- b. Csak az, hogy a szolgáltatás serverlessként szerepel-e
- c. Csak a szolgáltatás neve és a forráskód hossza
- d. Futásidő, memória, párhuzamosság, integrációk és hostingfeltételek

**303.** Mit jelent, ha egy alkalmazás neve sikeresen feloldódik?
- a. A kapcsolat biztosan működik.
- b. A névhez tartozó cím megállapítható.
- c. Minden port engedélyezett.
- d. A szolgáltatás biztosan egészséges.

**304.** Egy vállalat managed adatbázisra váltott. A platform karbantartásának egy részét a szolgáltató végzi, de az alkalmazás hibás rekordokat hoz létre. Melyik területet kell elsősorban felülvizsgálni?
- a. A szolgáltatás nevének és márkájának kiválasztását.
- b. Az ügyfél adatmodelljét és alkalmazási adatellenőrzését.
- c. A szolgáltató fizikai szervereinek elhelyezését.
- d. A platformkarbantartás szolgáltatói ütemezését.

**305.** Egy régió nem teljesíti a kötelező adatrezidencia-feltételt. Mi a helyes eljárás?
- a. A régió kiválasztása, ha olcsóbb
- b. A követelmény figyelmen kívül hagyása, ha van Availability Zone
- c. A régió kiválasztása, ha közelebb található
- d. A régió kizárása

**306.** Egy többzónás alkalmazás egyetlen zónában működő azonosítási szolgáltatást használ. Melyik tervezési lépés szükséges a zónareziliencia igazolásához?
- a. A másodlagos régió azonnali megszüntetése.
- b. Kizárólag a webkiszolgálók számának növelése.
- c. Kizárólag a backup retention módosítása.
- d. Az azonosítási függőség zónahiba melletti elérhetőségének vizsgálata.

**307.** Melyik állítás írja le az AWS Network ACL-t?
- a. Virtuális hálózatok közvetlen peeringje.
- b. Subnet szintű, állapotmentes hálózati kontroll.
- c. Webes kérések alkalmazási szintű irányítása.
- d. Privát szolgáltatásvégpont.

**308.** Egy hibás konfiguráció security posture eredményének lezárása csak a remediation és annak visszaellenőrzése után indokolt.
- a. True
- b. False

**309.** Egy szervezet több, különböző időben terhelt alkalmazást vonna össze kevesebb fizikai hostra. A csapat azt állítja, hogy a virtualizáció miatt kapacitástervezésre már nincs szükség. Melyik értékelés helyes?
- a. Helyes, ha minden VM azonos operációs rendszert használ.
- b. Helyes, mert a hypervisor korlátlan fizikai memóriát hoz létre.
- c. Nem helyes, mert egy hoston soha nem futhat több VM.
- d. Nem helyes: a megosztott host kapacitását és a workloadok együttes terhelését továbbra is tervezni kell.

**310.** Azure virtuális gépek támogatott régióközi replikációjához és DR-átvételéhez melyik szolgáltatás kapcsolódik?
- a. Azure Site Recovery
- b. Azure Backup retention policy
- c. Azure Blob lifecycle management
- d. Azure Files

**311.** Egy működő VM védelmével kapcsolatban melyik párosítás pontos?
- a. Backup: kizárólag memóriafoglalás; restore: kapacitásnövelés.
- b. Snapshot: adott időponthoz kapcsolódó állapotrögzítés; backup: szabályozottan megőrzött helyreállítási másolat.
- c. Image: hosszú távú adatvédelem; backup: új VM-ek alapkonfigurációja.
- d. Snapshot: fizikai szerver; restore: image-ek tárolója.

**312.** Egy kritikus alkalmazásnál téves adattörlés, alkalmazáspéldány-kiesés és teljes régiókiesés ellen is védekezni kell. A vállalat alacsony adatvesztési toleranciát és gyors helyreállítást vár, de korlátozott költségkerettel rendelkezik. Melyik tervezési megközelítés a leginkább indokolható?
- a. A backup, HA és DR-kontrollok üzleti célokhoz igazított kombinációja, igazolt helyreállítási képességgel.
- b. Egyetlen technológiai termék kiválasztása minden hibamodellhez.
- c. Kizárólag a mentési gyakoriság növelése.
- d. Kizárólag az alkalmazáspéldányok számának növelése.

**313.** Egy jóváhagyott régióban, titkosítással létrehozott adatbázis automatikusan megfelelőnek tekinthető akkor is, ha nincs tulajdonosa, megfelelő hozzáférés-kezelése, naplózása vagy auditálható Evidence-e.
- a. True
- b. False

**314.** Egy csapat több containeres komponenst működtet. A telepítések és a kívánt példányszám kezelése összetetté vált, de még nem döntöttek platformról. Melyik vizsgálat a leginkább indokolt?
- a. Annak felmérése, szükség van-e orkesztrációra, és vállalható-e a választott platform üzemeltetési összetettsége.
- b. Kubernetes bevezetése kizárólag azért, mert minden containerhez kötelező.
- c. A registry használata a futó példányok kívánt számának automatikus kezelésére.
- d. Az összes komponens egyetlen containerbe kényszerítése az igények vizsgálata nélkül.

**315.** Egy Azure-alkalmazás összes erőforrása ugyanahhoz az üzleti szolgáltatáshoz tartozik, de az elsődleges és helyreállítási komponensek külön régiókban működnek. Az erőforrások életciklusa összehangolt. Melyik csoportosítás lehet szakmailag indokolható?
- a. A management group használata közvetlen erőforrás-konténerként.
- b. Az elsődleges és helyreállítási régió egyetlen Availability Zone-nak tekintése.
- c. Az erőforrások közös resource groupban kezelése, ha az életciklus- és jogosultsági követelmények ezt támogatják.
- d. Az erőforrások kötelező elhelyezése külön Microsoft Entra tenantokban.

**316.** Két adatplatform megfelel az adatmodellnek. Az egyiknél bizonytalan a szükséges bővítmény támogatása, a másiknál magasabb a becsült költség. Mi a helyes döntési irány?
- a. A két jelöltet funkcióik számának összeadásával kell rangsorolni.
- b. A magasabb költségű jelöltet kell választani, mert az ár bizonyítja a megfelelést.
- c. A kompatibilitást és a teljes workload-követelményeket validálni kell a végleges választás előtt.
- d. Az alacsonyabb alapárú jelöltet kell választani a bővítmény vizsgálata nélkül.

**317.** Melyik megfogalmazás választja szét helyesen az ACID consistency és durability tulajdonságát?
- a. A consistency a műveletek együtt sikerülése, a durability az integritási szabályok megőrzése.
- b. A consistency a cache frissessége, a durability a cache-bejegyzés élettartama.
- c. A consistency a szabályos adatállapot megőrzése, a durability a sikeres commit eredményének tartóssága.
- d. A consistency a véglegesített módosítás tartóssága, a durability a párhuzamos műveletek elkülönítése.

**318.** Egy adatplatform privát elérést és titkosítást használ, de az alkalmazás minden felhasználó számára ugyanazzal a széles jogosultsággal olvas adatot. Melyik változtatás kezeli közvetlenül a fennmaradó problémát?
- a. A titkosítási beállítások megtartása és kizárólag a hálózati út rövidítése.
- b. A cache-TTL csökkentése minden adatkörnél.
- c. Az auditnaplózás kikapcsolása a terhelés csökkentésére.
- d. Az alkalmazási adat-hozzáférés és a szükséges jogosultságok célzott szétválasztása.

**319.** Miért nem garantálja egy container image önmagában, hogy az alkalmazás minden környezetben azonosan működik?
- a. Mert az image nem tartalmazhat alkalmazást.
- b. Mert a registry minden indításkor megváltoztatja az alkalmazáskódot.
- c. Mert a külső konfiguráció, szolgáltatások és a futtató platform feltételei továbbra is eltérhetnek.
- d. Mert ugyanaz az image csak egyszer indítható el.

**320.** Egy regionális erőforrás attól még elérhető lehet a világ különböző pontjairól, hogy maga az erőforrás egy meghatározott régióhoz kapcsolódik.
- a. True
- b. False

**321.** Melyik leírás adja meg helyesen a megmaradó sikerarány-alapú hibakeretet?
- a. Az adott időablak megengedett hibáinak száma mínusz az ugyanott bekövetkezett releváns hibák.
- b. Az SLO-célérték mínusz az átlagos CPU-kihasználtság.
- c. A pénzügyi budget mínusz a helyreállítás költsége.
- d. A teljes kérésszám mínusz a sikeres kérések száma.

**322.** Melyik állítás különíti el helyesen az AWS Organizations Rootot az AWS account root userétől?
- a. Az Organizations Root a szervezeti hierarchia legfelső konténere, a root user pedig egy adott account teljes hozzáférésű identitása.
- b. A két fogalom ugyanazt az identitást jelenti eltérő konzolnézetben.
- c. Az Organizations Root közvetlenül workload-erőforrásokat tartalmaz, a root user pedig accountokat csoportosít.
- d. Az Organizations Root egy globális erőforrás, a root user pedig Availability Zone.

**323.** Miért nem teljes rendelkezésre állási megoldás önmagában a load balancer?
- a. Mert kizárólag IP-címet oszt ki.
- b. Mert a közös függőségek, például az adatbázis, továbbra is kieshetnek.
- c. Mert nem használhat több célpéldányt.
- d. Mert minden célpéldányt hibásnak tekint.

**324.** Több kliens ugyanazt a könyvtárstruktúrát szeretné elérni. Melyik storage-modell illeszkedik legjobban?
- a. File storage
- b. Object storage minden esetben
- c. Kizárólag memória
- d. Ideiglenes helyi lemez

**325.** Miért kell külön kezelni a szolgáltatáselérhetőség, a feature-támogatás, a kvóta és a tényleges kapacitás vizsgálatát?
- a. Mert egy szolgáltatás regionális jelenléte nem garantálja a szükséges konfiguráció támogatását, az engedélyezett használati határt vagy a fizikai kapacitás rendelkezésre állását.
- b. Mert a négy fogalom kizárólag eltérő szolgáltatók azonos jelentésű elnevezése.
- c. Mert a kvóta minden esetben nagyobb a tényleges kapacitásnál.
- d. Mert a kapacitás kizárólag a resource group vagy Organizational Unit méretétől függ.

**326.** Stabil alapigény és bizonytalan tesztterhelés mellett vállalásalapú kedvezményt vizsgálsz. Mire alapoznád a műszaki értékelést?
- a. A tesztterhelés automatikus állandónak tekintésére.
- b. Kizárólag a legnagyobb kedvezmény ígéretére.
- c. A teljes jelenlegi kapacitás változatlan lekötésére használatvizsgálat nélkül.
- d. A bizonyítható alapigényre, előrejelzésre és konstrukciós feltételekre.

**327.** Melyik állítás írja le helyesen a latency és throughput különbségét?
- a. A latency a művelet várakozási ideje, a throughput az időegység alatt átvitt adatmennyiség
- b. A két fogalom minden workloadnál azonos értéket ad
- c. A latency redundancia, a throughput titkosítás
- d. Mindkettő kizárólag kapacitást jelent

**328.** Egy távoli storage-másolat olvasható, de új adatok nem írhatók bele. Milyen működési állapotról van szó?
- a. Részleges, csak olvasási üzleti működésről
- b. Teljes aktív-aktív működésről
- c. Automatikus adatvesztésről
- d. Korlátlan írási rendelkezésre állásról

**329.** Egy adatbázist elérő alkalmazásnak csak olvasásra van szüksége, de módosítási és törlési jogosultságot is kapott. Melyik célzott változtatás indokolt?
- a. A jogosultságok szűkítése a szükséges műveletekre.
- b. Nagyobb adatbázis-kapacitás biztosítása.
- c. Hosszabb auditnapló-megőrzés, a jogosultságok változatlanul hagyásával.
- d. Rövidebb cache-TTL beállítása.

**330.** Mit jelöl a kvóta a bemutatott kapacitáskezelési összefüggésben?
- a. Az engedélyezett fogyasztás határát
- b. A szolgáltatás minden időpontban szabad fizikai kapacitását
- c. Az alkalmazás indulásának maximális idejét
- d. A már működő alkalmazáspéldányok garantált számát

**331.** Miért nem egyenértékű két megoldás pusztán az alacsonyabb ár alapján?
- a. A költségoptimalizálásnál a szolgáltatási cél nem vizsgálandó.
- b. Azonos működési, teljesítmény- és megbízhatósági követelmény mellett kell összevetni őket.
- c. Az olcsóbb megoldás automatikusan azonos szolgáltatási szintet ad.
- d. A redundancia kizárólag pénzügyi tétel, nem működési követelmény.

**332.** Egy privát alkalmazás NAT-on keresztül kifelé kér adatot. Miért nem azonos a visszaérkező válasz egy tetszőleges új, kívülről kezdeményezett kapcsolattal?
- a. Mert a válasz mindig új publikus szervert hoz létre.
- b. Mert a kifelé indított kérésre nem érkezhet válasz.
- c. Mert a NAT minden bejövő portot megnyit.
- d. Mert a válasz a kifelé indított kapcsolathoz tartozik, míg az új bejövő kapcsolat külön elérési döntés.

**333.** Mit határoz meg elsősorban az útvonal?
- a. A kérés titkosítását.
- b. A célpéldány alkalmazásverzióját.
- c. A felhasználó jogosultságát.
- d. A forgalom továbbításának irányát.

**334.** Egy konténeres API cserélhető replikákkal működik, a tartós állapot külső tárolóban van. Több replika indítása után a közös adatforrás korlátozza az átbocsátást. Melyik értelmezés helyes?
- a. A több replika miatt a közös adatforrás már nem függőség.
- b. A külső állapottárolás garantálja a korlátlan horizontális skálázást.
- c. Az állapot életciklusa megfelelően elválhat a compute-tól, de a közös függőség kapacitása továbbra is korlát lehet.
- d. A replika cserélhetősége automatikusan bővíti az adatforrást.

**335.** Több elkülönített alkalmazáshálózat közös DNS- és hibrid kapcsolati szolgáltatást használna. Melyik topológiát érdemes mérlegelni?
- a. Hub–spoke mintát.
- b. Egyetlen közös Security Groupot minden platformon.
- c. Minden adatbázis közvetlen publikálását.
- d. A címtartományok szándékos átfedését.

**336.** Melyik kifejezés írja le azt, hogy az adatok mely országban vagy földrajzi területen tárolhatók és dolgozhatók fel?
- a. Resource ID
- b. Vendor lock-in
- c. Adatrezidencia
- d. Availability Zone ID

**337.** Melyik állítás írja le helyesen a zonális és a zone-redundant erőforrás közötti különbséget?
- a. A két fogalom teljesen azonos, kizárólag a szolgáltatók elnevezése tér el.
- b. A zonális erőforrás globális, a zone-redundant erőforrás kizárólag regionális elérési ponttal rendelkezik.
- c. A zonális erőforrás egy konkrét Availability Zone-hoz kötődik, míg a zone-redundant szolgáltatás több zóna infrastruktúráját használhatja.
- d. A zonális erőforrás több régióban, a zone-redundant erőforrás egyetlen adatközpontban működik.

**338.** Egy Kubernetes Deployment kívánt példányszámát növelik, de az új podok nem helyezhetők el a rendelkezésre álló worker node-okon. Mit kell elsőként a kívánt állapot és a tényleges futás különbségeként értékelni?
- a. A registryben található tagek betűrendjét.
- b. A kívánt példányszám automatikus törlését a definícióból.
- c. A podok erőforrásigényét, az elhelyezési feltételeket és a cluster rendelkezésre álló kapacitását.
- d. A Service nevét, mert az önmagában fizikai kapacitást teremt.

**339.** Egy vállalat olyan helyi rendszert működtet, amely internetkapcsolat nélkül is elérhető kell maradjon. Melyik megállapítás helyes?
- a. A SaaS automatikusan megoldja a követelményt
- b. A rendszerhez nincs szükség infrastruktúrára
- c. Az on-premises komponens indokolt lehet
- d. Mindenképpen public cloudra kell váltani

**340.** Miért csökkenhet a PaaS használatakor az infrastruktúra-üzemeltetési teher?
- a. Az ügyfél minden biztonsági felelőssége megszűnik
- b. Az ügyfél alkalmazáskódja megszűnik
- c. A szolgáltatás nem használ infrastruktúrát
- d. A szolgáltató az operációs rendszert és a futtatási platformot is kezeli

**341.** Miért érdemes a hálózati címtartományt a későbbi összekapcsolásokra tekintettel megválasztani?
- a. A subnetek később nem tartalmazhatnak erőforrást.
- b. A DNS kizárólag azonos tartományokkal működik.
- c. Az átfedő tartományok nehezíthetik a hálózatközi kommunikációt.
- d. A CIDR automatikusan titkosít.

**342.** Application Insightsban sikeres HTTP-válasz látszik, de a jelentkezés nem rögzült. Az adatbázis saját naplói nincsenek begyűjtve. Mi indokolt?
- a. Az Application Insights automatikusan tartalmazza az adatbázis minden belső eseményét.
- b. Az üzleti mentést külön ellenőrizzük, a kérésfüggőséget vizsgáljuk, és tisztázzuk a hiányzó platformadatokat.
- c. A hiányzó adatbázisnapló bizonyítja, hogy nem történt adatbázisművelet.
- d. A HTTP-siker alapján a mentést bizonyítottnak tekintjük.

**343.** Melyik állítás jellemzi a community cloud modellt?
- a. Kizárólag egyetlen magánszemély használja
- b. Mindig több public szolgáltatót kapcsol össze
- c. Bárki számára nyilvános ügyféladatokat biztosít
- d. Közös követelményekkel rendelkező szervezetek közössége használja

**344.** Egy vállalat a földrajzilag legközelebbi régiót tervezi használni. A vállalati telephelyről végzett mérések azonban egy távolabbi, szintén megfelelő régiónál alacsonyabb késleltetést mutatnak. Melyik döntés követi az előadásban bemutatott modellt?
- a. A távolabbi régió automatikus kizárása.
- b. A mért latency figyelembevétele a többi követelménnyel együtt.
- c. A legközelebbi régió automatikus kiválasztása.
- d. A hálózati teljesítmény figyelmen kívül hagyása.

**345.** Miért lehet indokolt külön queue-t használni egy pub/sub előfizetés mögött?
- a. Mert az eseményterjesztés mellett az adott fogyasztói ág terhelését is kezelni kellhet.
- b. Mert a queue minden előfizetőnek közös feldolgozási állapotot biztosít.
- c. Mert a queue megszünteti az előfizetők közötti funkcionális különbséget.
- d. Mert így a topic automatikusan adatbázisként működik.

**346.** Egy vállalat több DR-stratégiát hasonlít össze. A legfontosabb üzleti szempont az alacsony RTO, de a folyamatos erőforrásköltség is korlátozott. Mi a helyes döntési megközelítés?
- a. A célértékeket, készen tartott kapacitást, aktiválási munkát és költséget együtt kell értékelni.
- b. A DR-modellt kizárólag a rendelkezésre álló régiók száma határozza meg.
- c. Mindig a legolcsóbb mentési modellt kell választani.
- d. Mindig teljes kapacitású Active-Active modellt kell alkalmazni.

**347.** Egy termékadatot az adatbázisban módosítottak, de a cache invalidálása sikertelen volt. Az olvasók még a régi értéket kapják. Melyik állítás helyes?
- a. Az adatbázis helyes állapota mellett is maradhat elavult cache-másolat.
- b. A probléma kizárólag a relációs séma hiányából eredhet.
- c. A cache hit bizonyítja, hogy az adatbázis-módosítás sikertelen volt.
- d. A managed cache automatikusan visszavonja az adatbázis-módosítást.

**348.** Melyik meghatározás írja le legpontosabban a tárolási követelményprofilt?
- a. Az adatkör, elérési modell, teljesítmény, életciklus, védelem, integráció és költség összefoglalása
- b. Kizárólag a maximális kapacitás megadása
- c. A kiválasztott termék nevének rögzítése
- d. A tárolt fájlok alfabetikus listája

**349.** Miért nem elegendő az API-platformok közös gateway-szerepe a teljes szolgáltatási megfeleltetéshez?
- a. Mert az összehasonlítás csak az API-k elnevezése alapján végezhető el.
- b. Mert minden gateway azonos management plane-t és developer portalt biztosít.
- c. Mert a közös gateway-szerep kizárja az API-k publikálását.
- d. Mert az életciklus-, policy-, hálózati és backend-integrációs követelmények eltérő képességeket igényelhetnek.

**350.** A teszt- és éles környezet fogyasztását szeretnéd elkülöníteni. Melyik megoldás támogatja ezt?
- a. A naplózás egységes kikapcsolása.
- b. Következetes környezet- és tulajdonoscímkék.
- c. Minden erőforrás azonos riasztási küszöbe.
- d. A két környezet SLO-jának összevonása.

**351.** Miért nem tekinthető az edge helyszín automatikusan teljes cloud régiónak?
- a. Mert az edge helyszín minden esetben az ügyfél saját adatközpontja.
- b. Mert az edge helyszín általában korlátozottabb szolgáltatáskészlettel és kapacitással rendelkezik, és gyakran egy szülő régióhoz kapcsolódik.
- c. Mert edge helyszínen semmilyen adatfeldolgozás nem végezhető.
- d. Mert az edge helyszín kizárólag számlázási kedvezményt jelent.

**352.** Egy vállalat több Azure subscriptionre ugyanazt a régióhasználati szabályt szeretné alkalmazni. Melyik szint a legmegfelelőbb?
- a. Availability Zone
- b. Management group
- c. Egyetlen Azure resource
- d. Egyetlen virtuális gép

**353.** Mit jelent az ephemeral compute a tananyagban?
- a. Minden konténerben lévő adat szükségszerűen törlendő.
- b. A futtató példány nem az üzleti adatok egyetlen tartós megőrzési helye.
- c. A futtató példány soha nem használ üzleti adatot.
- d. Az alkalmazásnak nem lehet tartós állapota.

**354.** Egy gazdátlan tesztkörnyezet hónapok óta költséget termel. Melyik kontrollkombináció kezelné legjobban a problémát?
- a. Az erőforrás korlátlan megtartása
- b. Tulajdonosi tag, lejárati tag és szabályozott resource lifecycle
- c. Teljes adminisztrátori hozzáférés minden felhasználónak
- d. A költségriportok kikapcsolása

**355.** Miért nem szűnik meg az ügyfél biztonsági felelőssége SaaS használatakor?
- a. A SaaS minden környezetben on-premises
- b. A szolgáltató nem kezel infrastruktúrát
- c. A SaaS nem használ identitásokat
- d. A felhasználók, hozzáférések, adatok és saját konfiguráció továbbra is ügyfélfeladat lehet

**356.** Miért kell a HA-tervezés során a megmaradó kapacitást is vizsgálni?
- a. Mert minden alkalmazáspéldánynak mindig azonos terhelést kell kapnia.
- b. Mert a HA kizárólag a virtuális gépek számától függ.
- c. Mert a működő példányoknak kiesés után is ki kell szolgálniuk a szükséges terhelést.
- d. Mert a mentési kapacitás automatikusan alkalmazáskapacitássá alakítható.

**357.** Melyik művelet tartozik a horizontális kapacitásbővítéshez?
- a. A futtató példányok számának növelése
- b. Egy példány memóriájának növelése
- c. A guest OS frissítése
- d. Egy példány nagyobb konfigurációra váltása

**358.** Miért kell egy multi-region DR-tervben az alkalmazási függőségeket a célrégióban is vizsgálni?
- a. Mert a DR-terv kizárólag virtuális gépek indításából állhat.
- b. Mert a függőségek csak a mentési retentiont befolyásolják.
- c. Mert a replikált adatok önmagukban nem biztosítják az alkalmazás működőképességét.
- d. Mert a másodlagos régió nem használhat hálózati szolgáltatásokat.

**359.** Miért jelent az on-premises modell nagyobb közvetlen felelősséget?
- a. A szolgáltató kezeli az összes alkalmazást
- b. A kapacitás mindig automatikusan változik
- c. Nincs szükség üzemeltetési csapatra
- d. A szervezet több technológiai réteget maga kezel

**360.** Egy szolgáltatás RPO-célja 30 perc. A helyreállítás során 20 percnyi adatvesztést állapítanak meg. Melyik következtetés helyes?
- a. Az adatvesztési cél nem teljesült.
- b. A mentési retention nem megfelelő.
- c. A helyreállítási időcél is biztosan teljesült.
- d. Az adatvesztési cél teljesült.

**361.** Melyik Azure-elem kapcsolódik a webes kérések alkalmazási szintű irányításához?
- a. VNet-peering.
- b. NAT Gateway.
- c. Application Gateway.
- d. NSG.

**362.** Melyik állítás jellemzi helyesen a klasszikus inkrementális mentési modellt?
- a. Minden mentés a kijelölt adathalmaz egészét tartalmazza.
- b. A mentés folyamatosan működő tartalék adatbázist biztosít.
- c. A mentés az előző mentés óta történt változásokat rögzíti.
- d. Minden mentés az utolsó teljes mentés óta történt változásokat tartalmazza.

**363.** Egy éles tartalék példány átlagos terhelése alacsony. Milyen döntés indokolt?
- a. A tartalék automatikus pazarlásnak minősítése.
- b. Azonnali törlés az átlagos CPU alapján.
- c. A monitoring leállítása a tartalék példányon.
- d. A kiesési, csúcsterhelési és helyreállítási igény vizsgálata a csökkentés előtt.

**364.** Egy alkalmazás új kódverzióját a meglévő futtatási környezetbe helyezik. Melyik művelet történt?
- a. Fault Domain kialakítása
- b. Guest OS-leállítás
- c. Alkalmazásdeployment
- d. Vertikális skálázás

**365.** Melyik fogalmi besorolás következetes a compute-modellek összehasonlításában?
- a. Konténer: kapacitáskvóta; Kubernetes: runtime-verzió; serverless: zónaelhelyezés.
- b. Konténer: futtatási egység; Kubernetes: orkesztrációs platform; serverless: működési modell.
- c. Konténer: fizikai gép; Kubernetes: guest OS; serverless: backupmodell.
- d. Konténer: orkesztrációs platform; Kubernetes: image-formátum; serverless: tárolási réteg.

**366.** Egy rendszer webes API-ból és fájleseményre induló feldolgozásból áll. Az API több példány között kiszolgálható; a feldolgozás eredménye külső tárolásba kerül. Melyik terv követi a követelményalapú döntést?
- a. A függvényjelölt miatt az API válaszidő- és runtime-követelményeit elhagyjuk.
- b. Az eltérő compute-modellek megszüntetik a közös hozzáférési és adatfüggőségeket.
- c. Mindkét rész ugyanazt a modellt kapja, kizárólag a közös adatforrás miatt.
- d. A két workload külön jelöltet kaphat; a hosting, állapot, integráció és teljes költség együtt ellenőrizendő.

**367.** Egy alkalmazásnál az egyik VM kiesésekor a másik példány átveszi a forgalmat, de az átállás alatt rövid megszakítás jelentkezik. Melyik fogalom írja le legjobban a kialakítást?
- a. Garantáltan megszakításmentes Fault Tolerance.
- b. Kizárólag Backup and Restore.
- c. Hosszú távú adatarchiválás.
- d. Failoverrel működő High Availability.

**368.** Miért nem elegendő egy identity-based Allow szabály önálló vizsgálata?
- a. Mert az Allow mindig automatikusan explicit Denyra változik
- b. Mert kizárólag a resource neve határozza meg a hozzáférést
- c. Mert identity-based policy nem tartalmazhat Permissiont
- d. Mert az összes alkalmazandó policy-t és korlátozást, köztük az explicit Deny szabályokat is értékelni kell

**369.** Egy vállalat minden workloadját több szolgáltatónál szeretné párhuzamosan futtatni pusztán a lock-in elkerülésére. Melyik kockázatot kell leginkább mérlegelnie?
- a. A többlet architekturális és üzemeltetési összetettséget
- b. A measured service hiányát
- c. A fizikai infrastruktúra megszűnését
- d. A felhasználói felelősség eltűnését

**370.** Egy másik AWS account principalja rendelkezik forrásoldali Allow szabállyal, de a céloldalon nincs megfelelő trust vagy resource-based engedély. Mi várható?
- a. A hozzáférés megtagadható
- b. Automatikus teljes hozzáférés
- c. A principal root userré válik
- d. Az erőforrás automatikusan más régióba kerül

**371.** Egy alkalmazás közös Windows fájlútvonalat igényel. Melyik feltételt kell elsőként ellenőrizni egy cloud file szolgáltatásnál?
- a. A block volume IOPS-át
- b. Az SMB-támogatást és a klienskompatibilitást
- c. A Glacier restore-időt
- d. Az object lifecycle-szabályokat

**372.** Egy DR-próbán az alkalmazás 40 perc alatt helyreáll. Az RTO-cél 30 perc, az RPO-cél 20 perc, a tényleges adatvesztés 10 perc. Melyik értékelés helyes?
- a. Mindkét cél teljesült.
- b. Az RTO teljesült, az RPO nem.
- c. Az RPO teljesült, az RTO nem.
- d. Egyik cél sem teljesült.

**373.** Egy workloadnál kötelező a meghatározott operációsrendszer-kontroll és egy megfelelőségi követelmény teljesítése. Egy PaaS-jelölt kevesebb üzemeltetési munkát ígér, de a szükséges kontroll támogatása még nem igazolt; egy VM-jelölt nagyobb kezelési feladatot jelent. Melyik döntés követi a tanult workload-alapú módszert?
- a. A megfelelőségi követelményt figyelmen kívül hagyják, majd csak az árat hasonlítják össze.
- b. A PaaS-t választják pusztán azért, mert kevesebb üzemeltetési munkát ígér.
- c. A VM-et választják pusztán azért, mert az absztrakciós létrán alacsonyabb szinten áll.
- d. Először igazolják, mely jelöltek teljesítik a kötelező kontroll- és megfelelőségi feltételeket; az alkalmasakat ezután üzemeltetés és költség szerint mérlegelik.

**374.** Egy ügyfélportál felhasználói a webes felületet használják; a rendelési adatokat az alkalmazás olvassa. Melyik közvetlen felhasználói kapcsolat indokolt?
- a. Felhasználó → NAT Gateway.
- b. Felhasználó → webes belépési pont.
- c. Felhasználó → minden subnet.
- d. Felhasználó → adatbázis.

**375.** Melyik policy határozza meg, hogy ki vagy mi veheti fel az IAM Role-t?
- a. Retention policy
- b. Cost policy
- c. Naming policy
- d. Trust policy

**376.** Egy Kubernetes-csapat külön logikai területre szeretné szervezni két projekt objektumait ugyanazon a clusteren belül. Melyik Kubernetes-fogalmat vizsgálja meg először?
- a. Container digest
- b. Namespace
- c. Snapshot
- d. VM-image

**377.** Egy adatplatformhoz megfelelő jogosultságok tartoznak, de egy korábbi hozzáférési eseményt nem lehet rekonstruálni. Melyik kontrollterület hiányossága merül fel közvetlenül?
- a. Partíciótervezés.
- b. Auditnaplózás.
- c. Tranzakciós atomicity.
- d. Cache-élettartam.

**378.** Melyik állítás írja le pontosan a CloudWatch és CloudTrail eltérő szerepét és határát?
- a. Mindkettő ugyanazt az adatot gyűjti, csak más felületen.
- b. A CloudTrail minden üzleti naplót kivált, a CloudWatch minden művelet szereplőjét rögzíti.
- c. A CloudWatch-tünet és CloudTrail-esemény egybeesése önmagában gyökérok-bizonyíték.
- d. Működési adat és támogatott műveleti előzmény egészítheti ki egymást; a lefedettség konfigurációfüggő.

**379.** Egy regisztrációs szolgáltatás egészségellenőrzése csak a gép elérhetőségét vizsgálja. Az üzleti művelet hibás, a gép azonban válaszol. Mi következik ebből?
- a. Az ellenőrzés eredménye nem bizonyítja az üzleti funkció működését.
- b. A válaszoló gép minden alkalmazásfunkciója biztosan megfelelő.
- c. A hiba csak új zóna létrehozásával vizsgálható.
- d. A load balancer automatikusan kijavítja az üzleti logikát.

**380.** Melyik következtetés helyes a konténeres csomagolásból?
- a. A tartós adatkezelés többé nem szükséges.
- b. A host karbantartása minden esetben megszűnik.
- c. Az alkalmazás automatikusan Kubernetes-workloaddá válik.
- d. A hostingmodellt továbbra is ki kell választani.
