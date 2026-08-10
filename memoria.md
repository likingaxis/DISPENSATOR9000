# Memoria di Progetto - DISPENSATOR9000

## Stato Attuale
Siamo nella fase di "produzione a regime" del sistema di generazione appunti. La pipeline e la divisione dei ruoli tra agenti sono state stabilite e validate con successo.

### Ruoli Assegnati
- **Antigravity (Locale)**: 
  - Orchestrazione (esegue gli script Python `orchestrator.py`).
  - Retrieval & RAG (estrae testo dalle slide e crea l'Evidence Package).
  - *Reconciler* (tramite sub-agenti paralleli per estrarre la gerarchia semantica in YAML).
  - *Asset Selector* (valuta le immagini, scarta i falsi positivi/testo, tramite visione multimodale).
  - Git Manager (pusha i file preparatori su GitHub).
- **GPT-5.6 Sol (Web)**:
  - *Topic Writer* (legge `writer-input.md` da GitHub e scrive il markdown del singolo argomento).
  - *Chapter Reviewer* (legge `reviewer-input.md` da GitHub, fonde i topic, sistema lo stile e piazza le immagini, producendo il capitolo Canonical).

### Traguardi Raggiunti
1. **Refactoring Pipeline**: Separazione di `build-topic` in comandi idempotenti `prep-reconciler` e `prep-writer` per evitare blocchi dovuti ad attese manuali (`input()`).
2. **Risoluzione Immagini (Asset Selector)**: 
   - Creato sistema che genera una griglia di immagini (contact sheet) per eludere i limiti di caricamento immagini dell'LLM.
   - Delega della scelta a un sub-agente multimodale.
   - Aggiornato il prompt `asset-selector.md` con regola stringente per rifiutare i testi/bullet point rasterizzati.
3. **Validazione Workflow**: Eseguito un test completo (Capitolo 2 - Test Parziale) unendo due bozze fornite dall'utente. Il processo finale ha collocato correttamente le immagini estratte e ha generato il documento finale.

### Lavori in Corso (Capitolo 1)
- [x] **Chapter 1 Orchestration**: Successfully reconciled 3 topics (`intro-and-lifecycle`, `reliability-and-defects`, `hardware-vs-software`) and generated drafts.
- [x] **Full Chapter 1 Assembly**: Assembled the processed Chapter 1 topics into a "Canonical" document. The final assembled draft for Chapter 1 is saved in `runtime/chapter-drafts/chapter-1-introduction.md`.
- [x] **Image Integration**: Software failure graph was successfully injected into Chapter 1. The hardware graph was not extracted by the PDF parser due to vector graphic formatting, so it was omitted.
- [ ] **Automated Batch Workflow**: Refine the transition to a fully automated batch flow for future chapters.

### Prossimi Passi (In Attesa dell'Utente)
1. Pianificazione ed avvio della pipeline per il Capitolo 2.
2. Raffinamento del sistema di OCR/Estrazione per catturare correttamente i grafici vettoriali (svg/pdf) non rilevati nel Capitolo 1.
