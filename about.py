import json

datasets = {
    "landesbuecherei_dessau": {
        "title": "Sebastian Brants 'Narrenschiff', lateinische Ausgabe, Basel 1498",
        "about": """
Sebastian Brants 'Narrenschiff' war ein Bestseller des ausgehenden 15.
Jahrhunderts. Die spätmittelalterliche Moralsatire erschien erstmals 1494 in
deutscher Sprache in Basel. Entscheidend für den Erfolg in ganz Europa war die
lateinische Übersetzung 'Stultifera navis', die Sebastian Brant durch seinen
Schüler Jakob Locher anfertigen ließ und die erstmals 1497 ebenfalls in Basel
erschien. Erst diese Übersetzung war die Voraussetzung dafür, dass es
Übertragungen in andere europäische Sprachen gab. Im 'Narrenschiff' erzählt
Brant von einer von 109 Narren unternommenen Schiffsreise in das Land
'Narragonien'. Jeder Narr symbolisiert exemplarisch menschliches Fehlverhalten,
so z.B. Habsucht, Zwietracht, Völlerei, Ehebruch, Jähzorn, Gewalt, Undankbarkeit
oder Selbstgefälligkeit. Jedes Kapitel enthält einen Mottovers, einen
Holzschnitt sowie ein Spruchgedicht. Brant hält seinen Mitbürgern einen Spiegel
vor und verfolgt damit das Ziel, zu lehren und zu predigen, zu bessern und zu
bekehren. Wesentlich für die Wirkung und den Erfolg des Werkes sind die
Holzschnitte, die nach Vorgaben des Verfassers ausgeführt wurden. Als
Mediendateien liegen Digitalisate des gesamten Druckes (TIFF-Dateien) vor.
""",
        "links": [
            "https://speicherwolke.uni-leipzig.de/index.php/s/GydLm4pzuntWUtH",
        ],
        "formats": ["txt", "tsv", "xlsx", "tiff"],
        "licenses": ["CC0", "CC-BY-SA"],
    },
    "DBpedia": {
        "title": "DBpedia Dataset",
        "about": """
DBpedia ist ein Gemeinschaftsprojekt der Universität Leipzig und anderen
Institutionen, mit dem strukturierte Informationen aus Wikipedia extrahiert und
Webanwendungen zugänglich gemacht werden können. DBpedia ermöglicht es
weiterhin, diese Daten mit Informationen aus anderen Web-Anwendungen zu
verbinden.Wikipedia-Artikel bestehen meistens aus normalem Fließtext, enthalten
aber andererseits auch strukturierte Informationen, beispielsweise Infoboxen,
Tabellen, Kategorien, geographische Koordinaten und Weblinks. Diese
Informationen können extrahiert und als Datenbasis für fortgeschrittene Fragen
verwendet werden. Als Standard für die Daten wird das Resource Description
Framework (RDF) benutzt. Als Quelle werden verschiedene Sprachversionen
(Niederländisch, Japanisch, Englisch, Deutsch, Portugiesisch) von Wikipedia
verwendet.
""",
        "licenses": ["CC0", "CC-BY-SA"],
        "formats": ["rdf"],
        "links": [
            "http://wiki.dbpedia.org/",
            "http://wiki.dbpedia.org/services-resources/ontology",
            "http://dbpedia.org/sparql", "http://wiki.dbpedia.org/OnlineAccess",
            "http://wiki.dbpedia.org/downloads-2016-10",
        ]
    },
    "ddb": {
        "title": "API der DDB",
        "about": """
Die Deutsche Digitale Bibliothek (DDB) vernetzt die digitalen Bestände
der Kultur- und Wissenschaftseinrichtungen und macht sie zentral
zugänglich, für menschliche Nutzerinnen und Nutzer in Ihrem Portal und
für maschinellen Zugriff über ihr API.

Die Deutsche Digitale Bibliothek arbeitet spartenübergreifend, ihre
Partner sind Archive, Bibliotheken, Denkmalämter,
Forschungseinrichtungen, Mediatheken und Museen. Zur Zeit - Stand April
2018 - umfasst die DDB über 24 Millionen Datensätze von 369
datengebenden Einrichtungen. Jeden Monat kommen neue Datengeber hinzu.
Von den bei Coding da Vinci teilnehmenden Kultureinrichtungen ist ca.
die Hälfte mit ihren Daten bereits in der DDB vertreten.

Ein Datensatz in der Deutschen Digitalen Bibliothek besteht aus
Metadaten und, in der Hälfte der Fälle, aus Bild-, PDF-, Audio- oder
Videodateien, die eine Vorschau auf das beim Datengeber verfügbare
Digitalisat bieten. Das interne Metadatenformat der DDB ermöglicht die
semantische Verknüpfung der Datensätze sowohl untereinander,
beispielsweise über Personen, die als Schöpfer oder Gegenstand von
Werken vorkommen können, als auch mit externen Datenbanken wie der
Gemeinsamen Normdatei oder der Wikipedia. Alle Datensätze enthalten
maschinenlesbare Rechteauszeichnungen, die die rechtskonforme
Weiterverwendung der in der DDB verzeichneten digitalen Objekte
ermöglichen. Die Metadaten in der Deutschen Digitalen Bibliothek stehen
grundsätzlich unter der CC0-Lizenz, bei ca. 140.000 Objekten gibt es
umfangreichere Beschreibungstexte, deren urheberrechtlicher Status nicht
mit vertretbarem Aufwand geklärt werden kann und die deshalb nicht über
das API ausgeliefert werden.

Eine detaillierte Dokumentation des API inklusive einiger Codebeispiele
findet sich auf api.deutsche-digitale-bibliothek.de/doku. Komplette
Beispielanwendungen des API finden sich u.a. im github-Repositorium der
Deutschen Digitalen Bibliothek, darunter eine kartenbasierte Suche in
der DDB und der von Studenten der FU Berlin adaptierte Public Domain
Calculator. Weitere Beispiele sind der Twitter-Bot DDB Katzen und eine
interaktive Visualisierung der DDB-Bestände durch die FH Potsdam. Auch
bei Coding da Vinci sind mehrere auf dem DDB-API aufsetzende Projekte
entstanden, z.B. der JavaScript-WrapperDDBRest, die Kulturchronologie
und Mnemosyne. 
        """,
        "links": [
            "https://www.deutsche-digitale-bibliothek.de/",
            "https://api.deutsche-digitale-bibliothek.de/doku",
            "https://www.deutsche-digitale-bibliothek.de/content/terms/api",
            "https://github.com/Deutsche-Digitale-Bibliothek",
            "http://pro.europeana.eu/share-your-data/data-guidelines/edm-documentation",
            "https://api.deutsche-digitale-bibliothek.de/doku/display/ADD/Datenmodell",
        ],
        "formats": ["xml", "json", "edm"], "licenses": ["CC0"],
    },
    "dnb_portraits": {
        "title": "Buchhändlerporträts",
        "about": """
Aus der Blattsammlung der Bibliothek des Börsenvereins der Deutschen
Buchhändler stammen diese 2.747 Porträts von Druckern, Verlegern,
Buchhändlern, Buchbindern, Zensoren und anderen im Buchgewerbe Tätigen
vor allem aus dem deutschen Sprachraum. Die Sammlung wurde vom frühen
19. Jahrhundert bis zum zweiten Weltkrieg durch den Börsenverein
zusammengetragen. Es handelt sich teilweise um Originalgrafiken, oft
wurden aber auch Reproduktionen aus Publikationen ausgeschnitten. Es
dürfte sich um die größte Porträtsammlung zu diesem Thema handeln. Die
Porträts liegen als hochauflösende TIFF-Scans vor. Die Dateien sind
umfänglich mit Vokabular der GND (Gemeinsame Normdatei) erschlossen.
Ausgewählte Konzeptbezüge wie Porträtart (Brust, Halbfigurenbild etc.),
grafischen Technik, Größe, Entstehungszeit etc wurden mit der
international eingesetzten, sprachunabhängigen Klassifikation ICONCLASS
beschrieben. 
""",
        "links": [
            "https://speicherwolke.uni-leipzig.de/index.php/s/HScdv0wr2lQe63e",
        ],
        "formats": ["xml", "tiff"],
    },
    "dnb_1912": {
        "title": "Buchstadt 1912",
        "about": """
Die Sammlung ist ein vollständiges Exzerpt aller relevanten
Firmenadressen aus dem Leipziger Adressbuch von 1913. Das Jahr 1913 kann
als Höhepunkt der Entwicklung der Buchstadt Leipzig angesehen werden, in
der im folgenden Jahr gar die erste Weltausstellung auf deutschem Boden
stattfand. In den vorangegangenen Jahrzehnten hatte Leipzig wie kaum
eine andere Stadt von der Industrialisierung profitiert und seinen
Weltruhm als Stadt des Buches etabliert. Die wichtigsten deutschen
Verlage und Druckereien arbeiteten in Leipzig. Bedeutende Innovationen
im Druckgewerbe wurden hier eingeführt. Die Adressdaten zeigen nicht nur
die schiere Menge der Unternehmen sondern lassen, übertragen auf eine
Karte, auch sehen, wie engmaschig die Stadt von der Druck- und
Verlagsindustrie durchwoben war. 
""",
        "links": [
            "https://speicherwolke.uni-leipzig.de/index.php/s/UUOordMT6H2ixwo",
        ],
        "formats": ["xml"],
    },
    "gotha": {
        "title": "Fechtbuch von Hans Talhoffer",
        "about": """
Die Herzogliche Bibliothek Gotha besaß seit Ende des 17. Jahrhunderts
eine hochkarätige Sammlung von sechs Handschriften zum mittelalterlichen
Zweikampf, darunter das älteste illustrierte Fechtbuch Europas.
Fechtbücher gehören zu den faszinierendsten Hinterlassenschaften des
späten Mittelalters und der Renaissance. Teils literarisch, teils in
lebendigen Bildern geben sie Prinzipien und Taktiken des Nahkampfes beim
Kampf mit Blankwaffen, aber auch beim Ringen wieder. Ihre Autoren
verfassten diese Bücher als Lehrwerk und Gedächtnisstütze für die
Ausbildung ihrer Schüler. Hans Talhoffer (ca. 1420-1490) verfügte über
Erfahrungen als Lohn- und Schaukämpfer, die er mit seinen
Fechthandschriften offensichtlich an einen noch über seine unmittelbaren
Schüler hinausgreifenden Personenkreis weitergeben wollte. Anschaulich
informiert er über Ausrüstungsgegenstände, Techniken beim Fechten und
Ringen und zeigt Szenen aus seinem Alltag als Fechtmeister. Das
Fechtbuch Hans Talhoffers entstand in oder nach den 1440er Jahren. Zwei
Handschriften befanden sich zunächst im Besitz ihres Auftraggebers. 1632
wurde es zusammen mit anderen Handschriften bei der Plünderung der
Münchner Hofbibliothek durch Herzog Wilhelm von Sachsen-Weimar erbeutet,
gelangte bei der Erbteilung 1640 nach Gotha und kam dort 1647 als
Gründungsbestand in die Bibliothek auf Schloss Friedenstein, wo es noch
heute aufbewahrt wird. Das Datenset umfasst die digitalen Faksimiles von
Talhoffers Fechtbuch aus dem Bestand der Forschungsbibliothek Gotha –
d.h. 455 hochaufgelöste Images mit beschreibenden Metadaten. 
""",
        "links": [
            "https://archive.thulb.uni-jena.de/ufb/receive/ufb_cbu_00009967",
            "https://archive.thulb.uni-jena.de/ufb/receive/ufb_cbu_00009967?XSL.Style=metsmods",
            "https://archive.thulb.uni-jena.de/ufb/oai/prints?verb=Identify",
        ],
        "formats": ["xml", "tiff"],
    },
    "gleimhaus": {
        "title": "Herbarium in drei Bänden aus den Jahren 1729 bis 1731",
        "about": """
Das Gleimhaus ist eines der ältesten deutschen Literaturmuseen.
Grundstock des Kunst-, Buch- und Handschriftenbestandes ist der Nachlass
des Dichters und "Netzwerkers" Johann Wilhelm Ludwig Gleim (1719-1803).
Die Bibliothek gilt als eine der größten privaten bürgerlichen
Büchersammlungen des 18. Jahrhunderts. Mit ihrer Bestandsgröße von rund
12.000 Bänden umfasst sie ein großes thematisches Sammlungsspektrum.

Eine echte Rarität ist das umfangreiche dreibändige Herbarium aus den
Jahren 1729 bis 1731, das außergewöhnlich gut erhalten ist und die Flora
der Zeit im mitteldeutschen Raum hervorragend abbildet. Herbarien dieses
Alters und in diesem Umfang sind außerordentlich selten.
""",
        "links": [
            "http://digishelf.de/ppnresolver?id=796882568",
            "http://www.digishelf.de/metsresolver?id=796882568",
            "http://digishelf.de/ppnresolver?id=796932956",
            "http://www.digishelf.de/metsresolver?id=796932956",
            "http://digishelf.de/ppnresolver?id=796933170",
            "http://www.digishelf.de/metsresolver?id=796933170",
        ],
        "formats": ["xml", "jpeg"],
    },
    "vivat": {
        "title": "Vivatbänder",
        "about": """
Das Gleimhaus ist eines der ältesten deutschen Literaturmuseen. Grundstock
des Kunst-, Buch- und Handschriftenbestandes ist der Nachlass des Dichters
und "Netzwerkers" Johann Wilhelm Ludwig Gleim (1719-1803), dessen 300.
Geburtstag in diesem Jahr gefeiert wird.

Die Vivatbänder sind Teil der Handschriftensammlung, die über 10000 Briefe,
aber auch Werkmanuskripte und andere handschriftliche Zeugnisse enthält. Bei
diesen so genannten Vivatbändern handelt es sich meist um schmale,
beschriebene oder bedruckte Stoffbänder, oft aus Seide, die im 18. Jh.
zunächst anlässlich militärischer Siege (vor allem Friedrichs II.)
angefertigt wurden. Ihre Bezeichnung resultierte daraus, dass sie häufig mit
dem Schriftzug VIVAT, also "Er lebe hoch" versehen waren. Neben diesen
Siegesbändern finden sich auch "Familien- und Freundschaftsbänder". Sie sind
ebenso anlassbezogen und scheinen besonders im bürgerlichen Milieu des
späteren 18. Jahrhunderts beispielsweise anlässlich von Taufen, Geburtstagen
oder Hochzeiten verbreitet gewesen zu sein. Nachweisbar sind solche Bänder
bis etwa in die Mitte des 19. Jahrhunderts. Alle hier präsentierten Bänder
sind solche Geburtstagsbänder von Freunden und Verwandten an Johann Wilhelm
Ludwig Gleim. Sie stammen aus einem Zeitraum von 1782 bis 1799. Gleim muss
noch wesentlich mehr Bänder besessen haben, die aber leider nicht in den
Sammlungen des Gleimhauses überliefert sind.

Die Bänder sind digitalisiert und werden als jpegs zur Verfügung gestellt. 
        """,
        "links": [
            "https://st.museum-digital.de/index.php?t=listen&type=4&&gesusa=849&instnr=13",
            "https://www.museum-digital.de/st/index.php?t=sammlung&instnr=13&gesusa=849",
            "https://handbook.museum-digital.info/?lan=de&q=Ausgabe/APIs",
        ],
        "formats": ["xml", "json", "jpeg"],
    },
    "hmt": {
        "title": "Historische Studierendenunterlagen der HMT Leipzig aus den Jahren 1843-1893",
        "about": """
Die Hochschule für Musik und Theater "Felix Mendelssohn Bartholdy"
feiert in diesem Jahr ihr 175-jähriges Bestehen. Seit der Gründung des
Konservatoriums 1843 sind die Inskriptionsunterlagen und
Zeugnisvorschriften der Studierenden nahezu vollständig vorhanden.
Dieses Alleinstellungsmerkmal bietet ein breites Spektrum an
Forschungsmöglichkeiten, die in und aus einem internationalen Kontext
heraus wahrgenommen werden. Die Dokumente sind neben der Ahnen- und
Regionalforschung besonders in Bezug auf das aktuelle Thema
„Kulturtransfer“ aufschlussreich. Darüber hinaus illustrieren sie durch
die handschriftliche Überlieferung authentisch ihren
Entstehungszusammenhang.

Bei den Mediendateien handelt es sich um Digitalisate von
Inskriptionsunterlagen sowie Zeugnisvorschriften der ersten 50 Jahre -
über 6000 Matrikel. Dabei liegen lediglich die Bilddateien vor - ein
etwa OCR-gelesener Volltext kann derzeit nicht bereitgestellt werden.
Die dazugehörigen Metadaten sind auf Grundlage der
Studierendenunterlagen intellektuell erstellt worden und enthalten neben
Inskriptionsnummer und -jahr der Studierenden deren Namen,
Herkunftsstadt und -land (in historischer Ansetzung) sowie eine
Ortskonkordanz für die aktuelle Länderbezeichnung. Normdaten für Namen
oder geografische Informationen wurden zum Zeitpunkt der Datenerfassung
leider nicht berücksichtigt. Als Konkordanz zwischen Mediendateien und
Metadaten dienen die Inskriptionsnummer (Zeugnisvorschriften) sowie eine
weitere interne Zählung (Inskriptionsunterlagen). 
""",
        "formats": ["csv", "jpeg"],
        "links": [
            "https://speicherwolke.uni-leipzig.de/index.php/s/2wjvzYDJyZWdzVm",
        ]
    },
    "amalia": {
        "title": "Stammbücher der Herzogin Anna Amalia Bibliothek Weimar",
        "about": """
    Stammbuch, Freundschaftsbuch oder auch Album Amicorum sind die
gebräuchlichsten unter den Begriffen für eine Textgattung, die von
Wittenberg Mitte des 16. Jahrhunderts ausging und bis in die 1950er
Jahre hauptsächlich in Deutschland sehr verbreitet war. Anfangs waren
Stammbücher vor allem bei Studenten beliebt, später fanden sie in fast
allen Gesellschaftsschichten großen Anklang. In diesen immer auch
unterwegs mitgeführten Büchern trugen sich Freunde und Bekannte des
Halters mit Widmungen, Wappen, Bildern, kleinen Texten und Gedichten
oder auch mit illustrierten Reiseskizzen ein. So bildet jedes Stammbuch
das gesellschaftliche Umfeld ab, in dem sich der Stammbuchhalter bewegt
hat. Die Stammbuchsammlung der Herzogin Anna Amalia Bibliothek (HAAB) in
Weimar stellt mit ca. 1.600 Exemplaren aus der Zeit von 1550 bis 1960
den weltweit größten Bestand dieser Art dar.

Zur Verfügung gestellt werden 30.000 Datensätze einzelner
Stammbucheintragungen mit dem jeweiligen Namen des Eintragenden sowie
Sprache, Ort und Datum dieser Eintragung; darüber hinaus werden
sämtliche Personennamen mit der GND verknüpft.

Hinweis zur Nutzung der SRU Schnittstelle Mittels des Abrufcodes
"Stammbucheintrag" werden alle Einzeleinträge über die SRU-Schnittstelle
ausgegeben. Der Vorteil ggü. den Exceltabellen liegt darin, dass laufend
neue Einträge (ca. 30-40 pro Tag) hinzukommen. Das Datenset der
SRU-Schnittstelle ist also umfangreicher. Außerdem liefert die
Schnittstelle mehr Datenfelder aus, als in der Exceltabelle enthalten
sind. Dort haben wir uns auf die wesentlichen Inhalte beschränkt.
Allerdings wurden aus den Exceltabellen auch Datensätze entfernt, bei
denen die Angaben im Datensatz nur unzureichend sind, wenn z.B. Datums-
und Namensangaben komplett fehlen. 
""",
        "formats": ["xls", "xml"], "links": [
            "http://sru.gbv.de/opac-de-32?version=1.2&recordSchema=picaxml&recordPacking=xml&operation=searchRetrieve&maximumRecords=20&query=pica.abr%3Dstammbucheintrag",
            "https://speicherwolke.uni-leipzig.de/index.php/s/Z5RMOD43NkgHc4r",
        ]
    },
    "historical_maps": {
        "title": "Historische Kartensammlung",
        "about": """
Die Sammlung besteht aus historischen Karten des 17. bis 19.
Jahrhunderts. Darunter sind Weltkarten, Stadtpläne, Verkehrskarten,
topographische Karten, Seekarten, Militärkarten oder auch physische
Karten verschiedenster Regionen weltweit. Alle ca. 1400 Karten wurden
digitalisiert und stehen als JPG- und hochauflösenden TIFF-Format
bereit. Des Weiteren beinhalten die Metadaten eine inhaltliche
Erschließung in Form von festgelegten geographischen Schlagworten und
einer nach einem geographischen Thesaurus erfolgten thematischen
Zuordnung. Jede Karte wurde georeferenziert. Die entstandenen
Koordinaten sind für eine Verortung im Raum verwendbar.
""",
        "formats": ["xml", "tsv", "jpeg", "tiff"],
        "links": [
            "https://speicherwolke.uni-leipzig.de/index.php/s/p3OptbKiHHoPEhU",
            "http://www.ifl-leipzig.de/",
        ],
    },
    "abb": {
        "title": "Andreas-Bach-Buch",
        "about": """
Das Andreas-Bach-Buch ist eine Sammelhandschrift mit 64 Klavier- und Orgelwerken
von Komponisten des 17. und 18. Jahrhunderts wie Johann Sebastian Bach,
Dieterich Buxtehude, Georg Böhm, Johann Kuhnau, Johann Pachelbel, Christian
Ritter, Georg Philipp Telemann, Anonyma, u.a. Geschrieben wurden die Notationen
zwischen 1705 und 1713 im Raum Erfurt-Arnstadt-Ohrdruf-Gotha von verschiedenen
Schreibern. Als Hauptschreiber gilt in Fachkreisen Johann Sebastian Bachs
älterer Bruder Johann Christoph Bach (1671 – 1721). Der Besitzverlauf ist wie
folgt nachgewiesen: Johann Christoph Bach, Johann Bernhard Bach, Johann Andreas
Bach, Johann Christoph Georg Bach, J.G. Möller, Christian Friedrich Michaelis
(Besitzvermerk 1820), Carl Ferdinand Becker (Besitzvermerk 1835). In dieser
Sammelhandschrift ist auch ein Autograph von Johann Sebastian Bach enthalten,
die Fantasie C-moll, BWV 1121, ein Orgeltabulatur, komponiert um 1706. Diese
Sammelhandschrift gehört zu einem Kleinod der Bach-Forschung. Einige
Kompositionen sind nur durch die Abschrift im Andreas-Bach-Buch überliefert.
Durch Schrift und Wasserzeichenvergleiche dieser Sammelhandschrift konnten in
den vergangenen Jahren die eindeutige Zuordnung von Bachschen Kompositionen
vorgenommen werden, die vorher als Anonymus ausgewiesen waren. Die
Sammelhandschrift besteht aus 128 Blatt verschiedener Blattsorten und
verschiedener Tinten. Das Titelblatt ist handschriftlich von Becker geschrieben.
Der Titel lautet „Orgelarchiv“. Das Andreas-Bach-Buch wurde 2007 restauriert.

Die Sammlung umfasst 257 Bilddateien sowie ein PDF-Scan des
maschinengeschriebenen Inhaltsverzeichnisses. Zusätzlich zu den Metadaten des in
RISM mit der ID 225006068 erfassten Katalogeintrages enthält der Datensatz eine
CSV-Datei mit aktualisiertem Inhaltsverzeichnis und zugehörigen Dateinamen. 
        """,
        "formats": ["xml", "csv", "jpeg", "pdf"],
        "links": [
            "https://opendata.leipzig.de/dataset/8150e534-a65c-442a-b414-0ac142270e74/resource/ec78d783-2481-454f-8684-244ee67c6b14/download/dlembeckeriii.8.4andreasbachbuchrismid225006068.xml",
            "https://opendata.leipzig.de/dataset/8150e534-a65c-442a-b414-0ac142270e74/resource/0c77e669-4231-4ed6-be89-468c3a433eed/download/andreasbachbuch.zip",
            "https://opendata.leipzig.de/dataset/8150e534-a65c-442a-b414-0ac142270e74/resource/804b5996-7cf0-42d5-ac21-b81451c84058/download/inhaltsverzeichnis.csv",
            "https://opendata.leipzig.de/dataset/andreas-bach-buch",
        ],
    },
    "altenburg": {
        "title": "Antike Keramik",
        "about": """
Die Sammlung antiker Keramik umfasst im Lindenau-Museum Altenburg etwa 400
Vasen.

Zusammengetragen wurde diese Kollektion von dem Sammler Bernhard August von
Lindenau (1779 - 1854). Sie ist eine von vier historischen Sammlungen. Bernhard
August von Lindenau trug ebenso eine weltbekannte Sammlung Frühitalienischer
Tafelmalerei vom 13. - 16. Jahrhundert, Gipsabgüsse nach antiken Vorbildern und
eine große Bibliothek zusammen.

Die meisten Gefäße der Lindenauschen Vasensammlung wurden in Athen und Korinth
produziert und kamen als begehrte Importe nach Etrurien (Mittelitalien), wo sie
in den Etruskertstädten Vulci und Chuisi gefunden wurden. Sie dienten den
Etruskern als luxuriöse Grabausstattung. Die oft figürlich oder ornamental
bemalten Keramiken dienten zum Aufbewahren von Salbölen und Parfüm oder als
festliches Trinkgeschirr. Sie waren außerdem Weihgaben in den Tempeln, Preise
für gewonnene Wettkämpfe oder fanden im Totenkult Anwendung. Im 18. und 19.
Jahrhundert wurden diese Gefäße zu Tausenden in Italien ausgegraben und
gelangten in den Kunsthandel. Die formenreiche antike Keramik gibt dem heutigen
Betrachter durch die vielen Motive ihrer Bemalung einen Einblick in das Leben
und die Mythologie der alten Griechen und ihrer Zeitgenossen.

Die Gefäße sind auf Fotografien abgebildet. 
""",
        "formats": ["xls", "jpeg"],
        "links": [
            "https://speicherwolke.uni-leipzig.de/index.php/s/IvHiDl76pCQ1ulq",
        ]
    },
    "mdv": {
        "title": "LVB Fahrplandaten im GTFS-Format (ÖPNV)",
        "about": """
Der Datensatz beinhaltet aktuelle Fahrplandaten sämtlicher in Leipzig
verkehrenden Straßenbahnen und Busse im standardisiertem GTFS-Format. Es handelt
sich um Solldaten d.h. geplante Fahrten (keine Echtzeitdaten). 
        """,
        "links": [
            "https://www.mdv.de/",
            "https://opendata.leipzig.de/dataset/lvb-fahrplandaten",
            "https://developers.google.com/transit/gtfs/",
            "https://opendata.leipzig.de/dataset/8803f612-2ce1-4643-82d1-213434889200/resource/b38955c4-431c-4e8b-a4ef-9964a3a2c95d/download/gtfsmdvlvb.zip",
        ],
        "formats": ["gtfs"],
    },
    "posterstein": {
        "title": "Sammlung Welker",
        "about": """
Im Jahr 2014 konnte das Museum Burg Posterstein über eine Landesförderung und
mit Unterstützung der Bürgerstiftung Altenburger Land eine einmalige Sammlung
von Portraitzeichnungen der 1819/1820 am Musenhof Löbichau der Herzogin von
Kurland (1761-1821) anwesenden Gäste ankaufen. Die Sammlung stammt aus dem
Besitz von Emilie von Binzer (1801-1891). Die 47 aquarellierten Zeichnungen
fertigte bis auf eine der Maler Ernst Welker (1784/88-1857) an. Die
portraitierten Löbichauer Gäste gehören alle zu engen Umfeld der Herzogin von
Kurland. Die historischen Persönlichkeiten treten als Fabelwesen auf, deren Kopf
Welker durch ein Portrait der entsprechenden Person ersetzte und sind alle mit
einem zweizeiligen Reim versehen. Der Datensatz umfasst hochauflösende Scans der
Zeichnungen sowie Informationen zu den abgebildeten historischen Personen.
Darunter sind die Herzogin selbst, ihre Töchter, Herzog August von
Sachsen-Gotha-Altenburg und zahlreiche Persönlichkeiten des damaligen
kulturellen Lebens.
""",
        "links": [
            "https://commons.wikimedia.org/wiki/Category:Museum_Burg_Posterstein",
        ],
        "formats": ["tiff"],
    },
    "press": {
        "title": "Druckmaschinensounds",
        "about": """ 
Die Daten umfassen Videobeispiele mit Sounds von drei Druckmaschinen. Auf diesen
wurde / wird mit den (ebenfalls veröffentlichten) Holzbuchstaben gedruckt.
""",
        "links": ["https://speicherwolke.uni-leipzig.de/index.php/s/g0QLf7PmlTuIs8y"],
        "formats": ["mp3", "mp4"],
    },
    "letters": {
        "title": "Holzbuchstaben",
        "about": """
Die Daten umfassen Scans von Holzbuchstaben, die zum Drucken von Plakaten
verwendet wurden. Die Drucktechnik ist das Hochdruckverfahren, oben liegende
Bereiche drucken. Das System der beweglichen Letter geht auf Johannes Gutenberg
zurück, der es im 15. Jh. entwickelte. Die Scans umfassen zwei Schriften, von
denen weder Name noch Erscheinungsjahr bekannt sind. (Diese Angaben sind bei
Holzbuchstaben generell selten zu finden). Da es sich um ein direktes
Druckverfahren handelt, ist der eigentliche Scan seitenverkehrt, der Datensatz
enthält zusätzlich gespiegelte Daten, die sich für eine Verwendung in diesem
Projekt evtl. besser eignen. Heute finden die Objekte vorwiegend im
künstlerischen Umfeld Anwendung.
""",
        "formats": ["jpeg"],
        "links": [
            "https://speicherwolke.uni-leipzig.de/index.php/s/bW48T2otdmNVf1e",
        ]
    },
    "sellow": {
        "title": "Reisetagebücher und Exkursionsberichte von Friedrich Sellow",
        "about": """
Die Historische Arbeitsstelle mit ihren historischen Bild- und
Schriftgutsammlungen ist weltweit eines der bedeutendsten Archive zur Geschichte
der Naturwissenschaften mit dem Schwerpunkt Biologie. Unmittelbar mit den
naturwissenschaftlichen Sammlungen des Museums für Naturkunde verknüpft, verfügt
die Abteilung über Dokumente aus mehr als 200 Jahren nationaler und
internationaler Wissenschaftsgeschichte. Die Korrespondenzen,
Verwaltungsunterlagen, Berichte, Objektlisten, Expeditionsberichte und
-tagebücher werden ergänzt durch Nachlässe, Lehrmaterialien, Karten,
Zeichnungen, Fotos und eine umfangreiche Sammlung historischer Porträts. 
        """,
        "formats": ["csv", "tiff", "pdf"],
        "links": [
            "http://gbif.naturkundemuseum-berlin.de/CDV2018/Sellow/Metadaten",
            "http://gbif.naturkundemuseum-berlin.de/CDV2018/Sellow/Transkripte",
            "http://gbif.naturkundemuseum-berlin.de/CDV2018/Sellow/",
            "http://gbif.naturkundemuseum-berlin.de/CDV2018/sellow-gallery.html",
        ]
    },
    "shells": {
        "title": "Muscheln und Schnecken des Museums für Naturkunde",
        "about": """
Die mehr als 30 Millionen Objekte umfassenden Sammlungen des Museums für
Naturkunde Berlin sind eine Forschungsinfrastruktur von weltweiter Bedeutung.
Sie stehen nicht nur eigenen Forschungsaktivitäten zur Verfügung, sondern auch
externen Wissenschaftlern, Künstlern, Lehrenden und vielen anderen
Nutzergruppen. Jedes Jahr besuchen Hunderte von Wissenschaftlern aus aller Welt
die Sammlungen des Museum, um dieses einzigarte Vergleichsmaterial zu
untersuchen. Zudem sind die Sammlungsobjekte ein historisch einmaliges Kulturgut
und Grundlage für eine vielfältige Wissensvermittlung. Diese vielseitig
genutzten Sammlungen zu erhalten, effizient zu nutzen und für die Zukunft weiter
zu entwickeln ist eine große Herausforderung.
""",
        "formats": ["csv", "jpeg"],
        "links": [
            "http://gbif.naturkundemuseum-berlin.de/CDV2018/Mollusken/Metadaten/",
            "http://gbif.naturkundemuseum-berlin.de/CDV2018/Mollusken/",
            "http://gbif.naturkundemuseum-berlin.de/CDV2018/mollusken-gallery.html",
        ]
    },
    "birds": {
        "title": "Tierstimmen",
        "about": """
Auf tierstimmenarchiv.de wird eine große Zahl wissenschaftlich geprüfter,
hochqualitativer Tierstimmen bereitgestellt. Der größere Teil der geschnittenen
Aufnahmen kann nicht unter einer offenen Lizenz zur Verfügung gestellt werden.
Jedoch existiert ein für Deutschland sehr interessanter Satz an Aufnahmen von
Vögeln, Amphibien und Säugetieren, die unter CC BY-SA lizenziert und hier
verfügbar sind. 
""",
        "formats": ["mp3", "json"],
        "links": [
            "http://labs.europeana.eu/api",
            "https://www.europeana.eu/portal/de/search?f%5BREUSABILITY%5D%5B%5D=open&q=tierstimmenarchiv",
            "https://codingdavinci.de/downloads/daten-2017/MfN-Tierstimmen.pdf",
        ]
    },
    "xplora": {
        "title": "MusiXplora",
        "about": """
Die Sammlung MusiX im Musikinstrumentenmuseum verknüpft biografische Daten von
Personen des Musiklebens (KomponistInnen, InterpretInnen,
InstrumentenbauerInnen, MäzenInnen, SammlerInnen) mit Metadaten ihrer
Wirkungsorte. Die Personen sind mit verbreiteten Identifikatoren wie GND, VIAF
oder Q versehen. Damit lassen sich auch weitere Datenquellen erschließen und
verknüpfen. 
        """,
        "formats": ["json"],
        "links": [
            "http://mfm.uni-leipzig.de/dt/Forschung/CDV2018.php",
        ]
    },
    "flax": {
        "title": "Flachsanbau und -verarbeitung",
        "about": """
Der Flachs (auch Lein) gehört zu den ältesten Kulturpflanzen. In der
Hauswirtschaft war er für die Herstellung von Leinwand unentbehrlich. Auch in
der Lausitz wurde er in den vergangenen Jahrhunderten in recht großem Umfang
angebaut. Die aufwendige Beschäftigung mit dem Flachs, mit dem Weben und Spinnen
nahm viel Raum im Leben der ländlichen Bevölkerung ein und widerspiegelt sich
nicht nur im materiellen Erbe, wie in Geräten und Kleidung, sondern auch im
immateriellen Erbe wie dem Liedgut und in mythologischen Vorstellungen (Sage von
der Mittagsfrau). Die Spinnstuben waren ein wichtiger sozialer und kultureller
Ort der Dorfgemeinschaft. „Spinnen und Weben wie in alten Zeiten“ erfreut sich
wieder einer gewissen Faszination. Darstellungen von Flachsanbau und
-verarbeitung sind ein beliebtes Thema musealer Präsentationen. Im Gegensatz zu
Gerätschaften als Museumsobjekt vermitteln Bilder einen intensiveren Eindruck
vom Gebrauch und der Arbeit. Im Bildarchiv des Sorbischen Instituts befinden
sich zahlreiche Fotografien zum genannten Thema. Oft sind auf ihnen Frauen bei
der Arbeit zu sehen. Während die dargestellte Arbeit einen zeitlichen Horizont
vermittelt, sind die abgebildeten Frauen durch ihre Tracht eindeutig in einer
bestimmten Region der sorbischen Lausitz zu verorten (um Hoyerswerda,
Niederlausitz, Kirchspiel Schleife). 
""",
        "formats": ["csv", "jpeg"],
        "links": [
            "https://speicherwolke.uni-leipzig.de/index.php/s/C99LbgXSSPdgFxV",
        ]
    },
    "muka": {
        "title": "Muka-Statistik 1884",
        "about": """
Während der bürgerlichen Modernisierung im 19. Jahrhundert wurden
Bevölkerungsstatistiken seitens des deutschen Staates gern herangezogen, um die
Germanisierungspolitik zu kaschieren oder als ethnische Selbstauflösung
darzustellen. Dem wurden von sorbischer Seite eigene Untersuchungen
entgegengesetzt. In den 1880er-Jahren ermittelte Arnošt Muka (Ernst Muka/ Ernst
Mucke, 1854-1932) während seiner Wanderungen durch beide Lausitzen eine
Statistik der Sorben. Sie wurde 1886 in der Zeitschrift „Časopis Maćicy
Serbskeje“ publiziert. Die Erhebung spiegelt das gesamte damalige Leben der
Sorben wider und war seinerzeit die genaueste Darstellung der Verhältnisse,
wodurch sie im In- und Ausland viel Beachtung fand. Sie beinhaltet nicht nur
statistische Daten, sondern auch Beschreibungen zur materiellen Volkskultur wie
etwa der Bauweise oder den Trachten. Muka erfasste die Bevölkerungszahlen für
die einzelnen Dörfer, geordnet nach Kirchgemeinden in der Ober- und
Niederlausitz.

In der vorliegenden Tabelle sind die Orte alphabetisch geordnet nach dem
sorbischen Namen mit der jeweiligen deutschen Entsprechung. Angefügt wurden die
Geokoordinaten und die absolute und prozentuale Aufteilung zwischen sorbisch-
und deutschsprachiger Bevölkerung. 
""",
        "formats": ["csv"],
        "links": [
            "https://datahub.io/biblioteka-archiw/datenmuka",
        ]
    },
    "bienert": {
        "title": "Sammlung Theodor Bienert",
        "about": """
Die umfangreiche Sammlung Theodor Bienert dokumentiert mit über 12.000 Objekten
in 100 Mappen die Bauwerke, Orte und Landschaften der sächsischen Topographie
vom ausgehenden 16. bis zum frühen 20. Jahrhundert. Zu den Blättern in
unterschiedlichen Zeichen-, Druck- und Reproduktionstechniken zählen sowohl
Meisterwerke von Adrian Zingg, Ludwig Richter und Johann Christian Klengel als
auch Kuriositäten wie Guckkastenbilder und Massenmedien wie Postkarten und
Stadtpläne.

Die Werke wurden im Zuge des Inventarisierungs- und
Provenienzforschungsprojektes Daphne der SKD im Kupferstich-Kabinett erfasst.
Diese Erfassung in einer Datenbank ermöglicht eine übergreifende Erschließung
der topographisch geordneten Sammlung als Quelle für Architektur- und
Heimatgeschichte, Landschaftsentwicklung, Technikgeschichte und Volkskunde. 
""",
        "formats": ["xml", "jpeg"],
        "links": [
            "http://forschung.skd.museum/fileadmin/user_upload/dokumente/Metadaten_Sammlung_Bienert.zip"
        ],
    },
    "walter": {
        "title": "Einblicke: Hermann Walter und das Atelier Hermann Walter in der Fotosammlung des Stadtarchivs Leipzig",
        "about": """
Hermann Walter (1838-1909) ist heute als Dokumentarist des "alten Leipzigs"
bekannt und erlangte besonders durch die frühe Spezialisierung auf
Architekturfotografie herausragende Bedeutung. Er erfasste Bauzustände,
Abrissarbeiten und begleitete auch langjährige Großbauprojekte des Leipziger
Hochbauamtes. Für seine Verdienste erhielt er die Goldene Ehrenmedaille der
Stadt Leipzig. Walters Atelier wurde von seinem Sohn und seinem Schwager
weitergeführt. Beide schufen zwischen dem Ersten Weltkrieg und 1935 nochmals
zahlreiche Aufnahmen, die uns das einstige Leipziger Stadtbild heute näher
bringen.

Die Digitalisate liegen im JPEG-Format mit eingebetteten Metadaten vor; die
erweiterten Metadaten mit den URLs der Digitalisate werden in einer CSV-Datei
zur Verfügung gestellt. Herkunft: Bildarchiv des Stadtarchivs Leipzig. Das
Stadtarchiv verwahrt über 2.000 Originalabzüge. Die Fotografien sind nicht Teil
eines abgeschlossenen Bestandes.
""",
        "links": [
            "https://speicherwolke.uni-leipzig.de/index.php/s/vCwddPDTpMBRwwO",
        ],
        "formats": ["csv", "jpeg"],
    },
    "vogel": {
        "title": "Fotothek Hermann Vogel-Sammlung",
        "about": """
Zu den Kostbarkeiten der fotografischen Sammlung des Stadtgeschichtlichen
Museums Leipzig gehört eine Kollektion von mehr als 500 Glasplatten und Abzügen,
die im Auftrag der renommierten Kunsthandlung von Hermann Vogel in Leipzig
angefertigt wurden. Auf den gut erhaltenen Glasnegativen aus der Kaiserzeit
findet man die Prachtbauten der Gründerjahre ebenso wie die vor dem Abriss
stehenden alten Bahnhöfe und Wassermühlen. Andere Bilder führen in das brodelnde
Messegeschehen oder halten wichtige Ereignisse der Zeitgeschichte fest. Zu der
Sammlung gehören aber auch Aufnahmen des sächsischen Herrscherhauses und
Porträts berühmter Schauspieler. Für das Projekt wurden die schönsten Aufnahmen
aus dem Atelier von Hermann Vogel ausgewählt. 
""",
        "formats": ["xls", "tiff"],
        "links": [
            "https://speicherwolke.uni-leipzig.de/index.php/s/Mun52I4EYKuVldn",
        ]
    },
    "kork": {
        "title": "Modelle antiker Bauwerken aus Kork",
        "about": """
In der zweiten Hälfte des 18. Jahrhunderts entstanden in der Werkstatt des
berühmten Antonio Chichi in Rom faszinierende Korkmodelle antiker Bauten. Das
gut zu bearbeitende Material war hervorragend geeignet für die detailgetreue
Wiedergabe der malerischen Ruinen. Die kostbaren Modelle, von denen sich nur
ganz wenige in Deutschland erhalten haben, wurden schnell zu begehrten Souvenirs
der nach Italien reisenden Fürsten. Auch das Haus Sachsen-Gotha-Altenburg erwarb
um 1775 eine erlesene Sammlung, die heute im Herzoglichen Museum Gotha zu sehen
ist. Diese kleine Kulturgeschichte der Phelloplastik stellt die Modelle im
Dialog mit Grafiken zeitgenössischer Künstler wie Giovanni Battista Piranesi
vor. Zahlreiche Zitate deutscher Italienreisenden machen das Rom der Zeit um
1800 lebendig, dessen Aura von Größe und Verfall nicht nur für Goethe zu einem
unvergesslichen Bildungserlebnis wurde.
""",
        "formats": ["xml", "jpeg"],
        "links": [
            "https://casimir.bsz-bw.de/files/18/korkmodelle-2018-03-14.xml",
            "https://casimir.bsz-bw.de/files/18/zip-korkmodelle.zip",
            "https://casimir.bsz-bw.de/frontdoor/index/index/docId/18",
        ]
    },
    "wax": {
        "title": "Modellfrüchte aus Wachs",
        "about": """
Um komplexere Zusammenhänge dem interessierten Laien besser veranschaulichen zu
können, bediente man sich im 18. Jahrhundert Modellen, die in kleinen,
kunstvollen Kabinetten gesammelt wurden. Das Obstmodellkabinett wurde mit dem
Ziel, Synergien zwischen Kultur- und Wirtschaftsförderung zu schaffen, über das
Landes-Industrie-Comptoir Weimar zwischen 1796 und 1822 vertrieben. Hier
erschien mit Sicklers "Der Teutsche Obstgärtner" auch die erste deutsche
Obstbauzeitschrift. Auf deren Titelsiegel, das ein Bild der Göttin der
Baumfrüchte zeigt, ist zu lesen: „In Hoffnung der Zukunft.“
""",
        "formats": ["xml", "jpeg"],
        "links": [
            "https://casimir.bsz-bw.de/files/18/modellfruechte-2018-03-14.xml",
            "https://casimir.bsz-bw.de/files/18/zip-modellfruechte.zip",
            "https://casimir.bsz-bw.de/frontdoor/index/index/docId/18",
        ]
    },
    "luise": {
        "title": "Meissner Porzellan",
        "about": """
Die hochgebildete Herzogin Luise Dorothea von Sachsen-Gotha-Altenburg (1710 —
1767) war eine leidenschaftliche Sammlerin des „Weißen Goldes". Besonders das
Meissner Porzellan hatte es ihr angetan, das sie in einem besonderen
Porzellan-Kabinett auf Schloss Friedenstein ihren Gästen präsentierte. Nicht nur
Voltaire war begeistert. Ihr langjähriger Briefpartner und Bewunderer Friedrich
der Große sprach von einem „kleinen Porzellan-Heiligtum" in Gotha. Die
bemerkenswert qualitätvolle Sammlung wurde von den Nachkommen der umschwärmten
Herzogin sorgsam gehegt und erweitert. 
""",
        "formats": ["xml", "jpeg"],
        "links": [
            "https://casimir.bsz-bw.de/files/18/meissner-porzellan-2018-03-14.xml",
            "https://casimir.bsz-bw.de/files/18/zip-meissen.zip",
            "https://casimir.bsz-bw.de/frontdoor/index/index/docId/18",
        ]
    },
    "speck": {
        "title": "Figuren und Kleinplastiken chinesischer Specksteine",
        "about": """
Die Stiftung Schloss Friedenstein Gotha bewahrt eine der größten und kostbarsten
Sammlungen chinesischer Specksteinarbeiten in Deutschland. Unter den fast 500
Figuren und Gefäßen finden sich neben fantasievollen Darstellungen der
Götterwelt auch Menschen und Tiere sowie eine Reihe von Reliefschnitzereien und
Alltagsgegenständen, die mit diesem Katalog erstmals in Gänze der Öffentlichkeit
erschlossen werden. Kunstschätze aus dem „Reich der Mitte" waren seit dem späten
17. Jahrhundert Teil der herzoglichen Kunstkammer auf Schloss Friedenstein. Mit
ihnen sollte der fürstliche Betrachter in ein „fernöstliches Arkadien" versetzt
werden, glaubte man doch damals an die politische und kulturelle Überlegenheit
Chinas gegenüber dem Abendland. Herzog August von Sachsen-Gotha-Altenburg
(1772-1822) konzentrierte etwa 100 Jahre später seine ostasiatischen Sammlungen
in einem sieben Räume umfassenden „Chinesischen Kabinett". Durch das Studium
dieser Schätze wollte er die Kulturgeschichte Chinas verstehen und schuf so in
Gotha eines der ältesten ethnographischen Museen Europas. 
""",
        "formats": ["xml", "jpeg"],
        "links": [
            "https://casimir.bsz-bw.de/files/18/speckstein-china-2018-03-14.xml",
            "https://casimir.bsz-bw.de/files/18/zip-specksteine.zip",
            "https://casimir.bsz-bw.de/frontdoor/index/index/docId/18",
        ]
    },
    "weise": {
        "title": "Briefe und Akten zur Kirchenpolitik Friedrichs des Weisen und Johanns des Beständigen 1513 bis 1532. Reformation im Kontext frühneuzeitlicher Staatswerdung",
        "about": """
Kurfürst Friedrich der Weise und sein Nachfolger Johann waren Schlüsselgestalten
der frühen Reformationsgeschichte. Als Landesherren Martin Luthers schufen sie
den politischen Rahmen für die Ausbreitung und Verfestigung der Wittenberger
Reformation im wettinisch beherrschten mitteldeutschen Raum und darüber hinaus.

Das Editionsprojekt macht die kirchenpolitischen Akten dieser beiden
herausragenden Reformationsfürsten erstmals in einer gedruckten und einer
elektronischen Fassung für die kirchen- und allgemeinhistorische Forschung
zugänglich.

Unter http://bakfj.saw-leipzig.de präsentiert das Projekt seit November 2015
seine Arbeitsergebnisse digital. Vorerst sind die Metadaten (Absender,
Empfänger, Orte, Datierung) der aufgenommenen Quellen recherchierbar. Nach und
nach werden die Regesten und Editionen ergänzt.

Das Datenset besteht ausschließlich aus Metadaten der erfassten Briefe der
Sammlung und umfasst die Absender, Adressaten, Absendeort, Briefdatum und sofern
bereits vorhanden, die Briefnummer der Druckausgabe. Personen und Orte sind bis
auf wenige Ausnahmen mit GND-Identifiern versehen.
""",
        "formats": ["xml"],
        "links": ["http://bakfj.saw-leipzig.de/api/cmif"],
    },
    "fahrrad": {
        "title": "Das Fahrrad",
        "about": """
Die SLUB fährt Fahrrad! Und das bereits seit 200 Jahren. In unseren Digitalen
Sammlungen findet sich eine kleine aber feine Kollektion rund um das Thema
"Radeln". Die sächsische Industrie brachte nach der Erfindung des Fahrrads 1817
zahlreiche technische Entwicklungen und Fahrradmarken hervor. Maschinenbau und
Feinmechanik waren dafür gute technologische Grundlagen. In Buch- und
Zeitungsverlagen entstanden für die Radfahrer des Bürgertums und später auch für
die Arbeiterklasse zahlreiche Tourenbücher, Wegweiser und Radfahrerkarten. Sie
eignen sich noch heute für Ausfahrten. Auch Dokumente der ersten sächsischen
Radfahrervereine und -verbände wurden inzwischen digitalisiert. Ein Großteil der
Textdigitalisate dieser Kollektion sind im Volltext durchsuchbar. Zahlreiche
historische Radfahrerbücher, die in anderen Bibliotheken digitalisiert wurden,
sind außerdem im SLUBlog und in Wikisource verlinkt. Historische Radfahrerkarten
finden Sie im Kartenforum der SLUB. Stichwort "Feinmechanik": In den
historischen Uhrmacher-Zeitschriften sind auch Produktideen für "Fahrräder"
enthalten – zu finden mittels Volltext- und Metadatensuche jener Kollektion. 
""",
        "formats": ["xml", "jpeg"],
        "links": [
            "http://digital.slub-dresden.de/oai/?verb=ListRecords&metadataPrefix=mets&set=the-bicycle",
            "http://digital.slub-dresden.de/oai/?verb=ListSets",
            "https://api.deutsche-digitale-bibliothek.de/doku/display/ADD/API+der+Deutschen+Digitalen+Bibliothek",
            "http://www.openarchives.org/OAI/openarchivesprotocol.html",
        ]
    },
    "staatarchiv": {
        "title": "Firmenakten des Börsenvereins der deutschen Buchhändler zu Leipzig",
        "about": """
Der Börsenverein der deutschen Buchhändler zu Leipzig war der zentrale
Berufsverband für den herstellenden und vertreibenden Buchhandel (Verlage und
Buchhandlungen). Ab Mitte der 1930er Jahre legte er Akten zu allen
buchhändlerisch tätigen Firmen an, die mit ihm als Mitglied oder durch Aufnahme
ins "Adressbuch des Deutschen Buchhandels" in Verbindung standen. Diese
Firmenakten wurden bis 1945, teilweise auch darüber hinaus geführt. Sie
dokumentieren damit eine auch für den Buchhandel schwierige und bewegte Zeit für
den gesamten deutschsprachigen Raum - und darüber hinaus: London, Riga und
Istanbul können stellvertretend für zahlreiche Orte außerhalb Deutschlands
genannt werden, in denen beim Börsenverein registrierte Verlage und
Buchhandlungen ihren Sitz hatten. Die Metadaten zu den Firmenakten zeigen die
internationale Vernetzung des Buchhandels über den "Leipziger Platz",
dokumentieren die Dichte von Buchhandlungen und Verlagen in einzelnen Orten und
ermöglichen die Spurensuche nach buchhändlerischen Unternehmen in jüdischem
Besitz.

Soweit erhalten geblieben, befindet sich das Geschäftsarchiv des alten Leipziger
Börsenvereins als Bestand "21765 Börsenverein der deutschen Buchhändler zu
Leipzig (I)" im Sächsischen Staatsarchiv, Staatsarchiv Leipzig. Die darin
enthaltenen über 22.000 Firmenakten haben einen Umfang von 80 laufenden Metern
und wurden 2014 bis 2016 archivisch verzeichnet. Die Verzeichnungsangaben zum
gesamten Bestand und weitere Informationen finden sich unter
http://www.archiv.sachsen.de/archiv/bestand.jsp?oid=11.02&bestandid=21765&syg_id=21765

Siehe auch: Thekla Kluttig: Über 22.000 Firmenakten des Börsenvereins der
Deutschen Buchhändler zu Leipzig online zu recherchieren. In: Sächsisches
Archivblatt 2016/2, S. 2 f. (https://publikationen.sachsen.de/bdb/artikel/27188)
""",
        "formats": ["csv"],
        "links": ["https://speicherwolke.uni-leipzig.de/index.php/s/OLi7F7Qs44LwNIa"],
    },
    "leupold": {
        "title": "Zeichnungen bergbaulicher Anlagen (Leupoldsammlung)",
        "about": """
Die vorliegenden Digitalisate stellen einen großen zusammenhängenden Bestand von
Zeichnungen, Rissen und Drucken der ehemaligen bergakademischen Zeichnungs- und
Risssammlung dar. Dabei handelt sich um einen beachtenswerten, wenngleich auch
bruchstückhaft überkommenen Bestand einer der bedeutenden alten
Lehrmittelsammlungen aus der Frühzeit der Bergakademie. Bereits vor der Gründung
der Freiberger Bergakademie legte im Jahr 1746 CARL FRIEDRICH ZIMMERMANN ein
umsichtiges und ausführliches Konzept zur Errichtung einer Bergakademie vor,
dass letztlich Jahrzehnte später mit der Gründung der Freiberger Bergakademie
weitgehend praktisch umgesetzt wurde. Das Ziel der Ausbildung an der neu
gegründeten Freiberger Bergakademie war eine fachspezifische Ausbildung in
Fächern des Montanwesens oder in tangierenden Spezialgebieten. Zur
Kernausbildung gehörte das Zeichnen bei dem man später das Freihandzeichnen,
Situationszeichnen, Planzeichnen, Risszeichnen, technisches Zeichnen und
Konstruktionszeichnen unterschied. Bei den Zeichnungen handelt es sich im
Wesentlichen um technische Zeichnungen, in den meisten Fällen um Unikate. Dass
diese für die Belange der Denkmalpflege eine große Bedeutung haben, zeigen
Baumaßnahmen in Brand-Erbisdorf sowie in Reichenau bei Frauenstein. Eine
Zeichnung ermöglichte den originalgetreuen Nachbau eines Schwungradhaspels beim
Bartholomäus Schacht (Brand-Erbisdorf), ein anderer Riss zeigt und erläutert die
technische Ausstattung einer heute denkmalgerecht freigelegten Erzwäsche
(Reichenau bei Frauenstein/Osterzgebirge). HANS LEUPOLD [* 1907, † 1981], Sohn
eines Studienrates, wurde in Annaberg im Erzgebirge geboren. Im Jahr 1927 begann
er ein Studium an der Freiberger Bergakademie. 1932 wechselte er an die
Technische Hochschule Breslau und schloss hier seine Ausbildung als
Diplomingenieur ab. LEUPOLD, von dem ein Teil seines persönlichen Nachlasses
sowie ein Teil seiner Sammlungen im Bergbau-museum Bochum aufbewahrt werden,
sammelte Zeit seines Lebens alles, was mit historischem Bergbau und der
Kulturgeschichte des Bergbaus im Zusammenhang stand. Dabei entstand eine große
private montanhistorische Sammlung. Diese umfasste historische Bücher,
Grubenlampen, Gezähe, bergmännische Uniformen, kunsthistorische Gegenstände mit
montanhistorischem Bezug, Autographen, Zeichnungen und Risse. Bei vielen
Objekten handelte es sich um historische Unikate, die aus Privat- oder
Familienbesitz oder von Antiquariaten bzw. Antiquitätenhändlern erworben wurden.
LEUPOLD erweiterte beständig seine Sammlung bei einer Vielzahl von Reisen in die
europäischen montanhistorischen Zentren. Dabei bildete das Erzgebirge einen
Sammlungsschwerpunkt.
""",
        "formats": ["xml", "jpeg"],
        "links": [
            "http://digital.ub.tu-freiberg.de/oai/?verb=ListIdentifiers&metadataPrefix=mets&set=leupold",
        ]
    },
    "diederichs": {
        "title": "Graphiksammlung des Eugen Diederichs Verlags",
        "about": """
Die Graphiksammlung des Eugen Diederichs Verlags der Leipziger und Jenaer Jahre
(1896-1945) ist ein zentraler und ungewöhnlicher Bestandteil des Nachlasses
Diederichs in der Thüringer Universitäts- und Landesbibliothek Jena (ThULB)
[Sign.: Nachl. Diederichs VIII]. Sie repräsentiert in umfassender Weise die
Buchgestaltung des Verlags und dokumentiert die historischen
Entwicklungsschritte der Reform der Buchgestaltung, die wesentlich von Eugen
Diederichs (1867-1930) getragen wurde. Standards und Innovationen, aber auch
Herstellungsprozesse werden transparent; ein weiterer Ertrag ist ein
Buchkünstler-Katalog von außerordentlicher Dichte.

Bei den Mediendaten handelt es sich u.a. um Bucheinbände, Vorschläge für
Schrifttypen, Grafiken und Buntpapiere. Die Schöpfer der Grafiken sind mit einer
GND-Angabe versehen. Teilweise existieren Links (über die PPN) zum
Bibliothekskatalog (OPAC) zu den jeweiligen Werken, die diese Grafiken
enthalten. 
""",
        "formats": ["jpeg", "png", "tiff"],
        "links": [
            "https://archive.thulb.uni-jena.de/hisbest/oai2?verb=ListRecords&metadataPrefix=mets&set=ArchFile_class_001:sammlung.diederichs",
            "https://archive.thulb.uni-jena.de/hisbest/rsc/viewer/HisBest_derivate_00010752/Diederichs_450612651_1904_0001.tif",
        ]
    },
    "leipzigdata": {
        "title": "Leipzig Data",
        "about": """
Ziel des Projekts "Leipzig Data" als Teil der Leipziger Initiative für Offene
Daten ist es, im Namespace einen Kernbestand von Daten über Leipziger Belange
als Leipzig Open Data unter der CC-0 Lizenz als Linked Open Data frei verfügbar
zu machen und fortzuschreiben. Dazu ist insbesondere eine entsprechende
Ontologie zu entwickeln, LEO – die Leipzig Ontology. Eine solcher
Kerndatenbestand als konsensual befestigte gemeinsame Freie Sprache ist die
Grundlage auch für die private Freie Rede Freier Bürger über strittige Leipziger
Sachverhalte, deren Sichtbarkeit und digitale Unterstützung als Leipzig Data mit
der Leipziger Initiative für Offene Daten befördert werden soll, ohne dass sich
die Initiative diese Meinungen zu eigen machen oder auch nur gutheißen muss. Die
Daten stehen zum Download bei github sowie über einen RDF Store mit SPARQL
Endpunkt bereit. Eine genauere Beschreibung der "kontrollierten Vokabulare"
(Ontologie) ist auf unseren Webseiten zu finden. 
""",
        "formats": ["turtle"],
        "links": [
            "http://leipzig-data.de/ontology/",
            "https://github.com/LeipzigData/RDFData",
            "http://leipzig-data.de/",
        ]
    },
    "stammbuch": {
        "title": "Stammbücher",
        "about": """
Die Universitäts- und Landesbibliothek Sachsen-Anhalt sammelt seit Langem
Stammbücher, die in der Region und bevorzugt im Umfeld der Universität
entstanden sind. Die ältesten Stammbücher haben Eintragungen aus der zweiten
Hälfte des 16. Jahrhunderts. Der Bestand umfasst heute fast 290 Stammbücher und
gehört damit zu den bedeutendsten Sammlungen in Deutschland. Stammbücher sind
ideale Quellen für die interdisziplinäre Forschung. Sie geben Aufschluss zu
Fragen der Heraldik und der Personen-, Familien- und Netzwerkforschung,
enthalten aber auch Material für sozial-, literatur-, kunst- und
mentalitätsgeschichtliche Studien. Notwendig dafür ist eine vollständige
Erschließung und Digitalisierung, die mit dem Ziel der Verfügbarkeit im Open
Access bereits begonnen wurde, mittlerweile liegen ca. 100 Stammbücher als
Digitalisate vor.
""",
        "formats": ["xml", "jpeg"],
        "links": [
            "http://digital.bibliothek.uni-halle.de/hd/oai/?verb=GetRecord&metadataPrefix=mods&identifier=oai:digital.bibliothek.uni-halle.de/hd:2634108&mode=view",
            "http://digital.bibliothek.uni-halle.de/hd/nav/classification/321544",
        ]
    },
    "weinhold": {
        "title": "Lehrbücher von Adolf Ferdinand Weinhold",
        "about": """
Adolf Ferdinand Weinhold, Lehrer an der Gewerbschule Chemnitz, gilt als
Begründer der Experimentalphysik und Schöpfer zahlreicher Versuchsanordnungen
und Geräte. So entwickelte Weinhold eine doppelwandige Glasflasche um
verflüssigte Gase aufzubewahren, und pumpte zwischen Innen- und Außenwand die
Luft ab. Das Vakuum verhindert den Wärmeaustausch mit der Umgebung und die
Flasche hält tiefe Temperaturen über Stunden hinweg. Das gleiche Prinzip findet
– heute vor allem für die Speicherung von Wärme – in der Thermoskanne Anwendung.

Die Auswahl umfasst 3 Lehrbücher von Adolf Ferdinand Weinhold in
unterschiedlichen Auflagen aus dem Wissenschaftlichen Altbestand der
Universitätsbibliothek Chemnitz. Zu jedem Werk werden die hochauflösenden
Bilddateien bereitgestellt. Die Metadaten enthalten neben der inhaltlichen
Struktur auch Verlinkungen zur GND, zu den Bilddateien in Originalgröße und den
Volltexten, soweit diese vorhanden sind. 
""",
        "formats": ["xml", "jpeg"],
        "links": [
            "https://box.tu-chemnitz.de/index.php/s/ZlaIbkNG8HAqCoH",
            "https://www.tu-chemnitz.de/ub/projekte-und-sammlungen/sammlungen/digitale_sammlung/collection.html?sammlung=5",
        ]
    },
    "bismarck": {
        "title": "Bismarck-Album",
        "about": """
Das Datenset ist eine Kombination der Bestände des Universitätsarchivs und der
Universitätsbibliothek Chemnitz und enthält das Bismarck Album aus dem Nachlass
Carl von Bach sowie das Mitgliederverzeichnis des Vereins Deutscher Ingenieure
aus dem Jahr 1895.

Dieses Album wurde dem Fürst Bismarck zu seinem 80 Geburtstag 1895 vom Verein
Deutscher Ingenieure überreicht. Das Album besteht aus 36 Blättern, wobei das
erste Blatt die Widmung des Gesamtvereines ist und die anderen 35 Blätter die
der einzelnen Bezirksvereine. Die Blätter zeigen Grafiken, die den Verein bzw.
die einzelnen Bezirksvereine verkörpern sollen. Im einleitenden Text werden die
einzelnen Grafiken beschrieben.

Die Metadaten des Bismarck-Albums sind je Seite in einer einzelnen Datei
erfasst. Die Metadaten des Mitgliederverzeichnisses sind in einer einzigen Datei
erfasst und enthalten neben der inhaltlichen Struktur auch Verlinkungen zur GND,
zu den Bilddateien in Originalgröße und den Volltexten. 
""",
        "formats": ["xml", "jpeg"],
        "links": [
            "https://box.tu-chemnitz.de/index.php/s/YfMr86DE7MmhoE4",
        ]
    },
    "handschriften": {
        "title": "Auswahl illuminierter mittelalterlicher Handschriften",
        "about": """
Die Universitätsbibliothek bewahrt ca. 3.000 mittelalterliche Handschriften auf,
die (ganz überwiegend) zwischen dem 8. und dem frühen 16. Jahrhundert entstanden
sind. Zahlreiche von ihnen weisen Buchschmuck auf, der von einfachen
Tintenzeichnungen auf ganz basalem Niveau bis hin zu äußerst qualitätvollen
Schmuckbuchstaben (Initialen) und illustrierenden Miniaturen in Deckfarben und
Gold reichen kann. Die künstlerische Ausschmückung mittelalterlicher Bücher war
kein ästhetischer Selbstzweck: Handschriften aus dieser Zeit funktionieren nicht
wie heutige Bücher, sie haben zum Beispiel üblicherweise kein Titelblatt, keine
Seitenzählungen und kein Inhaltsverzeichnis. Die Orientierung im Buch erfolgte
vielmehr über eine optische Navigation, über farbig-graphische Auszeichnungen
und hierarchisch abgestufte Buchschmuckelemente. Mit ihnen wurden Text- und
Abschnittsanfänge wie auch wichtige Sprungstellen innerhalb eines Fließtextes
optisch markiert und waren so für den Leser leicht auffindbar und anzusteuern.

Der hier vorgestellte Datenbestand umfasst IIIF-Manifeste sowie Links zur
Präsentation via Mirador von 72 mittelalterlichen Handschriften, die alle
besonderen Buchschmuck in hoher oder zumindest interessanter Qualität aufweisen.
Bei den Manifest-Dateien handelt es sich um json-Dateien, die Informationen zu
den Bilddaten der digitalisierten Handschriftenobjekte, zu deskriptiven
Metadaten (z. B. Inhalt, Material, Entstehungszeit und -ort der Handschriften)
sowie Informationen zur inhaltlichen Gliederung und zu wichtigen Abschnitten der
Handschriftenwerke enthalten.
""",
        "formats": ["tsv", "json"],
        "links": [
            "https://iiif.ub.uni-leipzig.de/static/collections/misc/cdvost2018.json",
        ]
    },
    "gbv": {
        "title": "Bibliothekskataloge, Verbundzentrale des GBV (VZG)",
        "about": """
Bibliothekskataloge verzeichnen Bücher, Zeitschriften und andere Medien mit
bibliographischen Angaben (Titel, Autor, Jahr...) und Exemplardaten (Standort,
Signatur, Verfügbarkeit...). Die Verbundzentrale des GBV stellt einheitliche
Schnittstellen zum Zugriff auf Kataloge von mehreren Hundert Bibliotheken
bereit, darunter alle Hochschulbibliotheken der GBV-Mitglieder Thüringen und
Sachsen-Anhalt. Für Sächsische Bibliotheken gibt es teilweise entsprechende
Schnittstellen. Konkret können Bibliothekskataloge per SRU-API durchsucht werden
(beispielsweise Suche nach einer ISBN oder nach allen Veröffentlichungen eines
Autors) und per DAIA-API ermittelt werden, welche Exemplare eines Titels
verfügbar oder ausgeliehen sind.

Die Metadaten frei verfügbar, sie können aber Verweise auf unfreie Cover,
Inhaltsverzeichnisse und andere Mediendateien enthalten.
""",
        "formats": ["xml", "json"],
        "links": [
            "https://verbundwiki.gbv.de/display/VZGVers/Coding+da+Vinci",
        ]
    }
}

print(json.dumps(datasets))
