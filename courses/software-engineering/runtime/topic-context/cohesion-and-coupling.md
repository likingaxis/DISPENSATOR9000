# Topic Context

**topic_id**: cohesion-and-coupling
**title**: Cohesion e Coupling

## Retrieval Metadata
- Primary fragments: 107
- Secondary fragments: 20
- Visual assets candidate: 63
- Estimated context tokens: ~7913

## 1. Primary Evidence (Official Coverage)

### Source: slides-08-design (`official-slides\II parte ISW\08-Progetto.pdf`)
#### Page 15
> © UniRoma2 - Ingegneria del Software 16

> Coesione • Per eseguire una funzione sono necessarie varie

> azioni.

> • Le azioni possono essere concentrate in un

> singolo modulo oppure sparse tra tanti.

> • Coesione di un modulo = Misura in cui il modulo

> espleta internamente tutte le azioni necessarie a

> espletare una data funzione (cioè senza interagire

> con le azioni interne ad altri moduli).

> • Coesione misura dunque il grado di interazione

> interna al modulo tra le azioni di una funzione.

#### Page 16
> © UniRoma2 - Ingegneria del Software 17

> Livelli di Coesione (1 è il peggiore, 7 il migliore)

> 1. Coincidental (nessuna relazione tra gli elementi del modulo).

> 2. Logical (elementi correlati, di cui uno viene selezionato dal modulo  chiamante)

> 3. Temporal (relazione di ordine temporale tra gli elementi).

> 4. Procedural (elementi correlati in base ad una sequenza predefinita di  passi da eseguire).

> 5. Communicational (elementi correlati in base ad una sequenza  predefinita di passi che vengono eseguiti sulla stessa struttura dati).

> 6. Informational (ogni elemento ha una porzione di codice indipendente  e un proprio punto di ingresso ed uscita; tutti gli elementi agiscono  sulla stessa struttura dati).

> 7. Functional (tutti gli elementi sono correlati dal fatto di svolgere una  singola funzione)

#### Page 17
> © UniRoma2 - Ingegneria del Software 18

> Livelli di Coesione (2)

> {

> optimal for the structured paradigm

> optimal for the OO paradigm

#### Page 18
> © UniRoma2 - Ingegneria del Software 19

> Coincidental Cohesion: example

> • Module functions:

> – print next line

> – invert characters of the second string

> parameter

> – add 7 to the fifth parameter

> – perform int-double conversion to the fourth

> parameter

#### Page 19
> © UniRoma2 - Ingegneria del Software 20

> Logical Cohesion: example

#### Page 20
> © UniRoma2 - Ingegneria del Software 21

> Temporal Cohesion: example

> • Module functions: – Open old_master_file – Open new_master_file – Open transaction_file – Open print_file – Initialize sales_region_table – Read first transaction_file records – Read first old_master_file record

#### Page 21
> © UniRoma2 - Ingegneria del Software 22

> Procedural Cohesion: example

> • Module functions:

> – Read part_number from database

> – Use part_number to update

> repair_record on maintenance_file

#### Page 22
> © UniRoma2 - Ingegneria del Software 23

> Communicational Cohesion: example

> • Ex. 1: module functions

> – Update record_a in database

> – Write record_a to the trajectory_file

> • Ex. 2: module functions

> – Calculate new_trajectory

> – Send new_trajectory to the printer

#### Page 23
> © UniRoma2 - Ingegneria del Software 24

> Informational Cohesion: example

#### Page 24
> © UniRoma2 - Ingegneria del Software 25

> Example Structure Chart & Modules Cohesion

#### Page 25
> © UniRoma2 - Ingegneria del Software 26

> Coupling • Misura il grado di accoppiamento tra moduli • Livelli di coupling (1 è il peggiore, 5 il migliore): 1.Content (un modulo fa diretto riferimento al contenuto  di un altro modulo). 2.Common (due moduli che accedono alla stessa  struttura dati) 3.Control (un modulo controlla esplicitamente  l'esecuzione di un altro modulo). 4.Stamp (due moduli che si passano come argomento  una struttura dati, della quale si usano solo alcuni  elementi). 5.Data (due moduli che si passano argomenti omogenei,  ovvero argomenti semplici o strutture dati delle quali si  usano tutti gli elementi).

#### Page 26
> © UniRoma2 - Ingegneria del Software 27

> Factors affecting Coupling

> Strength of coupling depends on:

> • the number of references of one module by  another

> • the amount of data passed/shared between  modules

> • the complexity of the interface between  modules

> • the amount of control exercised by one  module over another

#### Page 27
> © UniRoma2 - Ingegneria del Software 28

> Content Coupling: example

> p®q

> • Ex. 1: module p modifies a statement  of module q • Ex. 2: p refers to local data of module  q in terms of some numerical  displacement within q • Ex. 3: p branches to a local label of q

#### Page 28
> © UniRoma2 - Ingegneria del Software 29

> Common Coupling: example

> {

> }

> >

#### Page 29
> © UniRoma2 - Ingegneria del Software 30

> Control Coupling: example

> • Module p calls module q

> – and asks q to perform an action,

> – q passes back a flag (e.g. “task not

> completed”)

> – and also asks p to perform an action

> (e.g. “print an error message”)

#### Page 30
> © UniRoma2 - Ingegneria del Software 31

> Example Structure Chart & Modules Coupling

> parameters

> coupling

> s

#### Page 31
> © UniRoma2 - Ingegneria del Software 32

> Information hiding

> • I concetti di astrazione procedurale e astrazione  dei dati sono derivati da un concetto più generale  detto information hiding, introdotto da Parnas (1971) • La tecnica di information hiding consiste nel  definire e progettare i moduli in modo che i  dettagli implementativi (procedura e dati) non  siano accessibili ad altri moduli che non abbiano  necessità di conoscere tali dettagli • I vantaggi della tecnica di information hiding si  riscontrano quando è necessario apportare  modifiche (fasi di testing e manutenzione)

#### Page 32
> © UniRoma2 - Ingegneria del Software 33

> Esempio di information hiding

> Esempio di tipo  di dato astratto  (classe C++) realizzato con  information  hiding

#### Page 33
> © UniRoma2 - Ingegneria del Software 34

> Riusabilità

> • La riusabilità fa riferimento all'utilizzo di componenti  sviluppati per un prodotto all'interno di un prodotto  differente • Per componente riusabile si intende non solo un modulo o  un frammento di codice, ma anche progetti, parti di  documenti, insiemi di test data o stime di costi e durata • Vantaggi: – netta diminuzione di costi e tempi di produzione del software – incremento dell'affidabilità dovuto all'uso di componenti già  convalidati • La riusabilità nella fase di progetto si applica a: (a) moduli software (b) application framework, che incorpora la logica di controllo di un

> progetto (c) design pattern, che identifica una soluzione di progetto ricorrente

> in applicazioni dello stesso tipo  (d) architetture software comprendenti (a), (b) e (c)

#### Page 34
> © UniRoma2 - Ingegneria del Software 35

> Riusabilità (2)

> moduli software

> application

> framework

> design pattern

> architettura

> software

## 2. Secondary Evidence (BM25 Lexical + Concepts)

### Source: isw1-summary (`ISW (1).pdf`)
#### Page 85 (BM25: 28.66)
> Nella tabella sotto invece vediamo per ogni interazione che esiste tra moduli il relativo livello  di coupling.  Es. tra p e q viene definito il livello data, si assume cioè che sia aircraft type che status flag  siano parametri utilizzati dai rispettivi moduli.  Un altro esempio è l’interazione 4, dove i due moduli si scambiano parametri di output lista  di parti di aircraft. Il relativo coupling è definito Data or Stamp poiché evidentemente non si  hanno informazioni sull’effettivo utilizzo di questa lista di parti (se ne uso solo alcune allora  stamp else data), vale lo stesso per l’interazione 2.  Per l’interazione 3 invece come parametro di input codice di funzione, coupling di controllo in  quanto chi manda il messaggio chiede al modulo di eseguire la funzione.  Dopodiché anche 5 e 6 Data Coupling, mentre per l’accoppiamento tra p e t e p e u livello di  coupling Common. Nella figura non vi è l’arco che identifica l’interazione in quanto p e t e p e  u non si scambiano effettivamente dei messaggi ma accedono allo stesso database in  update mode (NB se fosse stato scritto in read mode allora non sarebbe stato  accoppiamento di tipo common).  (FINE ESEMPIO)    Information Hiding ​ Consiste nel progettare e definire i moduli in modo che gli altri moduli vedano solo quanto  serve, nascondendo quindi i dettagli implementativi (procedura e dati) che ad essi non sono  necessari. I vantaggi si riscontrano quando è necessario apportare modifiche (fasi di testing  e manutenzione)    Nel caso dell’uso di Information Hiding invece si usano qualificatori di accesso (private,  getter e setter).    Riusabilità: ​ Fa riferimento all’utilizzo di componenti sviluppati per un prodotto all’interno di un prodotto  differente.  In generale per componente riusabile si fa riferimento a moduli, parte di codice, progetti,  parti di documenti, insiemi di test data, stime di costi o tempi etc..   Tra i principali vantaggi la netta diminuzione di costi e tempi di produzione del software e  incremento dell’affidabilità dovuto all’uso di componenti già convalidati.  Nella fase di Progetto, la riusabilità si applica a:  - singoli moduli software  - application framework (la logica che tiene insieme i moduli e che viene utilizzata per usare i  moduli)  - design pattern (a livello progettuale spesso capita di affrontare problemi ricorrenti, quindi si  sono definite soluzioni standard)

#### Page 151 (BM25: 27.16)
> Sappiamo che un modo per misurarla riguarda l’utilizzo dei concetti e le misurazioni di  Cohesion e Coupling, ma anche di Morfologia e Information Flow. ​ In questo caso si fa riferimento solo alla coesione e al coupling. ​ Alle risposte non sono associati valori numerici, ma delle etichette A, B C, o D. Viene  richiesto di fornire la percentuale di moduli in base al tipo (coesione coincidentale, logica o  temporale, procedurale o comunicativa, informational o functional). Invece di separare i 7 li  si raggruppa quindi in gruppi per un totale di 4 risposte. Lo stesso vale per il coupling, dove  viene richiesto di definire la distribuzione percentuale di coppie di moduli in base al tipo di  coupling (content, common, control, stamp o data). Successivamente si passa sugli attributi  generali di modularità e si torna quindi alle classiche checklist. Anche in questo caso,  essendo modularità un attributo con impatto positivo sull’indice, le risposte migliori sono  quelle tali per cui il valore è più alto.     Vediamo ora come calcolare il valore complessivo di modularità. ​ ​   Le prime due domande sono calcolate a parte come si vede sopra: in particolare si pesa  zero la coesione e il coupling peggiore (coincidentale e content) mentre si pesa a 3 quelle  migliori. Dividendo tutto per 50 si normalizza ottenendo quindi ancora un valore tra 0 e 1.     Torniamo a vedere come si effettua la valutazione di questi attributi. ​ La documentazione come anticipato deve essere analizzata in dettaglio dal Checklist  Evaluation Team per rispondere a ciascuna domanda, (tramite tecniche come Walkthrough o  Ispezioni). ​ Ogni membro del team deve rispondere alle domande in modo indipendente senza  confrontarsi subito con gli altri. ​ Durante le riunioni di Walkthrough o i meeting di ispezione i membri del team finalmente si  confrontano per verificare di aver dato le stesse risposte alle domande e il perché. Se sono  diverse allora bisogna discuterne per arrivare a un’unica risposta comune, per poter  finalmente calcolare il valore dell’attributo. ​   Si dà ad ogni attributo un template contenente la lista di domande della checklist, se la  domanda non è valutabile o non applicabile, e il punteggio. Si fa lo stesso per gli indici con la  lista degli attributi, se hanno peso negativo o positivo, il punteggio di ogni attributo, il calcolo  dell’index e il quality level (low, high o avg). ​

#### Page 81 (BM25: 25.68)
> Una buona divisione di un prodotto software in moduli è quella che permetti di ottenere:​ - Massima coesione (cohesion) interna ai moduli  - Minimo grado di accoppiamento (coupling) esterna ai moduli   La coesione rappresenta le interazioni interne al modulo e deve essere massimizzata, il  coupling fa invece riferimento all’interazione tra moduli e deve essere minimizzata. Il  problema di queste metriche è che se cerchiamo di massimizzare la coesione operiamo  negativamente sul coupling e viceversa, si vuole quindi trovare il numero di moduli che offra  il miglior tradeoff, e in questo senso facciamo riferimento esclusivamente al costo. Coesione: Per eseguire una funzione sono necessarie varie azioni, che possono essere  concentrate in un singolo modulo o sparse in tanti.  In altre parole, la coesione misura il grado di interazione interna al modulo tra le azioni di  una funzione.  La coesione si misura utilizzando una scala di valori, per un totale di 7:  1. Coincidentale: nessuna relazione tra azioni nel modulo. ​ 2. Logical: elementi correlati, ma solo uno di essi viene utilizzato dal modulo chiamante  3. Temporal: relazione temporale tra gli elementi  4. Procedurale: gli elementi sono correlati in base a una sequenza predefinita di passi  5. Communicational: leggermente migliore della procedurale, uguale ad essa solo le azioni  sono svolte sulla stessa struttura dati  6. Informational: ogni elemento ha una porzione di codice indipendente e un proprio punto di  ingresso e di uscita, inoltre ogni elemento agisce sulla stessa struttura dati.  7. Funzionale: tutti gli elementi sono correlati dal fatto di svolgere una singola funzione.  In base al tipo di approccio, possiamo avere come obiettivo o Informational (per paradigma  OO) o Functional (per programmazione strutturata).    (ES: saltare)  Es. di coesione coincidentale: stampa la prossima riga, inverti i char della seconda stringa  parametro, aggiungi 7 al quinto parametro etc…  sono tutte azioni scorrelate, un modulo del genere non è riusabile o mantenibile.  Spesso vi sono dei vincoli nella dimensione del numero di istruzioni minime per modulo,  quindi in tal caso anche per moduli semplici è necessario aggiungere istruzioni di questo tipo  per raggiungere la dimensione minima.

#### Page 83 (BM25: 24.18)
> A partire dalla descrizione di ogni modulo dobbiamo capire la relativa coesione: vediamo  moduli con coesione functional che svolgono una funzione ben precisa (es. memorizzare  record temperature, crea record temperature etc..), si hanno poi moduli a coesione  coincidentale che svolgono azioni scorrelate (es. inizializza le somme e apri i file, chiudi file  e stampa le temperature medie. Si poteva fare di meglio, ad es. creando un modulo dedicato  alla gestione dei file, uno a inizializzare le somme e l’altro a stampare le temperature medie),  poi moduli a coesione logica che fa varie cose ma ogni volta che lo utilizzo se ne fa una sola  in base a ciò che interessa al modulo chiamante.    Dobbiamo ora occuparci di misurare il coupling.  Il coupling misura il grado di accoppiamento tra moduli, anch’esso si misura usando una  scala, stavolta a 5 livelli dal peggiore al migliore:  1. Content: un modulo fa riferimento diretto al contenuto di un altro modulo, modificandolo o  semplicemente accedendovi (livello peggiore, forte dipendenza tra moduli)  2. Common: due moduli accedono in modalità read e write alla stessa struttura dati  3. Control: un modulo controlla esplicitamente l’esecuzione di un altro modulo  4. Stamp: due moduli interagiscono scambiandosi strutture dati della quale si usano solo  alcuni parametri (quindi diciamo che tra i parametri ce ne sono alcuni che non servono  all’altro modulo)  5. Data: due moduli interagiscono scambiandosi messaggi, in particolare passando come  argomento una struttura dati della quale si usano tutti i parametri    I fattori che influiscono sul grado di accoppiamento sono la quantità di dati condivisi tra  moduli, il numero di riferimenti che un modulo ha rispetto ad altri moduli, la complessità  dell’interfaccia tra moduli, il livello di controllo che un modulo esercita su un altro.    (ES: saltare)  Content Coupling: example  Degli esempi di content coupling è, dati due moduli p e q, ​ se p modifica un’istruzione di q, ​ se p fa riferimento a dati locali di q in termini di qualche “displacement” numerico (in

#### Page 136 (BM25: 23.06)
> METRICHE DI STRUTTURA​ Le metriche di struttura aiutano a quantificare la qualità di un software.  Le misure intermodulari permettono di quantificare le dipendenze tra moduli in base  all’architettura software determinata in fase di progettazione preliminare​ Un modulo come sappiamo è una sequenza contigua di istruzioni, delimitata da alcuni  elementi e che ha un certo identificatore (quando si pensa a un modulo si pensa a una parte  di software che può esser compilata indipendentemente). ​ È importante saper misurare la soluzione architetturale in quanto tutte le decisioni che  prendiamo in questa fase hanno impatto significativo sul software risultante, in particolare su  attributi di qualità come facilità di implementazione, affidabilità, manutenibilità e riusabilità  (nb affidabilità importante non solo per software critico!). Le misure offrono feedback per  capire se le caratteristiche del software soddisfano i requisiti.    La relazione tra progettazione preliminare e codice include relazioni 1 a 1 tra i seguenti  argomenti indicati nel design e nel codice: moduli, connessioni intermodulari e interfacce  data intermodulari.   Un’architettura software sappiamo essere un insieme di componenti che hanno tra loro  relazioni di dipendenza, si può quindi concettualizzare usando un grafo (structure chart),  dove i nodi sono i moduli e gli archi le relazioni di dipendenza. Le relazioni possono  rappresentare diverse cose (es. chiamata di procedura, flusso di dati etc…). ​ Quando si definisce l’architettura dei moduli è importante definire il valore della modularità,   cioè il grado con cui un software è definito da componenti discrete tale che il cambiamento  di una di esse comporta minimo impatto sulle altre componenti. ​ Si ricorda quindi che alta modularità è desiderabile, in quanto se si ha bassa modularità  allora è più facile fare errori -> difficile manutenzione, meno riusabili, meno affidabili etc…     La modularità può essere misurata tramite i seguenti sotto-attributi: cohesion, coupling,  morfologia e information flow. ​ - Coesione: grado con cui un modulo individualmente realizza un task ben definito.​ - Coupling: grado di interdipendenza tra moduli ​ Si voleva massimizzare coesione e minimizzare coupling per ottenere elevato livello di  modularità. ​ - Morfologia: misura la forma della structure chart.​ - Information Flow: considera il flusso di informazioni tra moduli -> interconnessione tra  moduli non solo dal punto di vista di scambio dati ma anche dal punto di vista del flusso di  controllo.

#### Page 84 (BM25: 20.10)
> linguaggi a basso livello come assembly, dove si utilizzano i displacement tra moduli per  passarsi informazioni), ​ se p utilizza un’etichetta locale del modulo q (caso del go to, se p fa goto su un’etichetta  interna di q, sta saltando direttamente nel suo flusso di controllo interno).  Questo tipo di coupling è molto difficile da trovare in codici attuali, si tratta del livello  peggiore di coupling perché ogni cambiamento a q richiede una modifica al modulo p.    Common Coupling: example  Riguardo il common coupling un esempio sono due moduli cca e ccb che accedono alla  stessa variabile globale in modalità lettura e scrittura. Si tratta di un grado comunque non  buono in quanto capire come si comporta la parte di codice dedicata alla variabile è più  difficile se vi sono più moduli che vi accedono e possono modificarla (problemi di sicurezza e  integrità dei dati della variabile)    Control Coupling: example​ Un esempio per il control coupling è se un modulo p chiama il modulo q chiedendogli di fare  qualcosa, dopodiché q invia un flag di ritorno a p che permette a p di svolgere una certa  azione (in base a quanto detto da q p si comporta di conseguenza). In questo senso q  esercita controllo su p in quanto in base alla sua risposta p si comporta di conseguenza.    Stamp e Data Coupling​ ￼Stamp e Data coupling sono infine il livello migliore in quanto i moduli si scambiano  informazioni tramite un’interfaccia ben definita scambiandosi messaggi contenenti solo  informazioni necessarie se Data altrimenti Stamp.  (FINE ESEMPIO)    Example Structure Chart (oggi chiamato architettura software)​ L’interazione tra moduli è evidenziata da degli archi numerati.  I moduli si scambiano dei messaggi, e questi messaggi veicolano dei parametri che possono  essere di input o di output.    (ES: saltare)  Es. p e q interagiscono scambiandosi il messaggio 1 che ha come parametro di input tipo di  aircraft e output status flag.

#### Page 151 (BM25: 16.52)
> Sappiamo che un modo per misurarla riguarda l’utilizzo dei concetti e le misurazioni di  Cohesion e Coupling, ma anche di Morfologia e Information Flow. ​ In questo caso si fa riferimento solo alla coesione e al coupling. ​ Alle risposte non sono associati valori numerici, ma delle etichette A, B C, o D. Viene  richiesto di fornire la percentuale di moduli in base al tipo (coesione coincidentale, logica o  temporale, procedurale o comunicativa, informational o functional). Invece di separare i 7 li  si raggruppa quindi in gruppi per un totale di 4 risposte. Lo stesso vale per il coupling, dove  viene richiesto di definire la distribuzione percentuale di coppie di moduli in base al tipo di  coupling (content, common, control, stamp o data). Successivamente si passa sugli attributi  generali di modularità e si torna quindi alle classiche checklist. Anche in questo caso,  essendo modularità un attributo con impatto positivo sull’indice, le risposte migliori sono  quelle tali per cui il valore è più alto.     Vediamo ora come calcolare il valore complessivo di modularità. ​ ​   Le prime due domande sono calcolate a parte come si vede sopra: in particolare si pesa  zero la coesione e il coupling peggiore (coincidentale e content) mentre si pesa a 3 quelle  migliori. Dividendo tutto per 50 si normalizza ottenendo quindi ancora un valore tra 0 e 1.     Torniamo a vedere come si effettua la valutazione di questi attributi. ​ La documentazione come anticipato deve essere analizzata in dettaglio dal Checklist  Evaluation Team per rispondere a ciascuna domanda, (tramite tecniche come Walkthrough o  Ispezioni). ​ Ogni membro del team deve rispondere alle domande in modo indipendente senza  confrontarsi subito con gli altri. ​ Durante le riunioni di Walkthrough o i meeting di ispezione i membri del team finalmente si  confrontano per verificare di aver dato le stesse risposte alle domande e il perché. Se sono  diverse allora bisogna discuterne per arrivare a un’unica risposta comune, per poter  finalmente calcolare il valore dell’attributo. ​   Si dà ad ogni attributo un template contenente la lista di domande della checklist, se la  domanda non è valutabile o non applicabile, e il punteggio. Si fa lo stesso per gli indici con la  lista degli attributi, se hanno peso negativo o positivo, il punteggio di ogni attributo, il calcolo  dell’index e il quality level (low, high o avg). ​

#### Page 105 (BM25: 15.60)
> In una stratificazione corretta delle classi devono esserci oggetti boundary che si devono  occupare solo di catturare le richieste dell’utente e inoltrarle agli oggetti di controllo, che  conoscono la logica applicativa e interagiranno con gli oggetti entity (oggetti che  mantengono le informazioni) al fine di soddisfare la richiesta.  Ma in questi casi sto dando responsabilità di controllo a un oggetto entity -> non rispettano la  stratificazione BCE. Si introduce quindi un oggetto di controllo che si occupi della logica di esecuzione. Corso  fornisce gli esami propedeutici, student la carriera universitaria e courseoffering interpellato  solo eventualmente per iscrivere lo studente, si garantisce che le classi entity si limitino ad  avere le informazioni senza controllare.  (FINE ESEMPIO)    Isolando la logica di controllo in una classe apposita molti vantaggi tra cui a livello di  manutenibilità (eventuali modifiche sul come gestire le iscrizioni sono limitate a questa  classe senza dover cercare una classe che si occupasse anche di quello).  In questo caso (così come visto nelle applicazioni service oriented) gioca un ruolo  fondamentale il coupling (grado di accoppiamento). Il più desiderabile è l’Intra-Layer  Coupling: si vogliono evitare delle dipendenze tra elementi appartenenti a diversi layer  applicativi (con layer applicativi si intende BCE).  Si vuole favorire quindi l’Intra-Layer coupling ossia l’interazione all’interno di uno stesso  strato piuttosto che l’interazione tra strati differenti.  Si vuole quindi minimizzare l’Inter-Layer Coupling, e uno strumento utile per farlo è la Legge  di Demeter.    La Legge di Demeter (anche nota come “don’t talk to strangers” in quanto si basa sull’idea di  non “comunicare” con oggetti non noti).  Essa afferma che un metodo può inviare messaggi (cioè invocare metodi) solo ai seguenti  oggetti:  1) L’oggetto stesso (un metodo deve poter invocare i metodi su se stesso, es. usando this in  Java e C++)  2) Oggetti passati come argomenti nel metodo.  3) Oggetto elencato tra gli attributi dell oggetto stesso (strong law -> attributi ereditati non  possono essere usati)  4) Un oggetto creato dal metodo  5) Un oggetto che fa riferimento a una variabile globale

#### Page 138 (BM25: 14.88)
> Per misurarlo si usa r(G) = e-n+1. ​ Minore r(G) significa meno riuso -> migliore morfologia in quanto minor interdipendenza  Questa tecnica di misurazione tuttavia non tiene conto del numero di chiamate fatte da un  modulo ad un altro e non si tiene conto della dimensione dei moduli -> bisogna utilizzare  oltre che questa misura anche Tree Impurity per capire la morfologia.     Per approfondire come i moduli dipendano effettivamente uno dall’altro dobbiamo misurare  l’Information Flow. Questa misura assume che la complessità di un modulo dipenda da due  fattori principali: ​ - la complessità intrinseca del modulo (il suo codice)​ - la complessità della sua interfaccia (ossia quanto è aperto all’ambiente circostante, uanto  dipende/influenza altri moduli). ​ Il livello totale di information flow in un sistema è attributo intermodulare, tuttavia è possibile  anche misurare l’information flow tra un singolo modulo e il resto del sistema come quindi  attributo intramodulare.     Per misurare l’information flow si devono contare le connessioni tra un modulo con il resto  dei moduli del sistema (fan-in e fan-out di un modulo), inoltre si assume che le misure di  information flow sono basate su flussi di informazioni sia locali (ossia legati a un modulo che  chiama un altro modulo se diretto o il valore di ritorno di un metodo invocato se indiretto) che  globali (quando l’informazione tra moduli è condivisa e accessibile a tutti). ​ L’obiettivo dell’information flow è misurare quanto i moduli dipendano dagli altri, quindi può  essere utilizzato per individuare le parti critiche del sistema e capire se la nostra  progettazione può essere pericolosa in termini di affidabilità, manutenibilità, riusabilità etc… - Fan-In di un modulo M: rappresenta il numero di flussi locali  (diretti e indiretti) che terminano nel modulo M in aggiunta al  numero di flussi globali (strutture dati globali utilizzate dal  modulo M) -> tutto ciò che entra nel modulo sia in termini di  valori di ritorno che in termini di dati presi da strutture dati globali  fa parte del Fan-in del modulo. ​   - Fan-Out: rappresenta viceversa tutto ciò che “esce del  modulo”: il numero di flussi locali (diretti o indiretti) che partono  dal modulo M più il numero di aggiornamenti che M fa su  strutture dati globali.             È importante misurarli in quanto se un modulo ha alto fan-out allora esso probabilmente  influenza molti altri moduli, viceversa elevato fan-in indica che il modulo dipende da molti  altri moduli. Un modulo con elevato fan in e fan out è sicuramente un modulo che è al centro  del sistema, mentre uno con basso fan in e fan out alla periferia del sistema.     L’obiettivo è ovviamente ridurre il fan in e fan out per ogni modulo in quanto se elevato allora  indica un modulo complesso che potrebbe portare a più errori in quanto:​

#### Page 157 (BM25: 14.42)
> Sapendo che le componenti possono essere integrate a vari livelli come visto (livello  gerarchico, dalle componenti a basso lvl fino alle più importanti ad alto lvl) possiamo  utilizzare due approcci:  - Top-down testing: si parte dai livelli più alti di gerarchia fino ad arrivare alla radice per  componenti “meno rilevanti”. Poiché si parte da un insieme vasto di componenti è possibile  che queste non siano presenti, in tal caso sono sostituite con degli stubs, ossia delle funzioni  che emulano il comportamento della componente.  - Bottom-up testing: si procede dall’integrare le componenti individuali a basso livello di  gerarchia fino al sistema completo.    Non esiste un approccio migliore, tipicamente anzi queste strategie sono combinate in base  alle situazioni (es. disponiblità di componenti, stub etc…).    Come detto nell’approccio top-down le componenti ad alto livello sono sviluppate prima di  quelle a basso livello -> si devono usare gli stub che hanno la stessa interfaccia del  componente ma funzionalità limitate (un emulatore della funzione che sarà integrata dal  modulo).  Si parte quindi dalle componenti a livello più alto sostituendo quelle di basso livello non  ancora disponibili con stubs. Quando le componenti saranno disponibili, si sostituiranno e  così via.  Riguardo il Bottom-up testing invece si parte da componenti più in basso nella scala  gerarchica iterativamente fino a testare l’intero sistema. Poiché le componenti sono  disponibili per il test si utilizzano dei Test Drivers, codice che eserciterà il componente per  valutarne la capacità di integrazione con i livelli successivi.  ​   Bottom-up e Top-down possono essere confrontati da 4 punti di vista:   - Architectural Validation: con top-down è più facile identificare gli errori.  - System Demonstration: top-down permette di costruire demo con funzionalità limitate  (perché devo includere gli stubs) che può essere usata come strumento di convalida fin  dall’inizio del testing.   - Test Implementation: è più implementare tramite bottom-up.  - Test Observation: ossia valutare i risultati prodotti dall’attività di testing, in entrambi i casi è  difficile capire in base agli output dove si trova l’errore e possono essere necessari ulteriori  test.    Interface Testing  Due componenti che interagiscono tra loro conoscono solo la loro rispettiva interfaccia, non i  dettagli implementativi.  Ogni modulo o sottosistema ha un interfaccia ben definita, utilizzata per chiamare quel  modulo/sottosistema da altri componenti.  L’obiettivo di questo testing dell’interfaccia è scoprire difetti introdotti a causa di errori  d’interfaccia o assunzioni non valide relative all’interfaccia.  Questo testing è molto importante nel mondo object oriented perché gli oggetti sono definiti  secondo la loro interfaccia.  L’obiettivo dell’interface testing è quindi identificare dei test cases che testino l’interfaccia del  componente e non la sua struttura interna.

### Source: theory-summary (`teoria.pdf`)
#### Page 32 (BM25: 13.19)
> difficile da seguire - La complessità aumenta con troppi livelli di decorazione - È importante gestire con attenzione l’ordine con cui i

#### Page 14 (BM25: 11.76)
> Activity Diagram Rappresenta a vari livelli di astrazione il flusso di esecuzione, sia sequenziale che concorrente, in una applicazione object-oriented. In fase di OOA, viene usato per

#### Page 17 (BM25: 10.91)
> client e nasconde tutta l'architettura C/S che c'è dietro. L'architettura Two-Tier C/S è suddivisa in due livelli principali: • Client: l'interfaccia utente, che gestisce la logica di presentazione e talvolta

#### Page 50 (BM25: 8.73)
> diversi. i10 Transition Riusabilità Indica il grado in cui parti del

#### Page 45 (BM25: 8.39)
> Information Flow Le misure di Information Flow assumono che la complessità di un modulo dipende

#### Page 45 (BM25: 6.99)
> Information Flow Le misure di Information Flow assumono che la complessità di un modulo dipende da 2 fattori:

#### Page 45 (BM25: 6.58)
> Il livello totale di Information Flow attraverso un sistema è un'attributo inter- modulare, mentre se considerato il livello di Information Flow attraverso un singolo modulo è un'attributo intra-modulare. Le misure di Information Flow si

#### Page 45 (BM25: 6.58)
> modulare, mentre se considerato il livello di Information Flow attraverso un singolo modulo è un'attributo intra-modulare. Le misure di Information Flow si basano su:

#### Page 45 (BM25: 6.26)
> • La complessità delle interfacce del modulo Il livello totale di Information Flow attraverso un sistema è un'attributo inter- modulare, mentre se considerato il livello di Information Flow attraverso un

#### Page 7 (BM25: 5.18)
> • Incremento della qualità dei prodotti software; • Riduzione di tempi e costi di sviluppo. Per risolvere questi problemi si è adottato un processo che allo stesso tempo è

## 3. Visual Assets Candidates

- **asset_id**: 0aa41ce2-909a-4f4a-9098-65e21b00ab4e
  source: slides-08-design
  page: 15
  type: embedded_image
  path: `c576966b_p15_i0.jpeg`

- **asset_id**: 9064797f-1d3b-4406-8820-ecc1c5b3e97e
  source: slides-08-design
  page: 15
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 72c5b987-6ef3-4ac9-84cf-7aacdd5f683d
  source: slides-08-design
  page: 16
  type: embedded_image
  path: `c576966b_p16_i0.jpeg`

- **asset_id**: 4de32dfd-776c-4e0a-a9f8-be519edf4ce8
  source: slides-08-design
  page: 16
  type: embedded_image
  path: `c576966b_p16_i1.jpeg`

- **asset_id**: 77b4d1a6-0c1f-444f-b456-c2a8e0a18bff
  source: slides-08-design
  page: 16
  type: embedded_image
  path: `c576966b_p16_i2.jpeg`

- **asset_id**: ff268bfe-7d6b-4377-afdb-9faa6527fa5f
  source: slides-08-design
  page: 16
  type: embedded_image
  path: `c576966b_p16_i3.jpeg`

- **asset_id**: 0bd95beb-18af-4da8-a048-c80d2bb55d24
  source: slides-08-design
  page: 16
  type: embedded_image
  path: `c576966b_p16_i4.jpeg`

- **asset_id**: 82d859dc-de44-48ae-b42d-be4c1665409a
  source: slides-08-design
  page: 16
  type: embedded_image
  path: `c576966b_p16_i5.jpeg`

- **asset_id**: 566c18b4-80f0-49bd-be76-7a8365f932e6
  source: slides-08-design
  page: 16
  type: embedded_image
  path: `c576966b_p16_i6.jpeg`

- **asset_id**: 02972314-a0b7-462e-a63a-425d0ef7e9bf
  source: slides-08-design
  page: 16
  type: embedded_image
  path: `c576966b_p16_i7.jpeg`

- **asset_id**: 136f0353-08e4-4a5d-b72d-e920a7ed489a
  source: slides-08-design
  page: 16
  type: embedded_image
  path: `c576966b_p16_i8.jpeg`

- **asset_id**: bef737c4-b1db-4681-bea4-c0d1f10bd7f6
  source: slides-08-design
  page: 16
  type: embedded_image
  path: `c576966b_p16_i9.jpeg`

- **asset_id**: b8397d3d-0a96-40eb-82ed-7559f40a5247
  source: slides-08-design
  page: 16
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 0c56c5f4-f881-47f0-ad7b-84a0be22bc79
  source: slides-08-design
  page: 17
  type: embedded_image
  path: `c576966b_p17_i0.jpeg`

- **asset_id**: 2e89fd0e-bddf-4a48-9911-1be20169a343
  source: slides-08-design
  page: 17
  type: embedded_image
  path: `c576966b_p17_i1.png`

- **asset_id**: f25c2725-251f-4103-9d0f-daea7ce211f9
  source: slides-08-design
  page: 17
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 0c018dcd-c757-4055-bc3a-798893dd97a1
  source: slides-08-design
  page: 18
  type: embedded_image
  path: `c576966b_p18_i0.jpeg`

- **asset_id**: 9a940dd6-3bac-429e-87d7-5130d08c86d8
  source: slides-08-design
  page: 18
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b5a9b555-b8de-448c-8213-128d6454df0d
  source: slides-08-design
  page: 19
  type: embedded_image
  path: `c576966b_p19_i0.jpeg`

- **asset_id**: 42da8771-f90c-46ef-a4ba-c22b65007d51
  source: slides-08-design
  page: 19
  type: embedded_image
  path: `c576966b_p19_i1.jpeg`

- **asset_id**: 9874fbd0-f96f-4c2c-9168-4b5e259dbf2d
  source: slides-08-design
  page: 19
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 25237051-5cb2-45ad-9054-4269ed5b52d1
  source: slides-08-design
  page: 20
  type: embedded_image
  path: `c576966b_p20_i0.jpeg`

- **asset_id**: ed1753b6-60ec-48dc-86db-595dc02538ec
  source: slides-08-design
  page: 20
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: e437305f-eb13-4b71-b214-754f249296ae
  source: slides-08-design
  page: 21
  type: embedded_image
  path: `c576966b_p21_i0.jpeg`

- **asset_id**: e12a708c-bfe4-49c3-a05b-0280793a04b3
  source: slides-08-design
  page: 21
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 1bc7f746-86cf-4f20-ab2b-e13371e9b0ae
  source: slides-08-design
  page: 22
  type: embedded_image
  path: `c576966b_p22_i0.jpeg`

- **asset_id**: 97a658c2-54b7-4f34-9121-1d1383fe7ea7
  source: slides-08-design
  page: 22
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 6e50db6d-eb12-4bc8-9926-b8de9820085d
  source: slides-08-design
  page: 23
  type: embedded_image
  path: `c576966b_p23_i0.jpeg`

- **asset_id**: 96719fda-6b67-429f-8614-3554915616f6
  source: slides-08-design
  page: 23
  type: embedded_image
  path: `c576966b_p23_i1.png`

- **asset_id**: 8dcec393-460a-49bb-a85a-937bcbe01c11
  source: slides-08-design
  page: 23
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 6390e037-6d1f-4ae4-bb1b-7238afe40bca
  source: slides-08-design
  page: 24
  type: embedded_image
  path: `c576966b_p24_i0.jpeg`

- **asset_id**: 27bcd3f7-7867-4796-b3ad-05a93a197e56
  source: slides-08-design
  page: 24
  type: embedded_image
  path: `c576966b_p24_i1.jpeg`

- **asset_id**: 84614df5-58ef-484e-a19b-6624c1e98f98
  source: slides-08-design
  page: 24
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 986a030b-9ec7-4bd6-81b9-3ddbdefac93d
  source: slides-08-design
  page: 25
  type: embedded_image
  path: `c576966b_p25_i0.jpeg`

- **asset_id**: 8b5763f4-237c-478e-9042-5483cd42f509
  source: slides-08-design
  page: 25
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 79d7a9fa-638a-41af-a4a6-d607a66c687e
  source: slides-08-design
  page: 26
  type: embedded_image
  path: `c576966b_p26_i0.jpeg`

- **asset_id**: 242ff1c4-fc45-4c17-9482-e800af989e03
  source: slides-08-design
  page: 26
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 722bb7e4-fa5d-43b8-a6d6-ca2a87c4cd94
  source: slides-08-design
  page: 27
  type: embedded_image
  path: `c576966b_p27_i0.jpeg`

- **asset_id**: 0856e1ea-037d-4025-a60f-6bd02760b7fc
  source: slides-08-design
  page: 27
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 3207c538-ae90-4daf-bec5-e08c8c9890f8
  source: slides-08-design
  page: 28
  type: embedded_image
  path: `c576966b_p28_i0.jpeg`

- **asset_id**: d278c770-2a86-475d-8cb6-b0499fc3e5bf
  source: slides-08-design
  page: 28
  type: embedded_image
  path: `c576966b_p28_i1.png`

- **asset_id**: 7afc4e80-8dc4-4ec3-9038-9142c55b0818
  source: slides-08-design
  page: 28
  type: embedded_image
  path: `c576966b_p28_i2.png`

- **asset_id**: 81c53707-1fed-4ce4-b059-e3bd0a537597
  source: slides-08-design
  page: 28
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 708eeff0-a452-4c89-9277-e4006336f7d2
  source: slides-08-design
  page: 29
  type: embedded_image
  path: `c576966b_p29_i0.jpeg`

- **asset_id**: 25f2df8a-4ec9-4f2f-b02d-836b7cb3c6dd
  source: slides-08-design
  page: 29
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 4c2740f1-9d11-47a9-a6b4-a881ace9facf
  source: slides-08-design
  page: 30
  type: embedded_image
  path: `c576966b_p30_i0.jpeg`

- **asset_id**: e03bb554-b020-45b5-b787-04c96e70f51e
  source: slides-08-design
  page: 30
  type: embedded_image
  path: `c576966b_p30_i1.png`

- **asset_id**: 2bf6c589-5c49-4e10-ba4e-b046bc8a62a9
  source: slides-08-design
  page: 30
  type: embedded_image
  path: `c576966b_p30_i2.png`

- **asset_id**: 8341c393-a407-4888-9643-916ba305bf59
  source: slides-08-design
  page: 30
  type: embedded_image
  path: `c576966b_p30_i3.jpeg`

- **asset_id**: 267fcd9d-9ac3-4535-aa7b-558c246256f3
  source: slides-08-design
  page: 30
  type: embedded_image
  path: `c576966b_p30_i4.png`

- **asset_id**: 6b4b625f-864e-42c2-851e-c1e9b5814d2e
  source: slides-08-design
  page: 30
  type: embedded_image
  path: `c576966b_p30_i5.png`

- **asset_id**: ae155708-54f5-48c8-b1cb-4b6d965459cb
  source: slides-08-design
  page: 30
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 936723c8-bf86-4eee-a44b-afcd1c0bb174
  source: slides-08-design
  page: 31
  type: embedded_image
  path: `c576966b_p31_i0.jpeg`

- **asset_id**: b9477e63-3c10-4d83-ae3b-57f9736c3b74
  source: slides-08-design
  page: 31
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: e4e94df6-c6ba-49cd-94a1-50b6774b388d
  source: slides-08-design
  page: 32
  type: embedded_image
  path: `c576966b_p32_i0.jpeg`

- **asset_id**: afc7d74e-a444-4d39-9f75-95c5f13937fc
  source: slides-08-design
  page: 32
  type: embedded_image
  path: `c576966b_p32_i1.jpeg`

- **asset_id**: 4524982d-a312-4067-a3b4-d32ff6e5e6d1
  source: slides-08-design
  page: 32
  type: embedded_image
  path: `c576966b_p32_i2.jpeg`

- **asset_id**: 8bd2564b-7f03-4b06-a9c3-9034833bebdd
  source: slides-08-design
  page: 32
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 3dc80c24-b90c-4354-b810-27e437312ba9
  source: slides-08-design
  page: 33
  type: embedded_image
  path: `c576966b_p33_i0.jpeg`

- **asset_id**: 68a9e7a4-8fcf-4fc7-b827-9ab9bb04ea5a
  source: slides-08-design
  page: 33
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: bb10bc49-9305-4f05-8f57-4388eb334df4
  source: slides-08-design
  page: 34
  type: embedded_image
  path: `c576966b_p34_i0.jpeg`

- **asset_id**: a1e4755c-bbba-442b-8f5a-48a90c5262f4
  source: slides-08-design
  page: 34
  type: embedded_image
  path: `c576966b_p34_i1.png`

- **asset_id**: eb040931-8aca-4ad3-b9fa-dca813eca154
  source: slides-08-design
  page: 34
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

