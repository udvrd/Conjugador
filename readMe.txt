Szkript nyelvek projektmunka
Udvardi István - ZL8BUF

Spanyol Igeragozó

Ez a PyCharmbanban Python nyelven készült program egy egyszerű grafikus felületen keresztül segít a spanyol igék jelen idejű ragozásában. A felhasználó magyarul vagy spanyolul is megadhat egy igét, a program pedig felismeri, lefordítja, majd kiírja a megfelelő ragozást, egyszerű vizuális visszajelzéssel kiegészítve.

Spanyol igeragozás röviden:
A spanyol igéket három fő csoportba soroljuk a főnévi végződésük alapján: -ar, -er, -ir. A jelen idejű ragozás leveszi a végződést(ar,er,ir) és a hat személyre(én, te, ő...) egyedi ragot rendel a végződés alapján.
Személyes névmások: yo(én), tú(te), él/ella(ő), nosotros(mi), vosotros(ti), ellos/ellas(ők)
Ragok:
-ar esetén -o -as -a -amos -áis -an
-er esetén -o -es -e -emos -éis -en
-ir esetén -o -es -e -imos -ís -en
A visszaható(reflexív) igék a főnévi igenévként se végződést kapnak, ami azt jelzi, hogy a cselekvés visszahat az alanyra: vestir=öltöztetni, vestirse=öltözni, mint önmagát öltöztetni. Ragozásnál annyit számít, hogy az ige elé megjelenik a visszaható névmás, ami: me, te se, nos, os, se.
Rendhagyó igék esetén két fő eltérés fordulhat elő:
Tőhangváltás: az igető magánhangzója megváltozik (pl. pensar → pienso, e → ie)
Ragváltozás: a szabályos rag helyett módosított alak jelenik meg (pl. tener → tengo)

Az igék ragozása a https://www.e-spanyol.hu/igeragozas.php weboldalon ellenőrizhető.

Beépített függvények:
tkinter: Beépített GUI-könyvtár, a grafikus felület (ablak, gombok, beviteli mezők, vászon) megjelenítéséhez és kezeléséhez.
pandas: Táblázatos adatok (pl. ige-szótár) betöltéséhez és kezeléséhez
re: Reguláris kifejezések feldolgozásához, például igealakok elemzéséhez
openpyxl: Excel-fájlok (.xlsx) beolvasásához, mert a ragozási adatok Excelben vannak tárolva

Saját modulok:
translate.py - fordítás
ui_conjugate.py – ragozás
stem_utils.py - tőhangváltás
draw.py – rajzolás

main.py
output():
A fő vezérlőfüggvény, amely:
Beolvassa a beírt igét
Eldönti, hogy magyar vagy spanyol ige-e
Lefordítja az igét (translate függvényekkel)
Külön kezeli az haber imperszonális igét
Meghívja a ragozómodult (ui_conjugate_presente)
Megjeleníti a ragozást és a megfelelő arckifejezést (mosolygó, szomorú vagy gondolkodó smiley)
insert_nh(): Egyetlen „ñ” karaktert szúr be a beviteli mezőbe, és visszaadja a fókuszt a mezőnek (ha spanyolul szeretnénk megadni az igét és szükség lenne a betűre)
Objektumokok:
tk.Entry	Ige beviteli mező
tk.Button	„Ragozás” gomb, „ñ” gomb és "Kilépés" gomb
tk.Label	Eredmény és ragozás megjelenítése
tk.Canvas	Smiley arc kirajzolása (pozitív, negatív vagy gondolkodó visszajelzés)
tk.Tk()	A fő ablak inicializálása, címmel és mérettel

draw_smiley() – sikeres felismerés és ragozás esetén
draw_sad_smiley() – ha nincs találat vagy hibás a bemenet
draw_thinking_smiley() – ha a szó nem szerepel a szótárban, de ragozható

translate.py modul:
Ez a modul felelős a magyar és spanyol igék közötti fordításért. A fordítási adatokat egy Excel-fájl (verbos.xlsx) tartalmazza, amelynek első oszlopa a magyar igéket, a második pedig a spanyol megfelelőiket, a harmadik a rendhagyósági besorolást tartalmazza. A beolvasás openpyxl motorral történik. A két translate függvény kisbetűsít, tisztít, és a főnévi igenevek között vált.

draw.py:
Ez a modul felelős a grafikus felületen megjelenő arckifejezések kirajzolásáért. A tkinter.Canvas objektumra rajzol különböző hangulatú smiley-arcokat, attól függően, hogy a ragozás sikeres, sikertelen vagy bizonytalan volt.

stem_utils.py:
Ez a modul a spanyol igék szótövének módosításáért felelős a tőhangváltós igék esetében. Megkeresi a keresett betűből az utolsót és lecseréli a kívánt betű(k)re a megadott személyeknél (tőhangváltás esetén T/1 és T/2 személyeknél az eredeti alak marad). Van egy plusz szabály az oler ige miatt (szagolni, szagot árasztani), ami tőhangváltós, de mivel az első karakter változik, így bekerül egy +h betű az ige elejére.

ui_conjugate.py:
A program lelke, a ragozómodul. Ez a modul felelős a spanyol igék jelen idejű ragozásáért, beleértve a szabályos és rendhagyó igéket is. A ragozás logikája az ige szótövének és a megfelelő személyragoknak és személyeknek az összeillesztésén alapul.
Osztály:
UISpanishVerb
Ez az osztály reprezentál egy spanyol igét, és előkészíti a ragozáshoz szükséges adatokat.
Attribútumok:
infinitive Az ige főnévi alakja (pl. comer) 
is_reflexive Logikai érték, visszaható-e az ige 
group Az ige típusa: ar, er, ir 
irregular A rendhagyóságot jelző címkék listája (pl. ["eie", "g"])
stemPresente A jelen idejű ragozáshoz használt szótövek listája (6 elem, személyenként)
metódusok:
get_group() Meghatározza az ige csoportját a végződés alapján
get_irregular_tags() Beolvassa az Excel-szótárból az adott ige rendhagyósági címkéit
get_stem_presente() Elkészíti a jelen idejű szótövek listáját, figyelembe véve a rendhagyóságokat

Függvények
ui_conjugate_presente(verb_es) elvégzi egy spanyol főnévi ige jelen idejű ragozását 6 személyre szövegként formázva
Működés:
Létrehoz egy UISpanishVerb példányt
Lekéri a személyeket (yo, tú, stb.)
Összeállítja a ragozott alakokat: személy + szótő + rag
get_persons(verb) Visszaadja a személyes névmásokat, reflexív igék esetén a visszaható névmásokat is hozzáadja
get_endings(verb) Visszaadja a megfelelő jelen idejű személyragokat az ige csoportja és rendhagyósága alapján, kezeli az olyan különleges ragokat is, mint oy, eo, ímos, stb.


