# Topic Context

**topic_id**: cocomo
**title**: Modello COCOMO

## Retrieval Metadata
- Primary fragments: 39
- Secondary fragments: 10
- Visual assets candidate: 33
- Estimated context tokens: ~1026

## 1. Primary Evidence (Official Coverage)

### Source: slides-07-planning (`official-slides\I parte ISW - SistSW\07-Pianificazione.pdf`)
#### Page 28
> UniRoma2 - ISW/SSW 29

> Es. di modello algoritmico: COCOMO

> • COCOMO (COnstructive COst MOdel) è il modello introdotto da  Boehm (1981) per determinare il valore dell'effort • Il valore ottenuto per l'effort viene successivamente utilizzato per  determinare durata e costi di sviluppo • COCOMO comprende 3 modelli:

> – Basic (per stime iniziali) – Intermediate (usato dopo aver suddiviso il sistema in sottosistemi) – Advanced (usato dopo aver suddiviso in moduli ciascun sottosistema) • La stima dell'effort viene effettuata a partire da:

> – stima delle dimensioni del progetto in KLOC – stima del modo di sviluppo del prodotto, che misura il livello intrinseco

> di difficoltà nello sviluppo, tra:

> • organic (per prodotti di piccole dimensioni) • semidetached (per prodotti di dimensioni intermedie) • embedded (per prodotti complessi) • Nel 1995 è stato introdotto COCOMO II, più flessibile e sofisticato  rispetto alla versione precedente

#### Page 29
> UniRoma2 - ISW/SSW 30

> Esempio d'uso di COCOMO

> • Passo 1 Determinare l'effort nominale usando la formula:

> effort nominale = 3.2 × (KLOC)1.05 MM Esempio:

> 3.2 × (33)1.05 = 126 MM • Passo 2 Ottenere la stima dell'effort applicando un fattore moltiplicativo C basato su 15 cost drivers:

> effort = effort nominale × C Esempio:

> 126 × 1.15 = 145 MM • C (cost driver multiplier) si ottiene come produttoria dei cost driver ci.  Ogni ci determina la complessità del fattore i che influenza il progetto e può assumere uno tra più valori assegnati con variazioni intorno al  valore unitario (valore nominale)

> Modello Intermediate, modo organic

#### Page 30
> UniRoma2 - ISW/SSW 31

> Tabella di cost driver (Intermediate

> COCOMO)

#### Page 31
> Cost drivers ratings

> UniRoma2 - ISW/SSW 32

#### Page 32
> Complexity

> (CPLX)

> ratings

> UniRoma2 - ISW/SSW 33

#### Page 33
> Example cost drivers ratings Microprocessor-based communications processing software

> UniRoma2 - ISW/SSW 34

#### Page 34
> UniRoma2 - ISW/SSW 35

> COCOMO Time Schedule

> • Stima del tempo T alla consegna (product

> delivery):

> – Modo organic T  =  2.5 E 0.38  (months M)

> – Modo semi-detached T  =  2.5  E 0.35

> – Modo embedded T  =  2.5  E 0.32

#### Page 35
> UniRoma2 - ISW/SSW 36

> Development Costs Estimation • Development costs (C) are estimated by  allocating development effort (E) on phases and  staff activities, e.g.:

> – 16% preliminary design

> • 50% project manager • 50% analyst – 62% detailed design, coding and testing

> • 75% programmer/analyst • 25% programmer – 22% Integration

> • 30% analyst • 70% programmer/analyst • The cost per person-month of each staff category  (e.g., project manager, analyst, programmer, etc.)  is then used to obtain development costs

## 2. Secondary Evidence (BM25 Lexical + Concepts)

### Source: theory-summary (`teoria.pdf`)
#### Page 43 (BM25: 23.64)
> calcola partendo da 14 fattori di complessità tecnica. TFC = 0.65 + 0.01 ⋅ ΣFi, dove Fi è il punteggio di ciascun dei 14 fattori Modelli algoritmici empirici Il termine empirico indica che le relazioni matematiche non sono derivate da

#### Page 42 (BM25: 21.76)
> • Tecniche di scomposizione • Modelli algoritmici empirici Tecniche di scomposizione

#### Page 1 (BM25: 16.56)
> ▪Tecniche di scomposizione ▪Modelli algoritmici empirici ◦Metriche di struttura

#### Page 44 (BM25: 8.73)
> Dove C è un fattore moltiplicativo, chiamato cost driver multiplier, ed è basato su 15 cost drivers. Il tempo di consegna si deriva poi dalla formula: T = a ⋅Effortb, dove a e b sono

#### Page 3 (BM25: 8.56)
> integrazione, testing, uso, matunenzione e dimissione. Modelli Il modello del ciclo di vita del software specifica la serie di fasi attraverso cui il

#### Page 3 (BM25: 5.78)
> Modello Build & Fix Il modello Build & Fix è uno dei modelli di sviluppo software più semplici e primitivi, spesso adottato in contesti non professionali o da sviluppatori alle prime armi. In

#### Page 4 (BM25: 5.78)
> Modello a cascata (Waterfall) Il modello a cascata è uno dei più classici e storici modelli di sviluppo del software. È stato uno dei primi ad essere formalizzato e si basa su un approccio sequenzale e

#### Page 7 (BM25: 5.66)
> e ritardi. Modello Microsoft La Microsoft ha dovuto affrontare problemi di:

#### Page 7 (BM25: 5.66)
> • Continuo feedback dei customer durante il processo di sviluppo. Modello Agile Il modello Agile non è un singolo modello di sviluppo, ma un insieme di principi e

#### Page 4 (BM25: 5.17)
> verifica che il prodotto soddisfi effettivamente i bisogni dell'utente finale. Modello a prototipi IL modello di Rapid Prototyping è un approccio allo sviluppo del software che mette

## 3. Visual Assets Candidates

- **asset_id**: edaf58aa-8b49-43c6-ab69-a94a14e8084b
  source: slides-07-planning
  page: 28
  type: embedded_image
  path: `fe4c0322_p28_i0.png`

- **asset_id**: ba4e0bd4-0ad8-4b43-b94d-640be7492c88
  source: slides-07-planning
  page: 28
  type: embedded_image
  path: `fe4c0322_p28_i1.png`

- **asset_id**: 00a00642-9d27-48ab-abe7-4de112a447fa
  source: slides-07-planning
  page: 28
  type: embedded_image
  path: `fe4c0322_p28_i2.png`

- **asset_id**: b213312e-4e2d-4478-a238-9f2ee0153979
  source: slides-07-planning
  page: 28
  type: embedded_image
  path: `fe4c0322_p28_i3.png`

- **asset_id**: 76e354c1-a478-40d9-a0d7-2f4bff71892c
  source: slides-07-planning
  page: 28
  type: embedded_image
  path: `fe4c0322_p28_i4.png`

- **asset_id**: e52005f7-f3e4-4fa1-852f-ba2f57f1e939
  source: slides-07-planning
  page: 28
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: d6f1de7e-86a4-475a-935e-29bb9120c8d6
  source: slides-07-planning
  page: 29
  type: embedded_image
  path: `fe4c0322_p29_i0.png`

- **asset_id**: 541e9ff4-4688-45ae-a433-2970a6f6c1cb
  source: slides-07-planning
  page: 29
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 0d9e17c9-e654-4ab0-b6eb-c6f633399de8
  source: slides-07-planning
  page: 30
  type: embedded_image
  path: `fe4c0322_p30_i0.png`

- **asset_id**: 5a00968d-2006-401a-b8f6-0568cd5e3ce4
  source: slides-07-planning
  page: 30
  type: embedded_image
  path: `fe4c0322_p30_i1.png`

- **asset_id**: c914ff4c-5dc0-46d8-b363-ace678812fce
  source: slides-07-planning
  page: 30
  type: embedded_image
  path: `fe4c0322_p30_i2.png`

- **asset_id**: df1c18b7-4d53-49fa-85e9-8d8a966ee6c5
  source: slides-07-planning
  page: 30
  type: embedded_image
  path: `fe4c0322_p30_i3.png`

- **asset_id**: 509cfb21-d04f-4030-abbd-4e9fe9dafd70
  source: slides-07-planning
  page: 30
  type: embedded_image
  path: `fe4c0322_p30_i4.png`

- **asset_id**: ffdcd0fb-1011-4449-9df1-ae009050fd40
  source: slides-07-planning
  page: 30
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: c009a3df-3f07-4855-a200-0d637ca4c304
  source: slides-07-planning
  page: 31
  type: embedded_image
  path: `fe4c0322_p31_i0.png`

- **asset_id**: c4697743-36b5-4258-a54f-1a7f62cfc119
  source: slides-07-planning
  page: 31
  type: embedded_image
  path: `fe4c0322_p31_i1.jpeg`

- **asset_id**: b5685c48-df2b-4708-be6c-ccf49f914da9
  source: slides-07-planning
  page: 31
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 6e458929-ebe6-4623-8a5a-7098293da06e
  source: slides-07-planning
  page: 32
  type: embedded_image
  path: `fe4c0322_p32_i0.png`

- **asset_id**: 2c5a31e6-61aa-4262-a595-18d0650d6695
  source: slides-07-planning
  page: 32
  type: embedded_image
  path: `fe4c0322_p32_i1.png`

- **asset_id**: a5cc9dde-52c0-43ce-9fd5-5bd3c74e80a5
  source: slides-07-planning
  page: 32
  type: embedded_image
  path: `fe4c0322_p32_i2.png`

- **asset_id**: 2c2ef548-b85c-42b8-8941-4c9c79efbabe
  source: slides-07-planning
  page: 32
  type: embedded_image
  path: `fe4c0322_p32_i3.jpeg`

- **asset_id**: 48a0b963-09a1-4c1b-96d6-e7b08a675074
  source: slides-07-planning
  page: 32
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 03747946-9139-406e-9e26-b65a5745121c
  source: slides-07-planning
  page: 33
  type: embedded_image
  path: `fe4c0322_p33_i0.png`

- **asset_id**: 3438d4db-5525-49ef-9f1a-cce835efdebf
  source: slides-07-planning
  page: 33
  type: embedded_image
  path: `fe4c0322_p33_i1.png`

- **asset_id**: 76a891d8-2b83-4c56-98d1-73249c4d3819
  source: slides-07-planning
  page: 33
  type: embedded_image
  path: `fe4c0322_p33_i2.png`

- **asset_id**: 86652268-e5d3-4197-a94a-a8989ccfb4f9
  source: slides-07-planning
  page: 33
  type: embedded_image
  path: `fe4c0322_p33_i3.png`

- **asset_id**: 73e03979-170b-4e85-ab27-1076565000d2
  source: slides-07-planning
  page: 33
  type: embedded_image
  path: `fe4c0322_p33_i4.png`

- **asset_id**: 5c47666a-314f-48f1-9de9-7893771a71d8
  source: slides-07-planning
  page: 33
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: ef5d7aa9-3075-440d-980d-0e2c64116a52
  source: slides-07-planning
  page: 34
  type: embedded_image
  path: `fe4c0322_p34_i0.png`

- **asset_id**: dc82ae06-1b9f-4731-ae95-0a8f7d33df2a
  source: slides-07-planning
  page: 34
  type: embedded_image
  path: `fe4c0322_p34_i1.png`

- **asset_id**: b4d9a7cf-d0d7-4a20-9b04-008824122173
  source: slides-07-planning
  page: 34
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 6c9ed1ed-0be2-45fd-a554-8ac9243a88ca
  source: slides-07-planning
  page: 35
  type: embedded_image
  path: `fe4c0322_p35_i0.png`

- **asset_id**: c3c44eda-c765-4993-813b-57c6b8416424
  source: slides-07-planning
  page: 35
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

