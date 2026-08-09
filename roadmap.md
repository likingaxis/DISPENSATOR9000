# Project Roadmap — Study Notes System
Version: 0.1

## Obiettivo della roadmap

Questa roadmap descrive, in ordine operativo, cosa fare per costruire la prima versione funzionante del sistema e arrivare a produrre i primi appunti reali di **Ingegneria del Software**.

Il principio guida è evitare overengineering: ogni fase deve produrre qualcosa di utilizzabile prima di procedere alla successiva.

La roadmap termina con un MVP funzionante, capace di:

- conoscere il mio stile di appunti;
- acquisire e organizzare i materiali del corso;
- costruire una Course Map;
- recuperare le fonti corrette per un capitolo;
- produrre un capitolo Markdown;
- permettermi di revisionarlo;
- aggiornare lo Student Profile sulla base dei miei feedback;
- procedere capitolo per capitolo fino alla dispensa completa.

---

# FASE 0 — Congelare il design iniziale

## Obiettivo

Trasformare le idee discusse finora in un riferimento stabile, evitando di cambiare continuamente architettura durante l'implementazione.

## Cosa fare

1. Creare il repository GitHub del progetto.
2. Inserire `architecture.md`.
3. Creare:
   - `requirements.md`
   - `decisions.md`
   - `roadmap.md`
4. Stabilire che le decisioni importanti vengono salvate nel repository e non lasciate solo nelle chat.

## Struttura minima

```text
study-system/

├── docs/
│   ├── architecture.md
│   ├── requirements.md
│   ├── decisions.md
│   └── roadmap.md
│
├── profile/
├── courses/
├── system/
└── generated/
```

## Output

Repository iniziale con documentazione di base.

## Criterio di completamento

La struttura del progetto è creata e `architecture.md` è considerata la baseline v0.1.

---

# FASE 1 — Definire i requisiti verificabili

## Obiettivo

Stabilire chiaramente cosa deve fare il sistema prima di iniziare a programmarlo.

## Cosa fare

Creare `docs/requirements.md`.

Separare i requisiti in:

### Requisiti funzionali

Esempi:

- importare PDF e slide;
- estrarre testo;
- estrarre immagini;
- mantenere documento e pagina di provenienza;
- creare una Course Map;
- collegare fonti a chapter/topic;
- generare Canonical Notes in Markdown;
- usare lo Student Profile;
- permettere revisione manuale;
- generare Full Notes, Master Notes e Cheat Sheet.

### Requisiti non funzionali

Esempi:

- nessuna perdita della provenance;
- output versionabili con Git;
- retrieval ricostruibile;
- Markdown come formato principale;
- possibilità di sostituire il modello LLM;
- evitare dipendenza da un unico vector DB;
- elaborazione capitolo per capitolo;
- context window controllata.

### Fuori scope v0.1

Specificare esplicitamente:

- niente UI complessa;
- niente microservizi;
- niente fine-tuning;
- niente multi-agent framework complesso;
- niente automazione completa senza revisione umana.

## Output

`requirements.md`.

## Criterio di completamento

Ogni requisito deve poter essere verificato con un sì/no oppure con un test concreto.

---

# FASE 2 — Definire il modello dati minimo

## Obiettivo

Decidere quale informazione deve essere persistente prima di implementare parsing e retrieval.

Questa è una delle fasi più importanti.

## Cosa fare

Definire gli schemi minimi per:

### Source

```yaml
id:
filename:
type:
priority:
```

### Source Fragment

```yaml
id:
source_id:
page:
text:
topic_ids:
```

### Asset

```yaml
id:
source_id:
page:
file:
type:
topic_ids:
usefulness:
```

### Chapter

```yaml
id:
title:
order:
topics:
```

### Topic

```yaml
id:
title:
chapter_id:
source_fragments:
assets:
conflicts:
```

### Canonical Note

```yaml
chapter_id:
status:
file:
topics_covered:
unresolved_questions:
```

### Student Profile

Definire almeno:

```yaml
style_rules:
terminology:
structure_preferences:
formatting_preferences:
examples:
```

## Decisione importante

Non inserire informazioni solo perché “potrebbero servire”.

Partire dal minimo necessario per il primo corso.

## Output

File in:

```text
system/schemas/
```

ad esempio:

```text
source.schema.yaml
topic.schema.yaml
asset.schema.yaml
student-profile.schema.yaml
canonical-note.schema.yaml
```

## Criterio di completamento

È possibile rappresentare con questi schemi:
- una slide;
- un frammento di un riassunto;
- un'immagine;
- un topic;
- un capitolo;
- una nota canonica.

---

# FASE 3 — Preparare il materiale per lo Student Profile

## Obiettivo

Raccogliere abbastanza esempi del mio stile da permettere al sistema di dedurre pattern reali senza caricare inutilmente tutto il mio archivio.

## Cosa fare

1. Scegliere 2–4 dispense personali.
2. Preferire materie differenti.
3. Per ciascuna selezionare esempi rappresentativi:
   - spiegazione teorica;
   - sezione con formule;
   - sezione con bullet;
   - confronto/tabella;
   - eventuale uso di immagini;
   - capitolo lungo;
   - capitolo breve.
4. Se possibile mantenere anche almeno una dispensa completa per controlli trasversali.

## Non fare

Non scegliere solo le pagine “più belle”.

Servono campioni rappresentativi del modo reale in cui scrivo.

## Output

```text
profile/raw-examples/
```

## Criterio di completamento

Il corpus selezionato contiene esempi sufficientemente diversi da distinguere preferenze globali da caratteristiche specifiche di una singola materia.

---

# FASE 4 — Creare lo Student Style Model v1

## Obiettivo

Produrre una guida operativa del mio stile.

## Responsabilità

### Antigravity + modello long-context forte

Fa l'analisi massiva.

Per ogni dispensa deve produrre uno `style fingerprint`.

Esempi di aspetti da analizzare:

- organizzazione gerarchica;
- lunghezza dei paragrafi;
- rapporto testo/bullet;
- uso del grassetto;
- terminologia italiana/inglese;
- definizioni;
- esempi;
- formule;
- tabelle;
- immagini;
- tono;
- densità informativa;
- livello di dettaglio;
- transizioni tra concetti.

Poi confronta i fingerprint.

Deve distinguere:

```text
pattern globale
pattern specifico della materia
pattern occasionale
```

### ChatGPT

Riceve l'analisi risultante e:

- elimina generalizzazioni deboli;
- distingue stile da contenuto;
- converte i pattern in istruzioni utilizzabili dal Writer;
- crea una Style Guide chiara.

## Output

```text
profile/
├── style-guide.md
├── preferences.yaml
├── evidence.md
└── examples/
```

## Criterio di completamento

La Style Guide deve permettere a un altro LLM di produrre un testo plausibilmente vicino al mio modo di prendere appunti.

Non deve ancora essere perfetta.

---

# FASE 5 — Preparare il corso di Ingegneria del Software

## Obiettivo

Creare la directory del primo corso e raccogliere tutti i materiali originali.

## Cosa fare

Creare:

```text
courses/software-engineering/
```

Inserire:

- slide del docente;
- riassunto A;
- riassunto B;
- riassunto C;
- eventuale syllabus;
- programma d'esame;
- eventuali esercizi/materiali ufficiali.

## Registrare le fonti

Creare un registry con:

```yaml
source:
priority:
type:
description:
```

Esempio:

```text
priority 1 → slide ufficiali
priority 2 → materiale ufficiale supplementare
priority 3 → riassunti studenti
```

## Output

```text
courses/software-engineering/sources/
courses/software-engineering/source-registry.yaml
```

## Criterio di completamento

Tutte le fonti rilevanti sono presenti e classificate.

---

# FASE 6 — Implementare l'Ingestion Pipeline

## Obiettivo

Trasformare i documenti grezzi in dati strutturati senza ancora riassumerli.

## Responsabile principale

Antigravity.

## Cosa implementare

### 1. Parsing testo

Per ogni documento:

- testo;
- pagina/slide;
- heading quando rilevabile;
- blocchi;
- ordine.

### 2. Provenance

Ogni frammento deve sapere:

```text
source → page → block
```

### 3. Estrazione asset

Estrarre:

- diagrammi;
- immagini;
- screenshot;
- foto;
- grafici.

Mantenere:

- source;
- page;
- bounding box quando utile.

### 4. Fallback visuale

Alcuni diagrammi nelle slide possono essere composti da forme vettoriali e non essere immagini embedded.

Il sistema deve prevedere il rendering/crop della regione della pagina.

### 5. Pulizia

Rimuovere o marcare:

- header/footer ripetitivi;
- loghi;
- elementi decorativi;
- duplicati evidenti.

## Non fare ancora

- non creare il riassunto;
- non decidere la verità;
- non comprimere fortemente il testo.

## Output

```text
courses/software-engineering/extracted/
courses/software-engineering/assets/
```

## Criterio di completamento

Se scelgo una pagina qualsiasi di una fonte, posso trovare:
- il testo estratto;
- gli asset;
- i metadata;
- la provenienza corretta.

---

# FASE 7 — Costruire la prima Course Map

## Obiettivo

Ricostruire la struttura canonica dell'intero corso prima di scrivere gli appunti.

## Cosa deve fare Antigravity

Usando:
- slide;
- headings;
- programmi;
- riassunti;

proporre:

```text
Course
├── Chapter 1
│   ├── Topic 1
│   ├── Topic 2
│   └── ...
├── Chapter 2
└── ...
```

Per ogni topic associare preliminarmente:
- slide rilevanti;
- sezioni dei tre riassunti;
- asset;
- eventuali conflitti.

## Revisione umana

Io controllo:

- ordine;
- capitoli;
- topic mancanti;
- topic duplicati;
- livello di granularità.

## Output

```text
courses/software-engineering/course-model/
├── course.yaml
├── chapters/
└── topics/
```

## Criterio di completamento

L'indice del corso è approvato.

Non si procede alla generazione della dispensa prima di questo checkpoint.

---

# FASE 8 — Implementare retrieval e Chapter Context

## Obiettivo

Far sì che il sistema recuperi solo le informazioni necessarie per il capitolo/topic corrente.

## Prima versione

Non serve partire subito con un vector DB sofisticato.

Implementare in ordine:

1. lookup per topic;
2. metadata filtering;
3. keyword/BM25;
4. embeddings solo se portano un miglioramento reale.

## Il retrieval deve restituire

Per un topic:

```text
- fonti ufficiali rilevanti
- riassunto A
- riassunto B
- riassunto C
- immagini rilevanti
- provenance
- possibili conflitti
```

## Context levels

Preparare:

### Global Context
- Course Map;
- Style Guide;
- glossario;
- decisioni.

### Chapter Context
- evidence per il capitolo.

### Topic Context
- evidence per il topic.

## Test obbligatorio

Scegliere 5–10 topic casuali.

Controllare manualmente se il retrieval recupera realmente le parti giuste.

## Output

Retriever funzionante.

## Criterio di completamento

Il retrieval ha una precisione sufficiente da non richiedere la lettura manuale di tutti i PDF per ogni topic.

---

# FASE 9 — Definire la Course Memory

## Obiettivo

Evitare di inserire tutti i capitoli precedenti nella context window.

## Creare un formato compatto che contenga

- termini già definiti;
- decisioni terminologiche;
- convenzioni editoriali;
- concetti già spiegati;
- riferimenti tra capitoli;
- unresolved issues;
- correzioni globali;
- regole aggiornate dello Student Profile.

Esempio:

```yaml
defined_terms:
  - requirement
  - stakeholder

terminology:
  validation: "validation"
  verification: "verification"

cross_references:
  mvc: chapter-04
```

## Output

```text
courses/software-engineering/course-memory.yaml
```

## Criterio di completamento

Il Writer può capire il contesto generale senza ricevere integralmente tutti i capitoli precedenti.

---

# FASE 10 — Prompt Engineering del Writer

## Obiettivo

Creare il prompt che permette a ChatGPT di trasformare evidence + Student Profile in Canonical Notes di qualità.

## Consiglio operativo

Usare una chat separata dedicata al Prompt Engineering.

## Prompt da progettare

### 1. Evidence Reconciliation Prompt

Compito:
- confrontare le fonti;
- riconoscere accordi;
- riconoscere divergenze;
- rispettare la gerarchia delle fonti;
- non inventare.

### 2. Chapter Writer Prompt

Input:
- Style Guide;
- Chapter structure;
- evidence;
- Course Memory;
- asset candidates.

Output:
- Markdown.

### 3. Reviewer Prompt

Controlla:
- copertura;
- errori;
- contraddizioni;
- stile;
- ripetizioni;
- coerenza con fonti.

### 4. Feedback Integration Prompt

Trasforma le mie correzioni in:
- modifica locale;
- eventuale regola di stile globale;
- eventuale decisione specifica del corso.

## Output

```text
system/prompts/
├── reconcile.md
├── writer.md
├── reviewer.md
└── feedback-integration.md
```

## Criterio di completamento

Il prompt produce un risultato soddisfacente su un topic di prova.

---

# FASE 11 — Pilot su un singolo topic

## Obiettivo

Validare l'intera pipeline su una piccola unità prima di generare un capitolo intero.

## Workflow

```text
topic
↓
Antigravity retrieval
↓
evidence
↓
ChatGPT reconciliation
↓
ChatGPT writing
↓
review
↓
mia correzione
```

## Cosa verificare

- fonti corrette;
- nessuna omissione grave;
- stile;
- lunghezza;
- immagini;
- terminologia;
- Markdown;
- provenance;
- costo/tempo del workflow.

## Output

Una singola Canonical Note di topic.

## Criterio di completamento

Il risultato è abbastanza buono da giustificare il test su un capitolo completo.

---

# FASE 12 — Pilot sul primo capitolo completo

## Obiettivo

Produrre il primo vero capitolo di Ingegneria del Software.

## Workflow

Per ogni topic del capitolo:

1. retrieve;
2. reconcile;
3. write;
4. verify.

Poi:

5. assemblare il capitolo;
6. eliminare ripetizioni;
7. controllare transizioni;
8. controllare immagini;
9. controllare riferimenti interni.

## Mia revisione

Leggo il capitolo come se dovessi studiarlo.

Segnalo:

- troppo lungo;
- troppo corto;
- troppo schematico;
- troppo discorsivo;
- concetto poco chiaro;
- definizione mancante;
- esempio inutile;
- immagine utile/mancante;
- terminologia non mia.

## Output

```text
canonical/01-....md
```

## Criterio di completamento

Il capitolo è approvato come materiale da cui studierei realmente.

---

# FASE 13 — Aggiornare il sistema dal feedback

## Obiettivo

Fare in modo che il secondo capitolo sia migliore del primo.

## Classificare ogni feedback

### Locale

Vale solo per quel punto.

### Course-specific

Vale per Ingegneria del Software.

### Global style

Vale per tutti i miei appunti.

## Aggiornare

Possibili file:

```text
profile/style-guide.md
courses/software-engineering/decisions/
courses/software-engineering/course-memory.yaml
```

## Non fare

Non trasformare ogni singola correzione in una nuova regola globale.

## Criterio di completamento

Il sistema incorpora solo le correzioni realmente generalizzabili.

---

# FASE 14 — Produzione iterativa dell'intero corso

## Obiettivo

Produrre le Canonical Notes complete.

## Procedura

Ripetere:

```text
Chapter N
↓
retrieve
↓
write
↓
review
↓
user approval
↓
commit
↓
update memory
↓
Chapter N+1
```

## Git

Ogni capitolo approvato dovrebbe corrispondere a uno stato chiaramente versionato.

Esempio commit:

```text
Approve chapter 03 requirements engineering
```

## Criterio di completamento

Tutti i capitoli della Course Map sono presenti e approvati.

---

# FASE 15 — Global Review della dispensa

## Obiettivo

Controllare problemi che non sono visibili lavorando capitolo per capitolo.

## Verificare

- argomenti mancanti;
- duplicazioni;
- definizioni incoerenti;
- terminologia;
- riferimenti tra capitoli;
- concetti spiegati troppo tardi;
- immagini duplicate;
- stile variabile;
- capitoli troppo sbilanciati.

## Utilizzare la Course Map

Ogni topic deve risultare:

```text
covered
partial
missing
```

## Output

Canonical Notes v1 complete.

## Criterio di completamento

La knowledge canonica è considerata completa e pronta per gli output.

---

# FASE 16 — Creare gli Output Generators

## Obiettivo

Generare viste diverse senza reinterpretare completamente le fonti originali.

## Full Notes

Potrebbero coincidere quasi direttamente con l'assemblaggio delle Canonical Notes.

## Master Notes

Compressione orientata al ripasso:

- concetti chiave;
- definizioni;
- relazioni;
- esempi essenziali;
- tabelle comparative.

## Cheat Sheet

Compressione estrema:

- keyword;
- relazioni;
- formule;
- pattern;
- differenze importanti;
- errori da evitare.

## Scelta utente

```text
[ ] Full Notes
[ ] Master Notes
[ ] Cheat Sheet
```

## Output

Markdown.

Conversioni in PDF/DOCX/HTML restano opzionali.

## Criterio di completamento

Gli output possono essere rigenerati dalle Canonical Notes senza rileggere tutte le fonti.

---

# FASE 17 — Validazione del sistema

## Obiettivo

Capire se il progetto ha realmente risolto il problema iniziale.

## Metriche pratiche

Valutare:

- quanto materiale devo correggere;
- quante omissioni trovo;
- qualità dello stile;
- affidabilità del retrieval;
- qualità delle immagini selezionate;
- tempo per capitolo;
- costo LLM;
- quantità di intervento manuale.

## Domanda decisiva

> Studiare da questi appunti è realmente migliore rispetto a usare direttamente i tre riassunti esistenti?

Se la risposta è no, il sistema va corretto prima di essere generalizzato.

---

# FASE 18 — Test su una seconda materia

## Obiettivo

Dimostrare che il sistema è generico.

## Procedura

Creare:

```text
courses/new-course/
```

Riutilizzare senza modifiche sostanziali:

- Student Profile;
- schemas;
- ingestion pipeline;
- retrieval;
- Writer;
- Reviewer;
- output generators.

## Criterio di successo

La nuova materia richiede principalmente nuovi dati, non una nuova architettura.

---

# Ordine pratico immediato

Per iniziare realmente da oggi, l'ordine consigliato è:

```text
1. Repository GitHub
2. architecture.md
3. roadmap.md
4. requirements.md
5. schemas minimi
6. selezione vecchie dispense
7. Student Style Model v1
8. caricamento materiali Software Engineering
9. ingestion
10. Course Map
11. retrieval
12. prompt engineering
13. pilot topic
14. pilot chapter
15. correzione
16. produzione capitolo per capitolo
```

---

# Primo punto in cui inizierai realmente a creare gli appunti

La creazione degli appunti veri inizia nella:

## FASE 11 — Pilot su un singolo topic

e diventa operativa nella:

## FASE 12 — Pilot sul primo capitolo completo

Tutto ciò che viene prima serve a garantire che il primo capitolo venga generato:

- dalle fonti corrette;
- senza perdere provenance;
- rispettando il tuo stile;
- senza saturare inutilmente la context window;
- in una struttura riutilizzabile per tutto il resto del corso.

---

# Regola di avanzamento

Non passare automaticamente alla fase successiva.

Per ogni fase chiedersi:

1. L'output richiesto esiste?
2. È sufficientemente corretto?
3. È già utile al workflow successivo?
4. Stiamo aggiungendo complessità che non serve ancora?

Se le prime tre risposte sono sì e la quarta è no, procedere.

L'obiettivo non è costruire subito il sistema ideale.

L'obiettivo è arrivare il prima possibile a:

```text
un capitolo reale
+
fonti corrette
+
stile corretto
+
feedback umano
+
knowledge versionata
```

e poi migliorare il sistema sulla base dell'esperienza reale.
