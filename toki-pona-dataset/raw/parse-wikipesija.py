import xml.etree.ElementTree as ET
import re

pages = '''
ma Sakalin
jan Alesante Pusin
jan Semu Ku
toki pona
toki sin
jan Jesu
lipu sewi Pipija
nasin sewi pi jan Jesu
nasin sewi Jejuta
lipu sewi TaNaKa
toki Iwisi
jan Mose
jan sewi
nasin sewi Siki
nasin sewi Puta
lipu toki Nikija
sitelen tawa Pelejewana
soweli pi nena mama
pona
lipu
mi
ni
jan
toki
tawa
lon
ala
tenpo
sona
kama
wile
ma
lili
ken
nimi
taso
pilin
tan
ike
pali
jo
tomo
kepeken
suli
lukin
sewi
sitelen
tu
ante
seme
pana
sama
musi
suno
nasin
wan
ijo
en
kulupu
telo
kin
lawa
pini
ali
soweli
moku
luka
sin
nanpa
meli
ilo
ale
anu
sike
kalama
nasa
moli
wawa
pakala
kasi
weka
mama
awen
kon
poka
utala
mije
olin
pimeja
lape
insa
anpa
kiwen
seli
mani
waso
kute
linja
len
sijelo
poki
mun
suwi
akesi
pipi
open
lete
palisa
loje
kili
ko
walo
supa
kule
sinpin
kala
uta
nena
noka
monsi
oko
lupa
mu
unpa
jaki
esun
jelo
laso
pan
selo
pu
alasa
kipisi
namako
monsuta
leko
powe
po
majuna
kijetesantakalu
toki Sumi
jan Ape Sinso
jan Atatu
jan Jako Kin
jan Ajesilu
jan Akamenon
jan Alitotele
jan Atoje Ite
jan Eloto
jan Emanu Makon
jan Eneja
jan esun
jan Ilan Mu
jan Isa Nuton
jan Ka Maku
jan Kajekosu Sapusi Sowapi
jan Kaka
jan Kene Kupa
jan Kin Sonilu
jan Konpusi
jan Lase
jan lawa Konsantin nanpa tu pi ma Elina
jan li kama lon
jan Liki Seme
jan lili
jan lon lupa
jan Lutaki
jan Makokan
jan Mali Kuki
jan Mata Pa
jan Melani Masine
jan Mike Sakeson
jan Mike Te Sewante
jan Mosata
jan Muwama
jan Muwama Ali
jan No Mujon
jan Okuse
jan Okusi
jan Omelo
jan Otesiju
jan Owen Kentu
jan Papo Pikaso
jan Paton
jan pi tomo ala
jan Powi Sonsen
jan Puta
jan Sa Tawin
jan Seli Sapin
jan Si Sinpin
jan Sin Se Jun
jan Sinpo Wale
jan So Wasinton
jan Sojan Sepasijen Pake
jan sona
jan Sopoke
jan soweli
jan Susin Tuto
jan Tana Tan
jan Totoje
jan Wakon
jan Wasimi Pusin
jan Winko Sa
jan Kankunijeso
jan lawa Kulu nanpa tu
jan Leke
jan Ma Setun
jan Mikije Kopeso
jan Nelenta Mosi
jan Non Sonki
jan Ota Jukijo
jan Petan Meje
jan Pije
jan Sonja
jan Tante
akesi linja
akesi suli mute pi moku e ma tomo
kulupu jan Alapi
kulupu jan An
ante toki
ijo lili
ilo AIM
ilo ChatGPT
ilo jan
ilo Juni
ilo kon lawa
ilo kon pi tawa anpa
ilo Linu
ilo LiveJournal
ilo LMMS
ilo musi
ilo nanpa
ilo pi kalama musi
ilo pi sitelen weka
ilo Pilipili
ilo Pokalo
ilo Sulon
ilo tan kulupu KDE
ilo Tujolinko
ilo unpa
ilo utala Pola
insa lawa
jaki lili
musi Jali Kulese
jo jan
jo lili
kala pi poki insa mama
kalama musi Kalameletansen
kalama musi lawa pi ma Losi
sitelen musi suli Kalewala
telo suli Kalipi
kama kulupu Ijoko
kama sona
kama suli ike pi poki sijelo
kipisi ma Ilan
kiwen kasi
ko lete
kon ike
kon Itosen
kon Okisen
kon sewi jan
kulupu jan Elena
kulupu jan Jejuta
kulupu jan Lasena
kulupu jan pi tan sama
kulupu jan Sami
kulupu jan Sine
kulupu Katolika
kulupu Lepewa pi ma Kanata
kulupu ma Nosen
kulupu mama toki
kulupu nanpa Tesima
kulupu Nintento
kulupu pi nasin lawa
kulupu pi sijelo wan
kulupu Sinsi
kulupu utala
lawa kulupu
len noka
linja pona
lipu Anale
lipu Komon
lipu pi jan Ton Kikote pi ma La Mansa
lipu pi kon nasa
lipu pi ma pona sin
lipu pu
lipu sona pi nanpa ante pi wan ijo Atomo
lipu sona Pitanika
lipu Wasijemensi
lipu Wikiwajase
lipu Wisonali
kulupu toki Lowan
lupa mama
mani Elopa
meli pi olin meli
mije pi olin mije
mije sijelo
mun Mekuli
mun Posima Sentawi
mun seli
mun tawa
musi Antateje
musi ilo
musi kalama
musi Kiwen Lipu Kipisi
musi lipu
musi nanpa
musi Opa
musi Papa I Ju
musi sike
musi supa
musi utala Olinpi
musi utala Tekanto
nanpa pi sewi pini ala
nanpa weka
nasin anpa pi nena ma
nasin Esitensalin
nasin Konpusi
nasin kulupu
nasin lawa nimi
nasin mani
nasin pi jan sewi ala
nasin sewi
nasin sewi Intu
nasin sewi Isilan
nasin sewi Kantonpe
nasin sewi Pawaji
nasin sitelen Apapeto
nasin telo Amasona
nasin telo Misisipi
nasin telo Tona
nasin To
pakala pilin
pali kasi
pan suwi
pana sona
pimeja mun
pini ala
sike e suno
sike kipisi kasi
sike wan
sitelen a
sitelen Alapi
sitelen Emosi
sitelen lape monsuta
sitelen lape sona
sitelen nanpa Akan
sitelen nanpa Alapi
sitelen Parahumans
sitelen pi jan Pepa en soweli Kawa
sitelen pi toki pona
sitelen pona pi jan Mimoku
sitelen sitelen
sitelen tawa
sitelen tawa "utala pi ma lon telo pi sitelen lape"
sitelen tawa Metopoli
sitelen tawa pi lon ala
sitelen tawa pi lon ala pi ma Nijon
sona lon
sona ma
sona mun
sona pi nasin ijo
sona pi toki tawa pana pona
sona sona
soweli alasa pi walo pimeja
soweli li pona lon telo li moku e kasi
soweli lili pi linja kiwen
soweli pi lawa sewi
soweli pi nena linja
soweli poki
soweli suwi lape pi kasi suli
suwi lete
tawa lon kon Precision Air nanpa 494
tawa musi
tawa suli pi jaki Kolona
telo pimeja pi pali seli
telo sijelo loje
telo suli Alansi
telo suli Mesitelane
telo suli Pasipi
telo wawa
lipu lawa pi ken jan lon ma Mewika
ma Mewika
ma lawa
ma Anku
ma Antekapaputa
ma Awisi
ma Ekuwato
ma Enkon
ma Esawato
ma Kanpusi
ma Kata
ma Katelo
ma Kenja
ma Kajana
ma Kijana pi ma Kanse
ma Kilipasi
ma Kolonpija
ma Konko pi ma tomo Kinsasa
ma Kosalika
kulupu ma Elopa
ma Kupa
ma Lowasi
ma Aja
ma Akan
ma Alan
ma Alan lete
ma Alensina
ma Ankola
ma Antola
ma Apika
ma Asepajan
ma Elina
ma Eliteja
ma Epanja
ma Esalasi
ma Esi
ma Ilakija
ma Ilan
ma Imala
ma Inli
ma Intonesija
ma Isale
ma Isilan
ma Italija
ma Itejopija
ma Jamanija
ma Jeloson
ma Juke
ma Jukolawija
ma Kakasi
ma Kalasi
ma Kaletoni sin
ma Kamelun
ma Kana
ma Kanata
ma Kanpija
ma Kanse
ma Kantun
ma Kapon
ma Kapuwesi
ma Kasatan
ma Katemala
ma Keneta
ma Kilisa
ma Kine
ma Kinejekatolija
ma Kinepisa
ma Kinli
ma Kiposi
ma Komo
ma Konko
ma Konko pi ma tomo Pasawi
ma Kosiwa
ma Kuse Kiposi
ma Lajo
ma Lanka
ma Lapanuwi
ma Lapewija
ma Lawi
ma Lijatuwa
ma lili
ma Lipija
ma Lisensan
ma Lominija
ma Lowensina
ma Lusepu
ma Lusi
ma Luwanta
ma Malakasi
ma Malasija
ma Malawi
ma Mali
ma Malipe
ma Manin
ma Masu
ma Mata
ma Mesiko
ma Mijama
ma Monko
ma Mosanpi
ma Motowa
ma Nalo
ma Namipija
ma Nijon
ma Nise
ma Nosiki
ma Nusilan
ma Opeki
ma Oselija
ma Pakisan
ma Palani
ma Palata
ma palisa Kasa
ma Panama
ma Panla
ma Pantelen
ma Papuwanjukini
ma Pela
ma Peli
ma Penen
ma Penesuwela
ma Pesije
ma Peson
ma pi kasi suli
ma pi telo lili
ma Pilisin
ma Pinesowi
ma Pisi
ma Polipija
ma pona
ma Posan
ma Posuka
ma Potuke
ma Powija
ma Pukina Paso
ma Pulunsi
ma Punawi
ma Sajusi
ma Sameka
ma Samowa
ma San Malino
ma Sanpija
ma Santapiken
ma Sasali
ma Sate
ma Sato Sutan
ma Satome en ma Pinsipe
ma Seki
ma Sekolowenko
ma Seneka
ma Sensa
ma Sesele
ma Sesesele
ma Sijelalijon
ma Sikimen
ma Sile
ma Simolete
ma Sinakola
ma Sipusi
ma Siwewi
ma Somalilan
ma Sonko
ma Sopisi
ma Soson
ma Soson (tenpo pini)
ma Sulija
ma Sutan
ma Sutu
ma Suwana
ma Suwasi
ma Tansanija
ma Tansi
ma Tatasan
ma Tawan
ma Tawi
ma Tenesi
ma Toko
ma Tominika pi ma tomo Santo Tominko
ma tomo lili Oteken
ma tomo Onkon
ma tomo Tentemonte
ma Tosi
ma Tosiki
ma Tuku
ma Tuwinita en ma Topeko
ma Ulukawi
ma Usali
ma Wajomin
ma wawa
ma Wije
ma Lunpan
ma Monako
ma Mosijo
ma Mowisi
ma Mulitanija
ma Naselija
ma Netelan
ma Ontula
kulupu pi ilo sona
ilo kon
ilo kon pi supa pali
ilo kon Plasma
ilo Potoso
ilo sona
ilo Tuwita
ilo Wesi
jan Alan Tuwin
kulupu KDE
lipu ilo
pipi pi ilo sona
lipu ni li tan lipu Panton la o lukin
lipu ni o mute
lipu ni o tawa
lipu ni o wan
lipu ni o weka
lipu pi toki ante
lipu pi wile lukin
jan pi toki pona
lipu pi toki pona
kama kulupu Etoso
kama sona pi jan Sonja
kulupu pi toki pona pi ma Anku
kulupu toki pi toki pona lon ilo Jaku
lipu ku
Wikipesija:lipu pi toki Inli/Where is Toki Pona used?
lipu Tokipona.info
luka pona
nanpa seme la nimi li kama
nasin nanpa pona
nimi pu
nimi sin
sitelen pona
sitelen pona pi jan Makuwe
sitelen telo
suno pi toki pona
toki pona luka
toki Tokima
sitelen toki
toki ilo
toki pi kulupu toki Apika Asija
toki pi kulupu toki Osonesija
toki pi kulupu toki Palata Elopa
toki pi kulupu toki Sonko Po
toki pi kulupu toki Tuki
toki pi ma Apika
toki pi ma Palata
toki Ajenu
toki Epanja
toki Inota
toki Italija
toki Ju
toki Kantun
kulupu toki Kemani
kulupu toki Sami
toki Lasina
toki Lipulali
toki Lomansi
toki Lominija
toki Lowenki
toki Malasija
toki Mawi
nanpa pi sona lon Toki Pona
nanpa toki ISO
nasin toki lawa
toki Netelan
toki Nijon
toki Nolon
toki Pilipina
toki Powija
toki Posuka
toki Potuke
toki Sawili
toki sewi
toki Somalija
toki Sonko
toki Takalo
toki Ala
toki Alan
toki Alapi
toki Anku
toki Apasiso
toki Apikan
toki Asapaka
toki Awasa
toki Awawi
toki Ekala
toki Elepen
toki Elina
toki Epelanto
toki Ikuli
toki Ilan
toki Inli
toki Insi
toki Intelinwe
toki Intonesija
toki Intusan
toki Isilan
toki Ito
toki Iwisi sin
toki jaki
toki Kaleku
toki Kalijala
toki Kamajo
toki Kanse
toki Kasatan
toki Katala
toki Katelo
toki Keni
toki Kijukiju
toki Kinla
toki Kopasa
toki Kosa
toki Lalen
toki Lanpun
toki Latan
toki Lawi
toki Lije
toki Lomani
toki Losa
toki Losupan
toki luka
toki Lusi
toki Majoli
toki mama
toki Menkijeli
toki Mini
toki moli
toki Mon
toki Mosijo
toki nasa
toki Nosiki
toki Nowija
toki Palata Elopa nanpa wan
toki Panla
toki Pelalusi
toki Peson
toki pi jan Juta
toki Po
toki Pula
toki Saleja
toki Sami lete
toki Sankita
toki Seki
toki Sensa
toki Sinupuwanon
toki Sisin
toki Soleso
toki Soma
toki Tami
toki Tansi
toki Tapawenjo
toki Tata
toki Topisin
toki Tosi
toki Tuki pi tenpo pini
toki Tuwi
toki Ukawina
toki Ulaliso
toki Wakilu
toki Wata
toki Wije
toki Tuki
toki Utu
wile sona
jan:Xirdim/poki ko/toki Saleja/ja
leko Lupiko
jan musi
kalama musi
ma lawa lili musi
musi sijelo
tenpo musi
toki musi
akesi suli tan musi
musi pi jan lawa moli
kiwen en ilo en lipu
musi Kensin
musi pi sike noka
musi pi sike palisa tan ma Mewika
musi Pokemon
musi Sansi
musi Sutoku
musi Utala Pi Jan Meli
pilin musi
sike noka
sitelen Ju-Ki-O!
sitelen tawa pi Jan Utala Mun
misikeke
nasin lawa
sitelen lape
jan mute pi sijelo wan
jan pi mama sama
kulupu kule
lanpan
lawa ante
nasin jan
pona nasa
sitelen pi ken jan
tenpo utala
tomo suli pi ma tomo Papili
tonsi
wan olin
ike tawa li pakala e ilo awen pi sijelo jan
ilo pali pi nanpa tan ken nasa
jan Josi Salin
jan pi wile unpa ala
jan sewi Ese
jan sewi Nipeho
jan Wankeli
kili pi selo waso
kulupu jan Ajenu
lawa kule
lawa ma
lawa pi ken ala pilin e ijo wan taso
lipu pi jan lili pi jan Tokin
ma tomo Lontan
ma Ipelija
ma Kaliponja
ma Kuli
ma Nowa Sema
ma Nupansuwi
ma Pajan
ma Pilipina
ma tomo Kolon
ma tomo Paja
ma Wenpa
musi "kasi en jan moli li utala"
musi Mikaliwi
musi sike pi lipu tu tu
nasin Joka
kipisi:nasin toki ike
ma Pasila
ma Pelalusi
pilin e ijo wan
sijelo jan
sitelen An
sitelen Te
telo walo unpa
tenpo suno pi jan pali pi ma ali
toki ilo Wisupesi
toki Kuwenja
toki, ma ale o!
ma Tuki
nasin sewi Kolisu
jan Nowa
jan sewi Aton
jan sewi Juno
jan sewi Jupite
jan sewi Kopi
jan sewi Le
jan sewi Minewa
jan sewi Olo
jan sewi Seju
jan sewi Sete
jan sewi Wesile
ma anpa ike
ma sewi pona
mama sewi
nasin pi mama sewi mute
nasin pi mama sewi wan
nasin sewi Kemetesin
nasin sewi Omalo
nasin sewi Otun
nasin sewi pi jan Alawan
nasin sewi pi ma Loma
nasin sewi Sinto
nasin sewi Tesu
nasin sewi Watapawi
tomo pi nasin sewi
nasin Wisinu
nasin telo
nasin telo Jansi
nasin telo Lena
nasin telo Misuwi
nasin telo Molawa
nasin telo Nile
nasin telo Nisite
ilo mun
mun Masi
mun Satunu
jan:Juna/mun Ulanu
kiwen lon pimeja mun
mun Elopa
mun Enkelatu
mun Ijo
mun Jupite
mun Kanimi
mun Luna
mun Netunu
mun Pantola
mun pi mun Satunu
mun Puto
mun Ulanu
mun Wenu
sitelen pi palisa mama mun
suno lili
weka suno lon kon
nanpa ilo
nasin sona
sona nanpa
sona sijelo
sona tawa
laso wawa
nasin pi len toki
poki sijelo lili
sona toki
jan Winsen Tan Kowe
jan Mikelanselo
jan Lejonato pi ma Winsi

jan Ana
jan Apajan Linkon
jan Pane Sasu
jan lawa Elisepe nanpa tu
jan Anipa
jan Ape Ansan
jan Asa Antuki
jan Asune Miku
jan Eta Wan Wa
jan Isa Asimo
jan Jan Silesen
jan Juli Kakalin
jan Juliju Kesali
jan Ka Sakan
jan Kalu suli
jan Kansi
jan Kitopa Kolon
jan lawa Iwan pi nanpa tu tu
jan Mako Polo
jan Male
jan Maten Lute Kin lili
jan Mi Pen
jan Mimoku
jan Napolejon Ponapa
jan Nasi
jan Nijo Anson
jan Oloja
jan Onta Esa Tonsan
jan Pankin Losewe
jan Pawa Opama
jan Pen-Kulijon
jan Penito Musolini
jan Pensamin Pankin
jan Petopen
jan Pijoke
jan Piki Nise
jan Sewen Akin
jan Si Telu
jan So Patan
jan Son Li Ja
jan Suse Eten Ekin
jan Tana Tun
jan Temusin
jan Wan Sepe
jan Wasimi Lenin
jan Wekilusu
jan Wilijan pi lanpan ma
jan Koleko
kulupu jan
kute ala
jan Lipe
meli kon
nasin pi jan utala
jan Oto Tome
jan pi pilin ike lon kulupu
pilin jan
jan lawa Sa nanpa tu wan
jan Saman Lusi
jan Sameno
jan Sen
jan Sopija Jano
jan suli
kulupu jan Tata
jan Tokin
jan Tupu
jan Wilijan Sepija
jan Ewi Peseli
jan lawa
jan Alekanto pi ma Maketonija
jan Alekanto suli
jan Jojane Pajulu nanpa tu
jan lawa pi ma Mewika
jan Santepu
jan Sun Sunsan
telo sijelo loje
'''
  
def parseXML(xmlfile):  
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    encyclopedia = {}

    for page in root:
        if page.tag != '{http://www.mediawiki.org/xml/export-0.11/}page':
            continue

        title = page.find('{http://www.mediawiki.org/xml/export-0.11/}title').text
        text = page.find('{http://www.mediawiki.org/xml/export-0.11/}revision').find('{http://www.mediawiki.org/xml/export-0.11/}text').text
        if text is not None and len(text) > 500:
            encyclopedia[title] = text

    return encyclopedia

count = 0
result = parseXML('wiki.xml')
for title, content in result.items():
    title = title.replace('/', '_').replace('"', '').replace("'", '').replace(":", '__').replace('\\', '_').replace('?', '_')
    content = re.sub(r'<gallery>[^<]*</gallery>', '', content, flags=re.DOTALL)
    content = '\n'.join([line.strip() for line in content.split('\n') if line.strip() != ''])

    test_content = re.sub(r'{[^}]*}', '', content, flags=re.DOTALL).replace('{', '').replace('}', '').strip()

    if len(re.sub(r'\s', '', re.sub(r'\[\[[^\]]*\]\]', '', test_content, flags=re.DOTALL))) < 400:
        continue
    count += 1

    with open(f'encyclopedia/tok/{title}.txt', 'w') as f:
        f.write(content.encode("ascii", "ignore").decode('utf-8'))

print(count)