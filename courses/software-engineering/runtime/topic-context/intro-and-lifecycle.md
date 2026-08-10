# Topic Context

**topic_id**: intro-and-lifecycle
**title**: Fondamenti e Ciclo di Vita

## Retrieval Metadata
- Primary fragments: 111
- Secondary fragments: 0
- Visual assets candidate: 53
- Estimated context tokens: ~1406

## 1. Primary Evidence (Official Coverage)

### Source: slides-01-intro (`official-slides\I parte ISW - SistSW\01-Introduzione.pdf`)
#### Page 0
> UniRoma2 - ISW/SSW 1

> Ingegneria del Software (A.A. 2025/2026)

> • Docente:

> Prof. Andrea D’Ambrogio

> • Obiettivi:

> – fornire i metodi e le tecnologie per inquadrare la produzione del software all'interno di

> una disciplina ingegneristica

> – presentare il processo software e le più moderne tecniche di produzione

> • Esami:

> – 2 appelli a fine di ogni semestre

> – 2 appelli a settembre

> • Testo consigliato:

> – I. Sommerville, Software Engineering, Addison-Wesley (anche in italiano)

> • Materiale didattico: distribuito su piattaforma MS Teams

#### Page 1
> UniRoma2 - ISW/SSW 2

> SwEng: Unconsummated Marriage

> • Software Engineering

> – disciplina per la produzione del software secondo i

> principi dell’ingegneria (progettazione e validazione) – essenziale per fare del sw un prodotto industriale

> • Se manca si incorre in – scarsa qualità del prodotto – scarsa competitività

> • cost overrun • time overrun

#### Page 2
> UniRoma2 - ISW/SSW 3

> SwEng: Unconsummated Marriage

> • Sw Eng disciplina giovane …..

> – per anni i costruttori di Hw hanno visto la produzione di

> sw come attività banale, simile a USO del calcolatore,  che richiede principalmente abilità – per anni l’abilità programmativa, la conoscenza delle

> ultime novità su linguaggi, interfacce etc., è stata  considerata sufficiente a fare un ingegnere del sw – per anni la Sw Eng è stata considerata una branca

> della teoria della programmazione (o informatica  teorica)

#### Page 3
> UniRoma2 - ISW/SSW 4

> SwEng: Unconsummated Marriage

> • Matrimonio non consumato……

> – quello tra la teoria della programmazione e i principi

> dell’ingegneria (progettazione e validazione)  (D.L.Parnas, CACM, Sept. 1997)

> • Cose da far sposare – ingegneri conoscano bene la teoria della

> programmazione  – informatici teorici conoscano bene i principi

> dell’ingegneria

#### Page 4
> UniRoma2 - ISW/SSW 5

> SwEng: Unconsummated Marriage

> • Esempio: ingegneria chimica

> – matrimonio tra chimica e ingegneria (termodinamica,

> meccanica, dinamica fluidi etc.) – nessuno considera più l’ingegneria chimica come

> branca della chimica

> • SwEng, termine coniato oltre 50 anni fa – conferenza NATO, Garmisch, Germania 1968

> – per testimoniare l'esigenza che il software fosse

> inquadrato all'interno di una disciplina ingegneristica.

#### Page 5
> UniRoma2 - ISW/SSW 6

> SwEng: Unconsummated Marriage

> • Risultati del ’68

> – l’attività della programmazione non è né una scienza né

> una matematica. Ciò perché il programmatore non  aggiunge conoscenza a conoscenza, bensì costruisce  un PRODOTTO – gli ingegneri devono basare sulla teoria della

> programmazione i loro principi di progettazione e  convalida dei prodotti software – i problemi e i rischi connessi alla produzione e all’uso

> del software (bassa qualità, time e cost overrun) sono  tipici dei prodotti costruiti da persone NON  QUALIFICATE o, meglio, EDUCATE PER ALTRE  PROFESSIONI

#### Page 6
> UniRoma2 - ISW/SSW 7

> Aspetti tipici dell’Ingegneria del Sw

> (1)

> • ACCIDENTALI del prodotto sw (superabili col progresso della  tecnologia)

> • di attitudine • di manutenzione • di specifica e progetto • di teaming

#### Page 7
> UniRoma2 - ISW/SSW 8

> Ciclo di vita del Sw = 3 Stadi, 6 Fasi

> • Produzione Sw = sviluppo + manutenzione • Sviluppo (stadio1) = 6 fasi

> 1. Requisiti  2. Specifiche (o analisi dei requisiti) 3. Pianificazione 4. Progetto (preliminare e dettagliato) 5. Codifica  6. Integrazione • Manutenzione (stadio2)

> – copre circa il 60% dei costi del ciclo di vita • Dismissione (stadio3)

#### Page 8
> UniRoma2 - ISW/SSW 9

> L'effetto delle modifiche

> • L'effetto delle modifiche varia secondo la fase in cui  vengono introdotte. • In fasi avanzate, una modifica può comportare rivolgimenti  che richiedono nuove risorse o correzioni importanti al  progetto, cioè costi supplementari

#### Page 9
> UniRoma2 - ISW/SSW 10

> Dov’è il Testing?

> • Non esplicitamente menzionato tra le 6 fasi

> • Non è una fase separata

> • E’ un’attività che ha luogo durante l’intero sviluppo

> • In due modi:

> – Verifica (alla fine di ogni fase)

> – Validazione (alla fine dello sviluppo)

> • Verifica = la fase è stata ben svolta? (are we  building the product right?)

> • Validazione = il prodotto finale è buono? (are we  building the right product?)

#### Page 10
> Defect Removal Efficiency (DRE)

> • Fa riferimento alla percentuale di difetti trovati prima

> del rilascio del prodotto software

> • Se il team di sviluppo trova 900 difetti prima del

> rilascio e gli utenti trovano 100 difetti in un intervallo

> temporale standard a partire dalla data di rilascio

> (tipicamente 90 giorni) allora il valore di DRE è pari al

> 90%

> • In base a statistiche aggiornate al 2016, il DRE medio

> negli Stati Uniti è pari al 92% (i valori cambiano in

> base al modello di ciclo di vita)

> UniRoma2 - ISW/SSW 11

#### Page 11
> UniRoma2 - ISW/SSW 12

> Aspetti tipici dell’Ingegneria del Sw

> (2)

> • ESSENZIALI del prodotto sw (non superabili col progresso  dei mezzi e conoscenze)

> • complessità • conformità • cambiabilità • invisibilità

#### Page 12
> UniRoma2 - ISW/SSW 13

> Aspetti tipici dell’Ingegneria del Sw

> (3)

> DI COSTO del prodotto sw

> • costo verso dimensione (size) • costo verso repliche • costo verso ampiezza di mercato

#### Page 13
> UniRoma2 - ISW/SSW 14

> Aspetti di Costo

> • Costo proporzionale al quadrato del size (C=aS2)

> – fare due prodotti di size S/2 costa meno che farne uno

> di size S

> • Produrre una replica non costa niente

> • Vendere un prodotto di size doppio per il mercato

> – richiede un prezzo 4 volte superiore a parità di

> (ampiezza di) mercato

> – richiede un mercato (di ampiezza) 4 volte maggiore a

> parità di prezzo

#### Page 14
> UniRoma2 - ISW/SSW 15

> Definizioni (1)

> • Prodotto Sw (o brevemente Sw) =  = Codice + Documentazione • Artefatto= prodotto Sw intermedio – documento requisiti – documento di specifica  – documento di progetto • Codice = prodotto Sw finale • Sistema Sw = insieme organizzato di prodotti Sw

## 2. Secondary Evidence (BM25 Lexical + Concepts)

*No secondary evidence found.*

## 3. Visual Assets Candidates

- **asset_id**: f5ebfdab-cd06-44be-b358-de747dd5d196
  source: slides-01-intro
  page: 0
  type: embedded_image
  path: `5928463e_p0_i0.png`

- **asset_id**: 16e65e97-2035-4a19-a507-520094cbdb70
  source: slides-01-intro
  page: 0
  type: embedded_image
  path: `5928463e_p0_i1.png`

- **asset_id**: 365b1066-1e50-4466-9d42-17389cf672de
  source: slides-01-intro
  page: 0
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 87bf317c-2d79-4a8a-8aac-7a536a4e48d2
  source: slides-01-intro
  page: 1
  type: embedded_image
  path: `5928463e_p1_i0.png`

- **asset_id**: 6b4ab93c-805e-4e49-9e59-529cc5307e45
  source: slides-01-intro
  page: 1
  type: embedded_image
  path: `5928463e_p1_i1.png`

- **asset_id**: aa768b51-9271-4009-9209-7b2d8828dff7
  source: slides-01-intro
  page: 1
  type: embedded_image
  path: `5928463e_p1_i2.png`

- **asset_id**: af3fb414-2ff4-4535-853f-b57836c7ff25
  source: slides-01-intro
  page: 1
  type: embedded_image
  path: `5928463e_p1_i3.png`

- **asset_id**: cc1be3bc-1003-4b2a-9288-91abfb315dee
  source: slides-01-intro
  page: 1
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b8546f4b-c658-40f8-8f63-6ce8ebf42508
  source: slides-01-intro
  page: 2
  type: embedded_image
  path: `5928463e_p2_i0.png`

- **asset_id**: 3f7814d9-e831-40de-bf44-081101e4c84c
  source: slides-01-intro
  page: 2
  type: embedded_image
  path: `5928463e_p2_i1.png`

- **asset_id**: a03f8bc7-ac47-4bea-beb3-8a210983fc8e
  source: slides-01-intro
  page: 2
  type: embedded_image
  path: `5928463e_p2_i2.png`

- **asset_id**: c69f3ff9-482d-4917-b416-a3a5bd38dbf3
  source: slides-01-intro
  page: 2
  type: embedded_image
  path: `5928463e_p2_i3.png`

- **asset_id**: da87b487-2ad0-4086-bf61-3234be044e84
  source: slides-01-intro
  page: 2
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: ca8135f4-2c8a-413b-86d3-b286db477e86
  source: slides-01-intro
  page: 3
  type: embedded_image
  path: `5928463e_p3_i0.png`

- **asset_id**: 546fcb50-e51e-41ee-8327-e3d9dd908488
  source: slides-01-intro
  page: 3
  type: embedded_image
  path: `5928463e_p3_i1.png`

- **asset_id**: fa8171ba-9bce-4904-8524-a362d9d15a66
  source: slides-01-intro
  page: 3
  type: embedded_image
  path: `5928463e_p3_i2.png`

- **asset_id**: 510945c6-da9d-4e0d-9500-0a63cf52bf47
  source: slides-01-intro
  page: 3
  type: embedded_image
  path: `5928463e_p3_i3.png`

- **asset_id**: 31864430-5388-485b-b8ca-cff35c3b0a77
  source: slides-01-intro
  page: 3
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: cec3bdac-cb06-4cf7-ba2a-c55de5d386bb
  source: slides-01-intro
  page: 4
  type: embedded_image
  path: `5928463e_p4_i0.png`

- **asset_id**: a0731c35-7c28-4c9c-9335-89a6e2eea302
  source: slides-01-intro
  page: 4
  type: embedded_image
  path: `5928463e_p4_i1.png`

- **asset_id**: 9bb32cc4-1de3-4122-abfb-369c5658f3af
  source: slides-01-intro
  page: 4
  type: embedded_image
  path: `5928463e_p4_i2.png`

- **asset_id**: 8cf68c62-24b6-4499-b575-7d28a6a8a171
  source: slides-01-intro
  page: 4
  type: embedded_image
  path: `5928463e_p4_i3.png`

- **asset_id**: d46d9411-5739-46f4-9b66-581a64fe587a
  source: slides-01-intro
  page: 4
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 8fddb7b0-121e-41bd-8c19-1d23188b1fdf
  source: slides-01-intro
  page: 5
  type: embedded_image
  path: `5928463e_p5_i0.png`

- **asset_id**: c77290ef-284e-4275-b37a-78cb9477324e
  source: slides-01-intro
  page: 5
  type: embedded_image
  path: `5928463e_p5_i1.png`

- **asset_id**: 138b4438-5e4a-4f84-bf56-eeb468b4ec18
  source: slides-01-intro
  page: 5
  type: embedded_image
  path: `5928463e_p5_i2.png`

- **asset_id**: 0304dbb8-8c42-4f69-9d57-29ed4703aaa6
  source: slides-01-intro
  page: 5
  type: embedded_image
  path: `5928463e_p5_i3.png`

- **asset_id**: 482bdf31-3a62-4b41-ab4e-2af51ad2ec0f
  source: slides-01-intro
  page: 5
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: fec3cc75-b6d1-4a41-9996-8e399433870f
  source: slides-01-intro
  page: 6
  type: embedded_image
  path: `5928463e_p6_i0.png`

- **asset_id**: ec485409-8292-4d24-af44-14b092c5ec42
  source: slides-01-intro
  page: 6
  type: embedded_image
  path: `5928463e_p6_i1.png`

- **asset_id**: 52f7e064-000d-4ce8-8975-736763bef68e
  source: slides-01-intro
  page: 6
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 0d5bb275-2004-4f18-bd64-25d89c386f08
  source: slides-01-intro
  page: 7
  type: embedded_image
  path: `5928463e_p7_i0.png`

- **asset_id**: 773ae43c-4e62-47a6-ac4c-32da445cf7ba
  source: slides-01-intro
  page: 7
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 47719a0a-b98c-4efb-b61c-9853c26c95ea
  source: slides-01-intro
  page: 8
  type: embedded_image
  path: `5928463e_p8_i0.png`

- **asset_id**: e3af1244-63ed-44d6-9ccd-45c03d43ad6c
  source: slides-01-intro
  page: 8
  type: embedded_image
  path: `5928463e_p8_i1.png`

- **asset_id**: 379d5da8-a823-4bd7-a217-1ab8ae1ff985
  source: slides-01-intro
  page: 8
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: dd2d42a0-ff72-450a-a3c1-264f37608307
  source: slides-01-intro
  page: 9
  type: embedded_image
  path: `5928463e_p9_i0.png`

- **asset_id**: 4ba91581-f758-4563-94d3-9986128e8f73
  source: slides-01-intro
  page: 9
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 1478053b-6151-4df3-b6e2-246d40fe98f4
  source: slides-01-intro
  page: 10
  type: embedded_image
  path: `5928463e_p10_i0.png`

- **asset_id**: e70e5bb4-9acc-4f98-9f03-2fb6d221b53d
  source: slides-01-intro
  page: 10
  type: embedded_image
  path: `5928463e_p10_i1.png`

- **asset_id**: d29816f4-3d94-4f2c-9a06-d5a93b5cf421
  source: slides-01-intro
  page: 10
  type: embedded_image
  path: `5928463e_p10_i2.png`

- **asset_id**: 5a52b819-4394-47ee-a142-ba4ab60b4b9c
  source: slides-01-intro
  page: 10
  type: embedded_image
  path: `5928463e_p10_i3.png`

- **asset_id**: 5987ced7-2180-4f73-b0ed-44dc9d25c9cc
  source: slides-01-intro
  page: 10
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 4943d049-8713-4ac8-8cc7-3c4cfbdf7ff2
  source: slides-01-intro
  page: 11
  type: embedded_image
  path: `5928463e_p11_i0.png`

- **asset_id**: d9cb4b5f-ced2-4715-acd5-5500217a7b3b
  source: slides-01-intro
  page: 11
  type: embedded_image
  path: `5928463e_p11_i1.png`

- **asset_id**: 7d9c504e-8971-4936-9cd7-80529a1df41a
  source: slides-01-intro
  page: 11
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 430ad1dc-c32c-436e-be7b-ac257ebd5025
  source: slides-01-intro
  page: 12
  type: embedded_image
  path: `5928463e_p12_i0.png`

- **asset_id**: bb088ff4-7f07-49f9-88f4-6a28d0eea433
  source: slides-01-intro
  page: 12
  type: embedded_image
  path: `5928463e_p12_i1.png`

- **asset_id**: 92766911-d2e0-4d74-90b3-94c4e7823e0b
  source: slides-01-intro
  page: 12
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 38a17e88-22b9-4226-8392-3c487f7cbeca
  source: slides-01-intro
  page: 13
  type: embedded_image
  path: `5928463e_p13_i0.png`

- **asset_id**: 31afb572-b934-4efb-8c79-b2fb033e753d
  source: slides-01-intro
  page: 13
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b0b9cf98-4002-4d84-a483-9338fda7eb91
  source: slides-01-intro
  page: 14
  type: embedded_image
  path: `5928463e_p14_i0.png`

- **asset_id**: f04c62c7-aa62-499f-a591-2330c26b42da
  source: slides-01-intro
  page: 14
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

