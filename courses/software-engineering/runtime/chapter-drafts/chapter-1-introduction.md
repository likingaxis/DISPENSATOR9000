# Capitolo 1 — Introduzione

## Ingegneria del Software

### Def Ingegneria del Software
L'**Ingegneria del Software** è la disciplina per la produzione del software secondo i principi dell'ingegneria, in particolare progettazione e validazione.

È essenziale per trasformare il software in un prodotto industriale.

Gli obiettivi principali sono:
- fornire metodi e tecnologie per inquadrare la produzione del software come disciplina ingegneristica;
- presentare il processo software attraverso tecniche di produzione moderne.

L'assenza di principi di ingegneria del software può portare a:
- scarsa qualità del prodotto;
- scarsa competitività;
- *cost overrun*;
- *time overrun*.

### Origine della disciplina

Il termine **Software Engineering** fu coniato nel 1968 durante la conferenza NATO di Garmisch.

L'obiettivo era inquadrare il software all'interno di una disciplina ingegneristica, riconoscendo che la programmazione:
- non è soltanto scienza;
- non è soltanto matematica;
- comporta la costruzione di un prodotto.

Storicamente, per anni la produzione del software è stata vista dai costruttori di hardware come:
- un'attività banale basata sulla sola abilità di programmazione;
- una branca della teoria della programmazione.

Parnas, nel 1997, descrive il rapporto storico tra teoria della programmazione e principi dell'ingegneria come un **"matrimonio non consumato"**:
- gli ingegneri devono conoscere la teoria;
- gli informatici teorici devono conoscere i principi ingegneristici.

>[!question]- Che cos'è l'Ingegneria del Software e perché è necessaria?
> >[!done]- la risposta
> > L'Ingegneria del Software è la disciplina che applica principi ingegneristici alla produzione del software, in particolare progettazione e validazione, rendendolo un prodotto industriale. La mancanza di tali principi può portare a scarsa qualità, scarsa competitività e sforamenti di costi e tempi.

## Prodotto, Artefatto, Codice e Sistema Software

### Def Prodotto Software
Un **Prodotto Software**, o **Software**, è composto da:
- codice;
- documentazione.

### Def Artefatto
Un **Artefatto** è un prodotto software intermedio.

Esempi indicati:
- documento dei requisiti;
- documento di specifica;
- documento di progetto.

### Def Codice
Il **Codice** è il prodotto software finale.

### Def Sistema Software
Un **Sistema Software** è un insieme organizzato di prodotti software.

>[!question]- Si distinguano Prodotto Software, Artefatto, Codice e Sistema Software.
> >[!done]- la risposta
> > Il Prodotto Software è composto da codice e documentazione. Un Artefatto è un prodotto software intermedio, come un documento dei requisiti, di specifica o di progetto. Il Codice è il prodotto software finale. Un Sistema Software è un insieme organizzato di prodotti software.

## Aspetti del prodotto software

Gli aspetti del prodotto software vengono distinti in **accidentali** ed **essenziali**.

### Aspetti accidentali
Gli aspetti accidentali sono superabili con il progresso della tecnologia:
- attitudine;
- manutenzione;
- specifica e progetto;
- *teaming*.

### Aspetti essenziali
Gli aspetti essenziali non sono superabili con il progresso di mezzi e conoscenze:
- complessità;
- conformità;
- cambiabilità;
- invisibilità.

## Costo e dimensione del software

Il costo di produzione cresce con il quadrato della dimensione del prodotto:

$$
C = aS^2
$$

- $C$ = costo;
- $S$ = *size* del prodotto;
- $a$ = coefficiente della relazione.

Conseguenza:
- produrre due prodotti di dimensione dimezzata costa meno che produrre un unico prodotto intero.

Un'altra caratteristica economica importante è che:
- produrre una replica del software non comporta alcun costo.

### Dimensione, prezzo e mercato

Se la dimensione del prodotto raddoppia, a parità delle altre condizioni indicate:
- a parità di ampiezza del mercato:
    - il prezzo deve essere quattro volte superiore;
- a parità di prezzo:
    - il mercato deve essere quattro volte più grande.

>[!question]- Come varia il costo del software rispetto alla sua dimensione?
> >[!done]- la risposta
> > Il costo è proporzionale al quadrato della dimensione, secondo la relazione $C=aS^2$. Per questo produrre due prodotti di dimensione dimezzata costa meno che produrne uno intero. Inoltre, produrre una replica del software non comporta costo.

## Ciclo di Vita del Software

### Def ciclo di vita

Il ciclo di vita del software è articolato in tre stadi:

1. **Sviluppo**
2. **Manutenzione**
3. **Dismissione**

La **Produzione Software** comprende:
- sviluppo;
- manutenzione.

### Sviluppo

Lo sviluppo consiste in sei fasi:

1. **Requisiti**
2. **Specifiche**
    - indicate anche come analisi dei requisiti;
3. **Pianificazione**
4. **Progetto**
    - preliminare;
    - dettagliato;
5. **Codifica**
6. **Integrazione**

### Manutenzione

La manutenzione rappresenta una parte molto rilevante del ciclo di vita:
- copre circa il **60% dei costi** dell'intero ciclo di vita.

### Effetto delle modifiche

L'effetto di una modifica dipende dalla fase in cui viene introdotta.

Quando una modifica viene introdotta in fasi avanzate può comportare:
- rivolgimenti;
- necessità di nuove risorse;
- correzioni importanti;
- costi supplementari.

![[5928463e_p8_i1.png|400]]

>[!question]- Si descrivano gli stadi del ciclo di vita e le fasi dello sviluppo.
> >[!done]- la risposta
> > Il ciclo di vita comprende Sviluppo, Manutenzione e Dismissione. La Produzione Software comprende sviluppo e manutenzione. Lo sviluppo è composto da sei fasi: requisiti, specifiche o analisi dei requisiti, pianificazione, progetto preliminare e dettagliato, codifica e integrazione.

## Testing, Verification e Validation

Il ***testing*** non è una fase separata:
- accompagna l'intero sviluppo;
- viene svolto attraverso:
    - *verification*;
    - *validation*.

### Verification

La ***Verification*** ha luogo alla fine di ogni fase.

Serve ad accertare se la fase è stata svolta correttamente:

> *Are we building the product right?*

### Validation

La ***Validation*** si svolge alla fine dello sviluppo.

Serve ad accertare se il prodotto finale è quello corretto:

> *Are we building the right product?*

La distinzione quindi è:
- *Verification*:
    - riguarda la correttezza dello svolgimento delle singole fasi;
- *Validation*:
    - riguarda il prodotto finale alla conclusione dello sviluppo.

>[!question]- Qual è la differenza tra Verification e Validation?
> >[!done]- la risposta
> > La Verification viene svolta alla fine di ogni fase e controlla se quella fase è stata eseguita correttamente: "are we building the product right?". La Validation avviene alla fine dello sviluppo e controlla se il prodotto finale è quello giusto: "are we building the right product?".

## Defect Removal Efficiency

### Def DRE
La **Defect Removal Efficiency (DRE)** indica la percentuale di difetti trovati prima del rilascio rispetto al numero totale di difetti.

Nel totale vengono considerati:
- i difetti trovati prima del rilascio;
- i difetti trovati dagli utenti in un intervallo standard successivo al rilascio.

Il valore medio della DRE negli Stati Uniti, aggiornato al 2016, è:
- **92%**.

Il valore può variare in funzione del modello di ciclo di vita.

>[!question]- Che cosa misura la Defect Removal Efficiency?
> >[!done]- la risposta
> > La DRE misura la percentuale dei difetti trovati prima del rilascio rispetto ai difetti totali, includendo nel totale anche quelli individuati dagli utenti in un intervallo standard dopo il rilascio. Il valore medio indicato per gli Stati Uniti, aggiornato al 2016, è del 92%, ma varia con il modello di ciclo di vita.

## Ruoli nella produzione e nell'uso del software

Nel contesto di un prodotto software si distinguono tre soggetti:

- **cliente**
    - ordina il prodotto software;
- **sviluppatore**
    - produce il prodotto software;
- **utente**
    - usa il prodotto software.

### Software interno e software a contratto

La relazione tra cliente e sviluppatore permette di distinguere:

| Tipologia | Cliente | Sviluppatore |
| --- | --- | --- |
| **software interno** | coincide con lo sviluppatore | coincide con il cliente |
| **software a contratto** | soggetto distinto | soggetto distinto dal cliente |

>[!question]- Qual è la differenza tra software interno e software a contratto?
> >[!done]- la risposta
> > Nel software interno cliente e sviluppatore coincidono. Nel software a contratto, invece, cliente e sviluppatore sono soggetti differenti.

## Affidabilità Software

### Def Reliability

L'***affidabilità*** (*reliability*) può essere espressa a due livelli:

- **informalmente**
    - è la credibilità del prodotto software;
- **formalmente**
    - è la probabilità che il prodotto software lavori correttamente in un determinato intervallo temporale.

Intuitivamente:
- un prodotto con molti difetti è poco affidabile;
- l'affidabilità migliora man mano che il numero di difetti viene ridotto.

>[!question]- Come si definisce formalmente l'affidabilità software?
> >[!done]- la risposta
> > Formalmente, l'affidabilità software è la probabilità che il prodotto lavori correttamente in un determinato intervallo temporale. In modo informale può essere vista come la credibilità del prodotto.

## Errore, Difetto e Guasto

I tre concetti sono collegati ma non coincidono.

### Def errore
Un **errore** è l'azione errata di chi introduce un difetto nel prodotto software.

Può derivare, per esempio, da:
- ignoranza;
- distrazione.

### Def defect
Un **difetto** (*defect*) è un'anomalia presente in un prodotto software.

### Def failure
Un **guasto** (*failure*) è il comportamento anomalo del prodotto software dovuto alla presenza di un difetto.

La relazione è:

```text
errore → difetto → guasto
```

- l'errore introduce il difetto;
- il difetto può causare il guasto.

>[!question]- Si distinguano errore, difetto e guasto.
> >[!done]- la risposta
> > L'errore è l'azione errata che introduce un difetto nel prodotto software. Il difetto è un'anomalia presente nel prodotto. Il guasto è il comportamento anomalo del software dovuto alla presenza di un difetto. La relazione è quindi errore → difetto → guasto.

## Affidabilità osservata e difetti latenti

La relazione tra:
- affidabilità osservata;
- numero di difetti latenti;

non è semplice.

Elimare un difetto non produce sempre lo stesso miglioramento dell'affidabilità.

In particolare:
- eliminare difetti presenti in parti del prodotto raramente utilizzate ha piccoli effetti sull'affidabilità osservata;
- il miglioramento ottenuto dipende dalla localizzazione del difetto.

## Regola 10-90

Secondo la **regola 10-90**:
- il **90% del tempo di esecuzione totale** viene speso eseguendo;
- soltanto il **10% delle istruzioni**.

Questo 10% delle istruzioni costituisce il *core*, cioè il nucleo del programma.

Di conseguenza, l'effetto dell'eliminazione di un difetto sull'affidabilità dipende anche dalla sua posizione:
- se il difetto appartiene al *core*;
- se il difetto si trova fuori dal *core*.

>[!question]- Che cosa afferma la regola 10-90 e perché è rilevante per l'affidabilità?
> >[!done]- la risposta
> > La regola 10-90 afferma che il 90% del tempo di esecuzione totale viene speso eseguendo soltanto il 10% delle istruzioni, chiamato core del programma. Per questo il miglioramento dell'affidabilità ottenuto eliminando un difetto dipende dalla sua localizzazione e, in particolare, dal fatto che appartenga o meno al core.

## Operational Profile

### Def operational profile
L'***operational profile*** descrive come viene usato il prodotto software.

L'affidabilità osservata dipende dal profilo operativo:
- utenti differenti possono usare lo stesso software in modi diversi;
- quindi possono esercitare parti differenti del prodotto;
- un difetto può manifestarsi per un utente e non per un altro.

Conseguenza:
- l'affidabilità dipende anche dall'utente.

>[!question]- Perché l'affidabilità software dipende dall'utente?
> >[!done]- la risposta
> > L'affidabilità osservata dipende dall'operational profile, cioè da come il prodotto viene utilizzato. Utenti diversi possono avere profili operativi diversi, quindi un difetto può manifestarsi per un utente e non per un altro. Per questo l'affidabilità dipende anche dall'utente.

## Guasti Hardware e Software

Hardware e software possono entrambi manifestare guasti, ma la natura dei difetti è diversa.

### Software

I guasti software sono dovuti alla presenza di difetti nei programmi.

Il punto fondamentale è che:
- il software **non si consuma**;
- i difetti software sono *latenti*;
- se non vengono corretti, possono continuare a causare guasti del sistema.

### Hardware

I guasti hardware sono quasi sempre collegati ai componenti fisici:
- consumo;
- deterioramento;
- comportamento diverso da quello specificato;
- rottura.

Esempi di difetti hardware:
- alterazione di un resistore;
- condensatore in corto;
- porta logica bloccata:
    - su `1`;
    - su `0`.

### Conseguenza sulle metriche

A causa della differenza tra gli effetti dei difetti hardware e software:
- le metriche usate per l'affidabilità hardware **non sono estensibili al software**.

>[!question]- Perché le metriche di affidabilità hardware non possono essere estese direttamente al software?
> >[!done]- la risposta
> > I guasti hardware sono quasi sempre legati a consumo, deterioramento o rottura dei componenti, mentre i guasti software derivano da difetti latenti nei programmi e il software non si consuma. Poiché gli effetti dei difetti sono diversi, le metriche di affidabilità hardware non sono estensibili al software.

## Riparazione Hardware vs Software

Anche l'effetto della riparazione è diverso.

### Riparazione Hardware

Per riparare un difetto hardware:
- si sostituisce il componente difettoso.

Dopo la riparazione:
- l'affidabilità dell'hardware torna ai livelli originali.

### Riparazione Software

Dopo una riparazione del software:
- l'affidabilità può aumentare;
- l'affidabilità può anche diminuire.

Quindi, mentre la sostituzione del componente hardware riporta l'affidabilità al livello originale, una modifica software non garantisce automaticamente un aumento dell'affidabilità.

## Obiettivi di affidabilità

### Hardware: stabilità

L'obiettivo dell'affidabilità hardware è la **stabilità**:
- mantenere costante la frequenza di guasto.

### Software: reliability growth

L'obiettivo dell'affidabilità software è la **crescita dell'affidabilità**:
- far decrescere la frequenza di guasto.

| Aspetto | Hardware | Software |
| --- | --- | --- |
| origine tipica dei guasti | consumo, deterioramento, comportamento non conforme o rottura dei componenti | difetti latenti nei programmi |
| consumo | i componenti possono consumarsi | il software non si consuma |
| riparazione | sostituzione del componente difettoso | modifica del software |
| effetto della riparazione | affidabilità riportata al livello originale | affidabilità può aumentare o diminuire |
| obiettivo | stabilità della frequenza di guasto | diminuzione della frequenza di guasto |

>[!question]- Si confrontino gli obiettivi di affidabilità di hardware e software.
> >[!done]- la risposta
> > Per l'hardware l'obiettivo è la stabilità, cioè mantenere costante la frequenza di guasto. Per il software l'obiettivo è invece la crescita dell'affidabilità, ottenuta facendo diminuire la frequenza di guasto.

## Frequenza di guasto nel tempo

### Hardware

L'andamento della frequenza di guasto hardware nel tempo è influenzato da due fenomeni:
1. eliminazione dei componenti difettosi;
    - indicata come *mortalità infantile*;
2. usura.

### Software

La frequenza di guasto software è influenzata:
1. inizialmente dall'eliminazione dei difetti;
2. successivamente dall'invecchiamento dovuto alla manutenzione.

![[5928463e_p31_i3.png|400]]

La differenza resta quindi legata alla diversa natura dei due prodotti:
- per l'hardware intervengono fenomeni fisici dei componenti;
- per il software l'andamento è collegato all'eliminazione dei difetti e alla manutenzione.

## Availability

### Def disponibilità
La **disponibilità** (*availability*) del software è la percentuale del tempo in cui il software è risultato usabile nel corso della propria vita.

Dipende da:
- numero di guasti che si verificano;
- tempo necessario per ripararli.

### Importanza di Reliability e Availability

*Reliability* e *availability* sono cruciali nei sistemi in cui una caduta del servizio può causare:
- perdite economiche;
- perdite sociali;
- rischi di sicurezza.

>[!question]- Da quali fattori dipende la disponibilità del software?
> >[!done]- la risposta
> > La disponibilità è la percentuale del tempo in cui il software è risultato usabile nel corso della sua vita. Dipende dal numero di guasti che si verificano e dal tempo necessario per ripararli.

## Evoluzione della produzione del software

La produzione del software è passata attraverso tre fasi:
1. **abilità individuale**;
2. **fase artigianale**;
3. **fase industriale**.

Il termine **Ingegneria del Software** fu coniato nel 1968 durante la conferenza NATO di Garmisch.

### Definizione IEEE

Lo standard **IEEE Std. 610.12 (1990)** definisce l'Ingegneria del Software come l'applicazione di un approccio:
- sistematico;
- disciplinato;
- misurabile;

a:
- sviluppo;
- esercizio;
- manutenzione del software.

## Configurazione e caratteristiche del software

Il software è una configurazione di:
- programmi;
- documenti;
- dati multimediali.

Le caratteristiche indicate sono:
- deve essere ingegnerizzato;
- non si consuma;
- è complesso;
- è invisibile;
- si conforma;
- cambia.

## Scopi dei metodi di Software Engineering

I metodi e le tecniche di ingegneria del software servono a:
- assicurare la qualità;
- controllare il budget;
- gestire sistemi *legacy*;
- evitare ritardi;
- applicare nuove tecnologie.

>[!question]- Come viene definita l'Ingegneria del Software dallo standard IEEE Std. 610.12?
> >[!done]- la risposta
> > È definita come l'applicazione di un approccio sistematico, disciplinato e misurabile allo sviluppo, esercizio e manutenzione del software.

## Miti del Software

Tra i miti da sfatare rientrano le convinzioni che:
- aumentare il numero di programmatori risolva i ritardi;
- descrizioni generiche siano sufficienti;
- il lavoro finisca con il *deploy*;
- la qualità possa essere valutata soltanto alla fine;
- l'Ingegneria del Software sia costosa e rallenti la produzione.

>[!question]- Quali miti sul software vengono indicati?
> >[!done]- la risposta
> > I miti indicati sono che aggiungere programmatori risolva i ritardi, che bastino descrizioni generiche, che il lavoro termini con il deploy, che la qualità si possa valutare solo alla fine e che l'Ingegneria del Software sia costosa e rallenti la produzione.
