# Roadmap di Implementazione — Study Notes System
Versione: 0.1

Questa roadmap definisce l'implementazione progressiva del sistema descritto in `architecture.md`, focalizzandosi sulla v0.1 (MVP per Ingegneria del Software). L'approccio evita l'overengineering e mantiene l'utente umano nel ciclo decisionale (human-in-the-loop).

---

## Fase 1: Setup Struttura Repository e Modello Dati

**1. Obiettivo:** Inizializzare la Single Source of Truth su GitHub e definire gli schemi dati minimi, garantendo un'architettura knowledge-first versionabile.
**2. Input:** `architecture.md`, requisiti del sistema (se esistenti).
**3. Attività da eseguire:**
   - Creare l'alberatura del repository (es. `docs/`, `profile/`, `courses/`, `system/schemas/`).
   - Definire gli schemi minimi YAML/JSON per Source, Fragment, Asset, Chapter, Topic, Course Memory e Student Profile.
**4. Responsabilità:**
   - **Antigravity:** Setup del repository e scaffolding degli schemi.
   - **ChatGPT:** Nessuna (se non consulenza logica formale sugli schemi).
   - **Utente:** Approvazione dell'alberatura e validazione del modello dati.
**5. File/artefatti prodotti:** Struttura directory nel filesystem locale sincronizzata con GitHub, file di schema (es. `system/schemas/*.yaml`).
**6. Criterio di completamento:** Gli schemi sono sufficienti a mappare logicamente una slide, un frammento di testo estratto e una nota canonica. Il repository è stabile.
**7. Dipendenze:** Nessuna.
**8. Rischi o OPEN DECISION:** 
   - OPEN DECISION: Formato esatto di validazione degli schemi (es. JSON Schema, YAML formale o parser Python pydantic).

---

## Fase 2: Creazione dello Student Profile (Style Guide)

**1. Obiettivo:** Costruire il profilo stilistico dello studente (Student Profile) per garantire appunti personalizzati prima di iniziare la produzione del corso.
**2. Input:** Vecchie dispense universitarie rappresentative dello stile dello studente.
**3. Attività da eseguire:**
   - Ingestion di base delle vecchie dispense (estrazione testo semplice).
   - Analisi e classificazione dei pattern stilistici, del livello di dettaglio e della formattazione.
   - Generazione della Style Guide (draft) e del documento di preferenze utente.
**4. Responsabilità:**
   - **Antigravity:** Estrazione testuale massiva dalle dispense storiche, calcolo degli *style fingerprint*.
   - **ChatGPT:** Comprensione semantica dei fingerprint per dedurre la `style-guide.md`, eliminando rumore o pattern occasionali.
   - **Utente:** Fornisce le dispense iniziali, revisiona e approva la Style Guide definitiva.
**5. File/artefatti prodotti:** `profile/style-guide.md`, `profile/preferences.yaml`.
**6. Criterio di completamento:** Esiste una Style Guide approvata dall'utente capace di guidare la formattazione di testi futuri.
**7. Dipendenze:** Fase 1 (per lo schema dello Student Profile).
**8. Rischi o OPEN DECISION:** 
   - Rischio: Bias verso uno stile occasionale derivante da dispense storiche eterogenee; sarà mitigato dalla revisione umana.

---

## Fase 3: Ingestion Pipeline e Asset Extraction (Ingegneria del Software)

**1. Obiettivo:** Acquisire ed elaborare i materiali grezzi (raw sources) del corso di Ingegneria del Software per costruire la knowledge base.
**2. Input:** Slide del docente, dispense aggiuntive, riassunti degli studenti per il corso pilota.
**3. Attività da eseguire:**
   - Parsing dei documenti in testo grezzo e chunk/blocchi elaborabili.
   - Asset extraction: identificare, ritagliare ed estrarre diagrammi, immagini e screenshot.
   - Arricchimento dei metadati e mappatura esatta della provenance (documento → pagina → blocco).
**4. Responsabilità:**
   - **Antigravity:** Implementazione ed esecuzione dell'ingestion (parsing PDF/slide, chunking, estrazione visiva, metadata tagging).
   - **ChatGPT:** Nessuna.
   - **Utente:** Fornitura e caricamento del materiale.
**5. File/artefatti prodotti:** Directory `courses/software-engineering/sources/` e `courses/software-engineering/assets/` popolare con test grezzi, chunk indicizzati e immagini estratte.
**6. Criterio di completamento:** Ogni pezzo di testo o asset estratto ha la sua origine esatta ricostruibile. Nessun contenuto è stato ancora sintetizzato, solo organizzato.
**7. Dipendenze:** Fase 1.
**8. Rischi o OPEN DECISION:** 
   - OPEN DECISION: Stack tecnologico di estrazione PDF/slide (es. PyMuPDF, parser OCR avanzati) non specificato in architettura.

---

## Fase 4: Costruzione della Course Map

**1. Obiettivo:** Ricavare e approvare la struttura e l'indice del corso (Course Model) suddiviso in Chapter e Topic.
**2. Input:** Chunk elaborati dalla Fase 3 (header estratti, slide d'indice, syllabus).
**3. Attività da eseguire:**
   - Analisi degli indici dei documenti originali per mappare i macro argomenti.
   - Generazione dell'albero gerarchico del corso (Course → Chapter → Topic).
   - Classificazione e associazione preliminare dei frammenti e degli asset visivi ai rispettivi Topic.
**4. Responsabilità:**
   - **Antigravity:** Classifica ed elabora i topic mapping (possibilmente tramite LLM di fascia economica), proponendo il Course Model iniziale.
   - **ChatGPT:** Revisione semantica ad alto livello (opzionale) per risolvere duplicati logici nell'indice.
   - **Utente:** Controllo, modifica e approvazione formale dell'ordine dei capitoli e della nomenclatura.
**5. File/artefatti prodotti:** `courses/software-engineering/course-model/course.yaml` e relativi file gerarchici per capitoli e topic.
**6. Criterio di completamento:** Course Map approvata; esiste uno scheletro gerarchico in cui poter iniettare i contenuti.
**7. Dipendenze:** Fase 3.
**8. Rischi o OPEN DECISION:** Nessuno di rilievo, la validazione utente copre le incongruenze iniziali.

---

## Fase 5: Implementazione del Retrieval e Gestione Context Window

**1. Obiettivo:** Fornire al modulo di sintesi esclusivamente le evidenze pertinenti per evitare la saturazione della context window e massimizzare la signal density.
**2. Input:** Course Map (Fase 4), chunk di conoscenza estratti e arricchiti (Fase 3).
**3. Attività da eseguire:**
   - Costruzione di un Search Index ricostruibile offline, separato da GitHub (non una persistent cache intoccabile).
   - Sviluppo logico del Retrieval per assemblare contesti differenziati: Global Context, Chapter Context limitato, Local Topic Context.
**4. Responsabilità:**
   - **Antigravity:** Crea l'indicizzazione, progetta ed espone l'API o i comandi di Retrieval per raggruppare dinamicamente le evidenze (ragionamento puramente data-pipeline).
   - **ChatGPT:** Nessuna.
   - **Utente:** Nessuna supervisione tecnica richiesta.
**5. File/artefatti prodotti:** Script/modulo locale di ricerca e file d'indice derivati/temporanei; evidenze ritornate come bundle strutturati e legati alla provenance.
**6. Criterio di completamento:** Interrogando il modulo per un Topic specifico, vengono recuperate accuratamente e unicamente le evidenze di testo, immagini e metadata inerenti a esso.
**7. Dipendenze:** Fase 3, Fase 4.
**8. Rischi o OPEN DECISION:** 
   - OPEN DECISION: Metodologia esatta di indicizzazione e retrieve (Keyword/BM25 vs Vector Embeddings vs Graph-based). Optare per la più semplice possibile (KISS) nel v0.1.

---

## Fase 6: Definizione della Course Memory e Progettazione dei Prompt

**1. Obiettivo:** Configurare lo stato persistente d'apprendimento per Ingegneria del Software (Course Memory) e delegare l'ideazione dei prompt a ChatGPT.
**2. Input:** `profile/style-guide.md`, bundle di evidenze d'esempio generati dal Retrieval.
**3. Attività da eseguire:**
   - Discutere in chat con ChatGPT la forma ideale dei prompt per: Evidence Reconciliation (capire conflitti delle fonti), Chapter/Topic Writing (generare markdown rispettando lo stile), Feedback Integration (assimilare correzioni umane). *Non creare codici statici per i prompt per ora, delegare a ChatGPT in conversazioni separate la stesura definitiva.*
   - Definire la struttura della Course Memory per accumulare termini già spiegati, convenzioni del corso e decisioni superate, evitando di passare capitoli vecchi nella context window.
**4. Responsabilità:**
   - **Antigravity:** Predispone l'ambiente di immagazzinamento e la logica di update per la Course Memory.
   - **ChatGPT:** Affianca l'utente nel Prompt Engineering, rifinendo concettualmente e testando le sue istruzioni prima dell'utilizzo programmatico.
   - **Utente:** Guida la creazione dei prompt con ChatGPT e approva i comportamenti attesi.
**5. File/artefatti prodotti:** Modelli di prompt in `system/prompts/`, `courses/software-engineering/course-memory.yaml`.
**6. Criterio di completamento:** I prompt di scrittura e sintesi sono stati sperimentati concettualmente; la Course Memory è tecnicamente pronta per essere aggiornata alla fine di un ciclo.
**7. Dipendenze:** Fase 2, Fase 5.
**8. Rischi o OPEN DECISION:** Nessuno di critico.

---

## Fase 7: Pilot su un Singolo Topic

**1. Obiettivo:** Verificare per la prima volta la validità del flusso end-to-end senza saturare i costi, validando stile e correttezza fattuale su una porzione ridotta.
**2. Input:** Un (1) singolo Topic della Course Map di Ingegneria del Software, pacchetto di evidenze dal Retriever, Student Profile.
**3. Attività da eseguire:**
   - Recupero contestuale per il Topic.
   - Riconciliazione delle fonti (ufficiali vs riassunti) e successiva scrittura semantica (Semantic Synthesis) del Topic in Markdown.
   - (Opzionale) Inclusione condizionale degli asset.
   - Revisione manuale dell'output e simulazione del salvataggio.
**4. Responsabilità:**
   - **Antigravity:** Compila la context window assemblando l'evidence payload. Gestisce il flusso d'esecuzione deterministico.
   - **ChatGPT:** Legge l'evidenza, scrive il Markdown secondo le istruzioni stilistiche e seleziona gli asset visivi utili tra quelli proposti.
   - **Utente:** Revisione finale. Giudizio qualitativo e invio di un feedback ("human-in-the-loop").
**5. File/artefatti prodotti:** Markdown di prova per il singolo Topic.
**6. Criterio di completamento:** L'utente promuove la qualità degli appunti generati per il Topic: lo stile è percepito come "suo" e il materiale non omette nulla di critico.
**7. Dipendenze:** Fase 6.
**8. Rischi o OPEN DECISION:** Nessuno.

---

## Fase 8: Pilot su un Capitolo Completo (Ingegneria del Software)

**1. Obiettivo:** Produrre il primo vero artefatto canonico ("Canonical Notes" per Capitolo), connettendo logicamente più Topic e attivando la Course Memory.
**2. Input:** Un capitolo della Course Map, il set completo dei Topic afferenti.
**3. Attività da eseguire:**
   - Ciclo iterativo sui Topic del capitolo (Retrieval → Synthesis).
   - Fusione e revisione testuale dell'intero capitolo (risolvere contraddizioni locali, curare le transizioni e mantenere coerenza terminologica).
   - Sottoposizione all'utente e successiva integrazione del feedback.
   - Inserimento dei concetti neo-acquisiti nella Course Memory.
**4. Responsabilità:**
   - **Antigravity:** Gestione orchestrata dell'esecuzione del capitolo, archiviazione formale su GitHub dopo approvazione. Aggiornamento programmatico della Course Memory e aggiornamento degli State.
   - **ChatGPT:** Elabora il flow logico delle transizioni tra i topic. Scrittura delle Canonical Notes in Markdown.
   - **Utente:** Lettura completa, individuazione di eventuali deviazioni di stile nel lungo termine, approvazione.
**5. File/artefatti prodotti:** `courses/software-engineering/canonical/01-chapter-name.md`, Course Memory aggiornata.
**6. Criterio di completamento:** Esiste il primissimo capitolo di Ingegneria del Software studiabile, archiviato ed approvato su GitHub come Single Source of Truth.
**7. Dipendenze:** Fase 7.
**8. Rischi o OPEN DECISION:** 
   - Rischio: Saturazione del token limit/costo LLM per revisionare globalmente un capitolo se eccessivamente lungo. Potrebbe servire una strategia chunkata anche per le revisioni.

---

## Fase 9: Generazione Iterativa e Produzione degli Output Varianti

**1. Obiettivo:** Scalare il processo validato al resto del corso ed esportare le declinazioni finali destinate allo studio pratico (Cheat Sheet, Master Notes).
**2. Input:** Tutti i capitoli restanti della Course Map, Capitoli pre-approvati, Course Memory aggiornata.
**3. Attività da eseguire:**
   - Esecuzione del ciclo "Capitolo per Capitolo" per il resto del corso, previa sempre l'approvazione umana (human-in-the-loop).
   - Al completamento delle Canonical Notes, derivare i riepiloghi compattati senza attingere nuovamente alle raw sources.
**4. Responsabilità:**
   - **Antigravity:** Triggera il processo per i capitoli successivi, gestisce Git e produce gli scaffold per Full Notes, Master Notes e Cheat Sheet.
   - **ChatGPT:** Aggiorna il proprio stile mano a mano che riceve feedback. Sintetizza Master Notes e Cheat Sheet **solo** partendo dalle Canonical Notes.
   - **Utente:** Supervisione finale sui capitoli residui e sui formati output.
**5. File/artefatti prodotti:** Tutta la serie `canonical/*.md`, file di riepilogo `Master Notes` e `Cheat Sheet`.
**6. Criterio di completamento:** Il progetto MVP Ingegneria del Software possiede una Knowledge Base riutilizzabile completa, personalizzata e approvata.
**7. Dipendenze:** Fase 8.
**8. Rischi o OPEN DECISION:** Nessuno di bloccante.
