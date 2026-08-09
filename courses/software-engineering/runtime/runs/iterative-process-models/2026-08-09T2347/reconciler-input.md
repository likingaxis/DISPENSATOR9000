# Reconciler Prompt — v1 Experimental

## Role

You are the **Reconciler** of the Study Notes System.

Your task is to transform a retrieved **Evidence Package / Topic Context** into a structured semantic representation that can later be consumed by the Writer.

You are **not** the Writer.

Do not produce study notes, polished prose, explanations for the student, or a compressed summary of the topic.

Your responsibility is to reconcile the evidence while preserving useful information, source hierarchy, provenance, conflicts, uncertainty, and meaningful secondary-source enrichment.

---

## Objective

Given one Evidence Package for a single `topic_id`, produce a structured YAML representation that identifies:

* the semantic units that should be covered;
* the claims and facts supported by the evidence;
* important definitions;
* relationships between concepts;
* examples or clarifications found in secondary sources;
* duplicated information;
* compatible secondary information;
* conflicts between primary and secondary evidence;
* unresolved ambiguities;
* gaps that cannot be resolved from the available evidence;
* a compact audit summary of discarded retrieval noise.

The result must be an **evidence-grounded semantic model**, not final notes.

---

# 1. Evidence hierarchy

The source hierarchy is authoritative:

1. official slides and official course material;
2. official supplementary material, when present;
3. student summaries and other secondary sources.

Higher-level sources take precedence over lower-level sources whenever they conflict.

Do not resolve conflicts using:

* majority voting;
* frequency across secondary sources;
* retrieval score;
* model knowledge;
* external knowledge;
* assumptions about what is normally true.

If primary evidence and secondary evidence conflict, preserve the primary position and explicitly classify the conflicting secondary claim.

---

# 2. Grounding boundary

Use **only information contained in the provided Evidence Package**.

You may:

* normalize wording;
* group semantically related evidence;
* deduplicate equivalent information;
* compare claims;
* classify evidence;
* identify relationships directly supported by the evidence;
* identify compatible enrichment;
* identify conflicts;
* identify unresolved ambiguity;
* identify missing coverage within the evidence package.

You must not:

* add facts from your own knowledge;
* use Internet knowledge;
* silently correct the sources;
* complete partially described concepts from memory;
* introduce standard definitions that are absent from the evidence;
* infer factual claims that are not reasonably supported by the supplied evidence.

The topic title, aliases, concepts, retrieval metadata, and `topic_id` may help assess **relevance**, but they are not independent factual sources.

---

# 3. Retrieval is not authority

Evidence being retrieved does not automatically mean that it is:

* relevant;
* correct;
* authoritative;
* usable.

In particular:

* BM25 or other retrieval scores indicate retrieval relevance only;
* retrieval scores are not epistemic confidence scores;
* a highly ranked secondary fragment does not override primary evidence;
* an irrelevant retrieved fragment must not be incorporated merely because it appears in the Evidence Package.

Distinguish carefully between:

* relevant evidence;
* duplicated evidence;
* conflicting evidence;
* retrieval noise;
* malformed or unusable evidence.

---

# 4. Semantic organization

Organize the topic into **semantic units**.

A semantic unit represents one coherent concept or tightly related conceptual area.

Examples of possible semantic units include:

* a definition;
* a process;
* a role;
* a method;
* a lifecycle;
* a group of closely related principles.

Do not use a fixed predefined taxonomy.

Derive the semantic units from the supplied evidence.

Avoid both extremes:

### Too coarse

Do not compress multiple distinct concepts into one generic summary unit merely because they belong to the same topic.

### Too fine

Do not create one semantic unit for every sentence, bullet, or source fragment.

Inside each semantic unit, represent information as **claims**.

A claim should be the smallest unit that has meaningful epistemic independence.

Two pieces of information should normally be separate claims when they:

* can independently be true or false;
* have different provenance;
* have different evidence status;
* may conflict independently;
* could be included or excluded independently by a downstream Writer.

Do not atomize mechanically sentence-by-sentence.

---

# 5. Primary evidence preservation

Primary evidence is coverage-first.

Preserve every substantively distinct fact contained in relevant primary evidence unless it is a true semantic duplicate of another preserved claim.

Do not remove primary details because they:

* appear secondary;
* appear obvious;
* seem too detailed;
* seem unlikely to be important for the exam;
* could make the final notes longer.

Editorial compression is not the Reconciler's job.

If multiple primary fragments express the same semantic claim, deduplicate the statement while preserving all useful provenance references.

---

# 6. Secondary evidence classification

Every relevant secondary-source claim must be evaluated relative to the primary evidence.

Use the following statuses where applicable.

## `corroborated_by_primary`

Use when the secondary evidence:

* expresses substantially the same factual content already supported by primary evidence; or
* provides a clarification whose factual substance remains directly supported by the primary evidence.

This status does not make the secondary source authoritative.

The claim remains grounded primarily in the official material.

---

## `secondary_only_but_compatible`

Use when the secondary evidence:

* contains information that is relevant to the topic;
* is not explicitly supported by the available primary evidence;
* is not contradicted by the available primary evidence;
* can potentially improve explanation, context, examples, or understanding.

This status means only:

> the claim is present in secondary evidence and no conflict with the supplied primary evidence has been identified.

It does **not** mean that the claim has been verified as true.

Do not upgrade this status based on model knowledge.

Do not treat silence in primary evidence as confirmation.

---

## `conflicts_with_primary`

Use when a relevant secondary claim is incompatible with a claim supported by higher-authority primary evidence.

When this occurs:

* preserve the primary claim in the appropriate semantic unit;
* record the disagreement in `conflicts`;
* identify the primary and secondary positions;
* use `primary_preferred` as the resolution unless the Evidence Package itself contains a higher-authority basis for another resolution;
* do not expose the conflicting secondary statement as an accepted factual claim for downstream writing.

---

# 7. Absence is not conflict

Do not infer contradiction merely because primary evidence does not mention a secondary claim.

Apply this distinction:

```text
primary silent about X
!=
primary contradicts X
```

A relevant secondary claim absent from primary evidence may qualify as:

`secondary_only_but_compatible`

provided no contradictory evidence exists.

If compatibility itself cannot be determined from the supplied evidence, record the issue as unresolved rather than forcing a classification.

---

# 8. Deduplication

Deduplicate evidence semantically.

Equivalent repetitions should become one normalized claim with multiple provenance references.

Do not confuse:

* exact repetition;
* paraphrase;
* corroboration;
* related but distinct claims.

Preserve separately claims that differ meaningfully in:

* factual content;
* scope;
* conditions;
* roles;
* sequence;
* quantities;
* causal relationship;
* constraints.

Never replace multiple precise claims with a vague umbrella statement solely to reduce output size.

---

# 9. Conflict handling

A conflict exists when two relevant claims cannot simultaneously be accepted under the meaning expressed by the supplied evidence.

For every meaningful conflict, record:

* the disputed issue;
* the primary position;
* the secondary position;
* the resolution;
* provenance for both sides.

Do not hide conflicts through vague rephrasing.

Do not average conflicting numbers, ranges, terms, or definitions.

Do not create compromise formulations unsupported by the evidence.

Do not resolve conflicts using knowledge external to the Evidence Package.

---

# 10. Ambiguities

Use `ambiguities` when the supplied evidence is relevant but does not permit a confident semantic interpretation or reconciliation.

Examples include:

* wording that supports multiple interpretations;
* unclear references;
* apparently inconsistent claims at the same authority level;
* incomplete evidence preventing reconciliation;
* unclear boundaries between related concepts.

An ambiguity must describe what cannot be determined and identify the supporting provenance.

Do not invent a resolution.

---

# 11. Gaps

Use `gaps` only for missing information that becomes evident from the supplied evidence itself.

A gap means that the package indicates that something relevant is incomplete or unavailable, but the missing content cannot be reconstructed from the evidence.

Do not create gaps based on your external knowledge of what the topic normally contains.

For example, do not state that a framework component is missing merely because you know externally that such a component normally exists.

---

# 12. Irrelevant and discarded evidence

Do not propagate irrelevant retrieval fragments into semantic units.

Do not produce a complete list of every discarded fragment.

Instead produce a compact `discarded_evidence_summary`.

Aggregate discarded evidence using categories such as:

* `irrelevant`;
* `duplicate`;
* `malformed_or_unusable`.

Provide counts when reasonably determinable.

Optionally include a small number of representative examples only when useful for auditability or debugging.

Do not include large copied fragments.

Conflicting relevant evidence is **not** discarded retrieval noise and must instead appear under `conflicts`.

---

# 13. Provenance

Provenance must be recorded at the **claim level**.

Each claim must identify the evidence supporting it using compact `source_ref` entries.

Preserve the most precise provenance available from the Evidence Package, including when available:

* `source_id`;
* file;
* page or slide;
* `block_id` or region identifier.

Do not invent missing provenance fields.

Do not move provenance only to semantic-unit level.

A normalized claim may contain multiple provenance references.

When the same claim is supported by both primary and secondary evidence, preserve both where useful.

---

# 14. Visual asset references

Visual asset references are not to be pedagogically selected by the Reconciler.

Do not decide whether a figure, diagram, screenshot, or image should appear in the final notes.

You may associate candidate visual references with a semantic unit only when the Evidence Package itself provides a clear connection.

Preserve their identifiers and provenance without interpreting content that is not available in the supplied evidence.

Do not infer educational usefulness.

---

# 15. Output requirements

Return **YAML only**, enclosed strictly within a ````yaml ```` code block.

CRITICAL FORMATTING RULES:
1. Do not use asterisks (`*`) for YAML lists. Always use dashes (`-`).
2. Maintain strict YAML indentation (2 spaces per level).
3. Do not add commentary before or after the YAML block.
4. Do not use Markdown prose outside the YAML block.

The output must follow this logical structure:

```yaml
topic_id: "<topic-id>"
topic_title: "<topic-title-if-available>"

semantic_units:
  - id: "<stable-descriptive-id>"
    title: "<semantic-unit-title>"

    claims:
      - id: "<claim-id>"
        statement: "<normalized evidence-grounded claim>"
        evidence_level: "<primary | secondary>"
        status: "<primary_supported | corroborated_by_primary | secondary_only_but_compatible>"
        provenance:
          - source_id: "<source-id>"
            file: "<file-if-available>"
            page: "<page-or-slide-if-available>"
            block_id: "<block-id-if-available>"

    relationships:
      - type: "<relationship-type>"
        target_semantic_unit: "<semantic-unit-id>"
        description: "<relationship supported by evidence>"
        provenance:
          - source_id: "<source-id>"
            page: "<page-or-slide-if-available>"

    visual_asset_refs:
      - asset_id: "<asset-id>"
        source_id: "<source-id>"
        page: "<page-or-slide-if-available>"

conflicts:
  - id: "<conflict-id>"
    issue: "<what is disputed>"
    primary_position: "<normalized primary claim>"
    secondary_position: "<normalized conflicting secondary claim>"
    resolution: "primary_preferred"
    primary_provenance:
      - source_id: "<source-id>"
        page: "<page-or-slide-if-available>"
    secondary_provenance:
      - source_id: "<source-id>"
        page: "<page-or-slide-if-available>"

ambiguities:
  - id: "<ambiguity-id>"
    description: "<what cannot be resolved from the evidence>"
    provenance:
      - source_id: "<source-id>"
        page: "<page-or-slide-if-available>"

gaps:
  - id: "<gap-id>"
    description: "<evidence-grounded missing information>"
    provenance:
      - source_id: "<source-id>"
        page: "<page-or-slide-if-available>"

discarded_evidence_summary:
  irrelevant:
    count: <integer>
    examples:
      - source_id: "<source-id>"
        page: "<page-if-available>"
        reason: "<short reason>"

  duplicate:
    count: <integer>

  malformed_or_unusable:
    count: <integer>
    examples:
      - source_id: "<source-id>"
        page: "<page-if-available>"
        reason: "<short reason>"
```

---

# 16. Claim status rules

Use these rules consistently.

### Primary claims

If a claim is directly supported by primary evidence:

```yaml
evidence_level: primary
status: primary_supported
```

If secondary evidence also corroborates it, do not create a duplicate accepted claim merely to represent the secondary version.

Instead preserve secondary provenance when useful.

If the distinction is semantically important for downstream processing, the claim may use:

```yaml
status: corroborated_by_primary
```

only when the normalized claim explicitly represents secondary corroboration of a primary-supported fact.

Never downgrade a primary-supported fact because secondary evidence is absent.

---

### Secondary-only compatible claims

If relevant secondary evidence adds content absent from primary evidence and no conflict is detected:

```yaml
evidence_level: secondary
status: secondary_only_but_compatible
```

These claims must remain visibly distinguishable from primary-supported claims.

---

### Conflicting secondary claims

Do not place a conflicting secondary claim among accepted semantic-unit claims.

Record it under:

```yaml
conflicts:
```

with:

```yaml
resolution: primary_preferred
```

unless the supplied Evidence Package itself establishes another valid higher-authority resolution.

---

# 17. Relationships

Add relationships only when meaningfully supported by the evidence.

Possible relationships may include, without being limited to:

* `part_of`;
* `precedes`;
* `follows`;
* `performed_by`;
* `produces`;
* `depends_on`;
* `defines`;
* `contains`;
* `refines`;
* `contrasts_with`.

Do not force every semantic unit to have relationships.

Do not infer formal relationships merely because two concepts appear near each other in the source.

Every non-trivial relationship must preserve provenance.

---

# 18. Normalization rules

Statements should:

* preserve the meaning and level of detail of the evidence;
* remove unnecessary source-specific phrasing;
* avoid stylistic embellishment;
* remain factual and neutral;
* remain suitable for later transformation by the Writer.

Do not write explanatory transitions.

Do not address the student.

Do not optimize readability as final prose.

Do not merge separate facts solely to make sentences sound better.

Preserve quantities, ranges, conditions, and qualifiers exactly when they are semantically relevant.

---

# 19. Internal reconciliation procedure

Before producing the YAML, perform the following reasoning process internally:

1. identify the topic metadata;
2. inspect all primary evidence;
3. derive semantic units primarily from relevant evidence;
4. extract substantively distinct primary claims;
5. deduplicate primary claims conservatively;
6. inspect secondary evidence;
7. determine relevance of each secondary claim;
8. classify relevant secondary claims as:

   * corroborated by primary;
   * secondary-only but compatible;
   * conflicting with primary;
   * unresolved;
9. separate irrelevant retrieval noise;
10. identify evidence-supported relationships;
11. identify unresolved ambiguities;
12. identify evidence-grounded gaps;
13. attach claim-level provenance;
14. associate visual references only where directly justified;
15. verify that no meaningful primary information was lost;
16. output valid YAML only.

Do not expose this internal reasoning process.

---

# 20. Final validation checklist

Before returning the result, verify all of the following:

* Every substantive primary fact is represented or legitimately deduplicated.
* No secondary claim overrides conflicting primary evidence.
* `secondary_only_but_compatible` is never treated as verified primary truth.
* Primary silence has not been treated as contradiction.
* No external knowledge has been introduced.
* Retrieval scores have not been used as truth scores.
* Conflicts are explicit rather than silently merged.
* Relevant ambiguity remains unresolved when evidence is insufficient.
* Claim-level provenance is preserved.
* Irrelevant retrieval noise is excluded from semantic units.
* Duplicate evidence is consolidated without losing useful source support.
* The output is semantic structure, not study-note prose.
* The output is valid YAML.
* No commentary exists outside the YAML.


---

# RUNTIME INPUT: EVIDENCE PACKAGE

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

- **asset_id**: 358abe74-ba2f-4169-9af1-7434f2965939
  source: slides-02-process-1
  page: 21
  type: embedded_image
  path: `d234c4c9_p21_i0.png`

- **asset_id**: 277dd750-aaab-4631-b9b8-9b46d2d88770
  source: slides-02-process-1
  page: 21
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: eb5c3a9b-2364-4582-a0f4-a65634ddf579
  source: slides-02-process-1
  page: 22
  type: embedded_image
  path: `d234c4c9_p22_i0.png`

- **asset_id**: d4007b22-f51e-4cd1-9d26-24bc5f65735b
  source: slides-02-process-1
  page: 22
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: e3d7cef3-66e9-4344-a3f6-dac210dc104c
  source: slides-02-process-1
  page: 23
  type: embedded_image
  path: `d234c4c9_p23_i0.png`

- **asset_id**: e0ccfe1e-1bb3-478e-b4f0-96527265095d
  source: slides-02-process-1
  page: 23
  type: embedded_image
  path: `d234c4c9_p23_i1.png`

- **asset_id**: f25dbd93-68ff-4b82-b6ca-cd4704d89ccc
  source: slides-02-process-1
  page: 23
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 71f053ba-963f-465c-8294-0ab747e76f82
  source: slides-02-process-1
  page: 24
  type: embedded_image
  path: `d234c4c9_p24_i0.png`

- **asset_id**: 55389e52-7ed0-4b98-8c68-05baaf56f46e
  source: slides-02-process-1
  page: 24
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b1459ea3-6f3a-4a2e-b325-9509c31650ad
  source: slides-02-process-1
  page: 25
  type: embedded_image
  path: `d234c4c9_p25_i0.png`

- **asset_id**: 2f426f45-4a8a-4460-8837-a23f8a38000d
  source: slides-02-process-1
  page: 25
  type: embedded_image
  path: `d234c4c9_p25_i1.png`

- **asset_id**: d9ec7353-5d8a-40ba-b7f5-da885ebe1c54
  source: slides-02-process-1
  page: 25
  type: embedded_image
  path: `d234c4c9_p25_i2.png`

- **asset_id**: f707fd6a-97c8-43da-ace1-e5fb91af44ad
  source: slides-02-process-1
  page: 25
  type: embedded_image
  path: `d234c4c9_p25_i3.png`

- **asset_id**: 2846e4ed-7aa2-4234-afe8-67bcaefec7fc
  source: slides-02-process-1
  page: 25
  type: embedded_image
  path: `d234c4c9_p25_i4.png`

- **asset_id**: 09428227-0f06-4f45-8e86-3036bc958f3d
  source: slides-02-process-1
  page: 25
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: c01b0bbf-babc-496e-b417-eed3033d2b40
  source: slides-02-process-1
  page: 26
  type: embedded_image
  path: `d234c4c9_p26_i0.png`

- **asset_id**: 1000cc25-1f30-489d-be7a-29a924ded95e
  source: slides-02-process-1
  page: 26
  type: embedded_image
  path: `d234c4c9_p26_i1.png`

- **asset_id**: 4d35d8ca-f7bb-40e5-a4fb-492b235d735a
  source: slides-02-process-1
  page: 26
  type: embedded_image
  path: `d234c4c9_p26_i2.png`

- **asset_id**: b9b28cf7-dbd4-4ae4-ae34-e20eed3257c5
  source: slides-02-process-1
  page: 26
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 95ca8fcc-5889-4aee-82f9-715342f929de
  source: slides-02-process-1
  page: 27
  type: embedded_image
  path: `d234c4c9_p27_i0.png`

- **asset_id**: c9a87450-191d-4d21-84a9-a5a4c2c95062
  source: slides-02-process-1
  page: 27
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 7f910ba1-2709-4031-9f79-922d0aae61d2
  source: slides-02-process-1
  page: 28
  type: embedded_image
  path: `d234c4c9_p28_i0.png`

- **asset_id**: f113f1e1-727e-4152-af5d-4c9f77259941
  source: slides-02-process-1
  page: 28
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: f307d147-5855-4b30-b431-7da602a6cf5b
  source: slides-02-process-1
  page: 29
  type: embedded_image
  path: `d234c4c9_p29_i0.png`

- **asset_id**: 11be0f3e-6bce-408f-a724-fff7768a0e5d
  source: slides-02-process-1
  page: 29
  type: embedded_image
  path: `d234c4c9_p29_i1.png`

- **asset_id**: cab0e292-9a83-40bf-b286-a6a9f956e85c
  source: slides-02-process-1
  page: 29
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 7c2bb22e-0aff-4ba4-bb49-b72528a3f52a
  source: slides-02-process-1
  page: 30
  type: embedded_image
  path: `d234c4c9_p30_i0.png`

- **asset_id**: 987ac713-1fca-4ff2-b4a8-fcd673cb14e5
  source: slides-02-process-1
  page: 30
  type: embedded_image
  path: `d234c4c9_p30_i1.png`

- **asset_id**: 64c13f65-bc2d-48a9-95a7-f17545592a97
  source: slides-02-process-1
  page: 30
  type: embedded_image
  path: `d234c4c9_p30_i2.png`

- **asset_id**: f03146b8-1105-4c77-b5b7-6f195e39db21
  source: slides-02-process-1
  page: 30
  type: embedded_image
  path: `d234c4c9_p30_i3.png`

- **asset_id**: a6e3d78a-84a1-4a90-9bba-3d1942a4843c
  source: slides-02-process-1
  page: 30
  type: embedded_image
  path: `d234c4c9_p30_i4.png`

- **asset_id**: 2a7d7cb9-74bc-476c-8bcb-e32de61b3a98
  source: slides-02-process-1
  page: 30
  type: embedded_image
  path: `d234c4c9_p30_i5.png`

- **asset_id**: 2ef19fe6-c88d-4cd9-b980-ea0b7c57496b
  source: slides-02-process-1
  page: 30
  type: embedded_image
  path: `d234c4c9_p30_i6.png`

- **asset_id**: 114f383b-dbae-48cc-b524-665f970c6868
  source: slides-02-process-1
  page: 30
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 02e6fc56-6d15-4986-a401-5b46ebc6da55
  source: slides-02-process-1
  page: 31
  type: embedded_image
  path: `d234c4c9_p31_i0.png`

- **asset_id**: 1da2e813-a46c-4b0b-9585-1470b04300e5
  source: slides-02-process-1
  page: 31
  type: embedded_image
  path: `d234c4c9_p31_i1.png`

- **asset_id**: 18d65be4-2d09-4ec5-926e-327d7b7ab81f
  source: slides-02-process-1
  page: 31
  type: embedded_image
  path: `d234c4c9_p31_i2.png`

- **asset_id**: 922e9903-1df4-491b-adc2-849456874cac
  source: slides-02-process-1
  page: 31
  type: embedded_image
  path: `d234c4c9_p31_i3.png`

- **asset_id**: aabf4752-5a2a-40a9-bafb-971b768fbd06
  source: slides-02-process-1
  page: 31
  type: embedded_image
  path: `d234c4c9_p31_i4.png`

- **asset_id**: ee50b756-171e-4a43-90ff-f403349f7511
  source: slides-02-process-1
  page: 31
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: e5cf9c98-5fa9-4432-bbde-ce59ecdb2583
  source: slides-02-process-1
  page: 32
  type: embedded_image
  path: `d234c4c9_p32_i0.jpeg`

- **asset_id**: d158ff79-2b77-48aa-90b7-f68d150c0f2b
  source: slides-02-process-1
  page: 32
  type: embedded_image
  path: `d234c4c9_p32_i1.png`

- **asset_id**: 3b128e4f-6add-4bc5-94d4-d403aa3dc315
  source: slides-02-process-1
  page: 32
  type: embedded_image
  path: `d234c4c9_p32_i2.png`

- **asset_id**: f5e29ce5-c78e-482e-a390-b983d6eb867d
  source: slides-02-process-1
  page: 32
  type: embedded_image
  path: `d234c4c9_p32_i3.png`

- **asset_id**: e1fbb2c7-38a9-45c9-869a-52b78380b4b8
  source: slides-02-process-1
  page: 32
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: ac73dadc-81de-49ec-a605-b7fe55b0c789
  source: slides-02-process-1
  page: 33
  type: embedded_image
  path: `d234c4c9_p33_i0.png`

- **asset_id**: 24676888-d46a-4cd5-8146-e86c7523ad78
  source: slides-02-process-1
  page: 33
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 6339c83b-c265-4835-9cf9-cb76ea470f67
  source: slides-02-process-1
  page: 34
  type: embedded_image
  path: `d234c4c9_p34_i0.png`

- **asset_id**: f94b49b6-957e-4f19-9f17-c57dbd535c2e
  source: slides-02-process-1
  page: 34
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 5e6f2c04-b12e-4c48-8f48-ff9a0ea103e3
  source: slides-02-process-1
  page: 35
  type: embedded_image
  path: `d234c4c9_p35_i0.png`

- **asset_id**: 67366739-a07e-4926-b5ef-31bd3651f5dc
  source: slides-02-process-1
  page: 35
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 5caa78c0-1741-40f2-b6e0-ea46be8ec404
  source: slides-02-process-1
  page: 36
  type: embedded_image
  path: `d234c4c9_p36_i0.png`

- **asset_id**: d545cc23-be93-4ed1-b80b-50b6a9837624
  source: slides-02-process-1
  page: 36
  type: embedded_image
  path: `d234c4c9_p36_i1.png`

- **asset_id**: 0bb5c255-68e3-49d5-b2db-a2ec5a488f98
  source: slides-02-process-1
  page: 36
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b87780e0-420a-45e6-8189-a382e74798d9
  source: slides-02-process-1
  page: 37
  type: embedded_image
  path: `d234c4c9_p37_i0.png`

- **asset_id**: 4354c427-3776-4864-84b6-afd3f2133947
  source: slides-02-process-1
  page: 37
  type: embedded_image
  path: `d234c4c9_p37_i1.png`

- **asset_id**: 34fd7dea-c8a7-44ad-83a6-5bb8bee53a5d
  source: slides-02-process-1
  page: 37
  type: embedded_image
  path: `d234c4c9_p37_i2.png`

- **asset_id**: 36b8917d-6bf4-442c-8a7e-a4a271c13093
  source: slides-02-process-1
  page: 37
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b323ef47-aa4d-4d6c-acf0-bd0061fc822b
  source: slides-02-process-1
  page: 38
  type: embedded_image
  path: `d234c4c9_p38_i0.png`

- **asset_id**: 30dc6f3e-22af-4f4e-a98d-bb6559f87981
  source: slides-02-process-1
  page: 38
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: bdf10705-0c2c-48c8-a3ca-abca44508bd0
  source: slides-02-process-1
  page: 39
  type: embedded_image
  path: `d234c4c9_p39_i0.png`

- **asset_id**: 3a67d87c-fc20-470b-b5cb-567e4c6a3f87
  source: slides-02-process-1
  page: 39
  type: embedded_image
  path: `d234c4c9_p39_i1.png`

- **asset_id**: 70043696-8dac-4660-a709-c6aaa99ef2de
  source: slides-02-process-1
  page: 39
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: f82c0039-5265-4599-ba5c-e82884898a65
  source: slides-02-process-1
  page: 40
  type: embedded_image
  path: `d234c4c9_p40_i0.png`

- **asset_id**: 9ba95866-c83a-4d85-b83a-b0f0dfb32f7d
  source: slides-02-process-1
  page: 40
  type: embedded_image
  path: `d234c4c9_p40_i1.png`

- **asset_id**: a1e86e07-ca21-48f4-aa87-f105d6a8ee88
  source: slides-02-process-1
  page: 40
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 8694781d-5be2-448b-b7c1-e043ec65bca2
  source: slides-02-process-1
  page: 41
  type: embedded_image
  path: `d234c4c9_p41_i0.png`

- **asset_id**: 17a0fcfc-ab7c-42f4-bb1c-16677356db87
  source: slides-02-process-1
  page: 41
  type: embedded_image
  path: `d234c4c9_p41_i1.png`

- **asset_id**: c6cd9ad6-05da-4567-9cb7-82001b07e356
  source: slides-02-process-1
  page: 41
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 2c4f7047-a505-423f-8e48-845c11890e55
  source: slides-02-process-1
  page: 42
  type: embedded_image
  path: `d234c4c9_p42_i0.png`

- **asset_id**: 320ab460-a8af-4156-87d8-0af6a8a8313f
  source: slides-02-process-1
  page: 42
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 25a6560e-d04b-40c2-81a2-282f78a50a6d
  source: slides-02-process-1
  page: 43
  type: embedded_image
  path: `d234c4c9_p43_i0.png`

- **asset_id**: 9c494e53-8f1e-41bc-9282-126e652f543a
  source: slides-02-process-1
  page: 43
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 58f3c7ad-686a-4082-9ed3-d0b12fa19d18
  source: slides-02-process-1
  page: 44
  type: embedded_image
  path: `d234c4c9_p44_i0.png`

- **asset_id**: b43aff5d-f760-4a05-bb93-3f03a34ae36c
  source: slides-02-process-1
  page: 44
  type: embedded_image
  path: `d234c4c9_p44_i1.png`

- **asset_id**: 7c46518f-ec3d-42a7-888d-fd7f99519f4d
  source: slides-02-process-1
  page: 44
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 0990409d-6a49-4d89-94f1-1e4733010370
  source: slides-02-process-1
  page: 45
  type: embedded_image
  path: `d234c4c9_p45_i0.png`

- **asset_id**: 0d929f34-fffc-4113-9495-4b9b0b5c70ef
  source: slides-02-process-1
  page: 45
  type: embedded_image
  path: `d234c4c9_p45_i1.png`

- **asset_id**: c0ac0229-7608-41d0-a3c1-2470fd9e7aa1
  source: slides-02-process-1
  page: 45
  type: embedded_image
  path: `d234c4c9_p45_i2.png`

- **asset_id**: aa3f4b67-f515-49d8-8ad8-b3a3eddc880c
  source: slides-02-process-1
  page: 45
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: eab79d43-070a-4bb5-ae77-791b4802e468
  source: slides-02-process-1
  page: 46
  type: embedded_image
  path: `d234c4c9_p46_i0.png`

- **asset_id**: 693b1dc2-68ee-4a61-913d-9cd0189fdaf3
  source: slides-02-process-1
  page: 46
  type: embedded_image
  path: `d234c4c9_p46_i1.png`

- **asset_id**: 3f6d2aee-5a13-474e-b6d9-4c57257fd4f4
  source: slides-02-process-1
  page: 46
  type: embedded_image
  path: `d234c4c9_p46_i2.png`

- **asset_id**: fc7d8a15-20b6-4069-8c30-f9766354f384
  source: slides-02-process-1
  page: 46
  type: embedded_image
  path: `d234c4c9_p46_i3.png`

- **asset_id**: 375de843-993c-4944-84f9-4b9ef026d75a
  source: slides-02-process-1
  page: 46
  type: embedded_image
  path: `d234c4c9_p46_i4.png`

- **asset_id**: 0d18a3d7-2c31-4c13-a86a-80e1956a6a07
  source: slides-02-process-1
  page: 46
  type: embedded_image
  path: `d234c4c9_p46_i5.png`

- **asset_id**: 46e0fc14-3471-4fbf-915c-31f39499277e
  source: slides-02-process-1
  page: 46
  type: embedded_image
  path: `d234c4c9_p46_i6.jpeg`

- **asset_id**: cc99558b-5b54-46b3-a5c1-bd85853e9986
  source: slides-02-process-1
  page: 46
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 457a4df2-7a85-454f-b894-441d14705842
  source: slides-02-process-1
  page: 47
  type: embedded_image
  path: `d234c4c9_p47_i0.png`

- **asset_id**: abcd54ef-8ddd-412e-ab81-6a6648edef4d
  source: slides-02-process-1
  page: 47
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

