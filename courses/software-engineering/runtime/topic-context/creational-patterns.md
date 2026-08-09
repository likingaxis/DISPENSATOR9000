# Topic Context

**topic_id**: creational-patterns
**title**: Creational Patterns

## Retrieval Metadata
- Primary fragments: 223
- Secondary fragments: 10
- Visual assets candidate: 74
- Estimated context tokens: ~2690

## 1. Primary Evidence (Official Coverage)

### Source: slides-10-design-patterns (`official-slides\II parte ISW\10-Design patterns.pdf`)
#### Page 17
> 18

> Abstract Factory: esempio (2)

> Client

> Window1 Window2 ScrollBar1 ScrollBar2

> <<istantiates>>

> <<istantiates>>

> createWindow() createScollBar()

> Factory

> createWindow() createScollBar()

> Factory1

> createWindow() createScollBar()

> Factory2

> Window ScrollBar

> © UniRoma2 - Ingegneria del Software

#### Page 18
> 19

> Abstract Factory: esempio (3)

> Factory f = new Factory1(); Window w = f.createWindow(); ... ScrollBar s = f.createScrollBar();

> Window w = new Window1(); ... ScrollBar s = new ScrollBar1();

> Senza utilizzare l’Abstract Factory l’applicazione client deve

> esplicitamente istanziare gli oggetti. Il rispetto delle relazioni è cablato nel codice e deve essere

> noto al client.

> Con l’Abstract Factory la responsabilità è demandata alla

> Factory.

> © UniRoma2 - Ingegneria del Software

#### Page 19
> 20

> Abstract Factory: struttura

> Client

> ProductB1 ProductB2

> <<istantiates>>

> <<istantiates>>

> createProductA() createProductB()

> AbstractFactory

> createProductA() createProductB()

> ConcreteFactory1

> createProductA() createProductB()

> ConcreteFactory2

> AbstractProductA

> AbstractProductB

> ProductA1 ProductA2

> © UniRoma2 - Ingegneria del Software

#### Page 20
> 21

> Altre caratteristiche

> Applicabilità

> • A sistema che deve essere indipendente dalle  modalità di creazione dei prodotti con cui opera

> • A sistema che deve poter essere configurato per  usare famiglie di prodotti diverse

> • Il client non deve essere legato ad una specifica  famiglia Partecipanti

> • AbstractFactory e ConcreteFactory

> • AbstractProduct e ConcreteProduct

> • Applicazione Client

> © UniRoma2 - Ingegneria del Software

#### Page 21
> 22

> Altre caratteristiche (2)

> Conseguenze

> • Le classi concrete sono isolate e sotto controllo

> • La famiglia di prodotti può essere cambiata  rapidamente perché la factory completa  compare in un unico punto del codice

> • Aggiungere nuove famiglie di prodotti richiede  ricompilazione perché l’insieme di prodotti  gestiti è legato all’interfaccia della factory

> © UniRoma2 - Ingegneria del Software

#### Page 22
> 23

> Factory Method

> Scopo: Definire una interfaccia per la

> creazione di un oggetto, che consenta di  decidere a tempo di esecuzione quale  specifico oggetto istanziare.  Motivazione: E’ un pattern ampiamente

> usato nei framework, dove le classi astratte  definiscono le relazioni tra gli elementi del  dominio, e sono responsabili per la  creazione degli oggetti concreti.

> Classificazione: creazionale basato su classi

> © UniRoma2 - Ingegneria del Software

#### Page 23
> 24

> Factory Method: esempio

> Consideriamo un framework di gestione di

> documenti di tipo diverso.

> Le due astrazioni chiave sono Application e

> Document. Gli utilizzatori devono definire delle sotto

> classi per ottenere delle implementazioni  adatte all’applicazione specifica.

> Application contiene la logica per sapere

> quando un nuovo documento sarà creato,  ma non per sapere quale tipo di documento  creare.

> © UniRoma2 - Ingegneria del Software

#### Page 24
> 25

> Factory Method: esempio (2)

> Il pattern Factory incapsula la conoscenza

> della specifica classe da creare al di fuori  del framework

> createDocument() openDocument()

> Application

> open() close()

> Document

> open() close()

> PDFDocument

> createDocument()

> MyApplication

> Document doc = createDocument doc.open()

> return new PDFDocument()

> © UniRoma2 - Ingegneria del Software

#### Page 25
> 26

> Factory Method: struttura

> factoryMethod() anOperation()

> Creator Product

> ConcreteProduct

> factoryMethod()

> ConcreteCreator

> product = factoryMethod()

> return new concreteProduct()

> © UniRoma2 - Ingegneria del Software

#### Page 26
> 27

> Altre caratteristiche

> Applicabilità

> • Una classe non è in grado di sapere in anticipo le  classi di oggetti che deve creare. • Una classe vuole che le sue sottoclassi scelgano  gli oggetti da creare. • Le classi delegano la responsabilità di creazione. Partecipanti

> • Product e ConcreteProduct • Creator e ConcreteCreator Conseguenze

> • Elimina la necessità di riferirsi a classi dipendenti  dall’applicazione all’interno del codice.

> © UniRoma2 - Ingegneria del Software

#### Page 27
> 28

> Adapter

> Scopo: Convertire l’interfaccia di una

> classe esistente incompatibile con un client,  in una compatibile. Motivazione: Consideriamo un editor che

> consente di disegnare e comporre elementi  grafici. L’astrazione chiave è un singolo  oggetto grafico. Supponiamo di voler  integrare un nuovo componente, ma che  questo non abbia una interfaccia  compatibile con l’editor.

> Classificazione: strutturale basato su classi/oggetti

> © UniRoma2 - Ingegneria del Software

#### Page 28
> 29

> Adapter: esempio

> Supponiamo di voler integrare il componente

> Circle nell’editor che già supporta le forme  Triangle e Rectangle.

> getPosition() setPosition() Display()

> Shape

> Display()

> Rectangle

> Display()

> Triangle

> Show()

> Circle

> © UniRoma2 - Ingegneria del Software

#### Page 29
> 30

> Adapter: esempio (2)

> Soluzione 1: Object Adapter

> getPosition() setPosition() Display()

> Shape

> Display()

> Rectangle

> Display()

> Triangle

> Show()

> Circle

> Display()

> CircleAdapter

> © UniRoma2 - Ingegneria del Software

#### Page 30
> 31

> Adapter: esempio (3)

> Soluzione 1: Class Adapter

> getPosition() setPosition() Display()

> Shape

> Display()

> Rectangle

> Display()

> Triangle

> Show()

> Circle

> Display()

> CircleAdapter

> © UniRoma2 - Ingegneria del Software

### Source: slides-11-dp-examples (`official-slides\II parte ISW\11-Design Patterns - Esempi.pdf`)
#### Page 36
> Factory Method: esempio

> Uniroma2 - Ingegneria del Software 37

> Scenario: supponiamo di avere una applicazione  che legge dei dati da un file di testo contenente le  informazioni relative a delle rilevazioni di letture di  contatori per acqua e gas.

> Nel nostro codice abbiamo una classe dedicata a  questo scopo, che legge i vari formati dei file, la  classe AcquisizioneLetture:

#### Page 37
> Factory Method: esempio (2)

> Uniroma2 - Ingegneria del Software 38

> classi specializzate nella

> lettura di file in formato testo che implementano l'interfaccia FileLettureReader Ritornano un oggetto

> di tipo Lettura

#### Page 38
> Factory Method: esempio (3)

> • Succede però che il nostro cliente inizia a  vendere anche energia elettrica e deve di  conseguenza acquisire anche i file con le  relative letture.

> • E' quindi necessario gestire un tipo aggiuntivo  di file, e modifichiamo la nostra classe:

> Uniroma2 - Ingegneria del Software 39

#### Page 39
> Factory Method: esempio (4)

> Uniroma2 - Ingegneria del Software 40

> E' stato necessario aprire la

> classe e introdurre la modifica

#### Page 40
> Factory Method: esempio (5)

> • Operazione non pratica, soprattutto se  prevediamo di ripeterla in futuro.

> • Dovremmo separare il codice soggetto a  modifiche da quello sempre uguale, come fare?

> • Ad esempio incapsulando la creazione di  FileLettureReader all'interno di una nuova  classe FileReaderFactory:

> Uniroma2 - Ingegneria del Software 41

#### Page 41
> Factory Method: esempio (6)

> Uniroma2 - Ingegneria del Software 42

#### Page 42
> Factory Method: esempio (7)

> Uniroma2 - Ingegneria del Software 43

#### Page 43
> Factory Method: esempio (8)

> • Abbiamo ottenuto:

> • La chiusura di AcquisizioneLetture alle modifiche

> • La possibilità di riutilizzare ReaderFactory anche  altrove, isolando in essa le modifiche

> Uniroma2 - Ingegneria del Software 44

#### Page 44
> Factory Method: esempio (9)

> Uniroma2 - Ingegneria del Software 45

#### Page 45
> Factory Method: esempio (10)

> • Poi accade che acquisiamo due importanti  clienti, che vendono acqua e gas ed utilizzano  un proprio formato XML di interscambio dati

> • Adeguiamo il nostro codice alle nuove  esigenze, scrivendo due nuove factory class ad  hoc per loro,Cliente1ReaderFactory e  Cliente2ReaderFactory che derivano dalla  nostra ReaderFactory

> Uniroma2 - Ingegneria del Software 46

#### Page 46
> Factory Method: esempio (11)

> Uniroma2 - Ingegneria del Software 47

#### Page 47
> Factory Method: esempio (12)

> • Corretto, ma notiamo due cose:

> • AcquisizioneLetture ha sempre bisogno che gli  venga passato un factory per funzionare, tanto che  viene passato nel costruttore.

> • Le operazioni fatte sulla lettura, come abbiamo  visto all'inizio, sono sempre quelle. • Sarebbe utile quindi portare il factory  direttamente dentro AcquisizioneLetture per  rendere la classe autosufficiente, ma senza  perdere la flessibilità ottenuta fino ad ora.

> Uniroma2 - Ingegneria del Software 48

#### Page 48
> Factory Method: esempio (13)

> • Torniamo alla prima versione di AcquisizioneLetture,  ma questa volta incapsuliamo la creazione delle classi  FileLettureReader all'interno di un metodo astratto e  rendiamo quindi astratta tutta la classe.

> • Da questa deriviamo le varie versioni per i vari clienti,  implementando in ognuna di esse il metodo che  incapsula la creazione delle classi FileLettureReader.

> • Ora abbiamo una AcquisizioneLetture per ogni cliente,  ognuna contenente la propria logica di lettura dei file.

> Uniroma2 - Ingegneria del Software 49

#### Page 49
> Factory Method: esempio (14)

> Uniroma2 - Ingegneria del Software 50

> La classe base non conosce il  FileLettureReader su cui itera  e da cui ricava le letture,  perché questo dipende dalle  classi derivate. Abbiamo conservato  disaccoppiamento e  flessibilità.

#### Page 50
> Factory Method: esempio (15)

> Uniroma2 - Ingegneria del Software 51

#### Page 51
> Factory Method: esempio (16)

> Uniroma2 - Ingegneria del Software 52

#### Page 52
> Factory Method: esempio (17)

> Uniroma2 - Ingegneria del Software 53

#### Page 53
> Factory Method: esempio (17)

> Uniroma2 - Ingegneria del Software 54

> Creator AcquisizioneLetture

> Product FileLettureReader

> ConcreteCreator AcquisizioneLettureConcreta  AcquisizioneLettureCliente1  AcquisizioneLettureCliente2

> ConcreteProduct GasLettureReader  H2OLettureReader  EELettureReader  Cliente1GasLettureReader  Cliente1H2OLettureReader  Cliente2GasLettureReader  Cliente2H2OLettureReader

> Ricordando il diagramma UML del Factory Method,  abbiamo costruito:

#### Page 54
> Factory Method: esempio (18)

> Uniroma2 - Ingegneria del Software 55

#### Page 55
> Factory Method: esempio (19)

> Uniroma2 - Ingegneria del Software 56

## 2. Secondary Evidence (BM25 Lexical + Concepts)

### Source: theory-summary (`teoria.pdf`)
#### Page 1 (BM25: 20.56)
> ▪1. Abstract Factory ▪2. Factory Method

#### Page 22 (BM25: 20.56)
> l'esecuzione e sono quindi dinamiche. 1. Abstract Factory Fa parte della classe di DP creazionali ed ha lo scopo di fornire un'interfaccia per

#### Page 1 (BM25: 19.91)
> ▪1. Abstract Factory ▪2. Factory Method ▪3. Adapter

#### Page 25 (BM25: 19.91)
> 2. Factory Method L’idea di fondo è che la creazione di un oggetto non avviene direttamente nel

#### Page 24 (BM25: 15.85)
> - Cambiare famiglia di prodotti è facile: basta sostituire la factory - Aggiungere una nuova famiglia richiede nuove classi e

#### Page 25 (BM25: 11.78)
> codice, ma viene delegata a un metodo specializzato, chiamato appunto factory method . Questo metodo può essere ridefinito dalle sottoclassi per istanziare oggetti specifici. Nel codice orientato agli oggetti, spesso si vuole evitare

#### Page 25 (BM25: 10.22)
> concreta instanziare, mantenendo il codice cliente indipendente. Il Factory Method è utile quando un codice deve lavorare con un’interfaccia o una superclasse, ma non deve sapere quale sottoclasse concreta utilizzare. La

#### Page 25 (BM25: 9.78)
> di usare direttamente new per creare un’istanza di una classe concreta, perché così si rende il codice rigido e poco estensibile. Il Factory Method serve proprio a risolvere questo problema: consente alle sottoclassi di decidere quale classe

#### Page 25 (BM25: 9.38)
> semplici dove basta una new • Il Factory Method crea un solo oggetto per volta e si basa sul override del metodo da parte delle sottoclassi.

#### Page 0 (BM25: 8.69)
> ▪4. Service Oriented Architecture (SOA) ◦Design Patterns

## 3. Visual Assets Candidates

- **asset_id**: e092961c-294e-4b94-b15d-e7fdc70b79e3
  source: slides-10-design-patterns
  page: 17
  type: embedded_image
  path: `d060689a_p17_i0.png`

- **asset_id**: 91d30bc5-fffa-4ef7-8694-20896f3f3471
  source: slides-10-design-patterns
  page: 17
  type: embedded_image
  path: `d060689a_p17_i1.png`

- **asset_id**: 50023457-ac21-43ac-89c9-ee05c4b4b5f1
  source: slides-10-design-patterns
  page: 17
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 3e1954a3-bb0f-41fc-bed4-95d7a2e5fef3
  source: slides-10-design-patterns
  page: 18
  type: embedded_image
  path: `d060689a_p18_i0.png`

- **asset_id**: cbcc60ed-ed9a-4aa9-ade0-63d53164dbd3
  source: slides-10-design-patterns
  page: 18
  type: embedded_image
  path: `d060689a_p18_i1.png`

- **asset_id**: 31988f62-d91f-47c3-97ae-77004d83d3bf
  source: slides-10-design-patterns
  page: 18
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 8429a6d3-b9fe-4139-aa2f-c9157048f7b3
  source: slides-10-design-patterns
  page: 19
  type: embedded_image
  path: `d060689a_p19_i0.png`

- **asset_id**: 39c6e152-1e97-4991-b46b-f43d55122dab
  source: slides-10-design-patterns
  page: 19
  type: embedded_image
  path: `d060689a_p19_i1.png`

- **asset_id**: 72312117-7f9c-4cd0-9f23-fa1d3faa4177
  source: slides-10-design-patterns
  page: 19
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 7bea0999-d494-4591-b461-a740a181ca9e
  source: slides-10-design-patterns
  page: 20
  type: embedded_image
  path: `d060689a_p20_i0.png`

- **asset_id**: 4605a5d2-08f0-48a5-92c6-4d8aafa09e83
  source: slides-10-design-patterns
  page: 20
  type: embedded_image
  path: `d060689a_p20_i1.png`

- **asset_id**: 805c61b6-66e2-4292-a240-76e4d21317f5
  source: slides-10-design-patterns
  page: 20
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: c131efbd-0b3a-435c-a9fe-a769a86b9935
  source: slides-10-design-patterns
  page: 21
  type: embedded_image
  path: `d060689a_p21_i0.png`

- **asset_id**: 0b721786-b7ec-421e-8cff-245ab55e8f2a
  source: slides-10-design-patterns
  page: 21
  type: embedded_image
  path: `d060689a_p21_i1.png`

- **asset_id**: 016b5dad-c539-447b-95a3-a62c39377ff8
  source: slides-10-design-patterns
  page: 21
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 247c8926-3383-4908-bbdd-8a5b83244664
  source: slides-10-design-patterns
  page: 22
  type: embedded_image
  path: `d060689a_p22_i0.png`

- **asset_id**: 03ffb20e-ecc5-439b-8d16-b55981c92332
  source: slides-10-design-patterns
  page: 22
  type: embedded_image
  path: `d060689a_p22_i1.png`

- **asset_id**: 5e89e4f2-a466-46cd-be07-df6b6dcf7685
  source: slides-10-design-patterns
  page: 22
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 8f75953d-494f-4716-a61b-9af1b40626f0
  source: slides-10-design-patterns
  page: 23
  type: embedded_image
  path: `d060689a_p23_i0.png`

- **asset_id**: 63c469bc-6dea-4b65-b32d-6e69d6f7005a
  source: slides-10-design-patterns
  page: 23
  type: embedded_image
  path: `d060689a_p23_i1.png`

- **asset_id**: 4cffbbe4-6244-4493-a0fe-c63f70a7b96b
  source: slides-10-design-patterns
  page: 23
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 4e0d43b2-64eb-4944-ba64-7ddd7a6c9e38
  source: slides-10-design-patterns
  page: 24
  type: embedded_image
  path: `d060689a_p24_i0.png`

- **asset_id**: 8d08080f-5ac5-48b2-8fdc-3f300605922e
  source: slides-10-design-patterns
  page: 24
  type: embedded_image
  path: `d060689a_p24_i1.png`

- **asset_id**: 865d16e4-bb32-49f0-b165-610c09a5ddc8
  source: slides-10-design-patterns
  page: 24
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b107821b-c541-42e6-a021-f9f2b18f9ddd
  source: slides-10-design-patterns
  page: 25
  type: embedded_image
  path: `d060689a_p25_i0.png`

- **asset_id**: d1aeebad-df70-4029-8505-1fa92570abde
  source: slides-10-design-patterns
  page: 25
  type: embedded_image
  path: `d060689a_p25_i1.png`

- **asset_id**: 2b1b6572-e3c6-47d3-9927-ae634ddfe5f4
  source: slides-10-design-patterns
  page: 25
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 9eb3597c-669a-4d40-8f22-5eebad0673fd
  source: slides-10-design-patterns
  page: 26
  type: embedded_image
  path: `d060689a_p26_i0.png`

- **asset_id**: cef74877-f305-41f8-b251-fad1cda66c96
  source: slides-10-design-patterns
  page: 26
  type: embedded_image
  path: `d060689a_p26_i1.png`

- **asset_id**: da512363-7970-4a8e-bd22-c37e17d5dda6
  source: slides-10-design-patterns
  page: 26
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: df36ca2f-01d9-4fe6-87fc-4e1c6d7e1da0
  source: slides-10-design-patterns
  page: 27
  type: embedded_image
  path: `d060689a_p27_i0.png`

- **asset_id**: 3c4c0a8e-91eb-41c0-9e15-28a315abcadf
  source: slides-10-design-patterns
  page: 27
  type: embedded_image
  path: `d060689a_p27_i1.png`

- **asset_id**: 8aa859e4-9d99-4610-a221-916940400c0e
  source: slides-10-design-patterns
  page: 27
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 0eb42fc6-3a7e-4dc0-9e8d-66571bf63a7b
  source: slides-10-design-patterns
  page: 28
  type: embedded_image
  path: `d060689a_p28_i0.png`

- **asset_id**: 83e43283-2d64-4da7-83bf-e5683efd7e6d
  source: slides-10-design-patterns
  page: 28
  type: embedded_image
  path: `d060689a_p28_i1.png`

- **asset_id**: a4bfb72d-b408-4d9e-8880-26700b8ae40f
  source: slides-10-design-patterns
  page: 28
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: dd534863-8dd4-4970-ac56-2c54f3bf5e8e
  source: slides-10-design-patterns
  page: 29
  type: embedded_image
  path: `d060689a_p29_i0.png`

- **asset_id**: 82323a63-f616-442d-97d7-bf93df89fa63
  source: slides-10-design-patterns
  page: 29
  type: embedded_image
  path: `d060689a_p29_i1.png`

- **asset_id**: b8263c1e-a387-4263-8a8d-91a524c33451
  source: slides-10-design-patterns
  page: 29
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 61a860bb-bd50-46d0-a6ab-edc4f3d269b5
  source: slides-10-design-patterns
  page: 30
  type: embedded_image
  path: `d060689a_p30_i0.png`

- **asset_id**: d1d73685-3985-4c16-a667-928921cb6b52
  source: slides-10-design-patterns
  page: 30
  type: embedded_image
  path: `d060689a_p30_i1.png`

- **asset_id**: 5140c0d9-6144-4b64-8c01-2c8647c77571
  source: slides-10-design-patterns
  page: 30
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: f7103290-f63e-4669-9075-c1cedd50898a
  source: slides-11-dp-examples
  page: 36
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: c0c4965d-3cce-421e-b698-5f65074b0d6a
  source: slides-11-dp-examples
  page: 37
  type: embedded_image
  path: `ab9e6ef8_p37_i0.png`

- **asset_id**: 3d40334b-735b-41e6-a013-171bf1a28351
  source: slides-11-dp-examples
  page: 37
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: f9480c8b-e28e-4394-9770-405947744715
  source: slides-11-dp-examples
  page: 38
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: c325056b-73f5-473b-8c1d-b529a2fa1aaf
  source: slides-11-dp-examples
  page: 39
  type: embedded_image
  path: `ab9e6ef8_p39_i0.png`

- **asset_id**: 05258e5d-83fc-4ce4-a935-24d25c276cdb
  source: slides-11-dp-examples
  page: 39
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: c05a1b77-78ec-4f9b-859f-f293947a33cf
  source: slides-11-dp-examples
  page: 40
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: a51d6aba-23e2-4dea-bca5-e24638c1e5b8
  source: slides-11-dp-examples
  page: 41
  type: embedded_image
  path: `ab9e6ef8_p41_i0.png`

- **asset_id**: 9ac6c975-951c-4e93-9cec-254557e63460
  source: slides-11-dp-examples
  page: 41
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 3dc41739-9365-4e73-912c-b3cf22a9601e
  source: slides-11-dp-examples
  page: 42
  type: embedded_image
  path: `ab9e6ef8_p42_i0.png`

- **asset_id**: eff04a09-ad3b-46f5-9a39-e21cd879689c
  source: slides-11-dp-examples
  page: 42
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b0e34f93-9ebd-4fdb-a496-01f5ab813aef
  source: slides-11-dp-examples
  page: 43
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 9226325f-2813-4cd6-8cb2-e47232969bd3
  source: slides-11-dp-examples
  page: 44
  type: embedded_image
  path: `ab9e6ef8_p44_i0.jpeg`

- **asset_id**: 36481497-4b89-4e9f-9c9d-94c6470d4519
  source: slides-11-dp-examples
  page: 44
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b02f8d0e-d10f-4bc5-a8ef-482a45198d66
  source: slides-11-dp-examples
  page: 45
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 63c2c7ee-b984-4417-b720-80934b633502
  source: slides-11-dp-examples
  page: 46
  type: embedded_image
  path: `ab9e6ef8_p46_i0.png`

- **asset_id**: 15c22452-1c56-4b29-96be-e7de58db3ae4
  source: slides-11-dp-examples
  page: 46
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: fc9b584c-f41f-4d3c-b4b1-aa0b8e73a4d4
  source: slides-11-dp-examples
  page: 47
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: cbbf6079-7b7b-47cc-9553-ab86cb1c659e
  source: slides-11-dp-examples
  page: 48
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 1f31b6da-bdae-4d3e-82f1-dac973c27dcf
  source: slides-11-dp-examples
  page: 49
  type: embedded_image
  path: `ab9e6ef8_p49_i0.png`

- **asset_id**: 295ca0b7-5c6a-4683-aac8-99aff346aaf4
  source: slides-11-dp-examples
  page: 49
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 0becb746-a4d5-4c95-97e0-6674516d2981
  source: slides-11-dp-examples
  page: 50
  type: embedded_image
  path: `ab9e6ef8_p50_i0.png`

- **asset_id**: fb251d89-ba37-4adf-90e7-bc922f4dcf82
  source: slides-11-dp-examples
  page: 50
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 5d07be82-06be-4433-85c9-81d928164426
  source: slides-11-dp-examples
  page: 51
  type: embedded_image
  path: `ab9e6ef8_p51_i0.png`

- **asset_id**: ae20f5af-7bcd-48a9-9dfc-cc86f8514c0b
  source: slides-11-dp-examples
  page: 51
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 9711ce28-c36c-49bd-8b10-0555c4aa8ca8
  source: slides-11-dp-examples
  page: 52
  type: embedded_image
  path: `ab9e6ef8_p52_i0.png`

- **asset_id**: 08b84020-0e06-40fb-b421-708e7f921ecf
  source: slides-11-dp-examples
  page: 52
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 39b74a3b-bc0c-400f-bc34-afb8e1af5dc4
  source: slides-11-dp-examples
  page: 53
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 5c85c9ec-6ef6-44b2-b78c-cb1f6ee7b06c
  source: slides-11-dp-examples
  page: 54
  type: embedded_image
  path: `ab9e6ef8_p54_i0.png`

- **asset_id**: bf906edd-c711-4ae5-8e61-1a13eb2fe1e5
  source: slides-11-dp-examples
  page: 54
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: fdb4c7b9-53bb-4b8d-b752-3a8975d46854
  source: slides-11-dp-examples
  page: 55
  type: embedded_image
  path: `ab9e6ef8_p55_i0.png`

- **asset_id**: 0ec23426-adb1-4d34-93f0-cea2d910c216
  source: slides-11-dp-examples
  page: 55
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

