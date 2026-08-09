# Architecture — Study Notes System
Version: 0.1

## 1. Scopo

Costruire un sistema generico e riutilizzabile per trasformare materiali universitari eterogenei in appunti completi, coerenti e personalizzati sullo stile dello studente.

Il primo caso reale sarà **Ingegneria del Software**.

Input possibili:
- slide del docente;
- dispense;
- riassunti di altri studenti;
- libri o documenti integrativi;
- immagini, diagrammi, screenshot e fotografie presenti nei materiali.

Il formato primario sarà **Markdown**. PDF, DOCX e HTML saranno eventuali output derivati.

## 2. Output

A partire dalla stessa knowledge canonica:
- Full Notes;
- Master Notes;
- Cheat Sheet;
- qualsiasi combinazione dei tre.

In futuro: flashcard, quiz, glossari, domande d'esame e ripassi rapidi.

## 3. Principio architetturale

Architettura **knowledge-first**:

```text
Raw Sources
    ↓
Ingestion
    ↓
Course Knowledge
    ↓
Retrieval
    ↓
Semantic Synthesis
    ↓
Canonical Notes
    ↓
Selectable Outputs
```

La dispensa non è la knowledge base principale.

## 4. Ruoli

### Antigravity — engineering e data pipeline

Responsabilità:
- ingestion;
- parsing PDF/slide;
- estrazione testo;
- estrazione immagini e asset visivi;
- metadata e provenance;
- chunking;
- classificazione;
- topic mapping;
- deduplicazione;
- indicizzazione;
- retrieval;
- associazione topic ↔ fonti ↔ immagini;
- costruzione e manutenzione del Course Model;
- workflow tecnici;
- gestione repository;
- automazioni;
- controlli deterministici;
- eventuale conversione Markdown → PDF/DOCX/HTML.

Principio:

> Antigravity prepara, organizza, indicizza, mantiene e automatizza.

### ChatGPT — semantic synthesis e writing

Responsabilità:
- interpretazione e revisione dello Student Profile;
- riconciliazione tra fonti;
- comprensione concettuale;
- sintesi;
- spiegazione;
- scrittura delle Canonical Notes;
- selezione e integrazione degli asset visivi utili;
- coerenza terminologica;
- coerenza con i capitoli precedenti;
- revisione dopo feedback umano;
- generazione di Full Notes / Master Notes / Cheat Sheet.

Principio:

> ChatGPT comprende, riconcilia, spiega, scrive e revisiona.

### Utente — supervisione

Responsabilità:
- approvazione Course Map;
- approvazione Student Profile;
- revisione dei capitoli;
- correzione dello stile;
- segnalazione di errori/omissioni;
- approvazione delle Canonical Notes;
- scelta degli output.

La prima iterazione è esplicitamente **human-in-the-loop**.

## 5. GitHub come Single Source of Truth

GitHub contiene la knowledge persistente e versionata condivisa tra Antigravity e ChatGPT.

Non è il RAG e non deve essere usato come cache tecnica.

Struttura candidata:

```text
study-system/

├── docs/
│   ├── architecture.md
│   ├── implementation-plan.md
│   ├── requirements.md
│   └── decisions.md
│
├── profile/
│   ├── style-guide.md
│   ├── preferences.yaml
│   └── examples/
│
├── courses/
│   └── software-engineering/
│       ├── sources/
│       ├── course-model/
│       ├── assets/
│       ├── canonical/
│       └── decisions/
│
├── system/
│   ├── prompts/
│   ├── schemas/
│   ├── workflows/
│   └── config/
│
└── generated/
```

Indici, embeddings e cache possono vivere fuori dal repository ed essere ricostruibili.

## 6. Student Model

Lo Student Model descrive **come lo studente scrive e studia**.

Contiene:
- Style Guide;
- preferenze;
- convenzioni editoriali;
- livello di dettaglio;
- struttura tipica delle spiegazioni;
- uso di bullet;
- uso di esempi;
- terminologia;
- uso di tabelle;
- uso di formule;
- uso di immagini;
- esempi rappresentativi;
- correzioni accumulate nel tempo.

```text
profile/
├── style-guide.md
├── preferences.yaml
└── examples/
```

## 7. Creazione iniziale dello Student Profile

Processo:

```text
Vecchie dispense
      ↓
analisi per documento
      ↓
style fingerprint per documento
      ↓
analisi trasversale
      ↓
pattern globali
pattern specifici della materia
eccezioni
      ↓
Draft Style Guide
      ↓
revisione ChatGPT
      ↓
Style Guide v1
```

La fase massiva può essere eseguita in Antigravity con un modello long-context forte.

ChatGPT rifinisce il risultato:
- elimina pattern accidentali;
- distingue preferenze globali da caratteristiche della materia;
- trasforma l'analisi in regole operative per il Writer.

La Style Guide viene poi raffinata durante l'uso reale.

## 8. Course Model

Rappresenta **cosa contiene il corso**.

Struttura minima:

```text
Course
└── Chapter
    └── Topic
        └── Concept
```

Per ogni elemento:
- fonti rilevanti;
- posizione nelle fonti;
- tipo di fonte;
- importanza;
- immagini;
- relazioni;
- conflitti;
- contenuti mancanti;
- provenance.

## 9. Provenance

Ogni informazione deve mantenere il collegamento:

```text
content
→ source document
→ page / slide
→ block / region
→ topic
```

Questo consente verifica, riconciliazione, recupero immagini e debugging.

## 10. Gerarchia delle fonti

Default per Ingegneria del Software:

```text
1. materiale ufficiale del docente
2. eventuali fonti ufficiali supplementari
3. riassunti degli studenti
```

I riassunti servono per integrare, chiarire, spiegare e rilevare omissioni, non per sovrascrivere automaticamente il materiale ufficiale.

## 11. Immagini e asset

Antigravity:
- estrae;
- salva;
- conserva fonte e pagina;
- associa ai topic;
- classifica preliminarmente.

Categorie possibili:
- diagram;
- UML;
- architecture;
- chart;
- table;
- screenshot;
- equation;
- photo;
- illustration;
- decorative;
- logo.

ChatGPT decide:
- se l'asset è realmente utile;
- dove inserirlo;
- come introdurlo;
- se aggiungere spiegazione/didascalia.

## 12. Markdown come formato principale

Canonical Notes in Markdown:

```markdown
# Requirements Engineering

## Functional Requirements

I **functional requirements** descrivono...

![Requirements process](../assets/requirements-process.png)
```

Vantaggi:
- versionabile;
- diff leggibili;
- facile da modificare;
- GitHub-friendly;
- immagini e formule supportabili;
- facilmente processabile da LLM e tool;
- convertibile in altri formati.

## 13. Gestione Context Window

Tre livelli.

### Global Context
Piccolo e persistente:
- Course Map;
- Student Profile;
- gerarchia fonti;
- glossario;
- decisioni importanti;
- Course Memory.

### Chapter Context
Solo il necessario al capitolo:
- fonti pertinenti;
- estratti;
- immagini;
- conflitti;
- collegamenti ad altri capitoli.

### Local Topic Context
Solo le evidenze necessarie al topic corrente.

Principio:

> Massimizzare la signal density, non il numero di token.

## 14. Course Memory

Non reinserire tutti i capitoli precedenti nella context window.

Conservare una memoria compatta con:
- termini già definiti;
- decisioni terminologiche;
- convenzioni;
- relazioni tra capitoli;
- concetti già spiegati;
- riferimenti interni;
- correzioni globali;
- aggiornamenti Student Profile.

Se serve un capitolo precedente completo, viene recuperato via retrieval.

## 15. Workflow capitolo per capitolo

```text
Course Map approved
        ↓
Chapter N
        ↓
Antigravity prepara la knowledge
        ↓
Retrieval seleziona le evidenze
        ↓
ChatGPT sintetizza e scrive
        ↓
User Review
        ↓
Correzioni
        ↓
Canonical Chapter approved
        ↓
Course Memory / Style Profile update
        ↓
Chapter N+1
```

Passi:
1. Antigravity identifica le fonti rilevanti.
2. Antigravity prepara il Chapter Model.
3. Retrieval seleziona le evidenze.
4. ChatGPT confronta le fonti.
5. ChatGPT produce il draft Markdown.
6. ChatGPT verifica coerenza e qualità.
7. L'utente revisiona.
8. Le correzioni vengono integrate.
9. La Canonical Note viene approvata.
10. Si aggiorna la Course Memory.
11. Se necessario si aggiorna lo Student Profile.
12. Si passa al capitolo successivo.

## 16. Canonical Notes

```text
courses/software-engineering/canonical/
├── 01-introduction.md
├── 02-process-models.md
├── 03-requirements.md
├── 04-uml.md
└── ...
```

Devono essere:
- complete;
- coerenti;
- verificabili;
- versionate;
- modulari;
- indipendenti dagli output finali.

## 17. Output Layer

```text
Canonical Notes
      ↓
├── Full Notes
├── Master Notes
└── Cheat Sheet
```

La generazione non deve richiedere una nuova interpretazione completa delle fonti originali.

## 18. Retrieval / RAG

```text
GitHub Knowledge
      ↓
Indexer
      ↓
Search Index
├── keyword
├── metadata
└── embeddings
      ↓
Retriever
```

L'indice è ricostruibile. La knowledge persistente resta nel repository.

## 19. Uso dei modelli

### Modelli economici / Antigravity
Preferibili per:
- classification;
- tagging;
- mapping;
- metadata enrichment;
- retrieval support;
- asset classification;
- processing massivo.

### Modelli forti
Preferibili per:
- style analysis complessa;
- reconciliation;
- semantic synthesis;
- writing;
- review;
- decisioni concettuali difficili.

La scelta del modello deve rimanere configurabile.

## 20. No compressione prematura

Antigravity non deve produrre un riassunto aggressivamente compresso da usare come unica fonte.

Il preprocessing deve principalmente:

```text
FIND
CLASSIFY
LINK
RANK
DE-DUPLICATE
TAG
```

non:

```text
SUMMARIZE EVERYTHING
DECIDE THE TRUTH
```

## 21. Feedback e adattamento

Le correzioni vanno classificate:
- factual correction;
- stylistic preference;
- structural preference;
- terminology decision;
- course-specific preference;
- global student preference.

Solo le preferenze realmente generali aggiornano lo Student Profile globale.

## 22. MVP

Primo corso: **Ingegneria del Software**.

Input:
- slide;
- tre riassunti;
- eventuali materiali supplementari;
- vecchi appunti personali per lo Student Profile.

Il corso serve contemporaneamente come prodotto reale e test dell'architettura.

## 23. Test di generalizzazione

Dopo il primo corso, test su una materia diversa.

La generalizzazione è riuscita se restano invariati:
- architettura;
- Student Profile;
- workflow;
- repository structure;
- retrieval strategy;
- Writer pipeline;

cambiando principalmente:

```text
courses/<new-course>/
```

## 24. Cosa non implementare nella v0.1

Non prioritari:
- microservizi;
- Kubernetes;
- sistemi distribuiti;
- fine-tuning;
- knowledge graph sofisticati;
- multi-agent framework pesanti;
- completa autonomia agentica;
- UI avanzata;
- vector DB come source of truth.

## 25. Architettura sintetica

```text
                        GitHub
                Single Source of Truth
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
 Student Model       Course Model     Canonical Notes
        │                 │                 │
        └─────────────────┼─────────────────┘
                          │
             ┌────────────┴────────────┐
             │                         │
        ANTIGRAVITY                 CHATGPT
             │                         │
        Engineering                  Cognition
             │                         │
        ingest                      understand
        parse                       reconcile
        classify                    synthesize
        map                         explain
        index                       write
        retrieve                    review
        extract assets              adapt style
             │                         │
             └────────────┬────────────┘
                          │
                     Human Review
                          │
                          ▼
                 Approved Knowledge
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
            Full        Master      Cheat
```

## 26. Regola architetturale principale

> **Antigravity owns the data pipeline.  
> ChatGPT owns semantic synthesis and writing.  
> GitHub owns persistent shared knowledge.  
> The user owns final approval.**

## 27. Prossimi passi

1. creare il repository;
2. salvare `architecture.md`;
3. definire `requirements.md`;
4. definire gli schemi minimi di Course Model e Student Model;
5. progettare il prompt/workflow per `style-guide.md`;
6. testarlo sulle vecchie dispense;
7. costruire la Course Map di Ingegneria del Software;
8. implementare il workflow del primo capitolo;
9. correggere l'architettura in base ai problemi reali;
10. automatizzare progressivamente il resto.
