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

Visual asset references are not to be pedagogically selected or filtered by the Reconciler.
Your job is simply to pass them along to the downstream Asset Selector.

You MUST associate EVERY visual asset provided in the "Visual Assets Candidates" section of the Evidence Package with the semantic unit that corresponds to the same page/slide or concept.
Do NOT filter or discard any visual asset candidates based on your own judgment of usefulness or because they are not explicitly referenced in the text.
Include ALL provided visual asset candidates in the `visual_asset_refs` of the most appropriate semantic unit, based on their `source_id` and `page`.

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

