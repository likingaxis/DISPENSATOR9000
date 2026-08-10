# Topic Context

**topic_id**: reliability-and-defects
**title**: Affidabilità, Guasti ed Errori

## Retrieval Metadata
- Primary fragments: 60
- Secondary fragments: 0
- Visual assets candidate: 25
- Estimated context tokens: ~571

## 1. Primary Evidence (Official Coverage)

### Source: slides-01-intro (`official-slides\I parte ISW - SistSW\01-Introduzione.pdf`)
#### Page 15
> UniRoma2 - ISW/SSW 16

> Definizioni (2)

> • Cliente = soggetto che ordina il prodotto Sw • Sviluppatore = soggetto che lo produce   • Utente = soggetto che lo usa

> • Sw interno = cliente e sviluppatore coincidono • Sw a contratto = cliente e sviluppatore sono  soggetti differenti

#### Page 16
> UniRoma2 - ISW/SSW 17

> Aspetti di Affidabilità

> (Sw Reliability)

> • Informalmente

> –credibilità del prodotto software

> • Formalmente

> –probabilità che il prodotto software lavori

> “correttamente” in un determinato  intervallo temporale

#### Page 17
> UniRoma2 - ISW/SSW 18

> Difetto, Guasto, Errore

> • Difetto (defect) – anomalia presente in un prodotto Sw

> • Guasto (failure)   – comportamento anomalo del prodotto Sw

> dovuto alla presenza di un difetto

> • Errore – azione errata di chi (per ignoranza, distrazione,

> etc) introduce un difetto nel prodotto Sw

#### Page 18
> UniRoma2 - ISW/SSW 19

> Affidabilità Sw

> • Intuitivamente:  –Un prodotto software con molti

> difetti è poco affidabile.    • E’ chiaro che:  –L’affidabilità del prodotto migliora

> via via che si riduce il numero di  difetti

#### Page 19
> UniRoma2 - ISW/SSW 20

> Caratteristiche dell’affidabilità Sw

> (1)

> • Relazione non-semplice tra:

> –affidabilità osservata  –e numero di difetti latenti

> • L’eliminare difetti dalle parti del prodotto  raramente usate

> –Ha piccoli effetti sull’affidabilità osservata.

#### Page 20
> UniRoma2 - ISW/SSW 21

> La regola 10-90

> • Esperimenti condotti su programmi di

> notevoli dimensioni mostrano che:

> –Il 90% del tempo di esecuzione totale è

> speso eseguendo il solo 10% delle

> istruzioni

> • Detto 10% è chiamato :

> –  core (nucleo) del programma

#### Page 21
> UniRoma2 - ISW/SSW 22

> Caratteristiche dell’affidabilità Sw

> (2)

> • Il miglioramento dell’affidabilità per  l’eliminazione di un difetto:

> – dipende dalla localizzazione del difetto

> (ovvero se appartiene o meno al nucleo  del programma)

#### Page 22
> UniRoma2 - ISW/SSW 23

> Caratteristiche dell’affidabilità Sw

> (3)

> • Dunque, l’affidabilità osservata  dipende da:

> –come è usato il prodotto   –in termini tecnici, dal suo profilo

> operativo (operational profile)

#### Page 23
> UniRoma2 - ISW/SSW 24

> Caratteristiche dell’affidabilità Sw

> (4)

> • Dunque, poiché utenti differenti usano il  software secondo profili operativi diversi:

> – I difetti che si manifestano per un utente

> • potrebbero non manifestarsi per l’altro

> • Dunque, l’affidabilità di un prodotto Sw:

> – Dipende dall’utente

## 2. Secondary Evidence (BM25 Lexical + Concepts)

*No secondary evidence found.*

## 3. Visual Assets Candidates

- **asset_id**: d1df730e-f257-4faf-86f5-9e9c8927ec5b
  source: slides-01-intro
  page: 15
  type: embedded_image
  path: `5928463e_p15_i0.png`

- **asset_id**: 3c55e684-a7c9-4c48-bd23-52f7e929d9f5
  source: slides-01-intro
  page: 15
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 04057c93-38d4-4ed2-8e24-d3f4a7bc03cf
  source: slides-01-intro
  page: 16
  type: embedded_image
  path: `5928463e_p16_i0.png`

- **asset_id**: ba23df77-d295-4650-a94a-c0c84bd95764
  source: slides-01-intro
  page: 16
  type: embedded_image
  path: `5928463e_p16_i1.png`

- **asset_id**: 0c026418-a391-41a4-811a-2aa5d49c6bc5
  source: slides-01-intro
  page: 16
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 5aea2f8f-d051-43a8-9a89-9a8f8c77867b
  source: slides-01-intro
  page: 17
  type: embedded_image
  path: `5928463e_p17_i0.png`

- **asset_id**: 9a500b6a-b6a1-4056-927b-166d4900c258
  source: slides-01-intro
  page: 17
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 497027c8-bb5e-4163-a8f1-6e01e3b7608e
  source: slides-01-intro
  page: 18
  type: embedded_image
  path: `5928463e_p18_i0.png`

- **asset_id**: 30c5277e-f257-4d91-a27f-7480193e96aa
  source: slides-01-intro
  page: 18
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 8bc36d4a-5462-4c12-977e-3f5325725a69
  source: slides-01-intro
  page: 19
  type: embedded_image
  path: `5928463e_p19_i0.png`

- **asset_id**: a44eb069-1107-4093-b9c3-16178835a4c1
  source: slides-01-intro
  page: 19
  type: embedded_image
  path: `5928463e_p19_i1.png`

- **asset_id**: b767ac6e-0c33-4409-b24b-3a67423be4cf
  source: slides-01-intro
  page: 19
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 86b6865a-7a5d-4f0b-99e1-8fb3a1b4147c
  source: slides-01-intro
  page: 20
  type: embedded_image
  path: `5928463e_p20_i0.png`

- **asset_id**: 40857c1d-df71-49c6-bb10-140fb8330748
  source: slides-01-intro
  page: 20
  type: embedded_image
  path: `5928463e_p20_i1.png`

- **asset_id**: 15ab7af6-231c-4aef-be1e-6e7d939b27ab
  source: slides-01-intro
  page: 20
  type: embedded_image
  path: `5928463e_p20_i2.png`

- **asset_id**: 0c5eacfa-bce0-4144-8e35-19e5d4b14335
  source: slides-01-intro
  page: 20
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 81b53c4a-bab7-4bd9-ac03-ad49bb94d2e8
  source: slides-01-intro
  page: 21
  type: embedded_image
  path: `5928463e_p21_i0.png`

- **asset_id**: e53d9abd-3bdd-4031-8dc7-369891de7d45
  source: slides-01-intro
  page: 21
  type: embedded_image
  path: `5928463e_p21_i1.png`

- **asset_id**: 596a8491-200f-4001-8a32-792e656baffd
  source: slides-01-intro
  page: 21
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 7be4e768-31de-46a6-9cf5-cb98c300d642
  source: slides-01-intro
  page: 22
  type: embedded_image
  path: `5928463e_p22_i0.png`

- **asset_id**: a9d9fbd4-6056-4fc5-afad-4f4e8d614b49
  source: slides-01-intro
  page: 22
  type: embedded_image
  path: `5928463e_p22_i1.png`

- **asset_id**: cbce8bb5-3a4d-4512-8268-eb972c8c5ed8
  source: slides-01-intro
  page: 22
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 7b01a1c0-e416-4dea-bbc4-af2a442f9865
  source: slides-01-intro
  page: 23
  type: embedded_image
  path: `5928463e_p23_i0.png`

- **asset_id**: f7a2dff4-bb8d-4f20-bd71-69011b6654ab
  source: slides-01-intro
  page: 23
  type: embedded_image
  path: `5928463e_p23_i1.png`

- **asset_id**: a5d5ca7a-aeb7-4d99-b512-890bc5bb2745
  source: slides-01-intro
  page: 23
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

