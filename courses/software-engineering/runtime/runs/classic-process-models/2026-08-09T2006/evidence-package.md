# Topic Context

**topic_id**: classic-process-models
**title**: Modelli Sequenziali (Waterfall, Prototyping)

## Retrieval Metadata
- Primary fragments: 136
- Secondary fragments: 0
- Visual assets candidate: 64
- Estimated context tokens: ~1720

## 1. Primary Evidence (Official Coverage)

### Source: slides-02-process-1 (`official-slides\I parte ISW - SistSW\02-Processo software parte1.pdf`)
#### Page 0
> UniRoma2 - ISW/SSW 1

> Il processo software

> • Processo software

> – serie di attività necessarie alla realizzazione del

> prodotto software nei tempi, con i costi e con le  desiderate caratteristiche di qualità.

> • Nel suo contesto:

> – si applicano metodi, tecniche e strumenti

> – si creano prodotti (sia intermedi che finali)

> – si stabilisce il controllo gestionale del progetto

> – si garantisce la qualità

> – si governano le modifiche

#### Page 1
> UniRoma2 - ISW/SSW 2

> Fasi del processo

> • Come visto, il processo software segue un ciclo di vita che si articola  in 3 stadi (sviluppo, manutenzione, dismissione). Nel primo stadio si  possono riconoscere due tipi di fasi:

> – fasi di tipo definizione

> – fasi di tipo produzione • Le fasi di definizione si occupano di "cosa" il software deve fornire. Si  definiscono i requisiti, si producono le specifiche

> • Le fasi di produzione definiscono "come" realizzare quanto ottenuto  con le fasi di definizione. Si progetta il software, si codifica, si integra e  si rilascia al cliente

> • Lo stadio di manutenzione è a supporto del software realizzato e  prevede fasi di definizione e/o produzione al suo interno

> • Durante ogni fase si procede ad effettuare il testing di quanto prodotto,  mediante opportune tecniche di verifica e validazione (V&V) applicate  sia ai prodotti intermedi che al prodotto finale

#### Page 2
> UniRoma2 - ISW/SSW 3

> Tipi di manutenzione

> • Manutenzione correttiva, che ha lo scopo di eliminare i

> difetti (fault) che producono guasti (failure) del software

> • Manutenzione adattativa, che ha lo scopo di adattare il

> software ad eventuali cambiamenti a cui è sottoposto

> l'ambiente operativo per cui è stato sviluppato

> • Manutenzione perfettiva, che ha lo scopo di estendere il

> software per accomodare funzionalità aggiuntive

> • Manutenzione preventiva (o software reengineering), che

> consiste nell'effettuare modifiche che rendano più semplici

> le correzioni, gli adattamenti e le migliorie

#### Page 3
> UniRoma2 - ISW/SSW 4

> Definizione di ciclo di vita

> • Def. IEEE Std 610-12 (Software Eng.  Terminology)

> – intervallo di tempo che intercorre tra l’istante in

> cui nasce l’esigenza di costruire un prodotto  software e l’istante in cui il prodotto viene  dismesso – include le fasi di definizione dei requisiti,

> specifica, pianificazione, progetto preliminare,  progetto dettagliato, codifica, integrazione,  testing, uso, manutenzione e dismissione – Nota: tali fasi possono sovrapporsi o essere

> eseguite in modo iterativo

#### Page 4
> UniRoma2 - ISW/SSW 5

> Modelli di ciclo di vita • Il modello del ciclo di vita del software specifica  la serie di fasi attraverso cui il prodotto software  progredisce e l'ordine con cui vanno eseguite,  dalla definizione dei requisiti alla dismissione • La scelta del modello dipende dalla natura  dell'applicazione, dalla maturità  dell’organizzazione, da metodi e tecnologie usate  e da eventuali vincoli dettati dal cliente • L'assenza di un modello del ciclo di vita  corrisponde ad una modalità di sviluppo detta  "build & fix" (o "fix-it-later"), in cui il prodotto  software viene sviluppato e successivamente  rilavorato fino a soddisfare le necessità del cliente

#### Page 5
> UniRoma2 - ISW/SSW 6

> Build&Fix

#### Page 6
> UniRoma2 - ISW/SSW 7

> Modello Waterfall

#### Page 7
> UniRoma2 - ISW/SSW 8

> Verification & Validation (V&V) nel Waterfall

#### Page 8
> UniRoma2 - ISW/SSW 9

> Rapid Prototyping

> Model

#### Page 9
> UniRoma2 - ISW/SSW 10

> Software Prototyping

> Rapid software development to

> elicit or validate requirements

#### Page 10
> UniRoma2 - ISW/SSW 11

> Uses of system prototypes

> • The principal use is to help customers and

> developers understand the software requirements

> – Requirements elicitation: users can experiment with a

> prototype to see how the system supports their work

> – Requirements validation: the prototype can reveal

> errors and omissions in the requirements

> • Prototyping can be considered as a risk reduction

> activity which reduces requirements risks

#### Page 11
> UniRoma2 - ISW/SSW 12

> Prototyping benefits

> • Misunderstandings between software users and

> developers are exposed

> • Missing services may be detected and confusing

> services may be identified

> • A working system is available early in the process

> • The prototype may serve as a basis for deriving a

> software specification

> • The prototype can support user training and

> product testing

#### Page 12
> UniRoma2 - ISW/SSW 13

> Prototyping process

#### Page 13
> UniRoma2 - ISW/SSW 14

> Prototypes as specifications

> • Some parts of the requirements (e.g. safety-

> critical functions) may be impossible to prototype

> and so do not appear in the specification

> • An implementation has no legal standing as a

> contract

> • Non-functional requirements cannot be

> adequately tested in a software prototype

#### Page 14
> UniRoma2 - ISW/SSW 15

> Throw-away prototyping

> • A prototype which is usually a practical implementation of  the product is produced to help discover requirements  problems and then discarded. The product is then  developed using some other development process

> • Used to reduce requirements risk

> • The prototype is developed from an initial requirement,  delivered for experiment then discarded

> • The throw-away prototype should NOT be considered as a  final product

> – Some characteristics may have been left out

> – There is no specification for long-term maintenance

> – The product will be poorly structured and difficult to maintain

#### Page 15
> UniRoma2 - ISW/SSW 16

> Throw-away prototyping process

#### Page 16
> UniRoma2 - ISW/SSW 17

> Throw-away prototype delivery

> • Developers may be pressurised to deliver a

> throw-away prototype as a final product

> • This is not recommended

> – It may be impossible to tune the prototype to meet non-

> functional requirements

> – The prototype is inevitably undocumented

> – The structure will be degraded through changes made

> during development

> – Normal organisational quality standards may not have

> been applied

#### Page 17
> UniRoma2 - ISW/SSW 18

> Prototyping key points

> • A prototype can be used to give end-users a concrete  impression of the product’s capabilities

> • Prototyping is becoming increasingly used for product  development where rapid development is essential

> • Throw-away prototyping is used to understand the product  requirements

> • Rapid development of prototypes is essential. This may  require leaving out functionality or relaxing non-functional  constraints

> • Visual programming is an inherent part of most prototype  development methods

#### Page 18
> UniRoma2 - ISW/SSW 19

> Visual programming

> • Scripting languages such as Visual Basic support

> visual programming where the prototype is

> developed by creating a user interface from

> standard items and associating components with

> these items

> • A large library of components exists to support

> this type of development

> • These may be tailored to suit the specific

> application requirements

#### Page 19
> UniRoma2 - ISW/SSW 20

> Visual programming (2)

#### Page 20
> UniRoma2 - ISW/SSW 21

> Problems with visual development

> • Difficult to coordinate team-based

> development

> • No explicit software architecture

> • Complex dependencies between parts of

> the program can cause maintainability

> problems

## 2. Secondary Evidence (BM25 Lexical + Concepts)

*No secondary evidence found.*

## 3. Visual Assets Candidates

- **asset_id**: a8a67443-1225-4b3a-9a52-31f5b76faace
  source: slides-02-process-1
  page: 0
  type: embedded_image
  path: `d234c4c9_p0_i0.png`

- **asset_id**: 147cdd2d-5ec8-4980-a1ba-57b5d8b11f46
  source: slides-02-process-1
  page: 0
  type: embedded_image
  path: `d234c4c9_p0_i1.png`

- **asset_id**: 7b3c4705-bd09-43ca-9050-3626aeac9be8
  source: slides-02-process-1
  page: 0
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 40f730dc-d4df-4aa9-90c7-9f2f327b5305
  source: slides-02-process-1
  page: 1
  type: embedded_image
  path: `d234c4c9_p1_i0.png`

- **asset_id**: edda521b-c9af-43f5-8d36-5a0ffa3a043a
  source: slides-02-process-1
  page: 1
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: ee24eb37-f97c-4933-8cda-8c8a09dc5af8
  source: slides-02-process-1
  page: 2
  type: embedded_image
  path: `d234c4c9_p2_i0.png`

- **asset_id**: e9dac647-efba-4a3c-a9c7-1a6aa736ea67
  source: slides-02-process-1
  page: 2
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 771dc522-afca-4bd2-8096-f5983e885a7f
  source: slides-02-process-1
  page: 3
  type: embedded_image
  path: `d234c4c9_p3_i0.png`

- **asset_id**: 9abdc679-9362-44e5-aa1e-5f0ceb2504c9
  source: slides-02-process-1
  page: 3
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 34bcd459-ed9a-473b-bca2-b6b61a369ae0
  source: slides-02-process-1
  page: 4
  type: embedded_image
  path: `d234c4c9_p4_i0.png`

- **asset_id**: 68c24d5e-9dcb-410e-992f-1c085e5f4744
  source: slides-02-process-1
  page: 4
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: c3aa4797-da22-4642-a180-1941448bc730
  source: slides-02-process-1
  page: 5
  type: embedded_image
  path: `d234c4c9_p5_i0.png`

- **asset_id**: 9a658522-193e-4458-84fd-9c30843ca262
  source: slides-02-process-1
  page: 5
  type: embedded_image
  path: `d234c4c9_p5_i1.jpeg`

- **asset_id**: 197bfa35-f069-4713-95ec-2c0e64a536ea
  source: slides-02-process-1
  page: 5
  type: embedded_image
  path: `d234c4c9_p5_i2.png`

- **asset_id**: 64e3c639-a3a1-49cb-bb4e-7ffc4c87c935
  source: slides-02-process-1
  page: 5
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 45d33581-cd11-405e-8611-3ba0e7c5c7f3
  source: slides-02-process-1
  page: 6
  type: embedded_image
  path: `d234c4c9_p6_i0.png`

- **asset_id**: 3799c78e-82dd-447c-870e-ebc016b77d42
  source: slides-02-process-1
  page: 6
  type: embedded_image
  path: `d234c4c9_p6_i1.png`

- **asset_id**: 64f0679a-cd5f-4299-a507-7fa20c2be3a9
  source: slides-02-process-1
  page: 6
  type: embedded_image
  path: `d234c4c9_p6_i2.png`

- **asset_id**: 9584b860-c340-454b-b77f-7a55b9b2f796
  source: slides-02-process-1
  page: 6
  type: embedded_image
  path: `d234c4c9_p6_i3.png`

- **asset_id**: a094c284-e860-48ea-964d-99463db620f1
  source: slides-02-process-1
  page: 6
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 5bca4451-731c-441d-bdc9-968e714636e5
  source: slides-02-process-1
  page: 7
  type: embedded_image
  path: `d234c4c9_p7_i0.png`

- **asset_id**: 1e2901da-435c-4397-b5fa-384661817739
  source: slides-02-process-1
  page: 7
  type: embedded_image
  path: `d234c4c9_p7_i1.png`

- **asset_id**: dde629c8-e799-45da-a995-cd6d780f2a87
  source: slides-02-process-1
  page: 7
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b8c22712-0992-44c6-8f3b-10083bc4043c
  source: slides-02-process-1
  page: 8
  type: embedded_image
  path: `d234c4c9_p8_i0.png`

- **asset_id**: c1ed17ae-7e52-4cf6-86d5-c78df94cb8d6
  source: slides-02-process-1
  page: 8
  type: embedded_image
  path: `d234c4c9_p8_i1.png`

- **asset_id**: ff95ccc0-0586-46af-ae17-cfaa00619715
  source: slides-02-process-1
  page: 8
  type: embedded_image
  path: `d234c4c9_p8_i2.png`

- **asset_id**: 9d20aba1-1d24-42a7-9acb-dfcb3cb4fa24
  source: slides-02-process-1
  page: 8
  type: embedded_image
  path: `d234c4c9_p8_i3.png`

- **asset_id**: 7772999b-a569-4c19-a2e1-1aeba72c9c00
  source: slides-02-process-1
  page: 8
  type: embedded_image
  path: `d234c4c9_p8_i4.png`

- **asset_id**: 56dee4db-353e-4a22-a9cc-dda156926cc2
  source: slides-02-process-1
  page: 8
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: dcc11333-4e3f-40ef-a7cf-bdb3394ee219
  source: slides-02-process-1
  page: 9
  type: embedded_image
  path: `d234c4c9_p9_i0.png`

- **asset_id**: ada5a658-aa46-4cf6-8d81-011e13d52cb4
  source: slides-02-process-1
  page: 9
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 0a08ef0d-57a7-4a1f-aeae-03bbd0305b38
  source: slides-02-process-1
  page: 10
  type: embedded_image
  path: `d234c4c9_p10_i0.png`

- **asset_id**: 67e0dc46-2631-4521-9b64-40d52b9075c5
  source: slides-02-process-1
  page: 10
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: ae09a569-f0f8-4997-bc6c-6f58123831e4
  source: slides-02-process-1
  page: 11
  type: embedded_image
  path: `d234c4c9_p11_i0.png`

- **asset_id**: c42c9883-3c85-46e9-95e9-41e00cae46db
  source: slides-02-process-1
  page: 11
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 0a93e8d2-3329-4fc5-a3c3-010a299e3261
  source: slides-02-process-1
  page: 12
  type: embedded_image
  path: `d234c4c9_p12_i0.png`

- **asset_id**: b6f6fe09-e1eb-401a-a9a5-eca174abb213
  source: slides-02-process-1
  page: 12
  type: embedded_image
  path: `d234c4c9_p12_i1.png`

- **asset_id**: 42aa5431-126b-4bf1-a781-d2f5d44acbf7
  source: slides-02-process-1
  page: 12
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 499748bc-bf1c-42b0-9eac-794bda790dab
  source: slides-02-process-1
  page: 13
  type: embedded_image
  path: `d234c4c9_p13_i0.png`

- **asset_id**: 19790a48-12bf-485a-9dc8-adfaeae0aeb0
  source: slides-02-process-1
  page: 13
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 8e2e032f-8a54-484a-b29d-2bf7a3db6fca
  source: slides-02-process-1
  page: 14
  type: embedded_image
  path: `d234c4c9_p14_i0.png`

- **asset_id**: c4548f85-ed58-4cb5-bd1d-d1481bff7508
  source: slides-02-process-1
  page: 14
  type: embedded_image
  path: `d234c4c9_p14_i1.png`

- **asset_id**: d333ae61-efef-47e7-909f-b3c4dd390d7a
  source: slides-02-process-1
  page: 14
  type: embedded_image
  path: `d234c4c9_p14_i2.png`

- **asset_id**: a9cd350f-2fab-4d23-a0dc-2606b13ca85b
  source: slides-02-process-1
  page: 14
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: cb33e99e-f82d-4de4-99c9-a6219242f117
  source: slides-02-process-1
  page: 15
  type: embedded_image
  path: `d234c4c9_p15_i0.png`

- **asset_id**: 23aa0abe-5da9-4a95-b52d-d58552d2e933
  source: slides-02-process-1
  page: 15
  type: embedded_image
  path: `d234c4c9_p15_i1.png`

- **asset_id**: cce1f1c4-1322-4d64-9793-be1a5e14d79d
  source: slides-02-process-1
  page: 15
  type: embedded_image
  path: `d234c4c9_p15_i2.png`

- **asset_id**: d4bc6fd1-831b-49d0-a70f-db6c61c725fa
  source: slides-02-process-1
  page: 15
  type: embedded_image
  path: `d234c4c9_p15_i3.png`

- **asset_id**: 7e28cae9-f5db-4731-8222-539631341474
  source: slides-02-process-1
  page: 15
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 5ad94e70-40ff-4386-befe-ad0df0446f6c
  source: slides-02-process-1
  page: 16
  type: embedded_image
  path: `d234c4c9_p16_i0.png`

- **asset_id**: 6098411d-1715-47c4-aef2-98b587b0769c
  source: slides-02-process-1
  page: 16
  type: embedded_image
  path: `d234c4c9_p16_i1.png`

- **asset_id**: 53b1e4a1-dad9-4ead-a55e-7d019ac9409b
  source: slides-02-process-1
  page: 16
  type: embedded_image
  path: `d234c4c9_p16_i2.png`

- **asset_id**: d6dd9b6c-81f7-4b05-a596-252eeb60a8d9
  source: slides-02-process-1
  page: 16
  type: embedded_image
  path: `d234c4c9_p16_i3.png`

- **asset_id**: 8026f2fe-3d6d-4948-afee-0f5acc3bb7bd
  source: slides-02-process-1
  page: 16
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 2fa2a51d-6dbb-4728-9d23-98d194cd69f7
  source: slides-02-process-1
  page: 17
  type: embedded_image
  path: `d234c4c9_p17_i0.png`

- **asset_id**: 790ad1b1-050c-4c13-a900-c9ce7703877a
  source: slides-02-process-1
  page: 17
  type: embedded_image
  path: `d234c4c9_p17_i1.png`

- **asset_id**: 00c2b7fb-52c9-4f40-949a-bf4bcc3f454b
  source: slides-02-process-1
  page: 17
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: da8a38f1-0ab1-479b-937d-a4b249bb3ddf
  source: slides-02-process-1
  page: 18
  type: embedded_image
  path: `d234c4c9_p18_i0.png`

- **asset_id**: 4c8ba63c-4808-4312-934f-853f96c8fa29
  source: slides-02-process-1
  page: 18
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 53807abd-7e07-48df-b5c6-9faced739ff5
  source: slides-02-process-1
  page: 19
  type: embedded_image
  path: `d234c4c9_p19_i0.png`

- **asset_id**: c980b10e-d651-42e0-b561-f742bb76932c
  source: slides-02-process-1
  page: 19
  type: embedded_image
  path: `d234c4c9_p19_i1.png`

- **asset_id**: 7e942908-b317-464f-98bd-43626239a41c
  source: slides-02-process-1
  page: 19
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 15ee9e75-02e7-43ff-a551-1254626ab353
  source: slides-02-process-1
  page: 20
  type: embedded_image
  path: `d234c4c9_p20_i0.png`

- **asset_id**: c65e3756-6b27-4cdf-aee2-436a3d51b4c9
  source: slides-02-process-1
  page: 20
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

