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

