>[!question]- Quali sono i quattro tipi di manutenzione del software?
> Quali scopi hanno le diverse forme di manutenzione nel ciclo di vita?
> >[!done]- la risposta
> > Sono quattro: **correttiva** (elimina difetti che causano guasti), **adattativa** (adatta a cambiamenti dell'ambiente), **perfettiva** (estende con nuove funzionalità) e **preventiva** (semplifica modifiche future, nota anche come *software reengineering*).

## Il Processo Software

Il **processo software** è la serie di attività necessarie alla realizzazione del prodotto software rispettando i tempi, i costi e le caratteristiche di qualità desiderate.
- si applicano metodi, tecniche e strumenti
- si creano prodotti intermedi e finali
- si stabilisce il controllo gestionale del progetto
- si garantisce la qualità e si governano le modifiche

### Ciclo di vita e fasi
Il **ciclo di vita** è l'intervallo di tempo tra la nascita dell'esigenza di un prodotto e la sua dismissione.
Si articola in tre stadi principali:
1. **Sviluppo**: si distingue in fasi di definizione e fasi di produzione
    - *fasi di definizione*: definiscono cosa il software deve fornire (requisiti e specifiche)
    - *fasi di produzione*: definiscono come realizzarlo (progettazione, codifica, integrazione e rilascio)
2. **Manutenzione**: supporta il software realizzato e può comprendere al proprio interno nuove fasi di definizione o produzione
3. **Dismissione**

![[assets/d234c4c9_p1_i0.png|400]]

> [!tip]
> Le fasi del ciclo di vita possono sovrapporsi o essere eseguite in modo iterativo. Durante ogni fase si applicano tecniche di *verification & validation* (V&V) sia al prodotto finale sia agli artefatti intermedi.

### Tipi di manutenzione
Lo stadio di manutenzione si divide in quattro categorie principali:
- **correttiva**: elimina i difetti (*fault*) che producono guasti (*failure*)
- **adattativa**: adatta il software ai cambiamenti dell'ambiente operativo
- **perfettiva**: estende il software per accomodare funzionalità aggiuntive
- **preventiva** (o *software reengineering*): effettua modifiche per rendere più semplici le correzioni e le migliorie future

## Modelli di Ciclo di Vita

Il **modello del ciclo di vita** specifica le fasi attraverso cui il prodotto progredisce e il loro ordine. La scelta dipende dall'applicazione, dalla maturità dell'organizzazione, dalle tecnologie utilizzate e dai vincoli del cliente.

### Build & Fix
L'assenza di un modello del ciclo di vita corrisponde alla modalità di sviluppo **Build & Fix** (o *fix-it-later*).
- il software viene sviluppato e continuamente rilavorato fino a soddisfare le necessità del cliente

### Modello Waterfall
Il **Waterfall** è uno dei principali modelli di ciclo di vita.
> [!info]
> Questo modello prevede attività di *verification & validation* (V&V) integrate, ma la sequenza formale delle sue fasi non è dettagliata in questi appunti.

## Software Prototyping

Il **software prototyping** consiste nello sviluppo rapido di software per elicitare o validare i requisiti.
- *requirements elicitation*: gli utenti sperimentano con un prototipo per osservare come il sistema supporta il loro lavoro
- *requirements validation*: il prototipo rivela errori e omissioni nei requisiti
- rappresenta un'attività fondamentale per la riduzione del rischio

### Benefici
- rende visibili i fraintendimenti tra utenti e sviluppatori
- permette di individuare servizi mancanti o confusi
- fornisce nelle prime fasi un sistema funzionante (*early working system*) e un'impressione concreta delle capacità
- funge da base per derivare una specifica software e per supportare *training* e *testing*

### Limiti dei prototipi come specifiche
Non tutte le caratteristiche del prodotto possono basarsi sul prototipo:
- parti complesse (es. funzioni *safety-critical*) possono essere impossibili da prototipare e quindi omesse
- un'implementazione non ha valore legale come contratto
- i requisiti non funzionali non possono essere testati adeguatamente

### Throw-away Prototyping
Nel **throw-away prototyping** viene prodotta un'implementazione pratica per aiutare a individuare problemi nei requisiti; il prototipo viene poi **scartato** e il prodotto reale viene sviluppato con un altro processo.
- **Svantaggi e problemi intrinseci**:
    - è scarsamente strutturato e privo di documentazione e specifiche per la manutenzione
    - la struttura è degradata dalle modifiche repentine e mancano standard di qualità
    - è impossibile adattarlo per fargli soddisfare i requisiti non funzionali

> [!warning]
> Spesso gli sviluppatori subiscono pressioni affinché il *throw-away prototype* venga consegnato come prodotto finale. Questa pratica è fortemente sconsigliata a causa dei problemi di mantenibilità e struttura sopra citati.

### Visual Programming
Il *visual programming* è una parte intrinseca della maggior parte dei metodi di sviluppo rapido di prototipi.
- utilizza linguaggi di *scripting* (es. Visual Basic)
- la *user interface* viene costruita partendo da elementi standard forniti da una libreria di componenti
- i componenti vengono poi adattati ai requisiti specifici dell'applicazione

**Svantaggi del Visual Programming:**
- rende molto difficile coordinare lo sviluppo basato su team
- non è presente un'architettura software esplicita
- le dipendenze complesse tra le parti del programma causano seri problemi di *maintainability*.
