# Organizzazione della Cartella "appunti IS"

Questa cartella è stata predisposta per facilitare la generazione manuale e supervisionata degli appunti di Ingegneria del Software (IS) utilizzando ChatGPT, bypassando i problemi di automazione (come il "Banner Bug") riscontrati con il sistema DISPENSATOR9000. 

Di seguito è descritto il contenuto di ogni file e cartella e come utilizzarli nel prompt per l'IA.

## 📄 File di Istruzioni e Contesto (Da fornire all'IA)

Questi file servono per "inquadrare" ChatGPT, spiegandogli qual è il suo ruolo, qual è il contesto e come deve scrivere gli appunti.

*   **`style-guide.md`**
    *   **Cosa fa:** È il System Prompt operativo del Writer. Contiene tutte le regole ferree su come formattare gli appunti: gerarchia dei titoli, uso del grassetto, sintassi di Obsidian per le immagini (`![[immagine.png]]`), pattern Q&A per le domande d'esame, e l'obbligo di usare l'inglese per i termini tecnici.
    *   **A cosa serve:** È il documento fondamentale da dare in pasto a ChatGPT *prima* di chiedergli di generare qualsiasi appunto, affinché l'output sia già perfettamente compatibile con Obsidian.
*   **`memoria.md`**
    *   **Cosa fa:** È il documento storico del progetto. Racconta cosa è stato fatto finora, perché il sistema automatico ha fallito (il problema con la selezione delle immagini) e quale deve essere l'approccio ora (generazione manuale supervisionata).
    *   **A cosa serve:** Dà a ChatGPT il "contesto". Leggendolo, l'IA capirà di dover agire come un esperto *Topic Writer / Chapter Assembler* umano-assistito, prestando molta attenzione a non inventare immagini inesistenti.

## 📚 Materiale Sorgente (PDF e Slide del Professore)

Questi file sono la "Golden Source", ovvero la verità assoluta da cui estrarre i concetti. Sono i materiali da cui l'IA deve prendere le informazioni per scrivere gli appunti.

*   **`ISW (1).pdf`**, **`IS_andrea.pdf`**, **`teoria.pdf`**
    *   **Cosa sono:** Materiale originale del corso, dispense, o appunti grezzi di teoria.
    *   **A cosa servono:** Da fornire all'IA come base di conoscenza (RAG manuale) quando le chiedi di sviluppare un determinato argomento.
*   **`risposte_domande_orali (2).pdf`**
    *   **Cosa fa:** Contiene le risposte tipiche alle domande orali dell'esame.
    *   **A cosa serve:** Perfetto da usare insieme al pattern Q&A descritto nella `style-guide.md`. Puoi chiedere all'IA: *"Integra queste domande da esame negli appunti usando il formato callout di Obsidian"*.
*   **Cartella `official-slides`**
    *   **Cosa contiene:** Le presentazioni ufficiali del professore (divise in Parte I e Parte II).
    *   **A cosa serve:** È la fonte primaria per l'ordine degli argomenti (il syllabus) e per capire il livello di dettaglio richiesto a lezione.
*   **Cartella `backbone`**
    *   **Cosa contiene:** I file YAML strutturali estratti in precedenza che dividono il corso in concetti logici.
    *   **A cosa serve:** Utile se vuoi far seguire a ChatGPT una struttura o scaletta prefissata per i capitoli.

## 📝 Appunti Estratti

*   **Cartella `ISW_obsidian_full`**
    *   **Cosa contiene:** Una massiccia estrazione di 166 pagine di appunti già convertiti in formato Markdown (con relative immagini separate).
    *   **A cosa serve:** Questo è un tesoro grezzo. Invece di far generare gli appunti da zero partendo dai PDF, puoi fornire a ChatGPT uno di questi file `.md` estratti e dirgli: *"Riformula questo documento grezzo seguendo rigorosamente le regole della `style-guide.md`, migliorando la leggibilità e sistemando le immagini"*. In questo modo il grosso del lavoro di trascrizione è già fatto.

---

### 🚀 Come procedere con ChatGPT (Workflow consigliato)

1.  **Inizializzazione:** Carica su ChatGPT i file `style-guide.md` e `memoria.md` e scrivi: *"Leggi questi file. Da ora in poi sarai il mio Topic Writer per gli appunti universitari di Ingegneria del Software."*
2.  **Lavorazione a blocchi:** Carica un capitolo alla volta (es. prendendolo dalla cartella `ISW_obsidian_full` o da un blocco di slide in `official-slides`).
3.  **Generazione:** Chiedi: *"Riscrivi questo materiale applicando la style-guide. Non inventare immagini, usa solo quelle presenti nel testo o ignorale se non sono veri diagrammi."*
