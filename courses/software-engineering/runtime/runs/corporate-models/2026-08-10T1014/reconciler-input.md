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

**topic_id**: corporate-models
**title**: Modelli Corporate (Microsoft, Netscape)

## Retrieval Metadata
- Primary fragments: 77
- Secondary fragments: 0
- Visual assets candidate: 68
- Estimated context tokens: ~1019

## 1. Primary Evidence (Official Coverage)

### Source: slides-02-process-1 (`official-slides\I parte ISW - SistSW\02-Processo software parte1.pdf`)
#### Page 48
> UniRoma2 - ISW/SSW 49

> Il Modello Microsoft1

> • La Microsoft, come altre organizzazioni che  sviluppano software commerciale, ha dovuto  affrontare, fin dalla metà degli anni 80, problemi di:

> – incremento della qualità dei prodotti software

> – riduzione di tempi e costi di sviluppo

> • Per cercare di risolvere tali problemi si è adottato  un processo che è al tempo stesso iterativo,  incrementale e concorrente e che permette di  esaltare le doti di creatività delle persone coinvolte  nello sviluppo di prodotti software

> 1 M.A. Cusumano and R.W. Selby, How Microsoft Builds Software, Communications of  the ACM, vol. 40, n. 6, June 1997.

#### Page 49
> UniRoma2 - ISW/SSW 50

> Approccio synch-and-stabilize

> • L'approccio usato attualmente da Microsoft è noto  come "synchronize-and-stabilize"

> • Tale approccio è basato su:

> – sincronizzazione quotidiana delle attività svolte da

> persone che lavorano sia individualmente che  all'interno di piccoli team (da 3 a 8 persone), mediante  assemblaggio dei componenti software sviluppati  (anche parzialmente) in un prodotto (daily build) che  viene testato e corretto

> – stabilizzazione periodica del prodotto in incrementi

> (milestone) successivi durante l'avanzamento del  progetto, piuttosto che un'unica volta alla fine

#### Page 50
> UniRoma2 - ISW/SSW 51

> Ciclo di sviluppo a 3 fasi

> • Planning phase

> – Define product vision, specification and schedule

> • Development phase

> – Feature development in 3/4 sequential subprojects,

> each resulting in a milestone release

> • Stabilization phase

> – Comprehensive internal and external testing, final

> product, stabilization and ship

#### Page 51
> UniRoma2 - ISW/SSW 52

> Planning phase

#### Page 52
> UniRoma2 - ISW/SSW 53

> Development phase

#### Page 53
> UniRoma2 - ISW/SSW 54

> Stabilization phase

#### Page 54
> UniRoma2 - ISW/SSW 55

> Strategie e Principi

> 1. Strategia per definire prodotto e processo:  "considerare la creatività come elemento  essenziale" Principi di realizzazione:

> a. Dividere il progetto in milestone (da 3 a 4) b. Definire una "product vision" e produrre una

> specifica funzionale che evolverà durante il progetto c. Selezionare le funzionalità e le relative priorità in

> base alle necessità utente d. Definire un'architettura modulare per replicare nel

> progetto la struttura del prodotto e. Assegnare task elementari e limitare le risorse

#### Page 55
> UniRoma2 - ISW/SSW 56

> Strategie e Principi (2)

> 2. Strategia per lo sviluppo e la consegna dei  prodotti: "lavorare in parallelo con frequenti  sincronizzazioni" Principi di realizzazione:

> a. Definire team paralleli ed utilizzare daily build per la

> sincronizzazione b. Avere sempre un prodotto da consegnare, con

> versioni per ogni piattaforma e mercato c. Usare lo stesso linguaggio di programmazione

> all'interno dello stesso sito di sviluppo d. Testare continuamente il prodotto durante il suo

> sviluppo e. Usare metriche per il supporto alle decisioni

#### Page 56
> UniRoma2 - ISW/SSW 57

> Esempio di metriche collezionate

#### Page 57
> UniRoma2 - ISW/SSW 58

> Milestones

#### Page 58
> UniRoma2 - ISW/SSW 59

> Modello  del ciclo

> di  sviluppo

> synch-

> and- stabilize

#### Page 59
> UniRoma2 - ISW/SSW 60

> Confronto tra modelli synch-and-stabilize e waterfall

### Source: slides-02-process-2 (`official-slides\I parte ISW - SistSW\02-Processo software parte2.pdf`)
#### Page 0
> UniRoma2 - ISW/SSW 61

> Il Modello Netscape2

> • Anche alla Netscape si è adottato un modello di tipo  synchronize-and-stabilize, con opportuni adattamenti allo  sviluppo di applicazioni Internet (browser e prodotti server):

> – dimensione dello staff

> • in media 1 tester ogni 3 sviluppatori (ma stessa produttività di Microsoft  nello sviluppo di prodotti comparabili, ad es. IE vs. Communicator)

> – processo

> • scarso effort di pianificazione (tranne che su prodotti server)

> • documentazione incompleta

> • scarso controllo sullo stato di avanzamento del progetto (lasciato  all’esperienza e all’influenza dei project manager)

> • scarso controllo su attività di ispezione del codice (code review)

> • pochi dati storici per il supporto alle decisioni

> 2 M.A. Cusumano and D.B. Yoffie, Software Development on Internet Time, IEEE  Computer, October 1999.

#### Page 1
> UniRoma2 - ISW/SSW 62

> Staffing

#### Page 2
> UniRoma2 - ISW/SSW 63

> Netscape Development Process (1)

#### Page 3
> UniRoma2 - ISW/SSW 64

> Netscape Development Process (2)

#### Page 4
> UniRoma2 - ISW/SSW 65

> Netscape Development Process (3)

## 2. Secondary Evidence (BM25 Lexical + Concepts)

*No secondary evidence found.*

## 3. Visual Assets Candidates

- **asset_id**: 2680fd7b-4aba-4589-87b5-0ae209a5b2d5
  source: slides-02-process-1
  page: 48
  type: embedded_image
  path: `d234c4c9_p48_i0.png`

- **asset_id**: 8b5872b0-b821-423d-8087-d61e9fe91b18
  source: slides-02-process-1
  page: 48
  type: embedded_image
  path: `d234c4c9_p48_i1.png`

- **asset_id**: 9af2281d-4aaf-4871-94d4-2495e17a77cb
  source: slides-02-process-1
  page: 48
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b617bfbe-1ddc-4aac-8077-ac777d70604a
  source: slides-02-process-1
  page: 49
  type: embedded_image
  path: `d234c4c9_p49_i0.png`

- **asset_id**: 6a25b1fa-caa3-42a8-8a78-6348916ed475
  source: slides-02-process-1
  page: 49
  type: embedded_image
  path: `d234c4c9_p49_i1.png`

- **asset_id**: 4b2e5fee-a5a9-4bc2-ba18-1d508255f519
  source: slides-02-process-1
  page: 49
  type: embedded_image
  path: `d234c4c9_p49_i2.png`

- **asset_id**: ddd842b5-bb2f-4adc-b13a-36cd2498f4c7
  source: slides-02-process-1
  page: 49
  type: embedded_image
  path: `d234c4c9_p49_i3.png`

- **asset_id**: e96045a8-ec45-45a6-ba03-5c7faacdf4a2
  source: slides-02-process-1
  page: 49
  type: embedded_image
  path: `d234c4c9_p49_i4.png`

- **asset_id**: d480cb76-c38c-45ff-9e11-01ac723497ce
  source: slides-02-process-1
  page: 49
  type: embedded_image
  path: `d234c4c9_p49_i5.png`

- **asset_id**: a4ccf392-c016-499d-821a-943a5f855433
  source: slides-02-process-1
  page: 49
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 9e0c2b3e-870b-4109-a304-b137b44624fe
  source: slides-02-process-1
  page: 50
  type: embedded_image
  path: `d234c4c9_p50_i0.png`

- **asset_id**: a7c0f273-28d4-4d43-88a9-3ec79dde8fc0
  source: slides-02-process-1
  page: 50
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: ef26eebc-6ff0-498b-ac34-698fcb5a6875
  source: slides-02-process-1
  page: 51
  type: embedded_image
  path: `d234c4c9_p51_i0.png`

- **asset_id**: 09e5fc82-82df-425d-993c-818f5ffd9fba
  source: slides-02-process-1
  page: 51
  type: embedded_image
  path: `d234c4c9_p51_i1.jpeg`

- **asset_id**: 082f5b0f-5ca2-4777-ac38-b2d39fe18e71
  source: slides-02-process-1
  page: 51
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: bbab2792-aa20-4021-aff0-a600781d07f2
  source: slides-02-process-1
  page: 52
  type: embedded_image
  path: `d234c4c9_p52_i0.png`

- **asset_id**: c7f32bfd-34f9-4244-9e82-3512b53958a6
  source: slides-02-process-1
  page: 52
  type: embedded_image
  path: `d234c4c9_p52_i1.jpeg`

- **asset_id**: 5c5b4ef2-2a04-4fe1-b8a0-36896679db3b
  source: slides-02-process-1
  page: 52
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 905ce492-4382-4f7d-ad17-0af7fa330e15
  source: slides-02-process-1
  page: 53
  type: embedded_image
  path: `d234c4c9_p53_i0.png`

- **asset_id**: d72937ea-8575-4ad7-a86e-de38b49ed2eb
  source: slides-02-process-1
  page: 53
  type: embedded_image
  path: `d234c4c9_p53_i1.jpeg`

- **asset_id**: fdf2d790-a3c3-42f9-b438-256593e60163
  source: slides-02-process-1
  page: 53
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 24435f16-f1bb-48c3-877c-3d3a7b487ac1
  source: slides-02-process-1
  page: 54
  type: embedded_image
  path: `d234c4c9_p54_i0.png`

- **asset_id**: fed27504-daa9-44c8-9e22-0e9ef3f4103e
  source: slides-02-process-1
  page: 54
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: fdee0548-22f1-476b-b196-3d8f77fd5a34
  source: slides-02-process-1
  page: 55
  type: embedded_image
  path: `d234c4c9_p55_i0.png`

- **asset_id**: 7401224f-939a-4637-813d-36ecfcc522d4
  source: slides-02-process-1
  page: 55
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b7c0c6a0-d3d9-49e1-b01b-21267f40ba35
  source: slides-02-process-1
  page: 56
  type: embedded_image
  path: `d234c4c9_p56_i0.png`

- **asset_id**: ef182c8e-c28d-4811-af37-83315f7bcf89
  source: slides-02-process-1
  page: 56
  type: embedded_image
  path: `d234c4c9_p56_i1.png`

- **asset_id**: 4bcdf16d-0f60-4507-ba44-bc7ec1ec58e3
  source: slides-02-process-1
  page: 56
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 89c31ec7-b7bc-40a6-bdfa-8875db8c46fd
  source: slides-02-process-1
  page: 57
  type: embedded_image
  path: `d234c4c9_p57_i0.png`

- **asset_id**: 53db57aa-6745-4083-9480-9be359d30d3b
  source: slides-02-process-1
  page: 57
  type: embedded_image
  path: `d234c4c9_p57_i1.jpeg`

- **asset_id**: 3d0f1d97-aff5-4264-9542-19547a5eb59d
  source: slides-02-process-1
  page: 57
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 7bee35d2-bf00-4766-9772-86448323fb2e
  source: slides-02-process-1
  page: 58
  type: embedded_image
  path: `d234c4c9_p58_i0.png`

- **asset_id**: 3a6b5f64-c9c9-4d51-9168-efba3d7e14ff
  source: slides-02-process-1
  page: 58
  type: embedded_image
  path: `d234c4c9_p58_i1.png`

- **asset_id**: 0353a105-2653-41bf-9ca7-ecfecc6fef4b
  source: slides-02-process-1
  page: 58
  type: embedded_image
  path: `d234c4c9_p58_i2.png`

- **asset_id**: 300523c5-1b22-4ccc-b46e-a9bdc97edd87
  source: slides-02-process-1
  page: 58
  type: embedded_image
  path: `d234c4c9_p58_i3.png`

- **asset_id**: 83c959f3-8a99-49e2-b1f9-8a9b6fbafc38
  source: slides-02-process-1
  page: 58
  type: embedded_image
  path: `d234c4c9_p58_i4.png`

- **asset_id**: 7a0c701a-2998-48f8-8835-161a3ee83f7f
  source: slides-02-process-1
  page: 58
  type: embedded_image
  path: `d234c4c9_p58_i5.png`

- **asset_id**: 98233bf3-ba9e-43f3-8675-ce7455040502
  source: slides-02-process-1
  page: 58
  type: embedded_image
  path: `d234c4c9_p58_i6.png`

- **asset_id**: 3cac629a-89c0-4c25-a9d9-c475e0c73265
  source: slides-02-process-1
  page: 58
  type: embedded_image
  path: `d234c4c9_p58_i7.png`

- **asset_id**: 6d1e66bb-45c3-48b5-a9f0-29c483aea6ce
  source: slides-02-process-1
  page: 58
  type: embedded_image
  path: `d234c4c9_p58_i8.png`

- **asset_id**: ebb4e6c8-303b-4282-8114-005b2046f16e
  source: slides-02-process-1
  page: 58
  type: embedded_image
  path: `d234c4c9_p58_i9.jpeg`

- **asset_id**: b16a6855-985f-4d75-9d2d-4c437fdb87ff
  source: slides-02-process-1
  page: 58
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: bf23ef63-74b7-4fca-aa42-f1bac3cf0d30
  source: slides-02-process-1
  page: 59
  type: embedded_image
  path: `d234c4c9_p59_i0.jpeg`

- **asset_id**: 915ce46c-bc29-4ee5-8853-4ec1992ccd16
  source: slides-02-process-1
  page: 59
  type: embedded_image
  path: `d234c4c9_p59_i1.png`

- **asset_id**: 7c3cf4cd-d83e-44dd-a5e7-26e97c752960
  source: slides-02-process-1
  page: 59
  type: embedded_image
  path: `d234c4c9_p59_i2.png`

- **asset_id**: e48b857a-0c92-49bf-8919-c3e7c603c0a9
  source: slides-02-process-1
  page: 59
  type: embedded_image
  path: `d234c4c9_p59_i3.png`

- **asset_id**: 3ba4e37b-edb0-473d-9386-0e6fe3baf2e2
  source: slides-02-process-1
  page: 59
  type: embedded_image
  path: `d234c4c9_p59_i4.png`

- **asset_id**: 85275c0a-ef3c-4d0a-a920-3129f60669ef
  source: slides-02-process-1
  page: 59
  type: embedded_image
  path: `d234c4c9_p59_i5.png`

- **asset_id**: 85c7e907-98e1-49cf-91da-f64b349556ee
  source: slides-02-process-1
  page: 59
  type: embedded_image
  path: `d234c4c9_p59_i6.png`

- **asset_id**: 7017f005-b316-4a30-abb7-059c55a2907f
  source: slides-02-process-1
  page: 59
  type: embedded_image
  path: `d234c4c9_p59_i7.png`

- **asset_id**: db138e41-c6be-4176-b379-23da7df6edb0
  source: slides-02-process-1
  page: 59
  type: embedded_image
  path: `d234c4c9_p59_i8.png`

- **asset_id**: ffe022c8-acf0-408d-8d64-e96618877dd9
  source: slides-02-process-1
  page: 59
  type: embedded_image
  path: `d234c4c9_p59_i9.png`

- **asset_id**: c61d4277-58e4-413a-ba29-e0af69f669c3
  source: slides-02-process-1
  page: 59
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: dcf43b9b-0d4f-463e-bf02-580447acf1da
  source: slides-02-process-2
  page: 0
  type: embedded_image
  path: `4f64ac69_p0_i0.png`

- **asset_id**: 6237beec-c26a-4fa5-af88-0a25bf175fa8
  source: slides-02-process-2
  page: 0
  type: embedded_image
  path: `4f64ac69_p0_i1.png`

- **asset_id**: 5b68b088-aa79-4401-b64c-6d47f422dc60
  source: slides-02-process-2
  page: 0
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: edabd826-99ac-4993-b2ae-0aff759d524a
  source: slides-02-process-2
  page: 1
  type: embedded_image
  path: `4f64ac69_p1_i0.png`

- **asset_id**: 600deab8-ab8a-4bc4-8a3c-e882d9b12983
  source: slides-02-process-2
  page: 1
  type: embedded_image
  path: `4f64ac69_p1_i1.png`

- **asset_id**: 32826a47-9148-46f7-9700-1d998d84313d
  source: slides-02-process-2
  page: 1
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: fda5383a-e451-4d56-a52c-a8a7b82bee37
  source: slides-02-process-2
  page: 2
  type: embedded_image
  path: `4f64ac69_p2_i0.png`

- **asset_id**: 25547837-ae27-4530-8fd0-4f4101a2e528
  source: slides-02-process-2
  page: 2
  type: embedded_image
  path: `4f64ac69_p2_i1.png`

- **asset_id**: 7f20f304-8df4-45b3-b29c-3b5975c6705a
  source: slides-02-process-2
  page: 2
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 45b79d54-1da6-4b2f-8f04-1832df595f43
  source: slides-02-process-2
  page: 3
  type: embedded_image
  path: `4f64ac69_p3_i0.png`

- **asset_id**: c9ef4e27-6d6c-42b3-9fb9-1607b21055f9
  source: slides-02-process-2
  page: 3
  type: embedded_image
  path: `4f64ac69_p3_i1.png`

- **asset_id**: 96fdd58a-2d8e-40dc-bd2d-68b5339452b4
  source: slides-02-process-2
  page: 3
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: dfa76384-43e5-4404-ab09-9f74bb6cd970
  source: slides-02-process-2
  page: 4
  type: embedded_image
  path: `4f64ac69_p4_i0.png`

- **asset_id**: f2281218-fcc9-40ba-8906-2144008ff6b7
  source: slides-02-process-2
  page: 4
  type: embedded_image
  path: `4f64ac69_p4_i1.png`

- **asset_id**: 1f3fbf14-87cf-4709-9887-b3f5beaaa619
  source: slides-02-process-2
  page: 4
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

