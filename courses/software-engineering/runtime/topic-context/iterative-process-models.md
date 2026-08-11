# Topic Context

**topic_id**: iterative-process-models
**title**: Sviluppo Iterativo e Modello a Spirale

## Retrieval Metadata
- Primary fragments: 202
- Secondary fragments: 0
- Visual assets candidate: 90
- Estimated context tokens: ~2721

## 1. Primary Evidence (Official Coverage)

### Source: slides-02-process-1 (`official-slides\I parte ISW - SistSW\02-Processo software parte1.pdf`)
#### Page 21
> UniRoma2 - ISW/SSW 22

> Process iteration

> • Requirements ALWAYS evolve in the course of a

> project so process iteration where earlier stages

> are reworked is always part of the process for

> large products

> • Iteration can be applied to any of the generic

> process models

> • Two (related) approaches

> – Incremental development

> – Spiral development

#### Page 22
> UniRoma2 - ISW/SSW 23

> Incremental development

> • The product is developed and delivered in increments  after establishing an overall architecture

> • Requirements and specifications for each increment may  be developed

> • Users may experiment with delivered increments while  others are being developed. Therefore, these serve as a  form of prototype

> • Intended to combine some of the advantages of  prototyping but with a more manageable process and  better structure

#### Page 23
> UniRoma2 - ISW/SSW 24

> Modello incrementale • Il prodotto software viene sviluppato e rilasciato  per incrementi (build) successivi

#### Page 24
> UniRoma2 - ISW/SSW 25

> Modello incrementale (cont.)

> • Include aspetti tipici del modello basato su rapid  prototyping (l’utente può sperimentare l’utilizzo del  prodotto contenente gli incrementi consegnati,  mentre i restanti sono ancora in fase di sviluppo)

> • Si rivela efficace quando il cliente vuole  continuamente verificare i progressi nello sviluppo  del prodotto e quando i requisiti subiscono  modifiche

> • Può essere realizzato in due versioni alternative:

> – versione con overall architecture

> – versione senza overall architecture (più rischiosa)

#### Page 25
> UniRoma2 - ISW/SSW 26

> Versione  con overall  architecture

#### Page 26
> UniRoma2 - ISW/SSW 27

> Versione senza overall architecture

#### Page 27
> UniRoma2 - ISW/SSW 28

> Impatto sui costi del software

> Numero di build

> Costo

> Costodi integrazione

> Costo dei build

> Regione di costo minimo

> Costo totale

#### Page 28
> UniRoma2 - ISW/SSW 29

> Confronto con modello a cascata Modello a cascata Modello incrementale

> • Feedback del cliente solo  una volta terminato lo  sviluppo

> • Continuo feedback da parte  del cliente durante lo  sviluppo • Fasi condotte in rigida  sequenza (l’output di una  costituisce input per la  successiva)

> • Fasi che possono essere  condotte in parallelo

> • Prevede fasi di progetto  dettagliato e codifica  dell’intero prodotto

> • Progetto dettagliato e  codifica vengono effettuate  sul singolo build • Team di sviluppo costituito  da un numero elevato di  persone

> • Differenti team di sviluppo,  ciascuno di piccole  dimensioni

> • Requisiti “congelati” al  termine della fase di  specifica

> • Requisiti suddivisi in classi di  priorità e facilmente  modificabili

#### Page 29
> UniRoma2 - ISW/SSW 30

> Modello a spirale

#### Page 30
> UniRoma2 - ISW/SSW 31

> Modello a spirale semplificato

> (versione

> lineare)

#### Page 31
> UniRoma2 - ISW/SSW 32

> Modello a spirale semplificato

#### Page 32
> UniRoma2 - ISW/SSW 33

> Modello full-spiral [Boehm, 1988]

#### Page 33
> UniRoma2 - ISW/SSW 34

> Risk management

> • Risk management is concerned with identifying  risks and drawing up plans to minimise their effect  on a project

> • A risk is a probability that some adverse  circumstance will occur

> • Categories of risk

> – Project risks affect schedule or resources

> – Product risks affect the quality or performance of the

> software being developed

> – Business risks affect the organisation developing or

> procuring the software

#### Page 34
> UniRoma2 - ISW/SSW 35

> Risks by category

> Risk Risk type Description

> Staff turnover Project Experienced staff will leave the project before it  is finished.

> Management change Project  There will be a change of organisational  management with different priorities.

> Hardware unavailability Project Hardware which is essential for the project will  not be delivered on schedule.

> Requirements change Project and  product

> There will be a larger number of changes to the  requirements than anticipated.

> Specification delays Project and  product

> Specifications of essential interfaces are not  available on schedule

> Size underestimate Project and  product

> The size of the system has been  underestimated.

> CASE tool under-performance Product CASE tools which support the project do not  perform as anticipated

> Technology change Business The underlying technology on which the system  is built is superseded by new technology.

> Product competition Business A competitive product is marketed before the  system is completed.

#### Page 35
> UniRoma2 - ISW/SSW 36

> The risk management process

> • Risk identification

> – Identify project, product and business risks

> • Risk analysis

> – Assess the likelihood and consequences of these risks

> • Risk planning

> – Draw up plans to avoid or minimise the effects of the

> risk

> • Risk monitoring

> – Monitor the risks throughout the project

#### Page 36
> UniRoma2 - ISW/SSW 37

> The risk management process (2)

#### Page 37
> UniRoma2 - ISW/SSW 38

> Risk identification (1)

> Risk types

> • Technology risks

> • People risks

> • Organisational risks

> • Tools risks

> • Requirements risks

> • Estimation risks

#### Page 38
> UniRoma2 - ISW/SSW 39

> Risk identification (2)

> Risk type Possible risks Technology The database used in the system cannot process as many  transactions per second as expected. Software components which should be reused contain defects  which limit their functionality. People It is impossible to recruit staff with the skills required. Key staff are ill and unavailable at critical times. Required training for staff is not available. Organisational The organisation is restructured so that different management are  responsible for the project. Organisational financial problems force reductions in the project  budget. Tools The code generated by CASE tools is inefficient. CASE tools cannot be integrated. Requirements Changes to requirements which require major design rework are  proposed. Customers fail to understand the impact of requirements changes.  Estimation The time required to develop the software is underestimated. The rate of defect repair is underestimated. The size of the software is underestimated.

#### Page 39
> UniRoma2 - ISW/SSW 40

> Risk analysis

> (1)

> • Assess probability and seriousness of each risk

> • Risk probability may be:

> – very low (<10%)

> – low (10-25%)

> – moderate (25-50%)

> – high (50-75%)

> – very high (>75%)

> • Risk effects might be catastrophic, serious,  tolerable or insignificant

#### Page 40
> UniRoma2 - ISW/SSW 41

> Risk analysis (2)

> Risk Probability Effects

> Organisational financial problems force reductions in the project  budget.

> Low Catastrophic

> It is impossible to recruit staff with the skills required for the project. High Catastrophic

> Key staff are ill  at critical times in the project. Moderate Serious

> Software components which should be reused contain defects which  limit their functionality.

> Moderate Serious

> Changes to requirements which require major design rework are  proposed.

> Moderate Serious

> The organisation is restructured so that different management are  responsible for the project.

> High Serious

> The database used in the system cannot process as many  transactions per second as expected.

> Moderate Serious

> The time required to develop the software is underestimated. High Serious

> CASE tools cannot be integrated. High Tolerable

> Customers fail to understand the impact of requirements changes. Moderate Tolerable

> Required training for staff is not available. Moderate Tolerable

> The rate of defect repair is underestimated. Moderate Tolerable

> The size of the software is underestimated. High Tolerable

> The code generated by CASE tools is inefficient. Moderate Insignificant

#### Page 41
> UniRoma2 - ISW/SSW 42

> Risk analysis

> (3)

> • Identify e.g., the top-ten risks by

> considering:

> –all catastrophic risks

> –all serious risks that have more than a

> moderate probability of occurrence

> • Rank such risks by order of importance

#### Page 42
> UniRoma2 - ISW/SSW 43

> Risk planning • Consider each risk and develop a strategy  to manage that risk

> • Avoidance strategies

> – The probability that the risk will arise is reduced

> • Minimisation strategies

> – The impact of the risk on the project or product

> will be reduced

> • Contingency plans

> – If the risk arises, contingency plans are

> strategies to deal with that risk

#### Page 43
> UniRoma2 - ISW/SSW 44

> Risk management strategies

> Risk Strategy

> Organisational  financial problems

> Prepare a briefing document for senior management showing  how the project is making a very important contribution to the  goals of the business.

> Recruitment  problems

> Alert customer of potential difficulties and the possibility of  delays, investigate buying-in components.

> Staff illness Reorganise team so that there is more overlap of work and  people therefore understand each other’s jobs.

> Defective  components

> Replace potentially defective components with bought-in  components of known reliability.

> Requirements  changes

> Derive traceability information to assess requirements change  impact, maximise information hiding in the design.

> Organisational  restructuring

> Prepare a briefing document for senior management showing  how the project is making a very important contribution to the  goals of the business.

> Database  performance

> Investigate the possibility of buying a higher-performance  database.

> Underestimated  development time

> Investigate buying in components, investigate use of a program  generator.

#### Page 44
> UniRoma2 - ISW/SSW 45

> Risk monitoring (1)

> • Assess each identified risks regularly to  decide whether or not it is becoming less or  more probable • To perform assessment look at risk factors (see next slide) • Also assess whether the effects of the risk  have changed (in such case go back to risk  analysis) • Each key risk should be discussed at  management progress meetings

#### Page 45
> UniRoma2 - ISW/SSW 46

> Risk monitoring (2)

> Risk factors

> Risk type Potential indicators

> Technology Late delivery of hardware or support software, many  reported technology problems

> People Poor staff morale, poor relationships amongst team  member, job availability

> Organisational organisational gossip, lack of action by senior  management

> Tools reluctance by team members to use tools,  complaints about CASE tools, demands for higher- powered workstations

> Requirements many requirements change requests, customer  complaints

> Estimation failure to meet agreed schedule, failure to clear  reported defects

#### Page 46
> UniRoma2 - ISW/SSW 47

> Altri modelli

> (1)

> Modello object-oriented

#### Page 47
> UniRoma2 - ISW/SSW 48

> Altri modelli (2)

> • Modello di ingegneria simultanea (o concorrente) – ha come obiettivo la riduzione di tempi e costi di sviluppo,

> mediante un approccio sistematico al progetto integrato e  concorrente di un prodotto software e del processo ad esso  associato. – Le fasi di sviluppo coesistono invece di essere eseguite in

> sequenza. • Modello basato su metodi formali – comprende una serie di attività che conducono alla specifica

> formale matematica del software, al fine di eliminare  ambiguità, incompletezze ed inconsistenze e facilitare la  verifica dei programmi mediante l'applicazione di tecniche  matematiche. – La Cleanroom Software Engineering (1987) ne

> rappresenta un esempio di realizzazione, in cui viene  enfatizzata la possibilità di rilevare i difetti del software in  modo più tempestivo rispetto ai modelli tradizionali

## 2. Secondary Evidence (BM25 Lexical + Concepts)

*No secondary evidence found.*

## 3. Visual Assets Candidates

- **asset_id**: 03dbd5bb-1a00-5a7f-af8f-7d09277b8c6b
  source: slides-02-process-1
  page: 21
  type: embedded_image
  path: `d234c4c9_p21_i0.png`

- **asset_id**: 848a63a8-fadb-5c21-8f54-087cd7a7df39
  source: slides-02-process-1
  page: 21
  type: page_render
  path: `d234c4c9_p21_render.png`

- **asset_id**: 6ab076ba-7a84-5e82-bf96-642b610e1adf
  source: slides-02-process-1
  page: 22
  type: embedded_image
  path: `d234c4c9_p22_i0.png`

- **asset_id**: 2e8594ef-865e-5cd6-b522-6f0397c1b9c7
  source: slides-02-process-1
  page: 22
  type: page_render
  path: `d234c4c9_p22_render.png`

- **asset_id**: 546d6df0-5eb8-5711-80c7-e1268a3d840b
  source: slides-02-process-1
  page: 23
  type: embedded_image
  path: `d234c4c9_p23_i0.png`

- **asset_id**: 9afe862c-16e8-5b4d-90d1-378d35fa4cc6
  source: slides-02-process-1
  page: 23
  type: embedded_image
  path: `d234c4c9_p23_i1.png`

- **asset_id**: 73d36a6e-28ff-5b39-9e35-50aa85075197
  source: slides-02-process-1
  page: 23
  type: page_render
  path: `d234c4c9_p23_render.png`

- **asset_id**: 6bb3544d-b16f-52db-bc7e-94a7d8d3bd05
  source: slides-02-process-1
  page: 24
  type: embedded_image
  path: `d234c4c9_p24_i0.png`

- **asset_id**: c0be8a93-ad6b-57c0-9b71-021ee1ce844d
  source: slides-02-process-1
  page: 24
  type: page_render
  path: `d234c4c9_p24_render.png`

- **asset_id**: 59564930-221a-589e-a8e9-2f8b69878530
  source: slides-02-process-1
  page: 25
  type: embedded_image
  path: `d234c4c9_p25_i0.png`

- **asset_id**: e161a69e-434c-5b8f-8886-487820587566
  source: slides-02-process-1
  page: 25
  type: embedded_image
  path: `d234c4c9_p25_i1.png`

- **asset_id**: 3a4879ea-a68d-56c6-8bb0-380f34648715
  source: slides-02-process-1
  page: 25
  type: embedded_image
  path: `d234c4c9_p25_i2.png`

- **asset_id**: a32ac318-2b62-5b24-bb41-59ab7aa81b91
  source: slides-02-process-1
  page: 25
  type: embedded_image
  path: `d234c4c9_p25_i3.png`

- **asset_id**: e695ee90-e525-5861-a37d-f854832377e7
  source: slides-02-process-1
  page: 25
  type: embedded_image
  path: `d234c4c9_p25_i4.png`

- **asset_id**: 6f41b361-6226-563f-ab6f-b505c0e3e1f9
  source: slides-02-process-1
  page: 25
  type: page_render
  path: `d234c4c9_p25_render.png`

- **asset_id**: 9b07fc87-48c9-5de7-86aa-0078cb5d3731
  source: slides-02-process-1
  page: 26
  type: embedded_image
  path: `d234c4c9_p26_i0.png`

- **asset_id**: cc20e509-e36f-5dec-afae-602e7ea89f17
  source: slides-02-process-1
  page: 26
  type: embedded_image
  path: `d234c4c9_p26_i1.png`

- **asset_id**: 4279c24e-3f86-5080-b99b-eeff4ca44d43
  source: slides-02-process-1
  page: 26
  type: embedded_image
  path: `d234c4c9_p26_i2.png`

- **asset_id**: 16d528a1-a518-50b3-80e3-05471e9f3eaa
  source: slides-02-process-1
  page: 26
  type: page_render
  path: `d234c4c9_p26_render.png`

- **asset_id**: f866fc51-d83a-5b1b-ad5f-361847bb4392
  source: slides-02-process-1
  page: 27
  type: embedded_image
  path: `d234c4c9_p27_i0.png`

- **asset_id**: 2795c45b-f894-5116-a48e-48b494f4398f
  source: slides-02-process-1
  page: 27
  type: page_render
  path: `d234c4c9_p27_render.png`

- **asset_id**: 55dd30c3-4492-5c82-8adb-18f3e5a04938
  source: slides-02-process-1
  page: 28
  type: embedded_image
  path: `d234c4c9_p28_i0.png`

- **asset_id**: c53eca42-e675-52e8-b283-57aae397eba2
  source: slides-02-process-1
  page: 28
  type: page_render
  path: `d234c4c9_p28_render.png`

- **asset_id**: 1afaab89-c517-5e00-9b15-253d2b78e1b8
  source: slides-02-process-1
  page: 29
  type: embedded_image
  path: `d234c4c9_p29_i0.png`

- **asset_id**: add98143-9a91-58c2-81ec-a96115a59d2b
  source: slides-02-process-1
  page: 29
  type: embedded_image
  path: `d234c4c9_p29_i1.png`

- **asset_id**: d93915bb-eec9-5c68-a483-45ba76910012
  source: slides-02-process-1
  page: 29
  type: page_render
  path: `d234c4c9_p29_render.png`

- **asset_id**: b564bacf-6d73-5dab-b1bc-041b3511fc99
  source: slides-02-process-1
  page: 30
  type: embedded_image
  path: `d234c4c9_p30_i0.png`

- **asset_id**: c9325161-fa82-5535-97e3-fdcad041ecd1
  source: slides-02-process-1
  page: 30
  type: embedded_image
  path: `d234c4c9_p30_i1.png`

- **asset_id**: 848cde1c-b5d9-5b73-b994-48b17ead67c6
  source: slides-02-process-1
  page: 30
  type: embedded_image
  path: `d234c4c9_p30_i2.png`

- **asset_id**: b4b889c8-df4f-5c73-9e13-971c92ded765
  source: slides-02-process-1
  page: 30
  type: embedded_image
  path: `d234c4c9_p30_i3.png`

- **asset_id**: 0b26970e-c211-50ae-9139-77f07d7672c9
  source: slides-02-process-1
  page: 30
  type: embedded_image
  path: `d234c4c9_p30_i4.png`

- **asset_id**: 5304fde8-51d5-5734-8900-98ad1fe68659
  source: slides-02-process-1
  page: 30
  type: embedded_image
  path: `d234c4c9_p30_i5.png`

- **asset_id**: 3e01353b-544a-5976-8f4b-106af2e518f5
  source: slides-02-process-1
  page: 30
  type: embedded_image
  path: `d234c4c9_p30_i6.png`

- **asset_id**: d8524c74-12ef-5dd5-9f56-c5913e884347
  source: slides-02-process-1
  page: 30
  type: page_render
  path: `d234c4c9_p30_render.png`

- **asset_id**: c0872a38-79de-5817-8068-22b694e01742
  source: slides-02-process-1
  page: 31
  type: embedded_image
  path: `d234c4c9_p31_i0.png`

- **asset_id**: cc644ff7-93f2-5cbc-a4df-56b914a7c54e
  source: slides-02-process-1
  page: 31
  type: embedded_image
  path: `d234c4c9_p31_i1.png`

- **asset_id**: f4ebe757-032b-5280-81fc-f4974bdd40f9
  source: slides-02-process-1
  page: 31
  type: embedded_image
  path: `d234c4c9_p31_i2.png`

- **asset_id**: bc4e4b92-ef93-547b-92a4-e36abd9c61c1
  source: slides-02-process-1
  page: 31
  type: embedded_image
  path: `d234c4c9_p31_i3.png`

- **asset_id**: 4855e17a-053b-5351-9c89-c4b66177a3c0
  source: slides-02-process-1
  page: 31
  type: embedded_image
  path: `d234c4c9_p31_i4.png`

- **asset_id**: b83980de-e7f1-5e16-b676-534ba5daeb76
  source: slides-02-process-1
  page: 31
  type: page_render
  path: `d234c4c9_p31_render.png`

- **asset_id**: 6640a098-01f4-5716-b5ea-0f6ffa1dd034
  source: slides-02-process-1
  page: 32
  type: embedded_image
  path: `d234c4c9_p32_i0.jpeg`

- **asset_id**: da80da8e-a551-52c6-a614-592ca388b97b
  source: slides-02-process-1
  page: 32
  type: embedded_image
  path: `d234c4c9_p32_i1.png`

- **asset_id**: 39760ce3-53ec-584c-bf46-ba3d9d62e7e4
  source: slides-02-process-1
  page: 32
  type: embedded_image
  path: `d234c4c9_p32_i2.png`

- **asset_id**: 0876accf-206d-5d6b-b979-6a402744530b
  source: slides-02-process-1
  page: 32
  type: embedded_image
  path: `d234c4c9_p32_i3.png`

- **asset_id**: 58695607-713d-5071-b787-2c9c444cbd57
  source: slides-02-process-1
  page: 32
  type: page_render
  path: `d234c4c9_p32_render.png`

- **asset_id**: c42942e1-4768-5235-bb89-be767b10fd4e
  source: slides-02-process-1
  page: 33
  type: embedded_image
  path: `d234c4c9_p33_i0.png`

- **asset_id**: 05dea701-a625-517a-a26a-1b5ed00cbde2
  source: slides-02-process-1
  page: 33
  type: page_render
  path: `d234c4c9_p33_render.png`

- **asset_id**: 95e5f519-abd8-5627-8997-923d9a82ef32
  source: slides-02-process-1
  page: 34
  type: embedded_image
  path: `d234c4c9_p34_i0.png`

- **asset_id**: de4989fa-050f-543a-b949-9e70af81446c
  source: slides-02-process-1
  page: 34
  type: page_render
  path: `d234c4c9_p34_render.png`

- **asset_id**: 6b588240-ad37-5199-a8e3-2b17ace3919d
  source: slides-02-process-1
  page: 35
  type: embedded_image
  path: `d234c4c9_p35_i0.png`

- **asset_id**: f5d4b6ca-8f6d-5111-a5a6-ad3750f84687
  source: slides-02-process-1
  page: 35
  type: page_render
  path: `d234c4c9_p35_render.png`

- **asset_id**: 4e2d40c6-ad16-52a0-9c72-740530b8e981
  source: slides-02-process-1
  page: 36
  type: embedded_image
  path: `d234c4c9_p36_i0.png`

- **asset_id**: b30229aa-6103-50d7-8469-633abb43d2bb
  source: slides-02-process-1
  page: 36
  type: embedded_image
  path: `d234c4c9_p36_i1.png`

- **asset_id**: 785d5ac2-aad5-5600-a644-f52b16225f31
  source: slides-02-process-1
  page: 36
  type: page_render
  path: `d234c4c9_p36_render.png`

- **asset_id**: b300848b-7f89-5647-805e-212343661ee1
  source: slides-02-process-1
  page: 37
  type: embedded_image
  path: `d234c4c9_p37_i0.png`

- **asset_id**: 92019bd4-ef32-5136-bcf3-452b67263af8
  source: slides-02-process-1
  page: 37
  type: embedded_image
  path: `d234c4c9_p37_i1.png`

- **asset_id**: 9f4db3c7-bd86-581b-9bfa-3e39a1d21393
  source: slides-02-process-1
  page: 37
  type: embedded_image
  path: `d234c4c9_p37_i2.png`

- **asset_id**: 43534bf1-0204-59e9-a0a8-bfd1f4649dcb
  source: slides-02-process-1
  page: 37
  type: page_render
  path: `d234c4c9_p37_render.png`

- **asset_id**: b139e36b-718f-5698-b818-bb894455ab8d
  source: slides-02-process-1
  page: 38
  type: embedded_image
  path: `d234c4c9_p38_i0.png`

- **asset_id**: 8a9f0bdc-2ce5-5619-885b-cc871c6b0da0
  source: slides-02-process-1
  page: 38
  type: page_render
  path: `d234c4c9_p38_render.png`

- **asset_id**: e022da0b-309a-554e-a4c5-9ba1ec9f5857
  source: slides-02-process-1
  page: 39
  type: embedded_image
  path: `d234c4c9_p39_i0.png`

- **asset_id**: bc3e7a32-6aae-57dd-883e-3963328c0b57
  source: slides-02-process-1
  page: 39
  type: embedded_image
  path: `d234c4c9_p39_i1.png`

- **asset_id**: 15e73e74-c936-5358-9c8d-4eeb98551a85
  source: slides-02-process-1
  page: 39
  type: page_render
  path: `d234c4c9_p39_render.png`

- **asset_id**: 7d5a197f-5f2a-5b89-8f64-b7a2b66b2d1f
  source: slides-02-process-1
  page: 40
  type: embedded_image
  path: `d234c4c9_p40_i0.png`

- **asset_id**: 2d406881-5b91-52c9-a594-8f180da87958
  source: slides-02-process-1
  page: 40
  type: embedded_image
  path: `d234c4c9_p40_i1.png`

- **asset_id**: fbff785c-06f2-5a4b-aeb2-1fdaa556c582
  source: slides-02-process-1
  page: 40
  type: page_render
  path: `d234c4c9_p40_render.png`

- **asset_id**: 11f0b343-7bbe-514e-8a95-eaa3352df5ba
  source: slides-02-process-1
  page: 41
  type: embedded_image
  path: `d234c4c9_p41_i0.png`

- **asset_id**: e4d498ca-6b36-59af-9f25-eaad4b4c8d6b
  source: slides-02-process-1
  page: 41
  type: embedded_image
  path: `d234c4c9_p41_i1.png`

- **asset_id**: 53e8fb42-9030-5701-aa62-2864e4421c18
  source: slides-02-process-1
  page: 41
  type: page_render
  path: `d234c4c9_p41_render.png`

- **asset_id**: d0b2cf69-427b-5672-9449-49d703ecb739
  source: slides-02-process-1
  page: 42
  type: embedded_image
  path: `d234c4c9_p42_i0.png`

- **asset_id**: 40e631ff-ff0d-50fc-ac7f-a8c807caea94
  source: slides-02-process-1
  page: 42
  type: page_render
  path: `d234c4c9_p42_render.png`

- **asset_id**: cab40df9-1180-5913-a62f-d2fd880978cb
  source: slides-02-process-1
  page: 43
  type: embedded_image
  path: `d234c4c9_p43_i0.png`

- **asset_id**: 6b4074fe-a72b-5a93-9a64-76f5d753f887
  source: slides-02-process-1
  page: 43
  type: page_render
  path: `d234c4c9_p43_render.png`

- **asset_id**: dbad898a-571c-5231-836e-b26d8db3c756
  source: slides-02-process-1
  page: 44
  type: embedded_image
  path: `d234c4c9_p44_i0.png`

- **asset_id**: f59eb228-5821-5560-bbde-865b36322ead
  source: slides-02-process-1
  page: 44
  type: embedded_image
  path: `d234c4c9_p44_i1.png`

- **asset_id**: 851f15ee-6b10-5f9c-9e78-3f159e2abeb8
  source: slides-02-process-1
  page: 44
  type: page_render
  path: `d234c4c9_p44_render.png`

- **asset_id**: 51961680-ce48-5b8f-bb62-2deeb46dd2e6
  source: slides-02-process-1
  page: 45
  type: embedded_image
  path: `d234c4c9_p45_i0.png`

- **asset_id**: d8525ded-1466-5098-836f-abd1aad7c10f
  source: slides-02-process-1
  page: 45
  type: embedded_image
  path: `d234c4c9_p45_i1.png`

- **asset_id**: 2b187db6-b6b5-57a4-add9-81a3ef2eef7a
  source: slides-02-process-1
  page: 45
  type: embedded_image
  path: `d234c4c9_p45_i2.png`

- **asset_id**: c3aa109e-0454-59cf-9c1d-de216274b206
  source: slides-02-process-1
  page: 45
  type: page_render
  path: `d234c4c9_p45_render.png`

- **asset_id**: 3b5d59d2-d873-5b47-ae04-1985258df284
  source: slides-02-process-1
  page: 46
  type: embedded_image
  path: `d234c4c9_p46_i0.png`

- **asset_id**: edeafccc-0eea-51de-8ccb-501099c52cd4
  source: slides-02-process-1
  page: 46
  type: embedded_image
  path: `d234c4c9_p46_i1.png`

- **asset_id**: 74d207f7-7410-5507-bb49-a013698c9579
  source: slides-02-process-1
  page: 46
  type: embedded_image
  path: `d234c4c9_p46_i2.png`

- **asset_id**: dff626f9-2a70-5c71-8a02-e4103462079e
  source: slides-02-process-1
  page: 46
  type: embedded_image
  path: `d234c4c9_p46_i3.png`

- **asset_id**: b6cb510a-93ee-548d-9b12-be1dcd1b61a4
  source: slides-02-process-1
  page: 46
  type: embedded_image
  path: `d234c4c9_p46_i4.png`

- **asset_id**: df2c30ce-51da-54fc-9163-7723581454ef
  source: slides-02-process-1
  page: 46
  type: embedded_image
  path: `d234c4c9_p46_i5.png`

- **asset_id**: 77e1bd7a-bb93-585f-9728-c68c1fea5882
  source: slides-02-process-1
  page: 46
  type: embedded_image
  path: `d234c4c9_p46_i6.jpeg`

- **asset_id**: 219357ff-3bd3-50db-b3ae-e90b8925ed03
  source: slides-02-process-1
  page: 46
  type: page_render
  path: `d234c4c9_p46_render.png`

- **asset_id**: 727a9538-a144-5043-9529-3b69437d445a
  source: slides-02-process-1
  page: 47
  type: embedded_image
  path: `d234c4c9_p47_i0.png`

- **asset_id**: 5e062220-dcb2-5f6a-a7c0-e49ccfbb6d34
  source: slides-02-process-1
  page: 47
  type: page_render
  path: `d234c4c9_p47_render.png`

