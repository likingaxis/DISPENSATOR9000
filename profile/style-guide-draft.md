# Prompt per ChatGPT/Opus: Generazione Style Guide

*Istruzioni per l'utente: Copia e incolla il seguente testo in una nuova chat con ChatGPT o Claude Opus.*

***

**Ruolo:** Sei un esperto di didattica, instructional design e Markdown per Obsidian.

**Obiettivo:** Devi scrivere la "Style Guide" definitiva (`style-guide.md`) che guiderà un sistema automatico (un LLM Writer) nella stesura di appunti universitari per me. Il sistema genererà i miei appunti leggendo documenti accademici grezzi e dovrà riscriverli in modo che sembrino scritti esattamente da me.

**Le mie Evidenze di Stile (Analizzate da Antigravity):**
1. Scrivo usando la sintassi nativa di Obsidian: le immagini sono inserite come `![[nome_file.jpg]]` (senza markdown standard) e uso callout ripiegabili come `>[!question]-` per simulare flashcard/domande d'esame, che contengono a loro volta `>[!done]-` per mostrare la risposta.
2. Odio i "muri di testo". La mia scrittura è fortemente "bullet-driven". Uso liste puntate annidate (`-`, tab `-`) per scomporre i concetti in gerarchie logiche (Concetto principale -> dettaglio -> sotto-dettaglio).
3. Mantengo sempre la terminologia tecnica informatica in inglese (es. *thread*, *query processing*), preferibilmente evidenziata in corsivo se introdotta per la prima volta.
4. Uso il **grassetto** per evidenziare le definizioni fondamentali o i nomi degli algoritmi, mai a caso.
5. Per la matematica e l'informatica teorica, uso sempre LaTeX in modo rigoroso (inline `$x$` o in blocco `$$x$$`).
6. Le sezioni principali sono introdotte da titoli H2 (`##`) o H3 (`###`). 

**Output Richiesto:**
Genera il documento Markdown completo `style-guide.md`. Il documento deve fungere da "System Prompt" o da insieme di istruzioni operative direttive (es. "Devi formattare così...", "Non scrivere mai paragrafi lunghi") che un LLM Writer dovrà applicare pedissequamente. Strutturalo in:
1. Principi Generali di Stile
2. Formattazione e Sintassi (inserisci esempi espliciti della sintassi Obsidian per immagini e liste)
3. Struttura Logica (densità, bullet point vs testo discorsivo)
4. Gestione di Matematica e Terminologia
5. Sezione Speciale: "Il pattern Q&A (Domande e Risposte in stile Obsidian)".
