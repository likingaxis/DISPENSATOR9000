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

### Lavori in Corso e Storico Capitoli
- **Capitolo 1**: Completato (include `intro-and-lifecycle`, `reliability-and-defects`, `hardware-vs-software`). Immagini reinserite manualmente.
- **Capitolo 2**: Completato in modalità ibrida/automatizzata (i sub-agenti hanno processato in parallelo i 5 topic).
- **Capitolo 3**: Parzialmente elaborato dalla pipeline. Il Reconciler ha processato i topic, ma **l'Asset Selector automatico ha fallito nuovamente** a causa del "Banner Bug" (selezionando titoli testuali al posto dei veri diagrammi su un batch di 195 immagini). Questo ha dimostrato l'attuale inaffidabilità del modello multimodale interno nel rispettare vincoli negativi ferrei. L'utente ha interrotto l'orchestrazione automatica per la fase di scrittura/assemblaggio, ripiegando sulla generazione manuale esterna tramite ChatGPT usando i prompt estratti (`writer.md` e `style-guide.md`).

### Problemi Aperti e Pivot Strategico
- **Fallimento del Visual Coverage Automatico**: L'estrazione e selezione totalmente autonoma delle immagini si è rivelata insoddisfacente. L'automazione di questo step necessita di supervisione umana (selezione manuale) o di un approccio drasticamente diverso.
- **Approccio Ibrido Confermata**: L'utente ha confermato la preferenza nell'utilizzare modelli esterni (ChatGPT) per il task di stesura finale (Topic Writer / Chapter Assembler), mantenendo la piattaforma locale (Antigravity) come preparatore dell'Evidence Package e manager dei file/RAG.

### Prossimi Passi (In Attesa dell'Utente)
1. Prosecuzione dei prossimi capitoli (Capitolo 4+) sfruttando il nuovo workflow ibrido: pipeline locale per la riconciliazione semantica e ChatGPT per la stesura markdown finale.
2. Rivalutazione del processo di gestione immagini per evitare perdite di tempo sui falsi positivi (titoli/banner).
