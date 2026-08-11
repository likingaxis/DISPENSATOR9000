# Capitolo 2 — Software Process

## Modelli Sequenziali (Waterfall, Prototyping)

### Def processo software
Il **processo software** è la serie di attività necessarie alla realizzazione di un prodotto software:
- nei tempi previsti;
- con i costi previsti;
- con le caratteristiche di qualità desiderate.

All'interno del processo software:
- si applicano metodi, tecniche e strumenti;
- si producono prodotti:
    - intermedi;
    - finali;
- si stabilisce il controllo gestionale del progetto;
- si garantisce la qualità;
- si governano le modifiche.

Il processo software segue un ciclo di vita articolato in stadi e fasi.

### Def ciclo di vita
Il **ciclo di vita del software** è l'intervallo di tempo compreso tra l'istante in cui nasce l'esigenza di costruire un prodotto software e l'istante in cui il prodotto viene dismesso.

Il ciclo di vita è articolato in tre stadi:
- **sviluppo**;
- **manutenzione**;
- **dismissione**.

Nello stadio di sviluppo si distinguono due tipi di fasi:
- **fasi di definizione**
    - riguardano *che cosa* il software deve fornire;
    - comprendono:
        - definizione dei requisiti;
        - produzione delle specifiche.
- **fasi di produzione**
    - definiscono *come* realizzare quanto stabilito nelle fasi di definizione;
    - comprendono:
        - progettazione del software;
        - codifica;
        - integrazione;
        - rilascio al cliente.

Nel complesso, il ciclo di vita include:
- definizione dei requisiti;
- specifica;
- pianificazione;
- progetto preliminare;
- progetto dettagliato;
- codifica;
- integrazione;
- *testing*;
- uso;
- manutenzione;
- dismissione.

Le fasi possono sovrapporsi ed essere eseguite in modo iterativo. Durante **ogni fase** viene effettuato il *testing* di ciò che è stato prodotto attraverso tecniche di *Verification & Validation* (V&V) sui prodotti intermedi e sul prodotto finale.

### Manutenzione
Lo stadio di manutenzione supporta il software già realizzato e può comprendere al proprio interno fasi di definizione e di produzione.

| Tipo | Scopo |
| --- | --- |
| **correttiva** | eliminare i *fault* che producono *failure* del software |
| **adattativa** | adattare il software ai cambiamenti dell'ambiente operativo per cui è stato sviluppato |
| **perfettiva** | estendere il software per accomodare funzionalità aggiuntive |
| **preventiva** | effettuare modifiche che rendano più semplici correzioni, adattamenti e migliorie (indicata anche come *software reengineering*) |

>[!question]- Si descrivano i tre stadi del ciclo di vita del software e la distinzione interna allo sviluppo.
> >[!done]- la risposta
> > Il ciclo di vita comprende sviluppo, manutenzione e dismissione. Nello sviluppo si distinguono fasi di definizione, che stabiliscono che cosa il software deve fornire attraverso requisiti e specifiche, e fasi di produzione, che stabiliscono come realizzarlo attraverso progettazione, codifica, integrazione e rilascio.

### Def modello del ciclo di vita
Il **modello del ciclo di vita del software** specifica la serie di fasi attraverso cui il prodotto software progredisce, l'ordine con cui tali fasi devono essere eseguite e il percorso dalla definizione dei requisiti fino alla dismissione. La scelta del modello dipende da natura dell'applicazione, maturità dell'organizzazione, metodi e tecnologie utilizzati ed eventuali vincoli imposti dal cliente.

L'assenza di un modello di ciclo di vita corrisponde alla modalità **Build & Fix** (*Fix-it-later*):
- il prodotto software viene sviluppato;
- successivamente viene rilavorato;
- la rilavorazione continua fino a soddisfare le necessità del cliente.

![[assets/d234c4c9_p5_i2.png|500]]

### Modello Waterfall
**Waterfall** è il modello sequenziale classico.

![[assets/d234c4c9_p7_i1.png|500]] Il materiale lo associa a una forte integrazione di *Verification & Validation* in ogni passaggio, anche se le fasi specifiche non vengono analizzate in dettaglio.

![[assets/d234c4c9_p6_i1.png|600]]

### Def software prototyping
Il ***software prototyping*** consiste nello sviluppo rapido di software con lo scopo di elicitare e validare i requisiti, aiutando clienti e sviluppatori a comprendere meglio le reali necessità del sistema.

![[assets/d234c4c9_p12_i1.png|500]]

![[assets/d234c4c9_p8_i1.png|500]]

Il prototipo interviene in due attività legate ai requisiti:
- *requirements elicitation*
    - gli utenti possono sperimentare direttamente con il prototipo per osservare come supporta il loro lavoro.
- *requirements validation*
    - il prototipo può rendere visibili errori e omissioni nei requisiti.

Il *prototyping* è quindi un'attività di **riduzione del rischio**, in particolare per i rischi legati ai requisiti.

L'impiego dei prototipi può:
- rendere visibili i fraintendimenti tra utenti e sviluppatori;
- permettere di individuare servizi mancanti o confusi;
- rendere disponibile un sistema funzionante già nelle prime fasi del processo;
- fornire una base da cui derivare una specifica software;
- supportare il *training* degli utenti e il *testing* del prodotto.

Tuttavia, usare un prototipo come base per una specifica presenta dei limiti:
- alcune parti dei requisiti (es. *safety-critical*) possono essere impossibili da prototipare e rischiano di non comparire nella specifica;
- un'implementazione non ha valore legale come contratto;
- i *non-functional requirements* non possono essere testati adeguatamente.

>[!question]- Qual è lo scopo del software prototyping e come può aiutare nella gestione dei requisiti?
> >[!done]- la risposta
> > Il software prototyping consiste nello sviluppo rapido di software per elicitare o validare i requisiti. Durante la requirements elicitation permette agli utenti di sperimentare il sistema, mentre durante la requirements validation può far emergere errori e omissioni. Per questo viene considerato anche un'attività di riduzione del rischio legato ai requisiti.

### Def Throw-away Prototyping
Nel **Throw-away Prototyping** viene realizzato un prototipo pratico per aiutare a individuare problemi nei requisiti. Il flusso fondamentale è:
1. si parte da un requisito iniziale;
2. si sviluppa il *throw-away prototype*;
3. il prototipo viene consegnato per la sperimentazione;
4. dopo la sperimentazione viene scartato;
5. il prodotto viene sviluppato tramite un altro processo di sviluppo.

![[assets/d234c4c9_p15_i3.png|600]]

Il *throw-away prototype* **non deve essere considerato un prodotto finale**. Nel prototipo:
- alcune caratteristiche del prodotto possono essere state omesse;
- non esiste una specifica per la manutenzione a lungo termine;
- la struttura sarà scarsamente organizzata e difficile da mantenere.
- può essere impossibile adattarlo ai *non-functional requirements*;
- è privo di documentazione;
- potrebbero non essere stati applicati i normali standard di qualità.

>[!warning]
> *Throw-away* significa che il prototipo va scartato: il fatto che sia funzionante non lo rende adatto a diventare il prodotto finale.

>[!question]- Si descriva il Throw-away Prototyping e si spieghi perché il prototipo non dovrebbe essere consegnato come prodotto finale.
> >[!done]- la risposta
> > Nel Throw-away Prototyping si sviluppa rapidamente un prototipo a partire da un requisito iniziale per sperimentare e individuare problemi nei requisiti. Il prototipo viene poi scartato. Non dovrebbe diventare il prodotto finale perché può essere incompleto, privo di documentazione, difficile da mantenere e non conforme ai requisiti non funzionali.

### Rapid e Visual Programming
Per i prototipi, la rapidità di sviluppo è essenziale e può richiedere compromessi come l'omissione di funzionalità o il rilassamento di vincoli non funzionali. Il *visual programming* è indicato come parte intrinseca della maggior parte dei metodi di sviluppo di prototipi.

Linguaggi di *scripting* supportano il *visual programming*, in cui il prototipo viene costruito:
1. creando una *user interface* a partire da elementi standard;
2. associando componenti a questi elementi.

Questo sviluppo è supportato da una vasta libreria di componenti adattabili.
![[assets/d234c4c9_p19_i1.png|500]]

Limiti dello sviluppo visuale:
- rende difficile coordinare uno sviluppo basato su team;
- non presenta un'architettura software esplicita;
- dipendenze complesse tra parti del programma possono creare problemi di *maintainability*.

>[!question]- Qual è il ruolo del Visual Programming nello sviluppo dei prototipi e quali problemi può introdurre?
> >[!done]- la risposta
> > Il visual programming permette di costruire rapidamente prototipi creando una user interface da elementi standard e associandovi componenti. Può però rendere difficile il coordinamento del team, non fornire un'architettura software esplicita e creare problemi di maintainability a causa di dipendenze complesse.

## Sviluppo Iterativo e Modello a Spirale

### Process Iteration
Nei progetti software grandi i requisiti evolvono durante il progetto. Per questo la ***process iteration***, la rielaborazione di stadi già affrontati, fa parte del processo. Può essere applicata a qualsiasi modello generico e permette di tornare su stadi precedenti attraverso due approcci: **Incremental Development** e **Spiral Development**.

### Def Incremental Development
Nel **Modello Incrementale** il prodotto viene sviluppato e consegnato attraverso *increment* (*build*) successivi, dopo aver stabilito (oppure no) un'architettura complessiva. Gli utenti possono sperimentare gli incrementi già consegnati mentre il resto del prodotto è in sviluppo, agendo così anche come *prototype*.

Combina i vantaggi del *prototyping* con un processo gestibile ed è efficace quando il cliente vuole verificare continuamente l'avanzamento o se i requisiti cambiano.

Il modello può avere due versioni:
1. **con architettura complessiva** (stabilita prima dei build);
2. **senza architettura complessiva** (più rischioso).

![[assets/d234c4c9_p26_i2.png|600]]

![[assets/d234c4c9_p23_i1.png|600]]

>[!question]- Si descriva il modello incrementale e si spieghi in quali situazioni risulta efficace.
> >[!done]- la risposta
> > Nel modello incrementale il prodotto viene sviluppato e consegnato attraverso incrementi successivi. Gli utenti possono sperimentare gli incrementi disponibili mentre il resto è in sviluppo, combinando i vantaggi del prototyping con un processo strutturato. È efficace quando il cliente vuole verificare l'avanzamento regolarmente e i requisiti possono cambiare.

### Modello Incrementale vs Waterfall

| Aspetto | Waterfall | Modello Incrementale |
| --- | --- | --- |
| *client feedback* | avviene solo dopo la conclusione dello sviluppo | è continuo durante lo sviluppo |
| fasi | strettamente sequenziali | possono essere condotte in parallelo |
| *detailed design* e *coding* | riguardano l'intero prodotto | vengono svolti sui singoli *build* |
| team di sviluppo | un team di grandi dimensioni | più team di piccole dimensioni |
| requisiti | vengono congelati dopo la fase di specifica | vengono divisi in classi di priorità e sono modificabili |

>[!question]- Si confrontino Waterfall e Modello Incrementale.
> >[!done]- la risposta
> > Nel Waterfall il feedback arriva alla fine, le fasi sono sequenziali, design e coding riguardano l'intero prodotto e i requisiti vengono congelati.

![[assets/d234c4c9_p28_i0.png|600]]

![[assets/d234c4c9_p24_i0.png|600]] Nel modello incrementale il feedback è continuo, le fasi in parallelo, design e coding lavorano sui singoli build e i requisiti sono prioritizzati e modificabili.

### Modello a Spirale
Il **Modello a Spirale** è il secondo approccio di *process iteration*. È presentato in due versioni:
- **versione semplificata** (lineare);

![[assets/d234c4c9_p31_i1.png|500]]
- **versione completa a spirale** (*full-spiral version*, Boehm 1988).

![[assets/d234c4c9_p32_i1.png|600]]

![[assets/d234c4c9_p30_i1.png|400]]

![[assets/d234c4c9_p29_i1.png|500]]

### Risk Management
Il ***risk management*** riguarda l'identificazione dei rischi (circostanze avverse) e la definizione di piani per minimizzare il loro effetto.

I rischi si classificano in:
| Categoria | Effetto |
| --- | --- |
| *project risks* | influenzano la pianificazione temporale o le risorse |
| *product risks* | influenzano la qualità o le prestazioni del prodotto |
| *business risks* | influenzano l'organizzazione |

Il processo si articola in quattro attività:
1. **risk identification**: individuare i rischi (*technology, people, organizational, tools, requirements, estimation risks*).
2. **risk analysis**: valutare ogni rischio per probabilità (da *very low* a *very high*) e serietà (*catastrophic, serious, tolerable, insignificant*).
3. **risk planning**: sviluppare *avoidance strategies*, *minimization strategies* e *contingency plans*.
4. **risk monitoring**: controllare regolarmente l'evoluzione di probabilità ed effetti dei rischi.

![[assets/d234c4c9_p36_i1.png|600]]

>[!question]- Si descriva il processo di Risk Management e la classificazione dei rischi.
> >[!done]- la risposta
> > Il processo comprende identification (individuare i rischi), analysis (valutare probabilità e serietà), planning (creare strategie di evitamento, minimizzazione e contingenza) e monitoring (controllo continuo). I rischi si classificano in project risks, product risks e business risks.

### Altri modelli iterativi
Il **Simultaneous / Concurrent Engineering** mira a ridurre tempo e costo di sviluppo attraverso un approccio sistematico al design integrato e concorrente. Le fasi coesistono e non sono puramente sequenziali.

![[assets/d234c4c9_p46_i6.png|500]]

Il **Formal Methods Model** (es. *Cleanroom Software Engineering*, 1987) usa una specifica matematica formale del software per eliminare l'ambiguità e facilitare la verifica dei programmi.

>[!question]- Cos'è il Concurrent Engineering e cos'è il Formal Methods Model?
> >[!done]- la risposta
> > Il Concurrent Engineering fa coesistere le fasi per ridurre tempi e costi tramite design integrato e concorrente. Il Formal Methods Model usa specifiche matematiche formali per eliminare le ambiguità e facilitare la verifica (es. Cleanroom).

## Metodologie Agile e Scrum

### Metodi Agile
Negli anni 2000, come reazione ai processi troppo restrittivi, è emerso l'approccio **Agile**: non un singolo modello, ma un insieme di principi che guidano flessibilità, collaborazione e consegna rapida di valore.

Include:
- comunicazione intensiva;
- feedback rapido dei clienti;
- autonomia dei team con poche regole esterne.

### L'Agile Manifesto
L'**Agile Manifesto** (2001) pone maggiore importanza su 4 valori rispetto ai loro corrispettivi tradizionali:
1. **Individui e interazioni** più di *processi e strumenti*.
2. **Software funzionante** più di *documentazione esaustiva*.
3. **Collaborazione col cliente** più di *negoziazione contrattuale*.
4. **Risposta al cambiamento** più di *seguire un piano*.

Contiene anche 12 principi pratici orientati alla consegna continua e all'accettazione del cambiamento.

### Scrum
**Scrum** è un framework Agile leggero e iterativo per gestire progetti complessi e consegnare valore in modo iterativo e incrementale.

I tre ruoli fondamentali sono:
- **Scrum Master**: assicura la corretta implementazione della metodologia e rimuove gli ostacoli.
- **Product Owner**: prioritizza i requisiti nel *Product Backlog*.
- **Development Team**: responsabile dello sviluppo e di produrre gli incrementi funzionanti.

![[assets/4f64ac69_p7_i1.png|600]]

Artefatti principali:
- **Product Backlog**: lista prioritizzata di funzionalità future.
- **Sprint Backlog**: elementi selezionati per lo sprint corrente.
- **Incremento**: risultato funzionante del lavoro dello sprint.

Eventi di uno **Sprint** (ciclo tipico 2-4 settimane):
1. **Sprint Planning**: selezione elementi.
2. **Daily Scrum**: *stand-up meeting* giornaliero.
3. **Sprint Review**: presentazione dell'incremento agli stakeholder.
4. **Sprint Retrospective**: pianificazione di miglioramenti nel processo lavorativo.

Scrum richiede una **Definition of Done (DoD)** per garantire alta qualità prima di integrare un work item (es. test superati, documentazione adeguata, nessuna rottura dell'integrazione).

### User Stories ed Epiche
Le **User Stories** descrivono un requisito utente dal suo punto di vista.
- *Template*: `As a <role>, I want <goal> so that <benefit>`.
- *Esempio*: As a user, I want to see a map so that I can find the way.

Le **Epics** sono storie utente molto grandi e complesse, da suddividere in storie più piccole durante lo sviluppo.

## Modelli Corporate (Microsoft, Netscape)

## Modello Microsoft — Synchronize-and-Stabilize

Dalla metà degli anni '80 Microsoft sviluppa un processo *iterative*, *incremental* e *concurrent* con l'obiettivo di:
- aumentare la qualità del software;
- ridurre tempi e costi;
- valorizzare la creatività.

L'approccio è noto come **Synchronize-and-Stabilize**.

![[assets/d234c4c9_p58_i9.png|600]]

### Principio di funzionamento

Il modello si basa su due idee centrali:

- **synchronization**
    - avviene quotidianamente;
    - utilizza *daily build*;
    - coinvolge team da 3 a 8 persone;
- **stabilization**
    - avviene periodicamente;
    - il prodotto viene stabilizzato in incrementi successivi;
    - ogni incremento corrisponde a una *milestone*;
    - la stabilizzazione non viene rimandata a un'unica fase finale.

Il ciclo di sviluppo è diviso in tre fasi:

1. **Planning**
2. **Development**
3. **Stabilization**

![[assets/d234c4c9_p53_i1.png|500]]

![[assets/d234c4c9_p57_i1.png|500]]

>[!question]- In cosa consiste il modello Microsoft Synchronize-and-Stabilize?
> >[!done]- la risposta
> > È un processo iterativo, incrementale e concorrente basato sulla sincronizzazione quotidiana tramite daily build e sulla stabilizzazione periodica del prodotto attraverso milestone successive. Il ciclo di sviluppo è diviso in Planning, Development e Stabilization.

## Strategie e principi del modello Microsoft

### Strategia per prodotto e processo

La creatività viene considerata un elemento essenziale.

I principi associati sono:
- dividere il progetto in 3-4 *milestone*;
- definire:
    - una *product vision*;
    - una specifica funzionale che evolve durante il progetto;
- selezionare funzionalità e priorità in base alle necessità dell'utente;
- definire un'architettura modulare per replicare la struttura del prodotto;
- assegnare task elementari;
- limitare le risorse.

### Strategia per lo sviluppo

Lo sviluppo procede in parallelo con sincronizzazioni frequenti.

I principi sono:
- definire team paralleli;
- utilizzare *daily build*;
- avere sempre un prodotto consegnabile;
    - con versioni per ogni piattaforma;
- testare continuamente il prodotto;
- utilizzare metriche a supporto delle decisioni.

>[!question]- Quali sono i principali principi organizzativi del modello Microsoft?
> >[!done]- la risposta
> > Il progetto viene diviso in 3-4 milestone, con una product vision e una specifica funzionale evolutiva. Le funzionalità vengono prioritarizzate in base alle necessità dell'utente, si usa un'architettura modulare, si assegnano task elementari e si limitano le risorse. Lo sviluppo avviene con team paralleli, daily build, testing continuo e metriche a supporto delle decisioni.

## Modello Netscape

Netscape adotta un modello **Synchronize-and-Stabilize** adattato allo sviluppo di applicazioni Internet.

### Organizzazione dello sviluppo

Lo staffing prevede in media:
- 1 *tester* ogni 3 sviluppatori.

Nonostante questa organizzazione, la produttività rimane comparabile a quella di Microsoft.

### Pianificazione e documentazione

Il processo presenta:
- scarso effort di pianificazione;
    - con eccezione dei server;
- documentazione incompleta.

### Controllo del progetto

Sono presenti:
- scarso controllo sull'avanzamento;
    - affidato soprattutto all'esperienza dei *project manager*;
- scarso controllo sulla *code review*;
- pochi dati storici a supporto delle decisioni.

>[!question]- Quali caratteristiche distinguono il modello Netscape?
> >[!done]- la risposta
> > Netscape usa un modello Synchronize-and-Stabilize adattato alle applicazioni Internet.

![[assets/d234c4c9_p59_i1.png|600]] Ha in media un tester ogni tre sviluppatori, poco effort di pianificazione salvo sui server, documentazione incompleta, scarso controllo su avanzamento e code review e pochi dati storici per supportare le decisioni.

## Capability Maturity Model (CMM)

## Def Capability Maturity Model

Il **Capability Maturity Model (CMM)** è un modello introdotto dal **SEI** (*Software Engineering Institute*) a partire dal 1993 per determinare il livello di maturità del processo software di un'organizzazione.

Il livello di maturità misura l'efficacia globale con cui vengono applicate le tecniche di *software engineering*.

Il modello si basa su:
- un questionario;
- una valutazione articolata in **5 livelli**.

I livelli sono cumulativi:
- ogni livello comprende anche tutte le caratteristiche definite per i livelli precedenti.

>[!question]- Che cos'è il Capability Maturity Model e che cosa misura?
> >[!done]- la risposta
> > Il CMM è un modello introdotto dal Software Engineering Institute a partire dal 1993 per determinare la maturità del processo software di un'organizzazione. La maturità misura l'efficacia globale nell'applicazione delle tecniche di software engineering. La valutazione usa un questionario e cinque livelli cumulativi.

## I 5 livelli del CMM

### Livello 1 — Initial

Il **Level 1 — Initial** è caratterizzato da un processo *ad hoc*:
- il successo dipende dagli "*heroes*".

### Livello 2 — Repeatable

Il **Level 2 — Repeatable** introduce il *basic project management*.

Il risultato è:
- supervisione gestionale;
- tracciamento del progetto;
- pianificazione stabile;
- *product baselines* stabili.

### Livello 3 — Defined

Il **Level 3 — Defined** introduce la definizione del processo.

Il risultato è un processo software:
- definito;
- istituzionalizzato;
- orientato al controllo della qualità del prodotto.

### Livello 4 — Managed

Il **Level 4 — Managed** si concentra sulla misurazione del processo.

Il risultato è:
- pianificazione della qualità del prodotto;
- tracciamento del processo software misurato.

### Livello 5 — Optimizing

Il **Level 5 — Optimizing** punta a:
- controllo del processo;
- miglioramento del processo.

Il risultato è il miglioramento continuo della capacità del processo.

| Livello | Nome | Focus principale | Risultato |
| --- | --- | --- | --- |
| 1 | Initial | processo *ad hoc* | successo dipendente dagli "*heroes*" |
| 2 | Repeatable | *basic project management* | supervisione, tracking, pianificazione e baseline stabili |
| 3 | Defined | definizione del processo | processo definito e istituzionalizzato per il controllo della qualità |
| 4 | Managed | misurazione del processo | pianificazione della qualità e tracking del processo misurato |
| 5 | Optimizing | controllo e miglioramento | miglioramento continuo della capacità del processo |

>[!question]- Si descrivano i cinque livelli del CMM.
> >[!done]- la risposta
> > Il Level 1 Initial è ad hoc e dipende dagli heroes. Il Level 2 Repeatable introduce il basic project management con pianificazione e baseline stabili. Il Level 3 Defined definisce e istituzionalizza il processo. Il Level 4 Managed misura il processo e ne traccia qualità e andamento. Il Level 5 Optimizing punta al controllo e al miglioramento continuo della capacità del processo.

## Key Process Areas

### Def KPA

Il CMM associa a ciascun livello di maturità alcune **Key Process Areas (KPA)**, scelte tra **18 KPA definite**.

Le KPA descrivono le funzioni che devono essere presenti per garantire l'appartenenza a un determinato livello.

Ogni KPA viene descritta rispetto a:
- obiettivi;
- impegni e responsabilità da assumere;
- capacità e risorse necessarie;
- attività da implementare;
- metodi per monitorarne l'implementazione;
- metodi per verificarne l'implementazione.

### KPA del Level 2

Le KPA del **Level 2 — Repeatable** sono:
- *Requirements management*;
- *Software project planning*;
- *Software project tracking & oversight*;
- *Software subcontract management*;
- *Software quality assurance*;
- *Software configuration management*.

### KPA del Level 3

Le KPA del **Level 3 — Defined** sono:
- *Organization process focus*;
- *Organization process definition*;
- *Training program*;
- *Integrated software management*;
- *Software product engineering*;
- *Intergroup coordination*;
- *Peer reviews*.

### KPA del Level 4

Le KPA del **Level 4 — Managed** sono:
- *Quantitative process management*;
- *Software quality management*.

### KPA del Level 5

Le KPA del **Level 5 — Optimizing** sono:
- *Defect prevention*;
- *Technology change management*;
- *Process change management*.

![[assets/4f64ac69_p15_i1.png|500]]

>[!question]- Che cosa sono le Key Process Areas nel CMM?
> >[!done]- la risposta
> > Le KPA sono le funzioni richieste per garantire l'appartenenza a un determinato livello di maturità. Il CMM ne definisce 18 complessive e le associa ai diversi livelli. Ogni KPA specifica obiettivi, responsabilità, capacità e risorse necessarie, attività, modalità di monitoraggio e modalità di verifica.

## Statistiche di adozione del CMM

### Situazione a febbraio 2000

A febbraio 2000 risultavano organizzazioni ad alta maturità sia negli USA sia fuori dagli USA.

Negli **USA**:
- 71 organizzazioni complessive:
    - 44 al Level 4;
    - 27 al Level 5.

Fuori dagli **USA**:
- 25 organizzazioni complessive:
    - Australia:
        - 1 al Level 4;
    - India:
        - 14 al Level 4;
        - 10 al Level 5.

### Aggiornamenti al giugno 2015

Le tendenze e il numero di *appraisal* per paese risultano aggiornati a giugno 2015.

![[assets/4f64ac69_p17_i1.png|500]]

![[assets/4f64ac69_p18_i1.png|500]]

>[!question]- Quali dati di adozione del CMM vengono riportati?
> >[!done]- la risposta
> > A febbraio 2000 risultavano 71 organizzazioni ad alta maturità negli USA, di cui 44 al Level 4 e 27 al Level 5. Fuori dagli USA erano 25: una organizzazione australiana al Level 4 e, in India, 14 al Level 4 e 10 al Level 5. Le tendenze e gli appraisal per paese sono inoltre aggiornati al giugno 2015.
