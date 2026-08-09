# Modelli Sequenziali (Waterfall, Prototyping)

## Processo software

### Def processo software
Il **processo software** è la serie di attività necessarie a realizzare un prodotto software:
- nei tempi previsti;
- con i costi previsti;
- con le caratteristiche di qualità desiderate.

All'interno del processo:
- si applicano metodi, tecniche e strumenti;
- si producono prodotti:
    - intermedi;
    - finali;
- si stabilisce il controllo gestionale del progetto;
- si garantisce la qualità;
- si governano le modifiche.

Il processo software segue un ciclo di vita articolato in stadi e fasi.

![[assets/d234c4c9_p0_i0.png|400]]

## Ciclo di vita del software

### Def ciclo di vita
Il **ciclo di vita del software** è l'intervallo di tempo compreso tra:
1. la nascita dell'esigenza di costruire un prodotto software;
2. la dismissione del prodotto.

Il ciclo di vita è articolato in tre stadi:
- **sviluppo**
- **manutenzione**
- **dismissione**

![[assets/d234c4c9_p1_i0.png|500]]

### Stadio di sviluppo

Nello sviluppo si distinguono due tipi di fasi.

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

Nel complesso, il ciclo di vita può comprendere:
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

Durante **ogni fase** viene effettuato il *testing* di ciò che è stato prodotto attraverso tecniche di *Verification & Validation* (V&V):
- sui prodotti intermedi;
- sul prodotto finale.

![[assets/d234c4c9_p3_i0.png|500]]

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

La manutenzione preventiva è indicata anche come *software reengineering*.

![[assets/d234c4c9_p2_i0.png|400]]

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

### Build & Fix

L'assenza di un modello di ciclo di vita corrisponde alla modalità *Build & Fix*, detta anche *Fix-it-later*:
- il prodotto viene sviluppato;
- successivamente viene rilavorato;
- la rilavorazione continua fino a soddisfare le necessità del cliente.

*Build & Fix* si contrappone quindi al caso in cui lo sviluppo segue un vero modello di ciclo di vita.

![[assets/d234c4c9_p4_i0.png|400]]

## Modello Waterfall

**Waterfall** è presentato come un modello nell'ambito dei modelli di ciclo di vita.

Il materiale associa al modello anche una sezione specifica dedicata alla *Verification & Validation* (V&V).

![[assets/d234c4c9_p6_i0.png|500]]

>[!warning]
> Le informazioni testuali disponibili non specificano le caratteristiche del modello Waterfall, la sequenza delle sue fasi o i dettagli della V&V associata. Questi elementi quindi non vengono ricostruiti.

## Software Prototyping

### Def software prototyping
Il *software prototyping* consiste nello sviluppo rapido di software con lo scopo di:
- elicitare i requisiti;
- validare i requisiti.

L'utilizzo principale dei *system prototypes* è aiutare:
- clienti;
- sviluppatori;

a comprendere meglio i requisiti software.

![[assets/d234c4c9_p9_i0.png|500]]

### Prototyping e requisiti

Il prototipo interviene in due attività legate ai requisiti.

- *requirements elicitation*
    - gli utenti possono sperimentare direttamente con il prototipo;
    - possono osservare come il sistema supporta il loro lavoro.
- *requirements validation*
    - il prototipo può rendere visibili:
        - errori nei requisiti;
        - omissioni nei requisiti.

Il *prototyping* può quindi essere considerato un'attività di **riduzione del rischio**:
- in particolare riduce i rischi legati ai requisiti.

![[assets/d234c4c9_p10_i0.png|500]]

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

![[assets/d234c4c9_p11_i0.png|400]]

### Limiti del prototipo come specifica

Usare un prototipo come base per una specifica presenta però dei limiti.

- alcune parti dei requisiti possono essere impossibili da prototipare;
    - per esempio funzioni *safety-critical*;
    - queste parti rischiano quindi di non comparire nella specifica derivata dal prototipo;
- un'implementazione non ha valore legale come contratto;
- i *non-functional requirements* non possono essere testati adeguatamente in un prototipo software.

![[assets/d234c4c9_p13_i0.png|400]]

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

![[assets/d234c4c9_p14_i0.png|500]]

### Il prototipo non è il prodotto finale

Il *throw-away prototype* **non deve essere considerato un prodotto finale**.

Nel prototipo:
- alcune caratteristiche del prodotto possono essere state omesse;
- non esiste una specifica per la manutenzione a lungo termine;
- la struttura sarà scarsamente organizzata e difficile da mantenere.

Durante lo sviluppo possono comunque esserci pressioni affinché il prototipo venga consegnato come prodotto finale, ma questa scelta non è raccomandata.

I problemi indicati sono:
- può essere impossibile adattarlo per soddisfare i *non-functional requirements*;
- è inevitabilmente privo di documentazione;
- la sua struttura viene degradata dalle modifiche effettuate durante lo sviluppo;
- potrebbero non essere stati applicati i normali standard di qualità dell'organizzazione.

![[assets/d234c4c9_p16_i0.png|500]]

>[!warning]
> *Throw-away* significa davvero che il prototipo va scartato: il fatto che sia funzionante non lo rende automaticamente adatto a diventare il prodotto finale.

>[!question]- Si descriva il Throw-away Prototyping e si spieghi perché il prototipo non dovrebbe essere consegnato come prodotto finale.
> >[!done]- la risposta
> > Nel Throw-away Prototyping si sviluppa rapidamente un prototipo a partire da un requisito iniziale per sperimentare e individuare problemi nei requisiti. Il prototipo viene poi scartato e il prodotto viene costruito con un altro processo. Non dovrebbe diventare il prodotto finale perché può essere incompleto, privo di documentazione, difficile da mantenere, degradato dalle modifiche e non conforme ai normali standard di qualità o ai requisiti non funzionali.

## Rapid Prototyping — punti chiave

Un prototipo può essere usato per fornire agli *end-user* un'impressione concreta delle capacità del prodotto.

Il *prototyping*:
- viene utilizzato in misura crescente nei prodotti in cui lo sviluppo rapido è essenziale;
- nel caso *throw-away* viene usato per comprendere i requisiti del prodotto.

Per i prototipi, la rapidità di sviluppo è essenziale.

Questa rapidità può richiedere compromessi:
- omissione di alcune funzionalità;
- rilassamento di alcuni vincoli non funzionali.

Il *visual programming* è indicato come parte intrinseca della maggior parte dei metodi di sviluppo di prototipi.

![[assets/d234c4c9_p17_i0.png|500]]

## Visual Programming per il Prototyping

### Costruzione del prototipo

Linguaggi di *scripting* come Visual Basic supportano il *visual programming*.

Nel visual programming il prototipo viene costruito:
1. creando una *user interface* a partire da elementi standard;
2. associando dei componenti a questi elementi.

Lo sviluppo è supportato da:
- una vasta libreria di componenti;
- possibilità di adattare i componenti ai requisiti specifici dell'applicazione.

![[assets/d234c4c9_p18_i0.png|500]]

### Limiti dello sviluppo visuale

Lo sviluppo visuale presenta alcuni problemi:
- rende difficile coordinare uno sviluppo basato su team;
- non presenta un'architettura software esplicita;
- dipendenze complesse tra parti del programma possono creare problemi di *maintainability*.

![[assets/d234c4c9_p20_i0.png|500]]

>[!question]- Qual è il ruolo del Visual Programming nello sviluppo dei prototipi e quali problemi può introdurre?
> >[!done]- la risposta
> > Il visual programming permette di costruire rapidamente prototipi creando una user interface da elementi standard e associandovi componenti, disponibili tramite apposite librerie e adattabili ai requisiti dell'applicazione. Può però rendere difficile il coordinamento del lavoro di team, non fornire un'architettura software esplicita e creare problemi di maintainability a causa di dipendenze complesse tra le parti del programma.