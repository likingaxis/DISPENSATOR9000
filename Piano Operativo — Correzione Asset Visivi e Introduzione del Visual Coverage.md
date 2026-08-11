# Piano Operativo — Correzione Asset Visivi e Introduzione del Visual Coverage

## Obiettivo

Correggere definitivamente il problema attuale della pipeline DISPENSATOR9000 per cui, durante la generazione delle dispense, vengono spesso selezionati:

- banner con titolo della slide;
- testo bianco su sfondo nero/blu;
- frammenti testuali;
- elementi decorativi;

mentre vengono scartati o ignorati:

- diagrammi;
- schemi di processo;
- grafici;
- lifecycle;
- architetture;
- modelli visuali;
- rappresentazioni UML/BPMN;
- altre figure didatticamente importanti.

Il caso guida è il Capitolo 2:

- `Waterfall`: viene preferito il banner al diagramma;
- `Spiral`: viene preferito il banner al diagramma;
- `Incremental`: funziona correttamente solo in alcuni casi.

La nuova pipeline deve passare da una selezione **file-centric** a una selezione **concept-centric**, introducendo un contratto esplicito di **Visual Coverage**.

---

# Principio architetturale

La pipeline NON deve più chiedersi:

> Quali di queste immagini estratte sono belle o utili?

Deve chiedersi:

> Quali concetti didattici presenti nel capitolo beneficiano di una rappresentazione visuale e quale asset rappresenta meglio ciascuno di essi?

Un diagramma associato direttamente a un concetto importante deve essere considerato parte del **coverage didattico**.

Esempio:

```text
Modello Waterfall
      ↓
esiste diagramma Waterfall nella slide
      ↓
visual concept richiesto
      ↓
miglior asset = diagramma
      ↓
diagramma obbligatorio nel capitolo
```

Il banner con scritto `Modello Waterfall` non deve mai essere considerato una rappresentazione del modello.

---

# Target Pipeline

Implementare progressivamente questo flusso:

```text
PDF Ingestion
    ↓
Fragments + Visual Assets
    ↓
Retriever / Reconciler
    ↓
Topic Writer
    ↓
Topic Draft SOLO TESTO
    ↓
Visual Asset Selector + Coverage Mapper
    ↓
visual-coverage.yaml
    ↓
Chapter Assembler / Reviewer
    ↓
Markdown con visual obbligatori
    ↓
Visual Coverage Validator
    ↓
PASS
    ↓
Candidate Canonical Note
```

Principio fondamentale:

**il Writer non deve più scegliere autonomamente le immagini.**

La decisione visuale deve avvenire in un solo punto della pipeline.

---

# STEP 1 — Congelare la responsabilità del Writer

## File

```text
system/prompts/writer.md
```

## Modifica

Rimuovere al Writer la responsabilità di inserire immagini provenienti direttamente da:

```text
visual_asset_refs
obsidian_path
Reconciler Report
```

Il Writer deve produrre solamente contenuto didattico Markdown testuale.

Aggiungere una regola esplicita:

```text
VISUAL ASSET BOUNDARY

Il Writer NON seleziona, valuta o inserisce immagini.

Anche se il Reconciler Report contiene visual_asset_refs o obsidian_path,
NON produrre sintassi Obsidian ![[...]].

La selezione e il posizionamento degli asset visuali appartengono
esclusivamente alla fase Visual Asset Selector / Chapter Assembler.

Il Writer deve produrre un Topic Draft completamente indipendente
dagli asset visuali.
```

## Motivazione

Oggi esistono due canali diversi attraverso cui un'immagine può entrare nel capitolo:

```text
Writer
Asset Selector / Reviewer
```

Questo rende impossibile garantire che un asset rifiutato dal Selector non sia già entrato nel draft.

Dopo questa modifica deve esistere un solo gate visuale.

## Test

Generare un Topic Draft.

Verificare:

```bash
grep -n '!\[\[' topic-draft.md
```

Risultato atteso:

```text
nessun risultato
```

---

# STEP 2 — Sanitizzazione deterministica dei Topic Draft

Non affidarsi solamente al prompt.

## File

```text
system/scripts/orchestrator.py
```

## Modifica

Prima di costruire il `reviewer-input.md`, eliminare deterministicamente eventuali embed Obsidian rimasti nei Topic Draft.

Implementare una funzione simile a:

```python
def strip_obsidian_images(markdown):
    ...
```

Deve eliminare righe del tipo:

```markdown
![[assets/example.png]]
![[assets/example.png|500]]
```

e possibilmente anche embed inseriti accidentalmente inline.

## Motivazione

Anche dopo la modifica al prompt Writer possono esistere:

- vecchi draft;
- output generati con versioni precedenti;
- errori del modello.

Il Chapter Reviewer deve sempre ricevere una base testuale pulita.

## Invariante

Prima dell'assemblaggio:

```text
Topic Drafts = ZERO immagini
```

---

# STEP 3 — Cambiare il modello dati dei candidate asset

## File principali

```text
system/scripts/orchestrator.py
system/scripts/retriever.py
```

## Problema attuale

Il selector riceve pochi dati:

```yaml
asset_id:
topic_id:
source_id:
page:
obsidian_path:
nearby_text:
```

`nearby_text` inoltre deriva dai primi blocchi testuali della pagina e non necessariamente dal testo semanticamente vicino all'immagine.

Questa informazione è insufficiente.

## Nuova struttura

I candidate devono essere raggruppati per slide.

Esempio:

```yaml
slides:

  - topic_id: classic-process-models
    source_id: slides-02-process-1
    page: 6

    slide_title: "Modello Waterfall"

    slide_text: |
      Modello Waterfall
      ...

    semantic_context:
      - concept_id: waterfall-model
        label: Modello Waterfall

    candidate_assets:

      - asset_id: ...
        obsidian_path: assets/d234c4c9_p6_i0.png
        asset_type: embedded_image
        width: 442
        height: 622
        aspect_ratio: 0.71
        classification: uncertain

      - asset_id: ...
        obsidian_path: assets/d234c4c9_p6_i1.png
        asset_type: embedded_image
        width: 259
        height: 120
        aspect_ratio: 2.16
        classification: uncertain
```

## Campi minimi da recuperare dal DB

Per ogni asset:

```text
asset_id
source_id
page_num
file_path
asset_type
width
height
aspect_ratio
bbox
classification
excluded_from_candidates
```

## Importante

Non troncare il contesto della slide a 200 caratteri.

Per l'Asset Selector usare almeno il testo completo della slide o un limite molto più alto.

---

# STEP 4 — Eliminare il falso concetto di `nearby_text`

## File

```text
system/scripts/orchestrator.py
```

Attualmente esiste una logica simile a:

```python
SELECT content
FROM fragments
WHERE source_id = ? AND page_num = ?
ORDER BY block_order
LIMIT 3
```

Questa NON rappresenta realmente il testo vicino all'immagine.

Rinominare la funzione.

Da:

```python
get_nearby_text()
```

a qualcosa come:

```python
get_page_text()
```

Recuperare tutti i fragment della slide:

```sql
SELECT content
FROM fragments
WHERE source_id = ?
AND page_num = ?
ORDER BY block_order
```

e concatenarli.

## Motivazione

Il selector deve capire:

> questa è la slide sul Waterfall

non solamente leggere casualmente i primi tre blocchi PDF.

---

# STEP 5 — Raggruppamento obbligatorio per slide

## Modifica concettuale

Non passare più:

```yaml
candidate_assets:
  - asset A slide 4
  - asset B slide 18
  - asset C slide 6
  - asset D slide 31
```

Passare:

```yaml
slides:

  - page: 6
    concept: waterfall
    candidate_assets:
      - p6_i0
      - p6_i1
      - p6_i2
      - p6_i3

  - page: 31
    concept: spiral
    candidate_assets:
      - p31_i0
      - p31_i1
      - p31_i2
      - p31_i3
```

## Invariante

Il modello deve vedere **contemporaneamente tutti gli asset concorrenti della stessa slide**.

Questa è una delle correzioni principali del Banner Bug.

---

# STEP 6 — Introdurre semantic role obbligatorio

## File

```text
system/prompts/asset-selector.md
```

Sostituire la semplice classificazione include/reject con:

```yaml
semantic_role:
information_value:
decision:
```

Ruoli ammessi indicativamente:

```text
process_diagram
lifecycle_diagram
architecture_diagram
uml_diagram
bpmn_diagram
flowchart
state_diagram
dependency_graph
conceptual_diagram
comparison_diagram
quantitative_chart
timeline
structured_table
technical_screenshot
code_example
visual_example

title_fragment
text_fragment
bullet_list_image
logo
decorative
background
icon
generic_photo
partial_fragment
duplicate
unusable
```

## Regola critica

```text
title_fragment → SEMPRE reject
text_fragment → SEMPRE reject
bullet_list_image → SEMPRE reject
decorative → SEMPRE reject
background → SEMPRE reject
```

Non permettere eccezioni.

---

# STEP 7 — Introdurre esplicitamente il Banner Bug nel prompt

Nel nuovo `asset-selector.md` inserire un failure case dedicato.

Esempio:

```text
BANNER SUBSTITUTION — ERRORE CRITICO

Se una slide contiene contemporaneamente:

A. un'immagine che mostra principalmente il titolo della slide;
B. un diagramma che rappresenta semanticamente il concetto del titolo;

DEVI:

A → semantic_role: title_fragment → reject
B → semantic_role appropriato → candidato preferito

Il fatto che il banner contenga esattamente il nome del concetto NON
lo rende una rappresentazione visuale del concetto.

"Waterfall Model" scritto in grande != diagramma Waterfall.
```

---

# STEP 8 — Introdurre i Visual Concepts

Il Selector non deve limitarsi a classificare gli asset.

Per ogni slide deve prima identificare:

```yaml
visual_concepts:
```

Esempio:

```yaml
visual_concepts:

  - concept_id: waterfall-model
    label: "Modello Waterfall"

  - concept_id: waterfall-vv
    label: "Verification & Validation nel Waterfall"
```

Il concept deve essere derivato solamente dal contesto fornito.

Non usare conoscenza esterna.

---

# STEP 9 — Introdurre requirement level

Ogni visual concept deve ricevere:

```text
required
recommended
not_needed
```

## Required

Quando il visual rappresenta strutture difficili da sostituire efficacemente con semplice testo.

Usarlo soprattutto per:

```text
processi
lifecycle
flow
modelli a fasi
diagrammi architetturali
grafici
UML
BPMN
gerarchie
state machines
diagrammi di confronto
```

Esempi Capitolo 2:

```yaml
waterfall_model:
  requirement: required

spiral_model:
  requirement: required

incremental_model:
  requirement: required

throw_away_prototyping_process:
  requirement: required
```

## Recommended

Visual concretamente utile ma non indispensabile.

## Not needed

Definizione o concetto puramente testuale.

## Regola

NON creare una quota artificiale di immagini.

Alcuni concetti possono correttamente avere:

```yaml
requirement: not_needed
```

---

# STEP 10 — Introduzione del Preferred Asset

Per ogni visual concept `required` o `recommended`, il selector deve stabilire se esiste una rappresentazione appropriata.

Esempio:

```yaml
concept_id: waterfall-model
requirement: required
coverage_status: covered

preferred_asset:
  asset_id: ...
  obsidian_path: assets/d234c4c9_p6_i0.png
  semantic_role: process_diagram
  information_value: high
```

Gli altri asset della slide restano classificati ma vengono rifiutati.

Esempio:

```yaml
candidates:

  - obsidian_path: assets/d234c4c9_p6_i0.png
    semantic_role: process_diagram
    information_value: high
    decision: include

  - obsidian_path: assets/d234c4c9_p6_i1.png
    semantic_role: title_fragment
    information_value: none
    decision: reject
```

---

# STEP 11 — Non obbligare il modello a scegliere qualcosa

Introdurre:

```yaml
coverage_status:
```

Valori:

```text
covered
uncovered_no_suitable_asset
```

Se la slide contiene un concetto visuale importante ma nessuna immagine disponibile è valida:

```yaml
concept_id: some-process
requirement: required
coverage_status: uncovered_no_suitable_asset
```

NON scegliere un banner per evitare l'assenza.

## Principio

```text
No image > wrong image
```

Ma:

```text
correct diagram > no image
```

---

# STEP 12 — Generare `visual-coverage.yaml`

Separare l'output diagnostico del selector dal contratto usato dall'Assembler.

## File runtime suggerito

```text
runtime/chapter-runs/<chapter>/<run>/asset-selector/visual-coverage.yaml
```

Schema:

```yaml
visual_coverage_version: "1.0"

chapter_id: chapter-2-software-process

required_visuals:

  - visual_id: visual-waterfall-model

    topic_id: classic-process-models

    concept:
      id: waterfall-model
      label: Modello Waterfall

    source:
      source_id: slides-02-process-1
      page: 6

    asset:
      asset_id: ...
      obsidian_path: assets/d234c4c9_p6_i0.png
      semantic_role: process_diagram

    placement:
      anchor_type: after_concept
      anchor_text: Modello Waterfall
      width: 600

    required: true
```

Separatamente:

```yaml
recommended_visuals:
```

e:

```yaml
uncovered_required_visuals:
```

---

# STEP 13 — Rendere gli anchor più robusti

Evitare quando possibile:

```yaml
after_concept: "qualcosa di vagamente simile"
```

Preferire riferimenti stabili.

Prima scelta:

```yaml
placement:
  anchor_type: after_semantic_unit
  semantic_unit_id: waterfall-model
```

Fallback:

```yaml
placement:
  anchor_type: after_concept
  anchor_text: Modello Waterfall
```

Il selector non deve inventare semantic unit ID.

Può usare solamente quelli ricevuti dall'input.

---

# STEP 14 — Aggiornare Chapter Reviewer

## File

```text
system/prompts/chapter-reviewer.md
```

Sostituire l'attuale concetto generico di `Selected Assets` con il nuovo `Visual Coverage Contract`.

Aggiungere:

```text
VISUAL COVERAGE IS BINDING

Per ogni elemento presente in required_visuals:

- DEVI inserire esattamente l'obsidian_path indicato;
- DEVI inserirlo una sola volta;
- DEVI rispettarne il placement;
- NON puoi sostituire l'asset;
- NON puoi ometterlo;
- NON puoi introdurre asset differenti.

Gli asset in recommended_visuals possono essere omessi se realmente ridondanti.

Gli asset non presenti nel Visual Coverage Contract NON devono essere introdotti.
```

---

# STEP 15 — Sintassi Markdown deterministica

Per:

```yaml
obsidian_path: assets/d234c4c9_p6_i0.png
width: 600
```

il Reviewer deve produrre esattamente:

```markdown
![[assets/d234c4c9_p6_i0.png|600]]
```

Sempre come blocco separato.

Mai:

```markdown
testo ![[image]] altro testo
```

---

# STEP 16 — Visual Coverage Validator Python

Questa parte è obbligatoria.

NON affidare la correttezza solamente al Chapter Reviewer.

## File suggerito

```text
system/scripts/visual_coverage.py
```

oppure direttamente una funzione nell'orchestrator inizialmente.

Il validator deve ricevere:

```text
visual-coverage.yaml
reviewer-output.md
```

e verificare almeno:

### VC1 — Required Presence

Ogni:

```yaml
required_visuals[].asset.obsidian_path
```

deve comparire nel Markdown.

### VC2 — Exactly Once

Ogni required asset deve comparire una volta.

### VC3 — No Unexpected Images

Recuperare tutti gli embed:

```text
![[...]]
```

dal Markdown.

Ogni asset deve essere presente nel contratto.

Un banner rifiutato non può comparire nel capitolo.

### VC4 — Correct Width

Se specificata:

```yaml
width: 600
```

verificare:

```markdown
![[assets/file.png|600]]
```

### VC5 — Uncovered Required

Se:

```yaml
uncovered_required_visuals
```

non è vuoto, registrare:

```yaml
visual_coverage_complete: false
```

anche se il Markdown è formalmente valido.

### VC6 — Correct Placement

Prima versione semplice:

verificare che l'asset compaia sotto la sezione/heading contenente il concept.

Versione successiva:

verificare una distanza massima dall'anchor.

---

# STEP 17 — Bloccare la promozione in caso di failure

Nel workflow:

```text
reviewer-output.md
      ↓
visual coverage validation
      ↓
PASS / FAIL
```

Se:

```yaml
status: fail
```

il capitolo NON deve diventare Candidate Canonical Note.

Esempio failure:

```yaml
visual_coverage_validation:

  status: fail

  missing:
    - visual-waterfall-model

  unexpected_assets:
    - assets/d234c4c9_p6_i1.png
```

Questo caso deve bloccare la pipeline.

---

# STEP 18 — Sistemare il problema dei vettoriali

Questa modifica è parallela ma importante.

## File

```text
system/scripts/ingest_pdfs.py
```

Attualmente i vettoriali vengono registrati come:

```text
VIRTUAL_RENDER_REQUIRED
```

ma non diventano asset fisici utilizzabili.

Correggere questo comportamento.

Quando:

```python
page.get_drawings()
```

indica presenza di grafica vettoriale significativa, creare anche un render reale della pagina.

Esempio concettuale:

```python
matrix = fitz.Matrix(2.5, 2.5)
pix = page.get_pixmap(matrix=matrix)
pix.save(...)
```

Registrarlo come asset:

```text
asset_type: page_render
```

o:

```text
asset_type: vector_page_render
```

Non usare più:

```text
VIRTUAL_RENDER_REQUIRED
```

come unico rappresentante della grafica vettoriale.

---

# STEP 19 — Il page render è contesto, non automaticamente output finale

Importante.

Non inserire automaticamente l'intera slide negli appunti.

Il render completo può servire al modello per capire:

```text
titolo
diagramma
frecce
rapporti spaziali
layout
```

Il Selector deve comunque preferire:

```text
embedded diagram
```

quando esiste già come asset completo e pulito.

Solo se lo schema non è disponibile separatamente si può considerare un futuro crop del page render.

---

# STEP 20 — Implementazione crop: seconda iterazione, non bloccante

Non complicare la prima patch introducendo subito object detection/crop automatico.

Prima implementare bene:

```text
slide grouping
semantic roles
preferred asset
visual coverage
validation
```

Questi cambiamenti dovrebbero già risolvere Waterfall e Spiral perché i diagrammi corretti risultano già estratti come raster in diversi casi.

Soltanto successivamente aggiungere:

```yaml
crop_bbox:
  x0:
  y0:
  x1:
  y1:
```

per le slide in cui il diagramma esiste solo come grafica vettoriale/composita.

---

# STEP 21 — Test specifici sul Capitolo 2

Il Capitolo 2 deve diventare il regression test principale.

## Test Waterfall

Slide 6.

Atteso:

```text
p6_i0 → include / process_diagram / high
p6_i1 → reject / title_fragment / none
```

Il capitolo deve contenere:

```markdown
### Modello Waterfall

...

![[assets/d234c4c9_p6_i0.png|...]]
```

Non deve contenere:

```text
p6_i1
```

---

# STEP 22 — Test Spiral

Slide 31.

Atteso:

```text
p31_i0 → preferred diagram
p31_i1 → title_fragment → reject
```

Il diagramma deve comparire vicino alla spiegazione del modello a spirale.

Il banner non deve comparire.

---

# STEP 23 — Test Incremental

Usare il caso positivo come controllo.

Slide 23.

La nuova pipeline NON deve peggiorare ciò che già funziona.

Atteso:

```text
p23_i0 → title/banner → reject
p23_i1 → diagram → include
```

---

# STEP 24 — Test Throw-away Prototyping

Verificare che il diagramma del processo venga conservato.

Concetto:

```text
initial requirement
      ↓
prototype
      ↓
experiment
      ↓
discard
      ↓
real development
```

Se esiste uno schema appropriato:

```yaml
requirement: required
coverage_status: covered
```

---

# STEP 25 — Test Risk Management

Se la slide contiene un vero schema:

```text
Identification
     ↓
Analysis
     ↓
Planning
     ↓
Monitoring
```

deve essere considerato visual concept.

Se invece contiene soltanto un elenco testuale reso graficamente:

```yaml
semantic_role: bullet_list_image
decision: reject
```

Il selector deve distinguere le due cose.

---

# STEP 26 — Metriche runtime

Produrre al termine dell'Asset Selector:

```yaml
coverage_summary:

  required_total: 8
  required_covered: 7
  required_uncovered: 1

  recommended_total: 4
  recommended_covered: 3

  rejected_title_fragments: 14
  rejected_decorative: 9
```

Queste metriche devono essere salvate nel run.

Servono per capire immediatamente se qualcosa è andato storto.

---

# STEP 27 — Warning automatici

Stampare warning nell'orchestrator quando:

```text
required_uncovered > 0
```

Esempio:

```text
[VISUAL COVERAGE WARNING]

3 required visual concepts are uncovered:

- waterfall-vv
- scrum-cycle
- cmm-levels
```

Non nascondere questi casi.

---

# STEP 28 — Regola quantitativa importante

NON imporre:

```text
N immagini per topic
```

o:

```text
massimo 2 immagini per topic
```

come regola rigida.

Il nuovo sistema è concept-driven.

Un topic può richiedere:

```text
0 visual
```

oppure:

```text
4 visual
```

se contiene quattro strutture realmente importanti.

La selezione deve dipendere dal coverage semantico, non da una quota editoriale.

---

# STEP 29 — Separare tre livelli concettuali

Nell'implementazione mantenere distinti:

## Physical Asset

```text
p6_i0.png
```

## Semantic Visual

```text
process_diagram
```

## Visual Concept

```text
waterfall-model
```

Mapping:

```text
waterfall-model
      ↓ represented by
process_diagram
      ↓ stored as
p6_i0.png
```

Questa separazione è il cuore della nuova architettura.

---

# STEP 30 — Non eliminare subito le euristiche geometriche

Le euristiche attuali su:

```text
width
height
aspect_ratio
repetition
```

possono rimanere come pre-filter.

Ma non devono essere il criterio finale.

Usarle per:

```text
likely_decorative
likely_banner
likely_icon
```

Non per decidere definitivamente:

```text
diagram/not diagram
```

La classificazione definitiva deve essere multimodale e semantica.

---

# STEP 31 — Aggiungere eventualmente `likely_banner`

Come ottimizzazione successiva, aggiungere alla classificazione ingestion:

```text
likely_banner
```

Segnali possibili:

```text
larghezza molto superiore all'altezza
altezza ridotta
posizione nella parte alta della slide
presenza di testo
assenza di struttura visuale interna
```

Ma il Selector deve comunque verificare visualmente.

---

# STEP 32 — Non fare Visual Selection nel Reconciler

Non spostare questa responsabilità nel Reconciler.

Il Reconciler deve continuare a gestire:

```text
claims
conflicts
evidence
semantic units
```

Può associare gli asset alla semantica, ma NON deve decidere:

```text
questa immagine è bella
questa va negli appunti
```

Visual Asset Selection rimane una fase indipendente.

---

# STEP 33 — Output intermedi da preservare

Per debugging salvare sempre:

```text
asset-selector/
├── candidates.yaml
├── images/
├── selector-input.md
├── selector-output.yaml
├── visual-coverage.yaml
└── validation.yaml
```

Non sovrascrivere gli output diagnostici.

Questo permetterà di capire in futuro:

```text
quali immagini erano disponibili?
come sono state classificate?
perché è stata scelta questa?
quale visual concept rappresentava?
il validator cosa ha rilevato?
```

---

# STEP 34 — Ordine consigliato di implementazione

Non implementare tutto contemporaneamente.

## Patch 1 — Correttezza strutturale

Implementare:

```text
1. Writer senza immagini
2. strip immagini dai vecchi draft
3. candidates raggruppati per slide
4. page text completo
5. metadata asset completi
```

Testare.

---

## Patch 2 — Nuovo Selector

Implementare:

```text
6. semantic_role
7. Banner Bug rules
8. visual_concepts
9. requirement level
10. preferred_asset
11. uncovered
```

Testare sul Capitolo 2.

---

## Patch 3 — Visual Coverage Contract

Implementare:

```text
12. visual-coverage.yaml
13. placement anchors
14. Chapter Reviewer binding
15. Markdown injection
```

Rigenerare Capitolo 2.

---

## Patch 4 — Validator

Implementare:

```text
16. Visual Coverage Validator
17. blocco promozione su FAIL
26. metriche
27. warning
```

Dopo questa patch il sistema possiede finalmente una garanzia.

---

## Patch 5 — Vector support

Implementare:

```text
18. page render
19. render come context
```

Testare sulle slide dove gli schemi non sono disponibili come raster embedded.

---

## Patch 6 — Crop semantico

Solo se necessario:

```text
page render
    ↓
vision
    ↓
crop_bbox
    ↓
physical diagram asset
```

Non iniziare da qui.

---

# Definition of Done

La modifica è considerata completata soltanto quando tutti i seguenti punti sono veri.

## Writer

```text
[ ] non inserisce immagini
[ ] non seleziona immagini
[ ] Topic Draft = testo puro
```

## Asset Selector

```text
[ ] riceve asset raggruppati per slide
[ ] riceve testo completo della slide
[ ] riceve metadata geometrici
[ ] assegna semantic_role a ogni asset
[ ] distingue title_fragment da diagram
[ ] identifica visual concepts
[ ] assegna required/recommended/not_needed
[ ] seleziona preferred_asset
[ ] può dichiarare uncovered
```

## Visual Coverage

```text
[ ] viene generato visual-coverage.yaml
[ ] required_visuals hanno asset preciso
[ ] ogni asset possiede placement
[ ] gli uncovered vengono preservati
```

## Chapter Reviewer

```text
[ ] riceve Topic Draft senza immagini
[ ] riceve Visual Coverage
[ ] inserisce required_visuals
[ ] non introduce immagini autonome
```

## Validator

```text
[ ] verifica required presence
[ ] verifica exactly once
[ ] verifica unexpected assets
[ ] verifica path
[ ] verifica width
[ ] verifica almeno approssimativamente il placement
[ ] può bloccare la promozione
```

## Regression test Capitolo 2

```text
[ ] Waterfall usa il vero diagramma
[ ] Waterfall non usa il banner
[ ] Spiral usa il vero diagramma
[ ] Spiral non usa il banner
[ ] Incremental continua a usare il diagramma corretto
[ ] gli altri process diagram utili vengono preservati
[ ] titoli neri/testo bianco non finiscono nel capitolo
```

---

# Regola finale per Antigravity

Non considerare risolto il problema quando il sistema semplicemente smette di inserire banner.

Il requisito è più forte:

> **Quando il materiale ufficiale contiene una rappresentazione visuale pedagogicamente importante di un concetto trattato negli appunti, la pipeline deve individuarla, associarla a quel concetto, preservarla nel Visual Coverage Contract e verificare deterministicamente che compaia nel capitolo finale.**

Quindi:

```text
NO banner
```

è soltanto metà del lavoro.

Il vero risultato è:

```text
concept explained
      +
correct diagram preserved
      +
correct placement
      +
automatic validation
```

Questo deve diventare l'invariante della pipeline.