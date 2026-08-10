# Modelli di processo software: sequenziali e iterativi

## Processo software

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

Il processo software segue un **ciclo di vita** articolato in stadi e fasi.

## Ciclo di vita del software

### Def ciclo di vita

Il **ciclo di vita del software** è l'intervallo di tempo compreso tra:
1. l'istante in cui nasce l'esigenza di costruire un prodotto software;
2. l'istante in cui il prodotto viene dismesso.

Il ciclo di vita è articolato in tre stadi:
- **sviluppo**;
- **manutenzione**;
- **dismissione**.

### Stadio di sviluppo

Nello sviluppo si distinguono due tipi di fasi:

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

### Fasi comprese nel ciclo di vita

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

Le fasi:
- possono sovrapporsi;
- possono essere eseguite in modo iterativo.

### Verification & Validation

Durante **ogni fase** viene effettuato il *testing* di ciò che è stato prodotto attraverso tecniche di ***Verification & Validation*** (V&V):
- sui prodotti intermedi;
- sul prodotto finale.

Il materiale associa inoltre al modello Waterfall una sezione specifica dedicata alla V&V.

![[assets/d234c4c9_p3_i0.png]]

## Manutenzione

Lo stadio di manutenzione supporta il software già realizzato e può comprendere al proprio interno:
- fasi di definizione;
- fasi di produzione.

### Tipi di manutenzione

| Tipo | Scopo |
| --- | --- |
| **correttiva** | eliminare i *fault* che producono *failure* del software |
| **adattativa** | adattare il software ai cambiamenti dell'ambiente operativo per cui è stato sviluppato |
| **perfettiva** | estendere il software per accomodare funzionalità aggiuntive |
| **preventiva** | effettuare modifiche che rendano più semplici correzioni, adattamenti e migliorie |

La manutenzione preventiva è indicata anche come ***software reengineering***.

>[!question]- Si descrivano i tre stadi del ciclo di vita del software e la distinzione interna allo sviluppo.
> >[!done]- la risposta
> > Il ciclo di vita comprende sviluppo, manutenzione e dismissione. Nello sviluppo si distinguono fasi di definizione, che stabiliscono che cosa il software deve fornire attraverso requisiti e specifiche, e fasi di produzione, che stabiliscono come realizzarlo attraverso progettazione, codifica, integrazione e rilascio.

## Modelli di ciclo di vita

### Def modello del ciclo di vita

Il **modello del ciclo di vita del software** specifica:
- la serie di fasi attraverso cui il prodotto software progredisce;
- l'ordine con cui tali fasi devono essere eseguite;
- il percorso dalla definizione dei requisiti fino alla dismissione.

La scelta del modello dipende da:
- natura dell'applicazione;
- maturità dell'organizzazione;
- metodi utilizzati;
- tecnologie utilizzate;
- eventuali vincoli imposti dal cliente.

## Build & Fix

L'assenza di un modello di ciclo di vita corrisponde alla modalità **Build & Fix**, detta anche *Fix-it-later*:
- il prodotto software viene sviluppato;
- successivamente viene rilavorato;
- la rilavorazione continua fino a soddisfare le necessità del cliente.

*Build & Fix* rappresenta quindi il caso in cui lo sviluppo avviene senza un modello di ciclo di vita.

![[assets/d234c4c9_p4_i0.png]]

## Modello Waterfall

**Waterfall** è un modello di ciclo di vita caratterizzato, nel confronto con lo sviluppo incrementale, da un'organizzazione strettamente sequenziale delle fasi.

Nel Waterfall:
- il *client feedback* avviene solo dopo la conclusione dello sviluppo;
- le fasi sono strettamente sequenziali;
- *detailed design* e *coding* riguardano l'intero prodotto;
- opera un team di sviluppo di grandi dimensioni;
- i requisiti vengono congelati dopo la fase di specifica.

![[assets/d234c4c9_p6_i0.png]]

>[!warning]
> Il materiale disponibile permette di ricavare queste caratteristiche dal confronto con il modello incrementale, ma non fornisce una descrizione testuale completa della sequenza interna delle fasi del Waterfall.

## Software Prototyping

### Def software prototyping

Il ***software prototyping*** consiste nello sviluppo rapido di software con lo scopo di:
- elicitare i requisiti;
- validare i requisiti.

L'utilizzo principale dei *system prototypes* è aiutare:
- clienti;
- sviluppatori;

a comprendere meglio i requisiti software.

![[assets/d234c4c9_p9_i0.png]]

### Prototyping e requisiti

Il prototipo interviene in due attività legate ai requisiti:

- ***requirements elicitation***
    - gli utenti possono sperimentare direttamente con il prototipo;
    - possono osservare come il sistema supporta il loro lavoro.
- ***requirements validation***
    - il prototipo può rendere visibili:
        - errori nei requisiti;
        - omissioni nei requisiti.

Il *prototyping* può quindi essere considerato un'attività di **riduzione del rischio**:
- in particolare riduce i rischi legati ai requisiti.

### Benefici del Prototyping

L'impiego dei prototipi può:
- rendere visibili i fraintendimenti tra utenti e sviluppatori;
- permettere di individuare:
    - servizi mancanti;
    - servizi confusi;
- rendere disponibile un sistema funzionante già nelle prime fasi del processo;
- fornire una base da cui derivare una specifica software;
- supportare:
    - *training* degli utenti;
    - *testing* del prodotto.

### Limiti del prototipo come specifica

Usare un prototipo come base per una specifica presenta dei limiti:

- alcune parti dei requisiti possono essere impossibili da prototipare;
    - per esempio funzioni *safety-critical*;
    - queste parti rischiano quindi di non comparire nella specifica derivata dal prototipo;
- un'implementazione non ha valore legale come contratto;
- i *non-functional requirements* non possono essere testati adeguatamente in un prototipo software.

>[!question]- Qual è lo scopo del software prototyping e come può aiutare nella gestione dei requisiti?
> >[!done]- la risposta
> > Il software prototyping consiste nello sviluppo rapido di software per elicitare o validare i requisiti. Durante la requirements elicitation permette agli utenti di sperimentare il sistema, mentre durante la requirements validation può far emergere errori e omissioni. Per questo viene considerato anche un'attività di riduzione del rischio legato ai requisiti.

## Throw-away Prototyping

### Def Throw-away Prototyping

Nel **Throw-away Prototyping** viene realizzato un prototipo, solitamente un'implementazione pratica del prodotto, per aiutare a individuare problemi nei requisiti.

Il flusso fondamentale è:
1. si parte da un requisito iniziale;
2. si sviluppa il *throw-away prototype*;
3. il prototipo viene consegnato per la sperimentazione;
4. dopo la sperimentazione viene scartato;
5. il prodotto viene sviluppato tramite un altro processo di sviluppo.

Il suo obiettivo è ridurre il rischio legato ai requisiti.

![[assets/d234c4c9_p14_i0.png]]

### Il prototipo non è il prodotto finale

Il *throw-away prototype* **non deve essere considerato un prodotto finale**.

Nel prototipo:
- alcune caratteristiche del prodotto possono essere state omesse;
- non esiste una specifica per la manutenzione a lungo termine;
- la struttura sarà scarsamente organizzata e difficile da mantenere.

Durante lo sviluppo possono esserci pressioni affinché il prototipo venga consegnato come prodotto finale, ma questa scelta non è raccomandata.

I problemi indicati sono:
- può essere impossibile adattarlo per soddisfare i *non-functional requirements*;
- è inevitabilmente privo di documentazione;
- la sua struttura viene degradata dalle modifiche effettuate durante lo sviluppo;
- potrebbero non essere stati applicati i normali standard di qualità dell'organizzazione.

>[!warning]
> *Throw-away* significa che il prototipo va effettivamente scartato: il fatto che sia funzionante non lo rende automaticamente adatto a diventare il prodotto finale.

>[!question]- Si descriva il Throw-away Prototyping e si spieghi perché il prototipo non dovrebbe essere consegnato come prodotto finale.
> >[!done]- la risposta
> > Nel Throw-away Prototyping si sviluppa rapidamente un prototipo a partire da un requisito iniziale per sperimentare e individuare problemi nei requisiti. Il prototipo viene poi scartato e il prodotto viene costruito con un altro processo. Non dovrebbe diventare il prodotto finale perché può essere incompleto, privo di documentazione, difficile da mantenere, degradato dalle modifiche e non conforme ai normali standard di qualità o ai requisiti non funzionali.

## Rapid Prototyping

Un prototipo può essere usato per fornire agli *end-user* un'impressione concreta delle capacità del prodotto.

Il *prototyping*:
- viene utilizzato in misura crescente nei prodotti in cui lo sviluppo rapido è essenziale;
- nel caso *throw-away* viene usato per comprendere i requisiti del prodotto.

Per i prototipi, la rapidità di sviluppo è essenziale.

Questa rapidità può richiedere compromessi:
- omissione di alcune funzionalità;
- rilassamento di alcuni vincoli non funzionali.

Il *visual programming* è indicato come parte intrinseca della maggior parte dei metodi di sviluppo di prototipi.

![[assets/d234c4c9_p17_i0.png]]

## Visual Programming per il Prototyping

### Costruzione del prototipo

Linguaggi di *scripting* come Visual Basic supportano il ***visual programming***.

Nel visual programming il prototipo viene costruito:
1. creando una *user interface* a partire da elementi standard;
2. associando dei componenti a questi elementi.

Lo sviluppo è supportato da:
- una vasta libreria di componenti;
- possibilità di adattare i componenti ai requisiti specifici dell'applicazione.

![[assets/d234c4c9_p18_i0.png]]

### Limiti dello sviluppo visuale

Lo sviluppo visuale presenta alcuni problemi:
- rende difficile coordinare uno sviluppo basato su team;
- non presenta un'architettura software esplicita;
- dipendenze complesse tra parti del programma possono creare problemi di *maintainability*.

>[!question]- Qual è il ruolo del Visual Programming nello sviluppo dei prototipi e quali problemi può introdurre?
> >[!done]- la risposta
> > Il visual programming permette di costruire rapidamente prototipi creando una user interface da elementi standard e associandovi componenti, disponibili tramite apposite librerie e adattabili ai requisiti dell'applicazione. Può però rendere difficile il coordinamento del lavoro di team, non fornire un'architettura software esplicita e creare problemi di maintainability a causa di dipendenze complesse tra le parti del programma.

# Sviluppo iterativo

## Process Iteration

### Perché il processo viene iterato

Nei progetti software di grandi dimensioni i requisiti evolvono durante il progetto.

Per questo la ***process iteration*** consiste nella rielaborazione di stadi già affrontati e fa parte del processo software.

L'iterazione:
- può essere applicata a qualsiasi modello di processo generico;
- permette di tornare su stadi precedenti e rielaborarli quando necessario;
- può essere realizzata attraverso due approcci collegati:
    - **Incremental Development**;
    - **Spiral Development**.

## Modello Incrementale

### Def Incremental Development

Nel **Modello Incrementale** il prodotto viene sviluppato e consegnato attraverso *increment* successivi, detti anche *build*, dopo aver stabilito un'architettura complessiva.

Il prodotto non viene quindi consegnato tutto insieme:
- viene realizzato attraverso più *build*;
- ogni *build* rappresenta un incremento successivo del prodotto;
- gli utenti possono sperimentare gli incrementi già consegnati mentre il resto del prodotto è ancora in sviluppo.

Gli incrementi consegnati possono agire anche come *prototype*:
- l'utente può provare concretamente quanto già realizzato;
- il resto del prodotto può continuare a essere sviluppato nello stesso periodo.

### Vantaggi e contesto d'uso

Il modello incrementale combina:
- i vantaggi del *prototyping*;
- un processo più gestibile;
- una struttura migliore.

È particolarmente efficace quando:
- il cliente vuole verificare continuamente l'avanzamento;
- i requisiti sono soggetti a modifiche.

### Versioni del modello incrementale

Il modello può essere realizzato in due versioni alternative:

1. **con architettura complessiva**
    - l'architettura generale viene stabilita prima dello sviluppo e della consegna dei successivi *build*;
2. **senza architettura complessiva**
    - lo sviluppo incrementale procede senza una struttura architetturale complessiva già stabilita;
    - questa versione è più rischiosa.

>[!question]- Si descriva il modello incrementale e si spieghi in quali situazioni risulta efficace.
> >[!done]- la risposta
> > Nel modello incrementale il prodotto viene sviluppato e consegnato attraverso incrementi o build successivi. Gli utenti possono sperimentare gli incrementi già disponibili mentre il resto del prodotto è ancora in sviluppo, e questi incrementi possono agire come prototipi. Il modello combina quindi i vantaggi del prototyping con un processo più gestibile e una struttura migliore. È efficace quando il cliente vuole verificare continuamente l'avanzamento e quando i requisiti possono cambiare.

## Modello Incrementale vs Waterfall

Le differenze principali tra **Waterfall** e **Modello Incrementale** riguardano:
- momento in cui entra il feedback del cliente;
- organizzazione delle fasi;
- granularità di *design* e *coding*;
- struttura dei team;
- gestione dei requisiti.

| Aspetto | Waterfall | Modello Incrementale |
| --- | --- | --- |
| *client feedback* | avviene solo dopo la conclusione dello sviluppo | è continuo durante lo sviluppo |
| fasi | strettamente sequenziali | possono essere condotte in parallelo |
| *detailed design* e *coding* | riguardano l'intero prodotto | vengono svolti sui singoli *build* |
| team di sviluppo | un team di grandi dimensioni | più team di piccole dimensioni |
| requisiti | vengono congelati dopo la fase di specifica | vengono divisi in classi di priorità e sono facilmente modificabili |

La differenza sul feedback è particolarmente netta:
- **Waterfall**
    - il cliente fornisce feedback quando lo sviluppo è ormai concluso;
- **Incrementale**
    - il feedback può accompagnare lo sviluppo in modo continuo.

Anche la gestione del lavoro cambia:
- Waterfall:
    - le fasi procedono in sequenza;
    - *detailed design* e *coding* coprono l'intero prodotto;
- Incrementale:
    - le fasi possono procedere in parallelo;
    - *detailed design* e *coding* vengono applicati ai singoli *build*.

>[!question]- Si confrontino Waterfall e Modello Incrementale.
> >[!done]- la risposta
> > Nel Waterfall il feedback del cliente arriva solo alla fine dello sviluppo, le fasi sono strettamente sequenziali, design dettagliato e coding riguardano l'intero prodotto, il team è grande e i requisiti vengono congelati dopo la specifica. Nel modello incrementale il feedback è continuo, le fasi possono essere svolte in parallelo, design e coding lavorano sui singoli build, operano più team piccoli e i requisiti sono organizzati in classi di priorità e facilmente modificabili.

## Modello a Spirale

Il **Modello a Spirale** è uno dei due approcci collegati alla *process iteration*, insieme allo sviluppo incrementale.

Il modello è presentato in due versioni:
- **versione semplificata**
    - lineare;
- **versione completa a spirale**
    - indicata come *full-spiral version*;
    - associata a Boehm, 1988.

>[!question]- Quali versioni del Modello a Spirale vengono presentate?
> >[!done]- la risposta
> > Vengono presentate una versione semplificata, lineare, e una versione completa a spirale, indicata come full-spiral version e associata a Boehm, 1988.

## Risk Management

### Def Risk Management

Il ***risk management*** riguarda:
- l'identificazione dei rischi;
- la definizione di piani per minimizzare il loro effetto sul progetto.

### Def Risk

Un **risk** è la probabilità che si verifichi una circostanza avversa.

I rischi possono essere classificati in tre categorie principali:

| Categoria | Effetto |
| --- | --- |
| *project risks* | influenzano la pianificazione temporale o le risorse |
| *product risks* | influenzano la qualità o le prestazioni del prodotto |
| *business risks* | influenzano l'organizzazione |

### Tipi di rischio

I tipi di rischio comprendono:
- *technology risks*;
- *people risks*;
- *organizational risks*;
- *tools risks*;
- *requirements risks*;
- *estimation risks*.

### Processo di Risk Management

Il processo di *risk management* è composto da quattro attività:

1. **risk identification**
2. **risk analysis**
3. **risk planning**
4. **risk monitoring**

### Risk Identification

La ***risk identification*** consiste nell'identificazione dei rischi che devono essere gestiti.

I rischi individuati diventano l'input delle successive attività di:
- analisi;
- pianificazione;
- monitoraggio.

### Risk Analysis

La ***risk analysis*** valuta ogni rischio lungo due dimensioni:

- **probabilità**
    - può variare da *very low* a *very high*;
- **serietà**
    - può essere:
        - *catastrophic*;
        - *serious*;
        - *tolerable*;
        - *insignificant*.

L'analisi caratterizza quindi il rischio considerando:
- quanto è probabile che si verifichi;
- quanto sarebbero seri i suoi effetti.

### Risk Planning

La ***risk planning*** consiste nello sviluppare, per ciascun rischio:
- *avoidance strategies*;
- *minimization strategies*;
- *contingency plans*.

Queste tre forme di pianificazione affrontano il rischio predisponendo strategie e piani destinati a minimizzarne l'effetto sul progetto.

### Risk Monitoring

Il ***risk monitoring*** controlla regolarmente l'evoluzione dei rischi identificati.

Durante il monitoraggio si valuta:
- se un rischio sta diventando:
    - più probabile;
    - meno probabile;
- se i suoi effetti sono cambiati.

Il monitoraggio non è quindi una valutazione eseguita una sola volta:
- i rischi già individuati vengono riesaminati regolarmente;
- si verifica come cambiano probabilità ed effetti.

>[!question]- Si descriva il processo di Risk Management.
> >[!done]- la risposta
> > Il risk management riguarda l'identificazione dei rischi e la preparazione di piani per minimizzarne gli effetti sul progetto. Il processo comprende risk identification, risk analysis, risk planning e risk monitoring. L'analisi valuta probabilità e serietà dei rischi; il planning predispone avoidance strategies, minimization strategies e contingency plans; il monitoring verifica regolarmente se probabilità ed effetti dei rischi identificati stanno cambiando.

>[!question]- Come vengono classificati e analizzati i rischi?
> >[!done]- la risposta
> > I rischi possono essere project risks, che influenzano schedule o risorse, product risks, che influenzano qualità o performance, e business risks, che influenzano l'organizzazione. La risk analysis valuta per ogni rischio la probabilità, da very low a very high, e la serietà, classificabile come catastrophic, serious, tolerable o insignificant.

## Altri modelli

### Simultaneous / Concurrent Engineering

Il **Simultaneous Engineering**, o **Concurrent Engineering**, mira a ridurre:
- tempo di sviluppo;
- costo di sviluppo.

Lo fa attraverso un approccio sistematico al *design* integrato e concorrente:
- del prodotto software;
- del relativo processo.

La caratteristica strutturale è che:
- le fasi coesistono;
- non vengono eseguite semplicemente in sequenza.

>[!question]- Qual è la differenza fondamentale nell'organizzazione delle fasi del Concurrent Engineering?
> >[!done]- la risposta
> > Nel Concurrent Engineering le fasi coesistono invece di essere eseguite in sequenza. L'approccio mira a ridurre tempo e costo di sviluppo attraverso il design integrato e concorrente del prodotto software e del relativo processo.

### Formal Methods Model

Il **Formal Methods Model** comprende attività che portano a una specifica matematica formale del software.

La specifica formale viene utilizzata per:
- eliminare l'ambiguità;
- facilitare la verifica dei programmi.

Come esempio viene indicato **Cleanroom Software Engineering**, 1987.

>[!question]- Qual è l'obiettivo del Formal Methods Model?
> >[!done]- la risposta
> > Il Formal Methods Model conduce a una specifica matematica formale del software, con l'obiettivo di eliminare l'ambiguità e facilitare la verifica dei programmi. Nel materiale viene indicato come esempio Cleanroom Software Engineering del 1987.