# Topic Context

**topic_id**: requirements-classification
**title**: Classificazione dei Requisiti

## Retrieval Metadata
- Primary fragments: 83
- Secondary fragments: 20
- Visual assets candidate: 32
- Estimated context tokens: ~6529

## 1. Primary Evidence (Official Coverage)

### Source: slides-03-req-sw (`official-slides\I parte ISW - SistSW\03-Requisiti software.pdf`)
#### Page 0
> UniRoma2 - ISW/SSW 1

> Requisiti Software • Requisiti software (software requirements):  descrizione dei servizi che un sistema software  deve fornire, insieme ai vincoli da rispettare sia in  fase di sviluppo che durante la fase di operatività  del software • Def. IEEE Std 610.12 (1990):

> (A) A condition or capability needed by a user to solve a

> problem or achieve an objective (B) A condition or capability that must be met or pos-

> sessed by a system or system component to satisfy a contract, standard, specification, or other formally imposed document (C) A documented representation of a condition or

> capability as in definition (A) or (B)

#### Page 1
> UniRoma2 - ISW/SSW 2

> Requisiti software (2)

> • I requisiti vengono generati applicando un  processo di ingegneria dei requisiti (requirements engineering)

> • Requirements abstraction (Davis, 1993)

> "If a company wishes to let a contract for a large software  development project, it must define its needs in a sufficiently  abstract way that a solution is not pre-defined. The requirements  must be written so that several contractors can bid for the  contract, offering, perhaps, different ways of meeting the client  organisation's needs. Once a contract has been awarded, the  contractor must write a system definition for the client in more  detail so that the client understands and can validate what the  software will do. Both of these documents may be called the  requirements document for the system"

#### Page 2
> UniRoma2 - ISW/SSW 3

> Tipi di requisiti • Requisiti utente (user requirements): – descrizione in linguaggio naturale, con

> eventuale aggiunta di diagrammi, dei servizi che  il sistema deve fornire e dei vincoli operativi – sono scritti per (e con) il cliente • Requisiti di sistema (system  requirements):

> – specificati mediante la stesura di un documento

> strutturato che descrive in modo dettagliato i  servizi che il sistema software deve fornire – il documento risultante costituisce un "contratto"

> tra cliente e fornitore

#### Page 3
> UniRoma2 - ISW/SSW 4

> Definizione dei termini

> • cliente (customer, client) la persona od organizzazione che paga per la  fornitura di un prodotto software

> • fornitore (supplier, contractor) la persona od organizzazione che produce  software per il cliente

> • utente finale (end-user) la persona che interagisce direttamente con il  prodotto software. Non corrisponde  necessariamente al cliente

#### Page 4
> UniRoma2 - ISW/SSW 5

> Esempi di requisiti

> • Requisito utente

> 1. Il sistema software deve fornire un mezzo per rappresentare e  visualizzare file esterni generati da altri tool • Requisito di sistema

> 1.1 L'utente deve avere la possibilità di definire il tipo dei file esterni

> 1.2 Ad ogni tipo di file esterno deve essere associato il tool che lo ha  generato

> 1.3 Ogni tipo di file esterno deve essere rappresentato mediante una  specifica icona sullo schermo

> 1.4 L'utente deve avere la possibilità di definire l'icona che  rappresenta il tipo di file esterno

> 1.5 Quando l'utente seleziona un'icona che rappresenta un file  esterno, deve poter essere eseguito il tool in grado di visualizzare  il file

#### Page 5
> UniRoma2 - ISW/SSW 6

> Chi legge i requisiti?

#### Page 6
> UniRoma2 - ISW/SSW 7

> Categorie di requisiti

> • Requisiti funzionali

> descrivono le funzionalità del sistema software, in  termini di servizi che il sistema software deve fornire, di  come il sistema software reagisce a specifici tipi di input  e di come si comporta in situazioni particolari

> Es.1 Il sistema software deve fornire un appropriato

> visualizzatore per i documenti memorizzati

> Es.2 L’utente deve essere in grado di effettuare ricerche

> sia sull’intero insieme di basi di dati che su un loro  sottoinsieme

> Es.3 Ad ogni nuovo ordine deve essere associato un

> identificatore unico (Order_ID)

#### Page 7
> UniRoma2 - ISW/SSW 8

> Categorie di requisiti (2)

> • Requisiti non funzionali descrivono le proprietà del sistema software in relazione a  determinati servizi o funzioni e possono anche essere relativi al  processo:

> • caratteristiche di efficienza, affidabilità, safety, ecc. • caratteristiche del processo di sviluppo (standard di processo, uso di  ambienti CASE, linguaggi di programmazione, metodi di sviluppo,  ecc.) • caratteristiche esterne (interoperabilità con sistemi di altre  organizzazioni, vincoli legislativi, ecc.) Es.1 Il tempo di risposta del sistema all'inserimento della password

> utente deve essere inferiore a 10 sec Es.2 I documenti di progetto (deliverable) devono essere conformi

> allo standard XYZ-ABC-12345 Es.3 Il sistema software non deve rilasciare ai suoi operatori nessuna

> informazione personale relativa ai clienti, tranne nominativo e  identificatore

#### Page 8
> UniRoma2 - ISW/SSW 9

> Categorie di requisiti (3) • Requisiti di dominio

> requisiti derivati dal dominio applicativo del sistema  software piuttosto che da necessità dettate dagli utenti

> • requisiti funzionali, nuovi o adattatati, relativi al particolare  dominio applicativo

> • requisiti non funzionali, nuovi o adattati, relativi a standard  esistenti o a procedure e regolamenti da applicare

> Es.1 I documenti di rendiconto contabile, secondo la

> normativa XYZ.03, devono essere stampati alla  ricezione e cancellati immediatamente

> Es.2 L'interfaccia utente per l'accesso al database

> magazzino deve essere conforme allo standard ZX.01

#### Page 9
> UniRoma2 - ISW/SSW 10

> Classificazione requisiti non funzionali

#### Page 10
> UniRoma2 - ISW/SSW 11

> Problemi con i requisiti software

> Ambiguità Cosa vedete?

#### Page 11
> UniRoma2 - ISW/SSW 12

> Problemi con i requisiti software (2)

> • Ambiguità: requisiti interpretabili in modo differente Esempio 1: specificare un tempo senza fornire il riferimento al fuso

> orario (in un applicazione che gestisce chiamate intercontinentali) Esempio 2: significato di "appropriato visualizzatore"

> • Interpretazione utente: visualizzatore specifico per ogni tipo di  documento • Interpretazione sviluppatore: generico visualizzatore di testo che  mostri il contenuto del documento • Incompletezza: i requisiti non includono la descrizione di  tutte le caratteristiche richieste • Inconsistenza: conflitti o contraddizioni nella descrizione  delle caratteristiche del sistema

> Esempio

> • Req 1: ogni form di input non deve contenere più di 5 campi editabili  dall'utente • Req 2: nella form di input relativa all'inserimento dei dati anagrafici  l'utente deve introdurre i seguenti dati: nome, cognome, anno di  nascita, luogo di nascita, indirizzo, telefono, fax, e-mail

#### Page 12
> UniRoma2 - ISW/SSW 13

> Verificabilità dei requisiti

> • I requisiti non funzionali espressi in modo generico

> dall'utente (es. il sistema software deve essere

> easy-to-use) possono risultare non quantificabili e

> difficili da verificare

> • E' quindi necessario esprimere i requisiti non

> funzionali usando una misura determinata che

> permetta di verificare quantitativamente se il

> requisito verrà soddisfatto dal sistema software

#### Page 13
> UniRoma2 - ISW/SSW 14

> Esempi di misure per requisiti

## 2. Secondary Evidence (BM25 Lexical + Concepts)

### Source: andrea-summary (`IS_andrea.pdf`)
#### Page 17 (BM25: 55.55)
> o  Ad esempio, tempi di risposta specifici, conformità agli standard di progetto e restrizioni sulla divulgazione di  informazioni personali.    RequisiƟ di Dominio: Questi requisiti derivano dal contesto applicativo specifico in cui il sistema verrà utilizzato.  Possono includere requisiti funzionali e non funzionali correlati a normative, procedure o regolamenti specifici del  dominio applicativo. o  Ad esempio, la conformità alle normative contabili o agli standard di interfaccia utente specifici per il dominio.  In sintesi, le categorie di requisiti aiutano a organizzare e distinguere diverse tipologie di informazioni necessarie per la  definizione e lo sviluppo di un sistema software. I requisiti funzionali definiscono ciò che il sistema farà, i requisiti non funzionali  definiscono come lo farà e le proprietà del sistema, mentre i requisiti di dominio tengono conto delle caratteristiche specifiche  dell'ambiente in cui il sistema verrà utilizzato.    Classiﬁcazione dei RequisiƟ Non Funzionali:   RequisiƟ di Performance: Definiscono le prestazioni richieste dal sistema, come tempi di risposta, velocità di  elaborazione o capacità di gestire un certo volume di dati.    RequisiƟ di Sicurezza: Riguardano la protezione dei dati, l'accesso autorizzato, l'integrità dei dati e la protezione da  attacchi.    RequisiƟ di Aﬃdabilità: Definiscono quanto il sistema deve essere affidabile, inclusa la capacità di evitare guasti o di  recuperarsi da essi.    RequisiƟ di Usabilità: Si riferiscono all'esperienza dell'utente durante l'interazione con il sistema, come l'interfaccia  utente intuitiva e la facilità d'uso.    RequisiƟ di CompaƟbilità: Definiscono la capacità del sistema di operare con altre applicazioni o piattaforme.

#### Page 17 (BM25: 51.09)
> o  Ad esempio, la fornitura di un visualizzatore per i documenti, la possibilità di effettuare ricerche e l'associazione  di un identificatore unico a ciascun ordine.    RequisiƟ Non Funzionali: Questi requisiti descrivono le proprietà del sistema in relazione alle prestazioni, all'affidabilità,  alla sicurezza e ad altre caratteristiche che non riguardano direttamente le funzionalità. Essi possono anche riguardare il  processo di sviluppo, gli standard da seguire e le normative da rispettare. o  Ad esempio, tempi di risposta specifici, conformità agli standard di progetto e restrizioni sulla divulgazione di  informazioni personali.    RequisiƟ di Dominio: Questi requisiti derivano dal contesto applicativo specifico in cui il sistema verrà utilizzato.  Possono includere requisiti funzionali e non funzionali correlati a normative, procedure o regolamenti specifici del  dominio applicativo. o  Ad esempio, la conformità alle normative contabili o agli standard di interfaccia utente specifici per il dominio.  In sintesi, le categorie di requisiti aiutano a organizzare e distinguere diverse tipologie di informazioni necessarie per la  definizione e lo sviluppo di un sistema software. I requisiti funzionali definiscono ciò che il sistema farà, i requisiti non funzionali  definiscono come lo farà e le proprietà del sistema, mentre i requisiti di dominio tengono conto delle caratteristiche specifiche  dell'ambiente in cui il sistema verrà utilizzato.    Classiﬁcazione dei RequisiƟ Non Funzionali:

#### Page 20 (BM25: 39.59)
>   Revisioni Informali: Incontri informali in cui gli stakeholder esaminano il documento dei requisiti e forniscono feedback.    Revisioni Formali: Processi strutturati di revisione che includono walkthrough* e ispezioni per analizzare in modo  dettagliato il documento dei requisiti.    ProtoƟpazione: Creazione di prototipi di parti del sistema per ottenere feedback dagli utenti e dai clienti sulla  correttezza dei requisiti.    Generazione dei Test-Case: Sviluppo di casi di test che riflettono i requisiti. La loro generazione può evidenziare  eventuali ambiguità o mancanze.    Analisi di Consistenza AutomaƟzzata: Per requisiti formali, possono essere utilizzati strumenti di analisi formale per  verificare la consistenza e la correttezza dei requisiti.    *Un walkthrough è un processo in cui un gruppo di persone, come sviluppatori, tester o stakeholder, esaminano attentamente un  prodotto, un documento o una parte del progetto per identificare errori, problemi o miglioramenti potenziali.* GESTIONE DEI REQUISITI  La gestione dei requisiti è un processo di identificazione e controllo delle modiﬁche che i requisiti subiscono durante il ciclo di  vita del progetto.    I requisiti di un sistema possono possono essere classificati in base alla loro evoluzione:   RequisiƟ stabili: Sono i requisiti che hanno una bassa probabilità di subire modifiche nel tempo. Questi sono spesso i  requisiti principali e fondamentali che non dovrebbero cambiare frequentemente.    RequisiƟ volaƟli: Sono i requisiti che hanno una probabilità elevata di subire modifiche nel tempo. Questi possono  essere ulteriormente suddivisi in:

#### Page 18 (BM25: 39.00)
>   RequisiƟ di Scalabilità: Indicano la capacità del sistema di adattarsi a un aumento del carico o dei dati senza perdita di  prestazioni.    RequisiƟ di Manutenibilità: Definiscono quanto sia facile modificare, estendere o correggere il sistema nel tempo.    RequisiƟ di Conformità: Si riferiscono alla necessità di rispettare normative, leggi o standard specifici.    Problemi con i RequisiƟ SoŌware:   Ambiguità: I requisiti possono essere interpretati in modi diversi da diverse parti interessate. Gli utenti e gli sviluppatori  possono interpretare i requisiti in modi diversi, portando a risultati diversi.     Incompletezza: I requisiti potrebbero non includere tutte le caratteristiche necessarie, portando a mancanze nel sistema  finale.    Inconsistenza: I requisiti potrebbero entrare in conflitto tra loro o contraddirsi, creando confusione e difficoltà  nell'implementazione.    Veriﬁcabilità dei RequisiƟ:  I requisiti non funzionali devono essere espressi in modo misurabile e quanƟﬁcabile per poter essere verificati.   Ad esempio, l'espressione "easy-to-use" è troppo generica e difficile da verificare, mentre una misura come "il tempo di risposta  deve essere inferiore a 2 secondi" è quantificabile e verificabile. DOCUMENTO DI SPECIFICA  Il documento di analisi dei requisiƟ, spesso chiamato "documento di specifica", è un documento ufficiale che rappresenta un  aspetto cruciale nella fase di sviluppo del software. Esso contiene una descrizione deƩagliata delle caratteristiche e dei requisiti  del sistema che deve essere sviluppato. È un punto di riferimento essenziale per i team di sviluppo, gli utenti finali e altre parti  coinvolte nel processo di sviluppo.     Il documento di specifica segue una struttura organizzata per assicurare chiarezza e coerenza. La struttura seguente è basata  sullo standard IEEE 830-1998, "IEEE Recommended PracƟce for SoŌware Requirements SpeciﬁcaƟons":

#### Page 19 (BM25: 37.80)
> 18 PROCESSO DI INGEGNERIA DEI REQUISITI  Il processo di ingegneria dei requisiti (requirements engineering) è una fase cruciale nello sviluppo del software in cui si  raccolgono, analizzano e documentano le esigenze degli utenti e si traducono in requisiti chiari e dettagliati. Questo processo può  variare in base al dominio applicativo, alle persone coinvolte e all'organizzazione che sviluppa il sistema software. Tuttavia, ci  sono una serie di attività comuni a tutti i processi di ingegneria dei requisiti:   Studio di Faƫbilità (Feasibility Study)    IdenƟﬁcazione e Analisi dei RequisiƟ (Requirements ElicitaƟon and Analysis)    Speciﬁca dei RequisiƟ (Requirements SpeciﬁcaƟon)    Convalida dei RequisiƟ (Requirements ValidaƟon)    GesƟone dei RequisiƟ (Requirements Management)

#### Page 17 (BM25: 36.26)
> 16 REQUISITI SOFTWARE  I requisiti software rappresentano le descrizioni dei servizi che un sistema software deve fornire, insieme ai vincoli da rispettare  durante il processo di sviluppo e nell'operatività del software stesso. Sono essenziali per comprendere le necessità degli utenƟ,  guidare lo sviluppo e garantire che il sistema soddisfi le aspeƩaƟve e i requisiƟ del cliente.   Secondo la deﬁnizione dello standard IEEE Std 610.12 del 1990, i requisiti software possono essere visti come condizioni o  capacità necessarie per risolvere un problema o raggiungere un obiettivo da parte dell'utente o come condizioni o capacità che  devono essere soddisfatte o possedute da un sistema o componente di sistema per adempiere a un contratto, standard, specifica  o altro documento formalmente imposto.    I requisiti vengono generati attraverso il processo di ingegneria dei requisiƟ, che coinvolge la comprensione delle esigenze degli  utenti, la loro traduzione in requisiti specifici e la documentazione di tali requisiti in modo accurato e completo.    Tipi di RequisiƟ:   RequisiƟ Utente (User Requirements): Questi requisiti sono descritti in linguaggio naturale e possono essere arricchiti  con l'uso di diagrammi. Definiscono i servizi che il sistema deve fornire e i vincoli operativi. Sono scritti in collaborazione  con il cliente e rappresentano la base per capire le aspettative dell'utente finale.    RequisiƟ di Sistema (System Requirements): Questi requisiti sono specificati in dettaglio attraverso un documento  strutturato. Questo documento descrive in modo approfondito i servizi che il sistema software deve fornire. Il  documento dei requisiti di sistema diventa una sorta di "contratto" tra il cliente e il fornitore, definendo in modo chiaro  cosa il sistema dovrà realizzare.    Deﬁnizioni:

#### Page 17 (BM25: 34.42)
> REQUISITI SOFTWARE  I requisiti software rappresentano le descrizioni dei servizi che un sistema software deve fornire, insieme ai vincoli da rispettare  durante il processo di sviluppo e nell'operatività del software stesso. Sono essenziali per comprendere le necessità degli utenƟ,  guidare lo sviluppo e garantire che il sistema soddisfi le aspeƩaƟve e i requisiƟ del cliente.   Secondo la deﬁnizione dello standard IEEE Std 610.12 del 1990, i requisiti software possono essere visti come condizioni o  capacità necessarie per risolvere un problema o raggiungere un obiettivo da parte dell'utente o come condizioni o capacità che  devono essere soddisfatte o possedute da un sistema o componente di sistema per adempiere a un contratto, standard, specifica  o altro documento formalmente imposto.    I requisiti vengono generati attraverso il processo di ingegneria dei requisiƟ, che coinvolge la comprensione delle esigenze degli  utenti, la loro traduzione in requisiti specifici e la documentazione di tali requisiti in modo accurato e completo.    Tipi di RequisiƟ:   RequisiƟ Utente (User Requirements): Questi requisiti sono descritti in linguaggio naturale e possono essere arricchiti  con l'uso di diagrammi. Definiscono i servizi che il sistema deve fornire e i vincoli operativi. Sono scritti in collaborazione  con il cliente e rappresentano la base per capire le aspettative dell'utente finale.    RequisiƟ di Sistema (System Requirements): Questi requisiti sono specificati in dettaglio attraverso un documento  strutturato. Questo documento descrive in modo approfondito i servizi che il sistema software deve fornire. Il  documento dei requisiti di sistema diventa una sorta di "contratto" tra il cliente e il fornitore, definendo in modo chiaro  cosa il sistema dovrà realizzare.    Deﬁnizioni:   Cliente (Customer, Client): È la persona o l'organizzazione che paga per la fornitura del prodotto software. Il cliente  stabilisce le esigenze e i requisiti del software.    Fornitore (Supplier, Contractor): È la persona o l'organizzazione che sviluppa il software per il cliente. Deve realizzare il  software in linea con i requisiti stabiliti.    Utente Finale (End-User): È la persona che interagisce direttamente con il prodotto software. Non è necessariamente il  cliente, ma è colui che userà effettivamente il sistema.    Categorie di RequisiƟ:

#### Page 20 (BM25: 34.34)
> GESTIONE DEI REQUISITI  La gestione dei requisiti è un processo di identificazione e controllo delle modiﬁche che i requisiti subiscono durante il ciclo di  vita del progetto.    I requisiti di un sistema possono possono essere classificati in base alla loro evoluzione:   RequisiƟ stabili: Sono i requisiti che hanno una bassa probabilità di subire modifiche nel tempo. Questi sono spesso i  requisiti principali e fondamentali che non dovrebbero cambiare frequentemente.    RequisiƟ volaƟli: Sono i requisiti che hanno una probabilità elevata di subire modifiche nel tempo. Questi possono  essere ulteriormente suddivisi in: o  Mutabili: Le modifiche sono legate a cambiamenti nell'ambiente operativo, come nuovi requisiti legali o  normativi.  o  EmergenƟ: Le modifiche sono causate da una migliore comprensione del sistema software, poiché il team  acquisisce una visione più chiara delle esigenze degli utenti o dei dettagli tecnici.  o  Consequenziali: Le modifiche sono legate all'introduzione di sistemi informatici nel flusso di lavoro aziendale,  che richiedono adeguamenti nel sistema software.  o  Di compaƟbilità: Le modifiche sono legate a cambiamenti nei sistemi e nei processi aziendali, che possono  richiedere modifiche per garantire che il sistema software rimanga compatibile con l'ambiente circostante.    GesƟone delle Modiﬁche di RequisiƟ:  Le modifiche dei requisiti vanno opportunamente pianificate mediante:

#### Page 19 (BM25: 34.08)
> ATTIVITA’ DI IDENTIFICAZIONE E ANALISI DEI REQUISITI  L'identificazione e l'analisi dei requisiti sono fondamentali nella fase di ingegneria dei requisiti e comportano la comprensione  dettagliata delle esigenze degli utenƟ e la loro traduzione in requisiƟ speciﬁci e chiari. Queste attività sono spesso svolte  attraverso interazioni con il cliente e gli utenti finali, coinvolgendo vari ruoli all'interno e all'esterno dell'organizzazione.   Comprensione del Dominio: L'analista deve acquisire conoscenze approfondite sul dominio applicativo in cui il sistema  sarà utilizzato. Questo può implicare la comprensione dei processi aziendali, delle esigenze degli utenti e delle sfide  specifiche del settore.    Raccolta dei RequisiƟ: Gli stakeholder vengono coinvolti per identificare e definire i requisiti utente. Questo coinvolge  interviste, sondaggi, workshop e altre tecniche per raccogliere informazioni dettagliate sulle esigenze.    Classiﬁcazione: I requisiti raccolti vengono suddivisi in gruppi logici e coerenti. Questo aiuta a organizzare i requisiti e a  gestirli in modo più efficace.    Risoluzione dei Conﬂiƫ: Eventuali conflitti o contraddizioni tra requisiti vengono identificati e risolti. Questo assicura  che i requisiti siano coerenti e allineati tra loro.    Assegnazione delle Priorità: Gli stakeholder assegnano priorità ai requisiti in base all'importanza e all'urgenza. Questo  aiuta a stabilire quali requisiti devono essere soddisfatti prima.    Veriﬁca dei RequisiƟ: I requisiti vengono controllati per assicurarsi che siano completi, non ambigui e coerenti. Ciò  include anche la verifica che soddisfino le esigenze degli stakeholder.    Tecniche di IdenƟﬁcazione dei RequisiƟ:   Ethnography: Un metodo che coinvolge l'osservazione diretta e l'interazione con gli utenti per comprendere le loro  esigenze e il contesto in cui operano.    Casi d'Uso (BasaƟ su Scenari): Scenari dettagliati di come il sistema verrà utilizzato, aiutando a identificare i requisiti  funzionali.    ProtoƟpazione: Creazione di prototipi di parti del sistema per mostrare agli utenti e ai clienti potenziali funzionalità e  interazioni, raccogliendo feedback per definire meglio i requisiti.    Tecniche di Analisi dei RequisiƟ:

#### Page 20 (BM25: 33.66)
> CONVALIDA DEI REQUISITI  La convalida dei requisiti è una fase cruciale nella fase di ingegneria dei requisiti. L'obiettivo principale è veriﬁcare se il  documento dei requisiti, derivato dall'analisi, rappresenta correttamente le aspettative del cliente e se contiene requisiti chiari,  completi e coerenti. Scoprire errori in questa fase è essenziale per evitare costosi rework e problemi nelle fasi successive del  ciclo di vita del progetto.    Controlli da EﬀeƩuare:   Validità: I requisiti devono rappresentare correttamente le esigenze degli stakeholder e del cliente. Devono rispondere  alle vere necessità e obiettivi.    Consistenza: I requisiti non devono entrare in conflitto tra loro o contraddirsi. Devono essere armoniosi e in accordo tra  loro.    Completezza: Tutti gli aspetti rilevanti del sistema devono essere coperti dai requisiti. Non dovrebbero esserci omissioni  significative.    Realizzabilità: I requisiti devono essere tecnologicamente fattibili e realizzabili entro i vincoli del progetto.    Veriﬁcabilità: Deve essere possibile verificare se i requisiti sono stati soddisfatti attraverso test e altre attività di verifica.    Tecniche di Convalida dei RequisiƟ:   Revisioni Informali: Incontri informali in cui gli stakeholder esaminano il documento dei requisiti e forniscono feedback.    Revisioni Formali: Processi strutturati di revisione che includono walkthrough* e ispezioni per analizzare in modo  dettagliato il documento dei requisiti.    ProtoƟpazione: Creazione di prototipi di parti del sistema per ottenere feedback dagli utenti e dai clienti sulla  correttezza dei requisiti.    Generazione dei Test-Case: Sviluppo di casi di test che riflettono i requisiti. La loro generazione può evidenziare  eventuali ambiguità o mancanze.    Analisi di Consistenza AutomaƟzzata: Per requisiti formali, possono essere utilizzati strumenti di analisi formale per  verificare la consistenza e la correttezza dei requisiti.    *Un walkthrough è un processo in cui un gruppo di persone, come sviluppatori, tester o stakeholder, esaminano attentamente un  prodotto, un documento o una parte del progetto per identificare errori, problemi o miglioramenti potenziali.*

### Source: theory-summary (`teoria.pdf`)
#### Page 9 (BM25: 58.70)
> fornire. Ci sono 3 categorie: Requisiti Funzionali I requisiti funzionali descrivono le funzionalità specifiche che il sistema deve offrire.

#### Page 9 (BM25: 58.15)
> input o situazioni. Requisiti non Funzionali I requisiti non funzionali specificano le qualità e le caratteristiche che il sistema

#### Page 9 (BM25: 52.84)
> • Usabilità: Facilità d'uso, accessibilità, design dell'interfaccia cliente. Requisiti di Dominio Un requisito di dominio descrive un comportamento, un vincolo o una regola che

#### Page 3 (BM25: 41.63)
> prodotto software progredisce e l'ordine con cui vanno eseguite, dalla definizione dei requisiti alla dismissione. Modello Build & Fix

#### Page 50 (BM25: 40.73)
> software per rispondere a nuovi requisiti o cambiamenti. 3. Attributi di qualità

#### Page 5 (BM25: 38.57)
> modello incrementale prevede un ciclo ripetuto di: 1. Analisi dei requisiti (parziali) 2. Progettazione

#### Page 9 (BM25: 33.81)
> Requisiti non Funzionali I requisiti non funzionali specificano le qualità e le caratteristiche che il sistema deve possedere, senza riferirsi a funzionalità specifiche. Essi influenzano

#### Page 9 (BM25: 32.91)
> Requisiti Funzionali I requisiti funzionali descrivono le funzionalità specifiche che il sistema deve offrire. Essi definiscono le azioni che il sistema deve compiere in risposta a determinati

#### Page 52 (BM25: 30.28)
> • Design Standard (standard di progettazione, si vuole cioè trasformare i requisiti software in progettazione software utilizzando un’adeguata documentazione progettuale come linguaggi di modellazione, specifiche di

#### Page 9 (BM25: 30.25)
> fornire, insieme ai vincoli da rispettare sia in fase di sviluppo che durante la fase di opertività del software. Esistono due categorie di requisiti SW: • Requisiti utente: Descrizione in liguaggio naturale dei servizi che il sistema

## 3. Visual Assets Candidates

- **asset_id**: 9500a9d3-77fa-4794-8826-7ef60603761a
  source: slides-03-req-sw
  page: 0
  type: embedded_image
  path: `22f896a8_p0_i0.png`

- **asset_id**: f4b53ffb-c04e-40c3-a20b-f1c59b5bfb85
  source: slides-03-req-sw
  page: 0
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b895ed5b-b3d7-44bb-b3cd-251bf59324f5
  source: slides-03-req-sw
  page: 1
  type: embedded_image
  path: `22f896a8_p1_i0.png`

- **asset_id**: 52dca446-2bb4-470b-a3a8-b2d10697b142
  source: slides-03-req-sw
  page: 1
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 54b12386-56ac-4915-8d6d-34f4a4caa1ed
  source: slides-03-req-sw
  page: 2
  type: embedded_image
  path: `22f896a8_p2_i0.png`

- **asset_id**: 33a5557a-afac-4738-ad0c-866aa3cc450c
  source: slides-03-req-sw
  page: 2
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: c0e3d2f7-fc0f-4b74-a7ee-08ab1ed65f86
  source: slides-03-req-sw
  page: 3
  type: embedded_image
  path: `22f896a8_p3_i0.png`

- **asset_id**: 2fa7b858-5cc1-4520-b330-44795d818f18
  source: slides-03-req-sw
  page: 3
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: d9f34759-23f5-46d6-98f8-7922af22ec80
  source: slides-03-req-sw
  page: 4
  type: embedded_image
  path: `22f896a8_p4_i0.png`

- **asset_id**: f5b0eb53-4544-4fb7-b5d1-b1d35e6dbfb8
  source: slides-03-req-sw
  page: 4
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: cbc315c7-f11c-40e5-b85e-686c44aac175
  source: slides-03-req-sw
  page: 5
  type: embedded_image
  path: `22f896a8_p5_i0.png`

- **asset_id**: 52fe1dd5-764a-4ecd-8ebd-99f637799745
  source: slides-03-req-sw
  page: 5
  type: embedded_image
  path: `22f896a8_p5_i1.png`

- **asset_id**: 0d1a7941-fa83-4f77-9d5d-29400dd0f918
  source: slides-03-req-sw
  page: 5
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 096b96b8-0016-40d0-805a-298f29ca965f
  source: slides-03-req-sw
  page: 6
  type: embedded_image
  path: `22f896a8_p6_i0.png`

- **asset_id**: 2ec10fbb-8c2c-4c48-9418-1d138070ee8f
  source: slides-03-req-sw
  page: 6
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 8071f925-8759-4b30-904a-abc68a344790
  source: slides-03-req-sw
  page: 7
  type: embedded_image
  path: `22f896a8_p7_i0.png`

- **asset_id**: 36b0d11f-8172-4305-9f8c-c78cadaf9dce
  source: slides-03-req-sw
  page: 7
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 385c8d2f-a6ba-44d3-81e0-2e8996ae56e2
  source: slides-03-req-sw
  page: 8
  type: embedded_image
  path: `22f896a8_p8_i0.png`

- **asset_id**: c3166fc2-82f8-4ad4-9f21-524a55e7a4f2
  source: slides-03-req-sw
  page: 8
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 3a81b856-bdb1-4c80-8c85-5cff0be03827
  source: slides-03-req-sw
  page: 9
  type: embedded_image
  path: `22f896a8_p9_i0.jpeg`

- **asset_id**: 258722ac-9179-4719-83a9-88ea5cef2c41
  source: slides-03-req-sw
  page: 9
  type: embedded_image
  path: `22f896a8_p9_i1.png`

- **asset_id**: 2e93f4ed-8572-4424-a508-697283410754
  source: slides-03-req-sw
  page: 9
  type: embedded_image
  path: `22f896a8_p9_i2.png`

- **asset_id**: 693be234-e2dd-404c-8317-9a72cc57d9be
  source: slides-03-req-sw
  page: 9
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 21efa5e8-41f8-47e1-80cd-9c9056e27994
  source: slides-03-req-sw
  page: 10
  type: embedded_image
  path: `22f896a8_p10_i0.png`

- **asset_id**: 0989e251-231c-4a02-8d5d-c285faec137b
  source: slides-03-req-sw
  page: 10
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: c2a20fd6-f005-42b0-a462-742087853d0d
  source: slides-03-req-sw
  page: 11
  type: embedded_image
  path: `22f896a8_p11_i0.png`

- **asset_id**: 33dfa867-bf21-4163-8e48-927472f8c89a
  source: slides-03-req-sw
  page: 11
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: ff2aa418-0a90-440b-8e5f-f8b451453dad
  source: slides-03-req-sw
  page: 12
  type: embedded_image
  path: `22f896a8_p12_i0.png`

- **asset_id**: 63ea7701-cbc1-4a02-b0ae-0ccbfc8315df
  source: slides-03-req-sw
  page: 12
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 00b89b5e-c38c-4bbe-8866-42cbf906ad55
  source: slides-03-req-sw
  page: 13
  type: embedded_image
  path: `22f896a8_p13_i0.png`

- **asset_id**: f94b8861-fa88-48a7-8928-8ed5ea942a56
  source: slides-03-req-sw
  page: 13
  type: embedded_image
  path: `22f896a8_p13_i1.png`

- **asset_id**: 4dfba590-728a-43d7-9264-ce6f2817f907
  source: slides-03-req-sw
  page: 13
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

