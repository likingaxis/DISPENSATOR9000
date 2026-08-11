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

- **asset_id**: 85dad3c9-9021-510c-869a-6a1304ffaabb
  source: slides-02-process-1
  page: 0
  type: embedded_image
  path: `d234c4c9_p0_i0.png`

- **asset_id**: c6125b90-7b10-54e6-9a66-dc257e66da29
  source: slides-02-process-1
  page: 0
  type: embedded_image
  path: `d234c4c9_p0_i1.png`

- **asset_id**: 2318ddab-1cb8-558f-b5ef-aa4ffb136ca5
  source: slides-02-process-1
  page: 0
  type: page_render
  path: `d234c4c9_p0_render.png`

- **asset_id**: ba6f558f-7db3-5e92-9ea6-d83db17481c0
  source: slides-02-process-1
  page: 1
  type: embedded_image
  path: `d234c4c9_p1_i0.png`

- **asset_id**: 7704bd99-5fd7-5b10-a712-daa7c0d7736b
  source: slides-02-process-1
  page: 1
  type: page_render
  path: `d234c4c9_p1_render.png`

- **asset_id**: d808bc37-18a4-59f3-99f3-76b7f3e97d13
  source: slides-02-process-1
  page: 2
  type: embedded_image
  path: `d234c4c9_p2_i0.png`

- **asset_id**: 79cdf2a9-f386-50dd-8959-ab00c32ed3cb
  source: slides-02-process-1
  page: 2
  type: page_render
  path: `d234c4c9_p2_render.png`

- **asset_id**: c09a8e76-869f-568c-9619-5a4a7a8191c8
  source: slides-02-process-1
  page: 3
  type: embedded_image
  path: `d234c4c9_p3_i0.png`

- **asset_id**: 66dc725e-0020-5120-a6fa-84da177bf55a
  source: slides-02-process-1
  page: 3
  type: page_render
  path: `d234c4c9_p3_render.png`

- **asset_id**: f3857ab8-009a-5a04-a2d3-1cef0d93690d
  source: slides-02-process-1
  page: 4
  type: embedded_image
  path: `d234c4c9_p4_i0.png`

- **asset_id**: fcd2dc00-8bdd-5f5b-8687-55babb691cdc
  source: slides-02-process-1
  page: 4
  type: page_render
  path: `d234c4c9_p4_render.png`

- **asset_id**: e5588461-ac29-50d7-a5a4-b151b5bc9399
  source: slides-02-process-1
  page: 5
  type: embedded_image
  path: `d234c4c9_p5_i0.png`

- **asset_id**: 13c24726-1575-5109-9373-e131b41757b1
  source: slides-02-process-1
  page: 5
  type: embedded_image
  path: `d234c4c9_p5_i1.jpeg`

- **asset_id**: 0ca319f6-7355-5866-a9e0-7898f122bb1b
  source: slides-02-process-1
  page: 5
  type: embedded_image
  path: `d234c4c9_p5_i2.png`

- **asset_id**: 483ff00e-2549-5f8b-b494-7a6978ab7f49
  source: slides-02-process-1
  page: 5
  type: page_render
  path: `d234c4c9_p5_render.png`

- **asset_id**: 9d83bf8d-a0bf-5401-b1e9-5957cb594d2e
  source: slides-02-process-1
  page: 6
  type: embedded_image
  path: `d234c4c9_p6_i0.png`

- **asset_id**: fea5106c-edbf-57fd-a200-f0242c15e1a6
  source: slides-02-process-1
  page: 6
  type: embedded_image
  path: `d234c4c9_p6_i1.png`

- **asset_id**: 99960a99-2ebd-547c-99e6-535bd6b4c47f
  source: slides-02-process-1
  page: 6
  type: embedded_image
  path: `d234c4c9_p6_i2.png`

- **asset_id**: 6da4ff92-bc69-5779-ba5c-d5349c911d67
  source: slides-02-process-1
  page: 6
  type: embedded_image
  path: `d234c4c9_p6_i3.png`

- **asset_id**: 90bca253-b78d-5bd8-ae62-bdaabf521a5f
  source: slides-02-process-1
  page: 6
  type: page_render
  path: `d234c4c9_p6_render.png`

- **asset_id**: 47e0079a-889d-5fef-9fcf-2aef54575986
  source: slides-02-process-1
  page: 7
  type: embedded_image
  path: `d234c4c9_p7_i0.png`

- **asset_id**: 896c4cf9-be88-518b-980b-2fdf9e04d167
  source: slides-02-process-1
  page: 7
  type: embedded_image
  path: `d234c4c9_p7_i1.png`

- **asset_id**: 064a750d-e506-5acf-bd7e-5dfd3c3bbdba
  source: slides-02-process-1
  page: 7
  type: page_render
  path: `d234c4c9_p7_render.png`

- **asset_id**: fc9040b4-5445-5e06-9b7d-6ead972a29e0
  source: slides-02-process-1
  page: 8
  type: embedded_image
  path: `d234c4c9_p8_i0.png`

- **asset_id**: 6f87b306-bfa5-58f6-9943-489be58342ff
  source: slides-02-process-1
  page: 8
  type: embedded_image
  path: `d234c4c9_p8_i1.png`

- **asset_id**: 8ef03137-25b3-5d1f-a0ce-b0eac8cbf14a
  source: slides-02-process-1
  page: 8
  type: embedded_image
  path: `d234c4c9_p8_i2.png`

- **asset_id**: 38469c89-3841-54f0-bb20-ee490769e4f9
  source: slides-02-process-1
  page: 8
  type: embedded_image
  path: `d234c4c9_p8_i3.png`

- **asset_id**: b86eda3a-9f4b-5ce6-8ab0-d02ed3c36c2b
  source: slides-02-process-1
  page: 8
  type: embedded_image
  path: `d234c4c9_p8_i4.png`

- **asset_id**: 388a67c7-267a-5834-93f8-3e73272a0bb4
  source: slides-02-process-1
  page: 8
  type: page_render
  path: `d234c4c9_p8_render.png`

- **asset_id**: 4c06fadc-3b60-5768-b98f-786edd063d69
  source: slides-02-process-1
  page: 9
  type: embedded_image
  path: `d234c4c9_p9_i0.png`

- **asset_id**: fc82540c-a7e9-5f5e-9a8b-52b63d33e704
  source: slides-02-process-1
  page: 9
  type: page_render
  path: `d234c4c9_p9_render.png`

- **asset_id**: 76c17ba3-283e-5108-9bd4-edb624f09c28
  source: slides-02-process-1
  page: 10
  type: embedded_image
  path: `d234c4c9_p10_i0.png`

- **asset_id**: 25fcac33-2d1f-50b0-86fc-192d63e4a075
  source: slides-02-process-1
  page: 10
  type: page_render
  path: `d234c4c9_p10_render.png`

- **asset_id**: 7cc61185-7bed-59cc-99e4-e1e0321e9f79
  source: slides-02-process-1
  page: 11
  type: embedded_image
  path: `d234c4c9_p11_i0.png`

- **asset_id**: b6e9e1ec-55c5-50b5-8a10-429826f888d9
  source: slides-02-process-1
  page: 11
  type: page_render
  path: `d234c4c9_p11_render.png`

- **asset_id**: 9f3a58f7-567f-5675-87c5-1db1d085c092
  source: slides-02-process-1
  page: 12
  type: embedded_image
  path: `d234c4c9_p12_i0.png`

- **asset_id**: 21e9b90d-0ea4-5b2c-8a5b-0e52fe4b1654
  source: slides-02-process-1
  page: 12
  type: embedded_image
  path: `d234c4c9_p12_i1.png`

- **asset_id**: 7f8689e4-bfe9-5026-bf9d-ecd8cb0a047c
  source: slides-02-process-1
  page: 12
  type: page_render
  path: `d234c4c9_p12_render.png`

- **asset_id**: cbf741e0-0c2e-5e3a-9e56-08f9a4bb890b
  source: slides-02-process-1
  page: 13
  type: embedded_image
  path: `d234c4c9_p13_i0.png`

- **asset_id**: cdc17eef-79f8-56b4-890e-365c22491846
  source: slides-02-process-1
  page: 13
  type: page_render
  path: `d234c4c9_p13_render.png`

- **asset_id**: f5e8d1f9-8b50-5f37-8f81-3a0bcc8f1f76
  source: slides-02-process-1
  page: 14
  type: embedded_image
  path: `d234c4c9_p14_i0.png`

- **asset_id**: 305fccfd-9969-5a7b-8c8b-4c3a7ca82024
  source: slides-02-process-1
  page: 14
  type: embedded_image
  path: `d234c4c9_p14_i1.png`

- **asset_id**: dc6b7f50-715e-5385-a232-8244216e7c33
  source: slides-02-process-1
  page: 14
  type: embedded_image
  path: `d234c4c9_p14_i2.png`

- **asset_id**: 8b9f74c5-e9cd-5303-90a0-623cbda04755
  source: slides-02-process-1
  page: 14
  type: page_render
  path: `d234c4c9_p14_render.png`

- **asset_id**: 341a8784-579a-57ea-8a58-80b3d481a3c8
  source: slides-02-process-1
  page: 15
  type: embedded_image
  path: `d234c4c9_p15_i0.png`

- **asset_id**: b66f323e-9982-5440-9bfa-804bcde24c93
  source: slides-02-process-1
  page: 15
  type: embedded_image
  path: `d234c4c9_p15_i1.png`

- **asset_id**: 1badec4c-f2d4-563e-9b09-bfba4b549944
  source: slides-02-process-1
  page: 15
  type: embedded_image
  path: `d234c4c9_p15_i2.png`

- **asset_id**: eb685f02-5d62-51f3-90b5-c58605f672ac
  source: slides-02-process-1
  page: 15
  type: embedded_image
  path: `d234c4c9_p15_i3.png`

- **asset_id**: 69b81c99-5c8c-5609-a39d-bfafba6e487f
  source: slides-02-process-1
  page: 15
  type: page_render
  path: `d234c4c9_p15_render.png`

- **asset_id**: 3ff60619-c123-5953-ab9d-45d14a6bfa9e
  source: slides-02-process-1
  page: 16
  type: embedded_image
  path: `d234c4c9_p16_i0.png`

- **asset_id**: 7277dea6-f69b-542e-a524-eea565717d1c
  source: slides-02-process-1
  page: 16
  type: embedded_image
  path: `d234c4c9_p16_i1.png`

- **asset_id**: 781d9aa4-3b4e-5d5d-ad64-d43e7d6afdda
  source: slides-02-process-1
  page: 16
  type: embedded_image
  path: `d234c4c9_p16_i2.png`

- **asset_id**: 7ec22bb4-016d-55f4-b4c7-8df2e93db672
  source: slides-02-process-1
  page: 16
  type: embedded_image
  path: `d234c4c9_p16_i3.png`

- **asset_id**: b954bf18-37e2-5900-9e65-b1b7d3debbbc
  source: slides-02-process-1
  page: 16
  type: page_render
  path: `d234c4c9_p16_render.png`

- **asset_id**: fd59e534-b505-56d3-822a-4115213ac713
  source: slides-02-process-1
  page: 17
  type: embedded_image
  path: `d234c4c9_p17_i0.png`

- **asset_id**: d010cd57-c305-5ab2-8807-d4f728a865a7
  source: slides-02-process-1
  page: 17
  type: embedded_image
  path: `d234c4c9_p17_i1.png`

- **asset_id**: 53954073-1610-55e8-9810-1a56a9a61b19
  source: slides-02-process-1
  page: 17
  type: page_render
  path: `d234c4c9_p17_render.png`

- **asset_id**: a2639d95-dfe7-5d88-8e26-9bab3cc3e20e
  source: slides-02-process-1
  page: 18
  type: embedded_image
  path: `d234c4c9_p18_i0.png`

- **asset_id**: ff4111c0-4e3a-5de6-9521-9a9b09c1869a
  source: slides-02-process-1
  page: 18
  type: page_render
  path: `d234c4c9_p18_render.png`

- **asset_id**: 1ebb70fc-d64c-5b67-9379-2f25066ee4f7
  source: slides-02-process-1
  page: 19
  type: embedded_image
  path: `d234c4c9_p19_i0.png`

- **asset_id**: 72dbe3ec-6ceb-5be5-9cab-4411c3a10928
  source: slides-02-process-1
  page: 19
  type: embedded_image
  path: `d234c4c9_p19_i1.png`

- **asset_id**: 40f102b1-2880-5922-a4e5-ba212c398fbb
  source: slides-02-process-1
  page: 19
  type: page_render
  path: `d234c4c9_p19_render.png`

- **asset_id**: 58b2e4ca-d7a6-5961-b7d3-d2726f6b4f2a
  source: slides-02-process-1
  page: 20
  type: embedded_image
  path: `d234c4c9_p20_i0.png`

- **asset_id**: 06e0e7a4-4861-58ff-8645-3cbc5ea7e244
  source: slides-02-process-1
  page: 20
  type: page_render
  path: `d234c4c9_p20_render.png`

