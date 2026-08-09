# Topic Context

**topic_id**: data-modeling
**title**: OOA e Modello dei Dati (Identificazione Classi)

## Retrieval Metadata
- Primary fragments: 530
- Secondary fragments: 10
- Visual assets candidate: 282
- Estimated context tokens: ~8453

## 1. Primary Evidence (Official Coverage)

### Source: slides-05a-ooa (`official-slides\I parte ISW - SistSW\05a-OOA.pdf`)
#### Page 0
> Object Oriented Analysis - OOA

> • La fase di OOA definisce, secondo un approccio ad  oggetti, COSA un prodotto software deve fare (mentre la  fase di OOD definisce, sempre secondo un approccio ad  oggetti, COME un prodotto software deve fare quanto  specificato in fase di OOA)

> • OOA e OOD devono fornire, ciascuno dal proprio punto di  vista, una rappresentazione corretta, completa e  consistente:

> – degli aspetti statici e strutturali relativi ai dati (modello dei dati)

> – degli aspetti funzionali del sistema (modello comportamentale)

> – degli aspetti di "controllo" e di come le funzioni del modello

> comportamentale modificano i dati introdotti nel modello dei dati  (modello dinamico)

> UniRoma2 - ISW/SSW 1

#### Page 1
> Metodi di OOA

> • Un metodo di OOA definisce l'insieme di procedure, tecniche e  strumenti per un approccio sistematico alla gestione e allo sviluppo  della fase di OOA • L'input di un metodo di OOA è costituito dall'insieme dei requisiti  utente (contenuti nel documento di analisi dei requisiti) • L'output di un metodo di OOA è costituito dall'insieme dei modelli del  sistema che definiscono la specifica del prodotto software (e che sono  anch'essi contenuti nel documento di analisi dei requisiti) • I metodi di OOA fanno principalmente uso di notazioni visuali (diagrammi), ma possono essere affiancati da metodi tradizionali per  la definizione di requisiti di sistema di tipo testuale (in linguaggio  naturale strutturato) • Lo sviluppo dei modelli di OOA non è un processo sequenziale (prima  modello dei dati, poi modello comportamentale, infine modello  dinamico) • La costruzione dei modelli avviene in parallelo, e ciascun modello  fornisce informazioni utili per gli altri modelli • I metodi di OOA fanno uso di un approccio iterativo, con aggiunta di  dettagli per raffinamenti successivi (iterazioni)

> UniRoma2 - ISW/SSW 2

#### Page 2
> Alcuni metodi di OOA (e OOD)

> • Catalysis: metodo OO particolarmente indicato per lo sviluppo di  sistemi software a componenti distribuiti.

> • Objectory: metodo ideato da I. Jacobson che fonda lo sviluppo di  prodotti software ad oggetti sull’individuazione dei casi d’uso utente  (use case driven).

> • Shlaer/Mellor: metodo OO particolarmente indicato per lo sviluppo di  sistemi software real-time.

> • OMT (Object Modeling Technique): metodo sviluppato da J.  Rumbaugh basato su tecniche di modellazione del software iterative.  Pone in particolare risalto la fase di OOA.

> • Booch: metodo basato su tecniche di modellazione del software  iterative. Pone in particolare risalto la fase di OOD.

> • Fusion: metodo sviluppato dalla HP a metà degli anni novanta.  Rappresenta il primo tentativo di standardizzazione per lo sviluppo di  software orientato agli oggetti. Si basa sulla fusione dei metodi OMT e  Booch.

> UniRoma2 - ISW/SSW 3

#### Page 3
> Notazioni per OOA (e OOD)

> • Ciascun metodo di OOA (e OOD) fa uso di una propria  notazione per la rappresentazione dei modelli del sistema • Al fine di unificare le notazioni per i metodi di OOA e OOD è  stato introdotto il linguaggio UML (Unified Modeling  Language), adottato nel 1997 come standard OMG (Object  Management Group) • UML è un linguaggio standard per la descrizione di sistemi software (orientati agli oggetti). Si compone di nove  formalismi di base (diagrammi con semantica e notazione  data) e di un insieme di estensioni. • UML è un linguaggio di descrizione, non è un metodo né  definisce un processo • Unified Software Development Process (in breve Unified  Process) è un tentativo di standardizzazione di processo di  sviluppo di sistemi orientati agli oggetti basato sull’uso di  UML.

> UniRoma2 - ISW/SSW 4

#### Page 4
> Diagrammi UML

> UniRoma2 - ISW/SSW 5

#### Page 5
> Formalismi UML

> I nove formalismi di base dello UML sono:

> 1. Use case diagram evidenziano la modalità (caso d’uso) con cui gli utenti (attori)  utilizzano il sistema. Possono essere usati come supporto per la  definizione dei requisiti utente. 2. Class diagram consentono di rappresentare le classi con le relative proprietà  (attributi, operazioni) e le associazioni che le legano. 3. State diagram rappresentano il comportamento dinamico dei singoli oggetti di  una classe in termini di stati possibili e transizioni di stato per  effetto di eventi. 4. Activity diagram sono particolari state diagram, in cui gli stati rappresentati  rappresentano azioni in corso di esecuzione. Sono  particolarmente indicati per la produzione di modelli di work-flow.

> UniRoma2 - ISW/SSW 6

#### Page 6
> Formalismi UML (2)

> 5. Sequence diagram evidenziano le interazioni (messaggi) che oggetti di classi diverse si  scambiano nell’ambito di un determinato caso d’uso, ordinate in  sequenza temporale. A differenza dei diagrammi di collaborazione,  non evidenziano le relazioni tra oggetti. 6. Collaboration diagram descrivono le interazioni (messaggi) tra oggetti diversi,  evidenziando le relazioni esistenti tra le singole istanze. 7. Object diagram permettono di rappresentare gli oggetti e le relazioni tra essi  nell’ambito di un determinato caso d’uso. 8. Component diagram evidenziano la strutturazione e le dipendenze esistenti tra  componenti software. 9. Deployment diagram evidenziano le configurazioni dei nodi elaborativi di un sistema real- time ed i componenti, processi ed oggetti assegnati a tali nodi.

> UniRoma2 - ISW/SSW 7

#### Page 7
> Modello dei dati

> • Rappresenta da un punto di vista statico e strutturale l'organizzazione logica dei dati da elaborare • Le strutture dati sono definite mediante lo stato degli  oggetti, che viene determinato dal valore assegnato ad  attributi e associazioni • Il modello dei dati viene specificato mediante il formalismo  dei class diagram che permette di definire:

> – classi – attributi di ciascuna classe – operazioni di ciascuna classe – associazioni tra classi • Il modello dei dati è di fondamentale importanza, visto  che, secondo l'approccio ad oggetti, un sistema software è  costituito da un insieme di oggetti (classificati) che  collaborano

> UniRoma2 - ISW/SSW 8

#### Page 8
> Modello dei dati (2)

> • Il modello dei dati viene costruito in modo iterativo ed  incrementale • Si tratta di un processo creativo, in cui giocano un ruolo  importante sia l'esperienza dell'analista che la  comprensione del dominio applicativo  • Durante la fase iniziale di costruzione del modello dei dati  occorre concentrarsi sulle cosiddette entity classes,  ovvero quelle classi che definiscono il dominio applicativo e  che sono rilevanti per il sistema • Le control classes (che gestiscono la “logica” del sistema) e  boundary classes (che rappresentano l'interfaccia utente)  vengono introdotte successivamente, usando le  informazioni del modello comportamentale • Le operazioni di ciascuna classe vengono identificate a  partire dal modello comportamentale, per cui vengono  inizialmente trascurate

> UniRoma2 - ISW/SSW 9

#### Page 9
> Approcci per l'identificazione delle classi

> • Noun phrase

> • Common class patterns

> • Use case driven

> • CRC

> • Mixed

> UniRoma2 - ISW/SSW 10

#### Page 10
> Approccio noun phrase

> • Una frase nominale (noun phrase) è una frase in cui il  sostantivo ha una prevalenza sulla parte verbale (sono  frasi di tipo assertivo)

> • I sostantivi delle frasi nominali usate per la stesura dei  requisiti utente sono considerati candidate classes

> • La lista delle candidate classes viene suddivisa in tre  gruppi:

> – Irrelevant (non appartengono al dominio applicativo e quindi

> possono essere scartate)

> – Relevant (evidenziano caratteristiche di entity classes)

> – Fuzzy (non si hanno sufficienti informazioni per classificarle come

> relevant o irrelevant, vanno analizzate successivamente)

> • Si assume che l'insieme dei requisiti utente sia completo e  corretto

> UniRoma2 - ISW/SSW 11

#### Page 11
> Approccio common class patterns

> • Basato sulla teoria della classificazione • Le candidate classes vengono identificate a partire da  gruppi (pattern) di classi predefinite:

> – Concept (es. Reservation) – Events (es. Arrival) – Organization (es. AirCompany) – People (es. Passenger) – Places (es. TravelOffice) • Non è un approccio sistematico, ma può rappresentare  una utile guida • A differenza dell'approccio noun phrase, non si concentra  sul documento dei requisiti utente • Può causare problemi di interpretazione dei nomi delle  classi

> UniRoma2 - ISW/SSW 12

#### Page 12
> Approccio use case driven

> • Si assume che: – Siano già stati sviluppati gli use case diagram ( e

> possibilmente anche i sequence diagram più  significativi) – Per ogni use case sia fornita una descrizione testuale

> dello scenario di funzionamento • Simile all'approccio noun phrase (si considera  l'insieme degli use case come insieme dei  requisiti utente) • Si assume che l'insieme degli use case sia  completo e corretto • Approccio function-driven (o problem-driven secondo la terminologia object oriented)

> UniRoma2 - ISW/SSW 13

#### Page 13
> Approccio CRC

> • L'approccio CRC (Class - Responsibility  – Collaborators) è basato su riunioni in  cui si fa uso di apposite card • Ciascuna card rappresenta una classe,  e contiene tre compartimenti, che  identificano:

> – Il nome della classe – Le responsabilità assegnate alla classe – Il nome di altre classi che collaborano

> con la classe • Le classi vengono identificate  analizzando come gli oggetti  collaborano per svolgere le funzioni di  sistema • Approccio utile per

> – Verifica di classi identificate con altri

> metodi – Identificazione di attributi e operazioni di

> ciascuna classe

> UniRoma2 - ISW/SSW 14

#### Page 14
> Approccio mixed

> • Basato su elementi presenti in ciascuno degli  approcci precedenti

> • Un possibile scenario potrebbe essere il  seguente:

> 1. L'insieme iniziale delle classi viene identificato in base  all'esperienza dell'analista, facendosi eventualmente  guidare dall'approccio common class patterns

> 2. Altre classi possono essere aggiunte usando sia  l'approccio noun phrase che l'approccio use case  driven (se gli use case diagram sono disponibili)

> 3. Infine l'approccio CRC può essere usato per verificare  l'insieme delle classi identificate

> UniRoma2 - ISW/SSW 15

#### Page 15
> Linee guida per l'identificazione delle entity classes 1. Ogni classe deve avere un ben preciso statement of  purpose 2. Ogni classe deve prevedere un insieme di istanze (oggetti) – le cosiddette singleton classes (per la quali si  prevede una singola istanza) non sono di norma  classificabili come entity classes 3. Ogni classe deve prevedere un insieme di attributi (non  un singolo attributo) 4. Distinguere tra elementi che possono essere modellati  come classi o come attributi 5. Ogni classe deve prevedere un insieme di operazioni (anche se inizialmente le operazioni vengono trascurate, i  servizi che la classe mette a disposizione sono  implicitamente derivabili dallo statement of purpose)

> UniRoma2 - ISW/SSW 16

#### Page 16
> Casi di studio (*)

> A. University Enrolment

> B. Video Store

> C. Contact Management

> D. Telemarketing

> (*) MACIASZEK, L.A. (2001): Requirements Analysis and

> System Design. Developing Information Systems with UML, Addison Wesley

> UniRoma2 - ISW/SSW 17

#### Page 17
> A. University Enrolment

> Problem statement

> • The university offers  – Undergraduate and postgraduate degrees  – To full-time and part-time students • The university structure – Divisions containing departments – Single division administers each degree – Degree may include courses from other divisions • University enrolment system – Individually tailored programs of study – Prerequisite courses  – Compulsory courses – Restrictions

> • Timetable clashes • Maximum class sizes, etc.

> UniRoma2 - ISW/SSW 18

#### Page 18
> A. University Enrolment

> Problem statement (2)

> • The system is required to  – Assist in pre-enrolment activities  – Handle the enrolment procedures • Pre-enrolment activities  – Mail-outs of

> • Last semester's examination grades to students  • Enrolment instructions  • During enrolment  – Accept students' proposed programs of study  – Validate for prerequisites, timetable clashes, class sizes, special

> approvals, etc.  • Resolutions to some of the problems may require  consultation with academic advisers or academics in  charge of course offerings

> UniRoma2 - ISW/SSW 19

#### Page 19
> B. Video Store Problem statement

> • The video store

> – Rentals of video tapes and disks to customers

> – All video tapes and disks bar-coded

> – Customer membership also be bar-coded.

> • Existing customers can place reservations on  videos to be collected at specific date

> • Answering customer enquiries, including enquiries  about movies that the video store does not stock  (but may order on request)

> UniRoma2 - ISW/SSW 20

#### Page 20
> C. Contact Management

> Problem statement

> • The market research company with established customer base of  organizations that buy market analysis reports • The company is constantly on the search for new customers  • Contact management system

> – Prospective customers – Actual customers – Past customers • The new contact management system to be developed internally and  be available to all employees in the company, but with varying levels  of access

> – Employees of Customer Services Department will take the ownership of

> the system • The system to permit flexible scheduling and re-scheduling of contact- related activities so that the employees can successfully collaborate to  win new customers and foster existing relationships

> UniRoma2 - ISW/SSW 21

#### Page 21
> D. Telemarketing Problem statement

> • The charitable society sells lottery tickets to  raise funds

> – Campaigns to support currently important charitable

> causes – Past  contributors  (supporters)  targeted  through  telemarketing and/or direct mail-outs  • Rewards (special bonus campaigns) – For bulk buying – For attracting new contributors • The society does not randomly target potential  supporters by using telephone directories or  similar means

> UniRoma2 - ISW/SSW 22

#### Page 22
> D. Telemarketing Problem statement (2)

> • Telemarketing application

> – To  support  up  to  fifty  telemarketers  working  simultaneously

> – To schedule the phone calls according to pre-specified

> priorities and other known constraints

> – To dial up the scheduled phone calls

> – To re-schedule unsuccessful connections

> – To arrange other telephone callbacks to supporters

> – To records the conversation outcomes, including ticket

> orders and any changes to supporter records

> UniRoma2 - ISW/SSW 23

#### Page 23
> Example A.1 – University Enrolment

> • Consider the following requirements for  the University Enrolment system and  identify the candidate classes:

> – Each university degree has a number of

> compulsory courses and a number of  elective courses.

> Degree Course

> CompulsoryCourse ElectiveCourse

> Relevant Fuzzy

> UniRoma2 - ISW/SSW 24

#### Page 24
> Example A.1 – University Enrolment

> • More requirements:

> – Each course is at a given level and has a credit-point

> value

> – A course can be part of any number of degrees

> – Each degree specifies minimum total credit points value

> required for degree completion

> – Students may combine course offerings into programs

> of study suited to their individual needs and leading to

> the degree in which enrolled

> UniRoma2 - ISW/SSW 25

#### Page 25
> Example A.1– University Enrolment (solution)

> Relevant classes Fuzzy classes

> Course CompulsoryCourse

> Degree ElectiveCourse

> Student StudyProgram

> CourseOffering

> UniRoma2 - ISW/SSW 26

#### Page 26
> Example B.1 – Video Store

> • Consider the following requirements for the  Video Store system and identify the  candidate classes:

> – The video store keeps in stock an extensive

> library of current and popular movie titles. A  particular movie may be held on video tapes or  disks.

> MovieTitle VideoTape VideoDisk

> VideoStore Stock Library

> Relevant Irrelevant

> UniRoma2 - ISW/SSW 27

#### Page 27
> Example B.1 – Video Store

> • More requirements:

> – Video tapes are in either "Beta" or "VHS" format

> – Video disks are in DVD format

> – Each movie has a particular rental period (expressed in

> days), with a rental charge to that period

> – The video store must be able to immediately answer

> any inquiries about a movie's stock availability and how

> many tapes and/or disks are available for rental

> – The current condition of each tape and disk must be

> known and recorded

> UniRoma2 - ISW/SSW 28

#### Page 28
> Example B.1 – Video Store (solution)

> Relevant classes Fuzzy classes

> MovieTitle RentalConditions

> VideoMedium

> VideoTape

> VideoDisk (or DVDDisk) BetaTape

> VHSTape

> UniRoma2 - ISW/SSW 29

#### Page 29
> Example C.1 – Contact Management

> • Consider the following requirements for the Contact Management  system and identify the candidate classes:

> – To "keep in touch" with current and prospective customer base

> – To store the names, phone numbers, postal and courier

> addresses, etc. of organizations and contact persons in these  organizations

> – To schedule tasks and events for the employees with regard to

> relevant contact persons

> – Employees can schedule tasks and events for other employees or

> for themselves

> – A task is a group of events that take place to achieve a result (e.g.

> to solve customer's problem)

> – Typical types of events are: phone call, visit, sending a fax,

> arranging for training, etc.

> UniRoma2 - ISW/SSW 30

#### Page 30
> Example C.1 – Contact Management (solution)

> Relevant classes Fuzzy classes

> Organization CurrentOrg

> Contact ProspectiveOrg

> Employee PostalAddress

> Task CourierAddress

> Event

> UniRoma2 - ISW/SSW 31

#### Page 31
> Example D.1 – Telemarketing

> Business use case diagram

> Schedule Phone

> Conversation

> CRUD Campaign and Supporter Details Telemarketer

> Enter Conversation

> Outcome

> Supporter

> UniRoma2 - ISW/SSW 32

#### Page 32
> Example D.1 - Telemarketing

> • Consider the following textual description for the  Telemarketing system’s use cases and identify  the candidate classes:

> – The telemarketer requests the system that the phone

> call to a supporter be scheduled and dialed up – Upon successful connection, the telemarketer offers

> lottery tickets to the supporter. During a conversation,  the telemarketer may need to access and modify both  campaign and supporter details (CRUD, create – read – update – delete) – Finally, the telemarketer enters the conversation

> outcome, i.e. the successful or unsuccessful results of  the telemarketing action

> UniRoma2 - ISW/SSW 33

#### Page 33
> Example D.1 – Telemarketing (solution)

> UniRoma2 - ISW/SSW 34

#### Page 34
> Linee guida per la specifica delle classi • Nomi di classe – Associare ad ogni classe un nome significativo nello specifico

> dominio applicativo – Adottare una convenzione standard per assegnare nomi alle

> classi, ad esempio:

> nome singolare, parole multiple devono essere congiunte, con  l'iniziale di ciascuna parola in carattere maiuscolo (es.  PostalAddress) – Definire una lunghezza massima per i nomi delle classi (non più di

> 30 caratteri) • Attributi e operazioni – Considerare inizialmente solo attributi che caratterizzano possibili

> stati di interesse per gli oggetti – Adottare una convenzione standard per assegnare nomi agli

> attributi, ad esempio:

> le parole devono essere scritte in carattere minuscolo, separate da un  carattere di underscore (es. street_name) – Ritardare l'aggiunta di operazioni fino al momento in cui sia

> disponibile il modello comportamentale, da cui vanno derivate

> UniRoma2 - ISW/SSW 35

#### Page 35
> Example A.2 – University Enrolment

> • Refer to Example A.1  • Consider the following additional requirements  from the Requirements Document:

> – A student's choice of courses may be restricted by

> timetable clashes and by limitations on the number of  students who can be enrolled in the current course  offering.

> UniRoma2 - ISW/SSW 36

#### Page 36
> Example A.2 – University Enrolment

> • More requirements:

> – A student's proposed program of study is entered in the on-line

> enrolment system

> – The system checks the program's consistency and reports any

> problems

> – The problems need to be resolved with the help of an academic

> adviser

> – The final program of study is subject to academic approval by the

> delegate of the Head of Division and it is then forwarded to the

> Registrar

> UniRoma2 - ISW/SSW 37

#### Page 37
> Example A.2 – University Enrolment (solution)

> Degree <<PK>> degree_name : String total_credit_points : Integer

> Course <<PK>> course_code : String <<CK>> course_name : String credit_points : Integer

> Student <<PK>> student_id : String student_name : String

> CourseOffering year : Date semester : Integer enrolment_quota : Integer

> StudyProgram year : Date semester : Integer

> UniRoma2 - ISW/SSW 38

#### Page 38
> Example B.2 – Video Store

> • Refer to Example B.1  • The additional requirements are: – The rental charge differs depending on video

> medium: tape or disk (but it is the same for the  two categories of tapes: Beta and VHS).

> UniRoma2 - ISW/SSW 39

#### Page 39
> Example B.2 – Video Store

> • More requirements:

> – The system should accommodate future video

> storage formats in addition to VHS tapes, Beta  tapes and DVD disks

> – The employees frequently use a movie code,

> instead of movie title, to identify the movie

> – The same movie title may have more than one

> release by different directors

> UniRoma2 - ISW/SSW 40

#### Page 40
> Example B.2 – Video Store (solution)

> MovieTitle <<PK>> movie_code : String movie_title : String director : String / is_in_stock : Boolean

> VideoTape

> BetaTape VHSTape

> VideoMedium video_condition : Byte $ number_currently_available : Integer

> VideoDisk RentalConditions rental_period_in_days : Integer rental_charge_per_period : Currency

> DVDDisk

> UniRoma2 - ISW/SSW 41

#### Page 41
> Example C.2 – Contact Management

> • Refer to Example C.1 and consider the  following additional information

> – A customer is considered current if there exists

> a contract with that customer for delivery of our  products or services. Contract management is,  however, outside the scope of our system.

> CurrentOrg ProspectiveOrg

> Fuzzy

> UniRoma2 - ISW/SSW 42

#### Page 42
> Example C.2 – Contact Management

> • More requirements:

> – Reports on contacts based on postal and courier addresses (e.g. find all

> customers by post code)

> – Date and time of the task creation are recorded

> – The "money value" of a task can be stored

> – Events for the employee are displayed on the employee's screen in the

> calendar-like pages (one day per page).

> • The priority of each event (low, medium or high) is visually distinguished on the  screen

> – Not all events have a “due time” - some are “untimed”

> – Event creation time cannot be changed, but the due time can.

> – Event completion date and time are recorded

> – The system stores identifications of employees who created tasks and

> events, who are scheduled to do the event (“due employee”), and who  completed the event

> UniRoma2 - ISW/SSW 43

#### Page 43
> Example C.2 – Contact Management (solution)

> Organization <<PK>> organization_id : Integer organization_name : String phone : String fax : String email : String is_current : Boolean

> Contact <<PK>> contact_id : Integer family_name : String first_name : String phone : String fax : String email : String

> Employee <<PK>> employee_id : String family_name : String first_name : String middle_name : String

> Task description : String created_dt : Date value : Currency

> Event description : String created_dt : Date due_dt : Date completed_dt : Date priority : Byte

> PostalAddress street : String po_box : String city : String state : String post_code : String country : String

> CourierAddress street_and_directions : String city : String state : String country : String

> UniRoma2 - ISW/SSW 44

#### Page 44
> Example D.2 - Telemarketing

> • Refer to Example D.1 • Consider the following additional information  – Each campaign

> • Has a title that is generally used for referring to it • Has also a unique code for internal reference  • Runs over a fixed period of time – Soon after the campaign is closed, the prizes are drawn and the

> holders of winning tickets are advised

> UniRoma2 - ISW/SSW 45

#### Page 45
> Example D.2 - Telemarketing

> • More requirements:

> – Tickets are uniquely numbered within each campaign

> – The total number of tickets in a campaign, number of tickets sold

> so far, and the current status of each ticket are known (e.g.  available, ordered, paid for, prize winner)

> – To determine the performance of the society's telemarketers, the

> duration of calls and the successful call outcomes (i.e. resulting in  ordered tickets) are recorded

> – Extensive information about supporters is maintained

> • Contact details (address, phone number, etc.)

> • Historical details such as the first and most recent dates when a  supporter had participated in a campaign

> • Any known supporter's preferences and constraints (e.g. times not to  call, usual credit card number)

> UniRoma2 - ISW/SSW 46

#### Page 46
> Example D.2 - Telemarketing

> • More requirements:

> – Telemarketing calls are made according to their priorities

> – Calls which are unanswered or where an answering machine was

> found, are rescheduled

> • Times of repeat calls are alternated

> • Number of repeat calls is limited

> – Limits may be different for different call types (e.g. a normal "solicitation"

> call may have different limit than a call to remind a supporter of an

> outstanding payment)

> – Call outcomes are categorized - success (i.e. tickets ordered), no

> success, call back later, no answer, engaged, answering machine,

> fax machine, wrong number, disconnected.

> UniRoma2 - ISW/SSW 47

#### Page 47
> Example D.2 – Telemarketing (solution)

> UniRoma2 - ISW/SSW 48

#### Page 48
> Identificazione delle associazioni • Alcuni attributi identificati con le classi  rappresentano associazioni (ogni attributo di tipo  non primitivo dovrebbe essere modellato come  un’associazione alla classe che rappresenta quel  tipo di dato) • Ogni associazione ternaria dovrebbe essere  rimpiazzata con un ciclo di associazioni binarie,  per evitare problemi di interpretazione • Nei cicli di associazioni almeno un’associazione  potrebbe essere eliminata e gestita come  associazione derivata, anche se per problemi di  efficienza spesso si introducono associazioni  ridondanti

> UniRoma2 - ISW/SSW 49

#### Page 49
> Specifica delle associazioni

> • Per assegnare nomi alle associazioni adottare la  stessa convenzione usata per gli attributi (le  parole devono essere scritte in carattere  minuscolo, separate da un carattere di  underscore)

> • Assegnare nomi di ruolo (rolename) alle estremità  dell’associazione (i rolename diventano i nomi  degli attributi nella classe all’estremità opposta  dell’associazione)

> • Determinare la molteplicità delle associazioni (ad  entrambe le estremità)

> UniRoma2 - ISW/SSW 50

#### Page 50
> Example C.3 – Contact Management

> • Refer to Examples C.1 and C.2 - specify associations • Consider, for example, the requirement:

> – The system allows producing various reports on our contacts based on

> postal and courier addresses

> PostalAddress street : String po_box : String city : String state : String post_code : String country : String

> CourierAddress street_and_directions : String city : String state : String country : String

> Contact <<PK>> contact_id : Integer family_name : String first_name : String phone : String fax : String email : String

> 0..1

> 0..1

> 0..1

> 0..1

> 0..1

> 0..1

> 0..1

> 0..1

> UniRoma2 - ISW/SSW 51

#### Page 51
> Example C.3 – Contact Management (solution – 1)

> CourierAddress street_and_directions : String city : String state : String country : String

> PostalAddress street : String po_box : String city : String state : String post_code : String country : String

> Organization <<PK>> organization_id : Integer organization_name : String phone : String fax : String email : String is_current : Boolean

> 0..1

> 0..1

> 0..1

> 0..1

> 0..1

> 0..1

> 0..1

> 0..1

> Contact <<PK>> contact_id : Integer family_name : String first_name : String phone : String fax : String email : String

> 0..1

> 0..1

> 0..1

> 0..1

> 0..1

> 0..1

> 0..1

> 0..1

> * 1

> contact

> *

> theOrganization

> 1 org_con

> UniRoma2 - ISW/SSW 52

#### Page 52
> Example C.3 – Contact Management (solution – 2)

> Task description : String created_dt : Date value : Currency

> 1

> 0..*

> theOrganization 1

> task

> 0..* 0..*

> contact

> task

> 0..*

> Employee <<PK>> employee_id : String family_name : String first_name : String middle_name : String

> 0..*

> 1

> 0..*

> 1

> emp_task

> Event description : String created_dt : Date due_dt : Date completed_dt : Date priority : Byte

> 1..* 1 event 1..*

> theTask

> 1

> 1 0..* 1 0..*

> created

> 1 0..* 1 0..* due

> 0..1 0..* 0..1 0..*

> completed

> UniRoma2 - ISW/SSW 53

#### Page 53
> Aggregazione

> • Rappresenta una relazione di tipo “whole-part” (contenimento) tra una classe composta (superset class) e  l’insieme di una o più classi componenti (subset classes) • Può assumere quattro differenti significati: – ExclusiveOwns (e.g. Book has Chapter, or Chapter is

> part of a Book)

> • Existence-dependency • Transitivity • Asymmetricity • Fixed property – Owns (e.g. Car has Tire)

> • No fixed property – Has (e.g. Division has Department)

> • No existence dependency • No fixed property – Member (e.g. Meeting has Chairperson)

> • No special properties except membership

> UniRoma2 - ISW/SSW 54

#### Page 54
> Specifica di aggregazione in UML

> • Aggregation

> – By-reference semantics

> – Hollow diamond ()

> – Corresponds to Has and Member aggregations

> • Composition

> – By-value semantics

> – Solid diamond (◆)

> – Corresponds to ExclusiveOwns and Owns

> aggregations

> UniRoma2 - ISW/SSW 55

#### Page 55
> Example A.3 – University Enrolment

> • Refer to Examples A.1 and A.2

> • Consider the following additional requirements:

> – The student's academic record to be available on demand

> – The record to include information about the student’s grades in

> each course that the student enrolled in (and has not withdrawn

> without penalty)

> – Each course has one academic in charge of a course, but

> additional academics may also teach in it

> • There may be a different academic in charge of a course each

> semester

> • There may be different academics for each course each semester

> UniRoma2 - ISW/SSW 56

#### Page 56
> AcademicRecord course_code : String year : Date semester : Integer grade : String

> Course <<PK>> course_code : String <<CK>> course_name : String credit_points : Integer

> AcademicInCharge

> Student <<PK>> student_id : String student_name : String current_fees : Money

> 0..* 0..* CourseOffering year : Date semester : Integer enrolment_quota : Integer

> 0..* 0..*

> 0..*

> 0..1

> 0..*

> 0..1

> *

> * takes

> *

> *

> takes_crsoff

> has_stud

> Example A.3 – University Enrolment (solution)

> UniRoma2 - ISW/SSW 57

#### Page 57
> Ereditarietà (generalizzazione)

> • Usata per rappresentare la condivisione di  attributi ed operazioni tra classi • Le caratteristiche comuni sono modellate in una  classe più generica (superclasse), che viene  specializzata nell’insieme di sottoclassi • Una sottoclasse eredita attributi ed operazioni  della superclasse • Caratteristiche: – Sostituibilità: un oggetto della sottoclasse è un valore

> legale per una variabile avente come tipo la  superclasse (es. una variabile di tipo Frutta può  avere un oggetto di tipo Mela come suo valore)  – Polimorfismo: la stessa operazione può avere differenti

> implementazioni nelle sottoclassi

> UniRoma2 - ISW/SSW 58

#### Page 58
> Specifica di ereditarietà in UML

> • Rappresenta relazioni di tipo:

> – “can-be”

> • Es. Student can be a TeachingAssistant

> – “is-a-kind-of”

> • Es. TeachingAssistant is a kind of Student

> • Supporto ad ereditarietà multipla

> – Es. TeachingAssistant is also a kind of Teacher

> • Viene rappresentata in UML con una linea, che

> collega la sottoclasse con la superclasse, avente

> una freccia diretta verso la superclasse

> UniRoma2 - ISW/SSW 59

#### Page 59
> Example B.3 – Video Store

> • Refer to Examples B.1 and B.2

> • The classes identified in Example B.2 imply a  generalization hierarchy rooted at the class VideoMedium

> • Extend the model to include relationships between  classes, and specify generalization relationships

> • Assume that the Video Store needs to know if a  VideoTape is a brand new tape or it was already taped  over (this can be captured by an attribute  is_taped_over)

> • Assume also that the storage capacity of a VideoDisk  allows holding multiple versions of the same movie, each  in a different language or with different endings

> UniRoma2 - ISW/SSW 60

#### Page 60
> Example B.3 – Video Store (solution)

> BetaTape VHSTape DVDDisk

> VideoTape is_taped_over : Boolean

> VideoDisk different_languages : Boolean different_endings : Boolean

> MovieTitle <<PK>> movie_code : String movie_title : String director : String / is_in_stock : Boolean

> VideoMedium video_condition : Byte $ number_currently_available : Integer 0..* 1 0..* 1

> available

> RentalConditions rental_period_in_days : Integer rental_charge_per_period : Currency

> 1..*

> 1

> 1..*

> 1 apply

> UniRoma2 - ISW/SSW 61

#### Page 61
> Object Diagram

> • Rappresentazione grafica di istanze di classi

> • Usati per

> – modellare relazioni complesse tra classi (a scopo

> esemplificativo)

> – illustrare le modifiche ai singoli oggetti durante

> l’evoluzione del sistema

> – Illustrare la collaborazione tra oggetti durante

> l’evoluzione del sistema

> UniRoma2 - ISW/SSW 62

#### Page 62
> Example A.4 – University Enrolment

> • Show an object diagram with few objects  representing the classes in Example A.3

> Don Donaldson : Student

> COMP224 : AcademicRecord

> COMP325 :

> Course

> COMP326 : AcademicRecord

> COMP225 :

> Course

> 2000 Sem2 : CourseOffering

> Rick Richards : AcademicInCharge

> UniRoma2 - ISW/SSW 63

## 2. Secondary Evidence (BM25 Lexical + Concepts)

### Source: theory-summary (`teoria.pdf`)
#### Page 11 (BM25: 32.31)
> sistema real-time e i componeti, processi ed oggetti assegnati a tali nodi. OOA - Modello dei dati Rappresenta da un punto di vista statico e strutturale l'organizzazione logica dei

#### Page 0 (BM25: 26.40)
> ▪Notazione UML ▪OOA - Modello dei dati ▪OOA - Modello Comportamentale

#### Page 10 (BM25: 25.31)
> completa e consistente: • Struttura dei dati - modello di dati • Aspetti funzionali del sistema - modello comportamentale

#### Page 11 (BM25: 22.72)
> Rappresenta da un punto di vista statico e strutturale l'organizzazione logica dei dati da elaborare. Il modello dei dati viene specificato mediante il formalismo dei class diagram permettendo di definire classi, attributi, operazioni e associzioni tra

#### Page 46 (BM25: 17.58)
> istruzioni), Data Flow (tenere traccia dei dati creati o gestiti dal programma), Strutture Dati (organizzazione dei dati). Flowgraph

#### Page 13 (BM25: 15.90)
> superclasse, avente una freccia diretta verso la superclasse. OOA - Modello Comportamentale Rappresenta gli aspetti funzionali del sistema da un punto di vista operativo,

#### Page 15 (BM25: 15.90)
> appartiene tale oggetto. Si possono usare criteri aggiuntivi, per esempio CRUD . OOA - Modello Dinamico Rappresenta il comportamento dinamico degli oggetti di una singola classe, in

#### Page 10 (BM25: 13.70)
> • Aspetti funzionali del sistema - modello comportamentale • Come le funzioni modificano i dati - modello dinamico Notazione UML

#### Page 20 (BM25: 12.74)
> stato valido a un altro valido. Garantisce dati affidabili e corretti

#### Page 17 (BM25: 12.36)
> In questo tipo di architettura abbiamo due tipologie di client: 1. Thin-Client: Tutto il processo applicativo e la gestione dei dati avviene nel server. Il client si occupa solo della presentazione.

## 3. Visual Assets Candidates

- **asset_id**: 7a843fda-2ecf-4d6e-966d-055a3ceb25f4
  source: slides-05a-ooa
  page: 0
  type: embedded_image
  path: `d0a25775_p0_i0.png`

- **asset_id**: 770cc9dd-c6cc-4216-98d5-67d23beb8225
  source: slides-05a-ooa
  page: 0
  type: embedded_image
  path: `d0a25775_p0_i1.png`

- **asset_id**: b61caf99-e155-4475-8f91-7f4e9581b1d3
  source: slides-05a-ooa
  page: 0
  type: embedded_image
  path: `d0a25775_p0_i2.png`

- **asset_id**: 8f1d511d-0d60-41e6-b022-cf43488ff1cd
  source: slides-05a-ooa
  page: 0
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: f0e901b5-cfa0-43df-b242-51ea56f8cae5
  source: slides-05a-ooa
  page: 1
  type: embedded_image
  path: `d0a25775_p1_i0.png`

- **asset_id**: 2349b9fe-d3c0-4efb-96d0-981c3ec65a1c
  source: slides-05a-ooa
  page: 1
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: fb45ced5-bb6e-466b-bb1a-5695ea937d49
  source: slides-05a-ooa
  page: 2
  type: embedded_image
  path: `d0a25775_p2_i0.png`

- **asset_id**: f097b908-bea8-4c1d-a71c-f2b7170fb3eb
  source: slides-05a-ooa
  page: 2
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: dfc3b4ae-dce3-442e-bcde-cfa73bf1e29a
  source: slides-05a-ooa
  page: 3
  type: embedded_image
  path: `d0a25775_p3_i0.png`

- **asset_id**: 34444612-3bda-422b-b440-f4b95cf4bd35
  source: slides-05a-ooa
  page: 3
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: d6dfcb24-c079-4745-b958-f7735e89c122
  source: slides-05a-ooa
  page: 4
  type: embedded_image
  path: `d0a25775_p4_i0.png`

- **asset_id**: a8b06da0-0109-45ff-97ef-2f4a27486966
  source: slides-05a-ooa
  page: 4
  type: embedded_image
  path: `d0a25775_p4_i1.png`

- **asset_id**: b9ba9161-a376-4f21-bc13-3c56dd2d8b72
  source: slides-05a-ooa
  page: 4
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 42bf9407-96ed-4049-8075-ad07c9cf7ef7
  source: slides-05a-ooa
  page: 5
  type: embedded_image
  path: `d0a25775_p5_i0.png`

- **asset_id**: 3ffdfcb8-422d-46ba-a4db-95223ce863cc
  source: slides-05a-ooa
  page: 5
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 3bed30c0-3cb0-4787-8d54-4cbb8fc05b5c
  source: slides-05a-ooa
  page: 6
  type: embedded_image
  path: `d0a25775_p6_i0.png`

- **asset_id**: 9774b146-3864-4964-9186-0a779893d382
  source: slides-05a-ooa
  page: 6
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: cf50b79f-dea8-46e9-91a3-2c460cdb48a9
  source: slides-05a-ooa
  page: 7
  type: embedded_image
  path: `d0a25775_p7_i0.png`

- **asset_id**: 05916535-1253-4caa-bb41-01cb652560ca
  source: slides-05a-ooa
  page: 7
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: f1ad3687-6fa7-40dd-b3b4-830a8bcd8007
  source: slides-05a-ooa
  page: 8
  type: embedded_image
  path: `d0a25775_p8_i0.png`

- **asset_id**: 49a6fbd5-6ec1-42e1-b4f3-d3f5f735e337
  source: slides-05a-ooa
  page: 8
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 30c88356-1085-4c73-a5a5-00414e13bd02
  source: slides-05a-ooa
  page: 9
  type: embedded_image
  path: `d0a25775_p9_i0.png`

- **asset_id**: e8745ab8-369e-415f-a0ac-049beef211ef
  source: slides-05a-ooa
  page: 9
  type: embedded_image
  path: `d0a25775_p9_i1.png`

- **asset_id**: 0fee4bf0-f286-452d-a31b-506528ef31c8
  source: slides-05a-ooa
  page: 9
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 4f9333c7-8328-4ac3-bf6d-4bddb06df7e1
  source: slides-05a-ooa
  page: 10
  type: embedded_image
  path: `d0a25775_p10_i0.png`

- **asset_id**: 172e5e2a-f980-4877-a908-7ca804283348
  source: slides-05a-ooa
  page: 10
  type: embedded_image
  path: `d0a25775_p10_i1.png`

- **asset_id**: 2ae850c9-a95f-4dfa-af28-c2326df258af
  source: slides-05a-ooa
  page: 10
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: f57dbaef-6ddb-437e-86dd-e5a1117538bb
  source: slides-05a-ooa
  page: 11
  type: embedded_image
  path: `d0a25775_p11_i0.png`

- **asset_id**: e06294bb-724d-49a6-b533-38a37a6866d5
  source: slides-05a-ooa
  page: 11
  type: embedded_image
  path: `d0a25775_p11_i1.png`

- **asset_id**: c42dbbc6-1add-40f8-912c-9f45d6baef10
  source: slides-05a-ooa
  page: 11
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 4638c1a3-8363-464e-afde-2cf6a9027725
  source: slides-05a-ooa
  page: 12
  type: embedded_image
  path: `d0a25775_p12_i0.png`

- **asset_id**: 29508970-d3f1-4a4e-8b54-8352ed23600c
  source: slides-05a-ooa
  page: 12
  type: embedded_image
  path: `d0a25775_p12_i1.png`

- **asset_id**: 6d5edb97-9e47-41fd-896a-b4ef1299a1fd
  source: slides-05a-ooa
  page: 12
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: c8150d53-21cc-4e0d-a210-3b47f63c0a70
  source: slides-05a-ooa
  page: 13
  type: embedded_image
  path: `d0a25775_p13_i0.png`

- **asset_id**: b120a4c9-7cc5-4990-af27-ee9d851b7996
  source: slides-05a-ooa
  page: 13
  type: embedded_image
  path: `d0a25775_p13_i1.png`

- **asset_id**: 25b3d76f-9ab1-472b-8acf-06deb6388059
  source: slides-05a-ooa
  page: 13
  type: embedded_image
  path: `d0a25775_p13_i2.png`

- **asset_id**: 72a2ac6f-da91-4a7d-9dd0-360ba563d336
  source: slides-05a-ooa
  page: 13
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: cf60db63-456a-4f4e-bfe1-b1065f3da5be
  source: slides-05a-ooa
  page: 14
  type: embedded_image
  path: `d0a25775_p14_i0.png`

- **asset_id**: 845ced61-1586-460f-80d6-b2e25294c7cc
  source: slides-05a-ooa
  page: 14
  type: embedded_image
  path: `d0a25775_p14_i1.png`

- **asset_id**: 976353be-6775-4a50-8c8d-e567aeab10bb
  source: slides-05a-ooa
  page: 14
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 7b4eaf03-12a5-4aee-b970-3d63f06d5b33
  source: slides-05a-ooa
  page: 15
  type: embedded_image
  path: `d0a25775_p15_i0.png`

- **asset_id**: 67b96092-eefa-48a0-959c-bac3cfdaeece
  source: slides-05a-ooa
  page: 15
  type: embedded_image
  path: `d0a25775_p15_i1.png`

- **asset_id**: ceeb3cad-316c-421c-9076-31288786a119
  source: slides-05a-ooa
  page: 15
  type: embedded_image
  path: `d0a25775_p15_i2.png`

- **asset_id**: 80dc7c7f-fbb8-4762-959a-675b5ea0fbb4
  source: slides-05a-ooa
  page: 15
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 6d6c005c-4661-4e4f-92df-587bcd93b2ca
  source: slides-05a-ooa
  page: 16
  type: embedded_image
  path: `d0a25775_p16_i0.png`

- **asset_id**: afa78c20-7fe2-4cfa-b47b-c7aa32a14f8e
  source: slides-05a-ooa
  page: 16
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 72061848-f4cb-4aeb-a64e-001b7647c6f2
  source: slides-05a-ooa
  page: 17
  type: embedded_image
  path: `d0a25775_p17_i0.png`

- **asset_id**: 6de64f0b-5d6d-4750-96dd-aa35c7db9950
  source: slides-05a-ooa
  page: 17
  type: embedded_image
  path: `d0a25775_p17_i1.png`

- **asset_id**: 506f42a1-d7b0-498c-8bf7-e42365a5a848
  source: slides-05a-ooa
  page: 17
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 6f77faae-ae24-490f-a59c-f535245cc9cb
  source: slides-05a-ooa
  page: 18
  type: embedded_image
  path: `d0a25775_p18_i0.png`

- **asset_id**: 847a3faf-cab4-412f-ad60-4623a3e1adcc
  source: slides-05a-ooa
  page: 18
  type: embedded_image
  path: `d0a25775_p18_i1.png`

- **asset_id**: 19b49a07-6980-48e4-a382-d1910876e87f
  source: slides-05a-ooa
  page: 18
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b93c2a6b-395c-4433-89d7-1047895ddbbe
  source: slides-05a-ooa
  page: 19
  type: embedded_image
  path: `d0a25775_p19_i0.png`

- **asset_id**: fe26c10b-8a16-4f9e-a80a-ea5b7814fa64
  source: slides-05a-ooa
  page: 19
  type: embedded_image
  path: `d0a25775_p19_i1.png`

- **asset_id**: d6435ce1-b7b1-44f4-b179-63891ba58484
  source: slides-05a-ooa
  page: 19
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: ab9dab8d-cb69-4684-ab7d-1568aa2728aa
  source: slides-05a-ooa
  page: 20
  type: embedded_image
  path: `d0a25775_p20_i0.png`

- **asset_id**: ef21c788-39e6-44d7-9128-9b42bf8b98ce
  source: slides-05a-ooa
  page: 20
  type: embedded_image
  path: `d0a25775_p20_i1.png`

- **asset_id**: d78310c8-1ffa-4513-b8aa-ef11b5a4fac9
  source: slides-05a-ooa
  page: 20
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 85db16e3-3ee5-4438-acde-1261f07483a5
  source: slides-05a-ooa
  page: 21
  type: embedded_image
  path: `d0a25775_p21_i0.png`

- **asset_id**: 4ef76e52-8f15-4d5e-bad6-747f4883ed3f
  source: slides-05a-ooa
  page: 21
  type: embedded_image
  path: `d0a25775_p21_i1.png`

- **asset_id**: 9a7cf720-337b-49e7-a72f-205f4cab99f3
  source: slides-05a-ooa
  page: 21
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 67895092-101e-48cf-a051-f34a99dde57d
  source: slides-05a-ooa
  page: 22
  type: embedded_image
  path: `d0a25775_p22_i0.png`

- **asset_id**: 6d7193d2-8266-414f-8223-b3dd1ebb9e77
  source: slides-05a-ooa
  page: 22
  type: embedded_image
  path: `d0a25775_p22_i1.png`

- **asset_id**: 3ef37645-3b83-4d2c-99d0-1be17cda5b4e
  source: slides-05a-ooa
  page: 22
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 3a842135-4e47-46c9-8bbc-25b3c35fa9d0
  source: slides-05a-ooa
  page: 23
  type: embedded_image
  path: `d0a25775_p23_i0.png`

- **asset_id**: e32a4316-e602-453b-989a-fad36fb8b6a7
  source: slides-05a-ooa
  page: 23
  type: embedded_image
  path: `d0a25775_p23_i1.png`

- **asset_id**: b4c2954d-344a-4eb9-880b-d253450dfef9
  source: slides-05a-ooa
  page: 23
  type: embedded_image
  path: `d0a25775_p23_i2.png`

- **asset_id**: 51624063-6351-477a-a66a-86c3a03455b0
  source: slides-05a-ooa
  page: 23
  type: embedded_image
  path: `d0a25775_p23_i3.png`

- **asset_id**: 170c96ee-8ca4-4219-9e2a-7ec17123c4af
  source: slides-05a-ooa
  page: 23
  type: embedded_image
  path: `d0a25775_p23_i4.png`

- **asset_id**: e7542c65-9fba-4858-aa5e-dfa1e8b15926
  source: slides-05a-ooa
  page: 23
  type: embedded_image
  path: `d0a25775_p23_i5.png`

- **asset_id**: 157ebee7-6fcf-4fde-8c26-ff113e0890d6
  source: slides-05a-ooa
  page: 23
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b34fc323-19e6-494c-b634-7491cc199232
  source: slides-05a-ooa
  page: 24
  type: embedded_image
  path: `d0a25775_p24_i0.png`

- **asset_id**: 1305c5d3-37d7-4152-82f4-fcab8a76be04
  source: slides-05a-ooa
  page: 24
  type: embedded_image
  path: `d0a25775_p24_i1.png`

- **asset_id**: c67b5b04-f628-4257-bfba-6c8254a758b5
  source: slides-05a-ooa
  page: 24
  type: embedded_image
  path: `d0a25775_p24_i2.png`

- **asset_id**: 05804923-a767-48bb-bde7-b29c379f3d89
  source: slides-05a-ooa
  page: 24
  type: embedded_image
  path: `d0a25775_p24_i3.png`

- **asset_id**: 1bc22634-6e86-4c0e-ab1c-0be58a63d9e8
  source: slides-05a-ooa
  page: 24
  type: embedded_image
  path: `d0a25775_p24_i4.png`

- **asset_id**: a75f1060-629f-41da-88dd-3d031e5f8e3a
  source: slides-05a-ooa
  page: 24
  type: embedded_image
  path: `d0a25775_p24_i5.png`

- **asset_id**: 3fe251f8-c626-4240-8a0b-327fe20eb37f
  source: slides-05a-ooa
  page: 24
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 7d10588d-bb83-4d6b-a974-59f1a338922c
  source: slides-05a-ooa
  page: 25
  type: embedded_image
  path: `d0a25775_p25_i0.png`

- **asset_id**: 6725b7b8-2465-4e45-bb72-8ceebd88c04a
  source: slides-05a-ooa
  page: 25
  type: embedded_image
  path: `d0a25775_p25_i1.png`

- **asset_id**: 8d9f5478-eed9-4635-849c-3c6067a063e4
  source: slides-05a-ooa
  page: 25
  type: embedded_image
  path: `d0a25775_p25_i2.png`

- **asset_id**: 3fa20894-d894-42f0-91a1-dbf50b6a9009
  source: slides-05a-ooa
  page: 25
  type: embedded_image
  path: `d0a25775_p25_i3.png`

- **asset_id**: c32d505c-c046-4054-b4bd-84fc7cf82897
  source: slides-05a-ooa
  page: 25
  type: embedded_image
  path: `d0a25775_p25_i4.png`

- **asset_id**: 1620b809-2926-431a-a73e-a1a8caf070af
  source: slides-05a-ooa
  page: 25
  type: embedded_image
  path: `d0a25775_p25_i5.png`

- **asset_id**: 35b07f00-8d9d-4dc4-84a7-1dccd856e56d
  source: slides-05a-ooa
  page: 25
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 274d6023-8d9a-4e18-85c8-f52bb071f037
  source: slides-05a-ooa
  page: 26
  type: embedded_image
  path: `d0a25775_p26_i0.png`

- **asset_id**: 95a93592-1e9b-4633-b944-106a3ccc4461
  source: slides-05a-ooa
  page: 26
  type: embedded_image
  path: `d0a25775_p26_i1.png`

- **asset_id**: 762a5484-1949-4ffc-b950-6ab57a2607b2
  source: slides-05a-ooa
  page: 26
  type: embedded_image
  path: `d0a25775_p26_i2.png`

- **asset_id**: a027482a-baa3-4bfe-be69-102a56f316f7
  source: slides-05a-ooa
  page: 26
  type: embedded_image
  path: `d0a25775_p26_i3.png`

- **asset_id**: 525dffcd-3c84-405b-8e88-bdfa1087caef
  source: slides-05a-ooa
  page: 26
  type: embedded_image
  path: `d0a25775_p26_i4.png`

- **asset_id**: 335f9ab7-d643-48b0-aa89-3eeef9ff9e1a
  source: slides-05a-ooa
  page: 26
  type: embedded_image
  path: `d0a25775_p26_i5.png`

- **asset_id**: c4e56b31-af73-404f-84a5-cc7330776743
  source: slides-05a-ooa
  page: 26
  type: embedded_image
  path: `d0a25775_p26_i6.png`

- **asset_id**: 1bf2cca2-643d-4c62-8080-9320f6937098
  source: slides-05a-ooa
  page: 26
  type: embedded_image
  path: `d0a25775_p26_i7.png`

- **asset_id**: 4997a271-f6f9-47dd-923b-156bf579200b
  source: slides-05a-ooa
  page: 26
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 0e76051e-1202-4c93-a1f5-b7be2f6c142f
  source: slides-05a-ooa
  page: 27
  type: embedded_image
  path: `d0a25775_p27_i0.png`

- **asset_id**: f45dec9e-0f2c-4743-a16e-bc3d8fcc9207
  source: slides-05a-ooa
  page: 27
  type: embedded_image
  path: `d0a25775_p27_i1.png`

- **asset_id**: 47dffe8b-1b5c-4b5a-9308-59d0f7e4e863
  source: slides-05a-ooa
  page: 27
  type: embedded_image
  path: `d0a25775_p27_i2.png`

- **asset_id**: 118ee956-94f5-4964-a092-d60ecb7c4468
  source: slides-05a-ooa
  page: 27
  type: embedded_image
  path: `d0a25775_p27_i3.png`

- **asset_id**: 740a665f-4da1-48f1-9931-af4ab15bce16
  source: slides-05a-ooa
  page: 27
  type: embedded_image
  path: `d0a25775_p27_i4.png`

- **asset_id**: 1f715c7e-b7b9-4d98-86c3-445b8bb7712f
  source: slides-05a-ooa
  page: 27
  type: embedded_image
  path: `d0a25775_p27_i5.png`

- **asset_id**: a079c823-d528-4456-985c-0ac2de8375cd
  source: slides-05a-ooa
  page: 27
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 79259e92-1bc5-464f-8e34-ecc6f20c0397
  source: slides-05a-ooa
  page: 28
  type: embedded_image
  path: `d0a25775_p28_i0.png`

- **asset_id**: f8f3f3dc-2567-4b59-9659-240f12575cc4
  source: slides-05a-ooa
  page: 28
  type: embedded_image
  path: `d0a25775_p28_i1.png`

- **asset_id**: c5ec2865-1323-4e82-a44c-4d5f492dea62
  source: slides-05a-ooa
  page: 28
  type: embedded_image
  path: `d0a25775_p28_i2.png`

- **asset_id**: 3646b635-511f-4456-84d7-c146821a582b
  source: slides-05a-ooa
  page: 28
  type: embedded_image
  path: `d0a25775_p28_i3.png`

- **asset_id**: 1ad50ca0-85fe-4000-8408-0376c98fb670
  source: slides-05a-ooa
  page: 28
  type: embedded_image
  path: `d0a25775_p28_i4.png`

- **asset_id**: d1786153-2541-45e7-b5ca-8f742d2b155c
  source: slides-05a-ooa
  page: 28
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: bba9c1cb-f62b-400a-a6f9-e32e1bc11862
  source: slides-05a-ooa
  page: 29
  type: embedded_image
  path: `d0a25775_p29_i0.png`

- **asset_id**: 16535af5-a5a1-4cd0-8025-82ae7f2bb0b3
  source: slides-05a-ooa
  page: 29
  type: embedded_image
  path: `d0a25775_p29_i1.png`

- **asset_id**: e2d30420-0a57-4ac3-a0c2-7b7b100e243b
  source: slides-05a-ooa
  page: 29
  type: embedded_image
  path: `d0a25775_p29_i2.png`

- **asset_id**: dddce859-0d6e-4216-bc04-6f05691d1136
  source: slides-05a-ooa
  page: 29
  type: embedded_image
  path: `d0a25775_p29_i3.png`

- **asset_id**: 91b3f6d0-0944-4354-b6e4-853e409c2753
  source: slides-05a-ooa
  page: 29
  type: embedded_image
  path: `d0a25775_p29_i4.png`

- **asset_id**: 96ef1ad2-dd4d-47b4-8c3b-3aff98a529f5
  source: slides-05a-ooa
  page: 29
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: e4c5b86a-c7db-4e8f-9dd6-9efc82dfd62d
  source: slides-05a-ooa
  page: 30
  type: embedded_image
  path: `d0a25775_p30_i0.png`

- **asset_id**: 5d515340-5b78-4404-9b55-b39ed65ec5dd
  source: slides-05a-ooa
  page: 30
  type: embedded_image
  path: `d0a25775_p30_i1.png`

- **asset_id**: f2e9e77b-24bd-4f4d-849b-fcaff7099f32
  source: slides-05a-ooa
  page: 30
  type: embedded_image
  path: `d0a25775_p30_i2.png`

- **asset_id**: bbf80290-ff9d-40a0-ae53-4f4d522a6dd7
  source: slides-05a-ooa
  page: 30
  type: embedded_image
  path: `d0a25775_p30_i3.png`

- **asset_id**: 7f7d6c9a-fbb2-4be6-977a-29109faca02e
  source: slides-05a-ooa
  page: 30
  type: embedded_image
  path: `d0a25775_p30_i4.png`

- **asset_id**: 750f4ca5-7053-40a7-8575-dba29701cccb
  source: slides-05a-ooa
  page: 30
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 4117cda4-8533-40ad-b471-f01604913b33
  source: slides-05a-ooa
  page: 31
  type: embedded_image
  path: `d0a25775_p31_i0.png`

- **asset_id**: 4f13c7b6-6e8a-42c8-81c5-265f37958c96
  source: slides-05a-ooa
  page: 31
  type: embedded_image
  path: `d0a25775_p31_i1.png`

- **asset_id**: b40e8fb9-0420-4526-b274-9c404bdbc3f6
  source: slides-05a-ooa
  page: 31
  type: embedded_image
  path: `d0a25775_p31_i2.png`

- **asset_id**: ba9fdc53-9263-4491-9c95-ee922f6991d1
  source: slides-05a-ooa
  page: 31
  type: embedded_image
  path: `d0a25775_p31_i3.png`

- **asset_id**: 1050d25e-fa8d-4c16-b6eb-ab065ef8cfea
  source: slides-05a-ooa
  page: 31
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: d95400db-c84f-41f5-aaf4-34932b2a21dd
  source: slides-05a-ooa
  page: 32
  type: embedded_image
  path: `d0a25775_p32_i0.png`

- **asset_id**: 7f210bae-5572-4dbb-b379-0d0fa1d39712
  source: slides-05a-ooa
  page: 32
  type: embedded_image
  path: `d0a25775_p32_i1.png`

- **asset_id**: 9bda34b2-0b25-4998-81ed-50a80ba9f8f0
  source: slides-05a-ooa
  page: 32
  type: embedded_image
  path: `d0a25775_p32_i2.png`

- **asset_id**: 4a5b3d7b-8cd0-4115-b48a-69cc7711669f
  source: slides-05a-ooa
  page: 32
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 6aade57b-501c-438f-a373-51a258808659
  source: slides-05a-ooa
  page: 33
  type: embedded_image
  path: `d0a25775_p33_i0.png`

- **asset_id**: b75da3c9-d529-4a97-afa2-5af575b94530
  source: slides-05a-ooa
  page: 33
  type: embedded_image
  path: `d0a25775_p33_i1.png`

- **asset_id**: b62b4846-5b72-472b-9bee-62b80da7c045
  source: slides-05a-ooa
  page: 33
  type: embedded_image
  path: `d0a25775_p33_i2.png`

- **asset_id**: de8cdd55-8418-43c6-bd65-bed349dd59d3
  source: slides-05a-ooa
  page: 33
  type: embedded_image
  path: `d0a25775_p33_i3.png`

- **asset_id**: 5b6be755-d4aa-4a4f-a530-b7f1d6458196
  source: slides-05a-ooa
  page: 33
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 9a4a2911-a566-4b00-858b-03f4c3480d22
  source: slides-05a-ooa
  page: 34
  type: embedded_image
  path: `d0a25775_p34_i0.png`

- **asset_id**: abb56957-17f2-4cbc-bbc6-7723677bacc0
  source: slides-05a-ooa
  page: 34
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 9d583560-c051-489f-8533-8de9ba04bb9f
  source: slides-05a-ooa
  page: 35
  type: embedded_image
  path: `d0a25775_p35_i0.png`

- **asset_id**: 57b5ed3c-935a-4f45-b81a-af736e79e71d
  source: slides-05a-ooa
  page: 35
  type: embedded_image
  path: `d0a25775_p35_i1.png`

- **asset_id**: ad9297c8-9f52-4a97-be94-76ecdd8e665c
  source: slides-05a-ooa
  page: 35
  type: embedded_image
  path: `d0a25775_p35_i2.png`

- **asset_id**: fdd0c658-d317-4a6a-bf4a-2f9739bbc118
  source: slides-05a-ooa
  page: 35
  type: embedded_image
  path: `d0a25775_p35_i3.png`

- **asset_id**: 87fcf6fd-f67f-45e4-8433-dfac7a403071
  source: slides-05a-ooa
  page: 35
  type: embedded_image
  path: `d0a25775_p35_i4.png`

- **asset_id**: 327ef1c8-3b52-4cae-82d5-26f65d74f6f2
  source: slides-05a-ooa
  page: 35
  type: embedded_image
  path: `d0a25775_p35_i5.png`

- **asset_id**: 5a7b1b0f-be48-434c-b320-5e78f5104fdd
  source: slides-05a-ooa
  page: 35
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: e2263363-41ae-41b1-852b-8124b4894433
  source: slides-05a-ooa
  page: 36
  type: embedded_image
  path: `d0a25775_p36_i0.png`

- **asset_id**: e6d99412-eacb-4d19-83b2-8d24a4b01ac6
  source: slides-05a-ooa
  page: 36
  type: embedded_image
  path: `d0a25775_p36_i1.png`

- **asset_id**: 2adbf788-7739-456e-bcec-e8172948e1e7
  source: slides-05a-ooa
  page: 36
  type: embedded_image
  path: `d0a25775_p36_i2.png`

- **asset_id**: 2503f780-8fed-41fc-87e9-e4f1c59cb8c4
  source: slides-05a-ooa
  page: 36
  type: embedded_image
  path: `d0a25775_p36_i3.png`

- **asset_id**: 8ccdb6f7-8da1-46d3-bac0-d4e01b0daa8f
  source: slides-05a-ooa
  page: 36
  type: embedded_image
  path: `d0a25775_p36_i4.png`

- **asset_id**: 2408f11b-340c-4e17-87ec-69a0049c577d
  source: slides-05a-ooa
  page: 36
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 572854a9-9e56-4a33-b49e-fce613919e6b
  source: slides-05a-ooa
  page: 37
  type: embedded_image
  path: `d0a25775_p37_i0.png`

- **asset_id**: 3315f825-c54c-4f3c-ace9-add626c733be
  source: slides-05a-ooa
  page: 37
  type: embedded_image
  path: `d0a25775_p37_i1.png`

- **asset_id**: 6adf9670-b560-48fb-8b1d-9b978c57797e
  source: slides-05a-ooa
  page: 37
  type: embedded_image
  path: `d0a25775_p37_i2.png`

- **asset_id**: dd83a3f8-d1bd-4313-9b4a-55043003ccb3
  source: slides-05a-ooa
  page: 37
  type: embedded_image
  path: `d0a25775_p37_i3.png`

- **asset_id**: 04e5bb1d-c061-4ad6-bb1f-d1e1a32027c7
  source: slides-05a-ooa
  page: 37
  type: embedded_image
  path: `d0a25775_p37_i4.png`

- **asset_id**: fb6f9d61-ca8f-4a0a-8a5f-c8bffac56f33
  source: slides-05a-ooa
  page: 37
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: f9405fbc-ae5d-418d-9ccc-519edc6e5865
  source: slides-05a-ooa
  page: 38
  type: embedded_image
  path: `d0a25775_p38_i0.png`

- **asset_id**: a9bbf622-e2ac-4e93-9681-ffcdf7893c9e
  source: slides-05a-ooa
  page: 38
  type: embedded_image
  path: `d0a25775_p38_i1.png`

- **asset_id**: bb5d398a-0f1e-4987-a6f4-f95de82c541e
  source: slides-05a-ooa
  page: 38
  type: embedded_image
  path: `d0a25775_p38_i2.png`

- **asset_id**: 33a4132b-c39c-4065-8d8a-56f46400b95f
  source: slides-05a-ooa
  page: 38
  type: embedded_image
  path: `d0a25775_p38_i3.png`

- **asset_id**: f6139534-2924-4b1e-a8e9-ca092ec5b7b4
  source: slides-05a-ooa
  page: 38
  type: embedded_image
  path: `d0a25775_p38_i4.png`

- **asset_id**: 676b6a90-c27f-4053-b35c-289e7be0e07a
  source: slides-05a-ooa
  page: 38
  type: embedded_image
  path: `d0a25775_p38_i5.png`

- **asset_id**: 2540030f-941f-41ef-8a83-8d62a0954e51
  source: slides-05a-ooa
  page: 38
  type: embedded_image
  path: `d0a25775_p38_i6.png`

- **asset_id**: 124a5696-3492-411d-8f43-00e53a376457
  source: slides-05a-ooa
  page: 38
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 36c8b161-a87b-4833-bc63-d44f7368020d
  source: slides-05a-ooa
  page: 39
  type: embedded_image
  path: `d0a25775_p39_i0.png`

- **asset_id**: ec9439d3-d209-432d-95a0-29e2fc5e2040
  source: slides-05a-ooa
  page: 39
  type: embedded_image
  path: `d0a25775_p39_i1.png`

- **asset_id**: 43a43d61-9abb-43cd-af4e-4dd9be0e8e06
  source: slides-05a-ooa
  page: 39
  type: embedded_image
  path: `d0a25775_p39_i2.png`

- **asset_id**: dbca3412-5376-4f6e-9a8b-e4b69481ed5b
  source: slides-05a-ooa
  page: 39
  type: embedded_image
  path: `d0a25775_p39_i3.png`

- **asset_id**: b1ee8e95-c3c3-483e-87ee-e338415c8f2e
  source: slides-05a-ooa
  page: 39
  type: embedded_image
  path: `d0a25775_p39_i4.png`

- **asset_id**: 21421609-445b-4bbb-9f43-2ea92ea98fbc
  source: slides-05a-ooa
  page: 39
  type: embedded_image
  path: `d0a25775_p39_i5.png`

- **asset_id**: 9bb658e8-a422-429c-815a-96f2a8e52963
  source: slides-05a-ooa
  page: 39
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: ec8dac87-db06-43b2-a6c2-e78fcb1a1ff2
  source: slides-05a-ooa
  page: 40
  type: embedded_image
  path: `d0a25775_p40_i0.png`

- **asset_id**: 7ae5d17f-3c68-4e9f-b0dd-d6cf0b8b7869
  source: slides-05a-ooa
  page: 40
  type: embedded_image
  path: `d0a25775_p40_i1.png`

- **asset_id**: 63bc5778-7195-4b5f-b234-b804306ea180
  source: slides-05a-ooa
  page: 40
  type: embedded_image
  path: `d0a25775_p40_i2.png`

- **asset_id**: 95da2977-aff9-4354-88cf-0d3a616adff6
  source: slides-05a-ooa
  page: 40
  type: embedded_image
  path: `d0a25775_p40_i3.png`

- **asset_id**: 9dc36b84-1741-4690-9446-7251b995e283
  source: slides-05a-ooa
  page: 40
  type: embedded_image
  path: `d0a25775_p40_i4.png`

- **asset_id**: 2fadb621-cea8-42a3-9c94-d6d77068ee9c
  source: slides-05a-ooa
  page: 40
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: d94b6e32-9d32-4103-b28c-31a158edaa20
  source: slides-05a-ooa
  page: 41
  type: embedded_image
  path: `d0a25775_p41_i0.png`

- **asset_id**: b0e8b3be-5c91-4d4b-bbd9-7145d34a3ef7
  source: slides-05a-ooa
  page: 41
  type: embedded_image
  path: `d0a25775_p41_i1.png`

- **asset_id**: 7e83c0dc-40bd-4c67-aa3e-76ea73541b69
  source: slides-05a-ooa
  page: 41
  type: embedded_image
  path: `d0a25775_p41_i2.png`

- **asset_id**: 34e5e060-b585-4743-b3fd-a2feba18f583
  source: slides-05a-ooa
  page: 41
  type: embedded_image
  path: `d0a25775_p41_i3.png`

- **asset_id**: 89d0553a-a27d-4b76-bfb8-9fea5ac25ec3
  source: slides-05a-ooa
  page: 41
  type: embedded_image
  path: `d0a25775_p41_i4.png`

- **asset_id**: dfe3b2dc-764c-4e6c-ab6c-18ef03debfa9
  source: slides-05a-ooa
  page: 41
  type: embedded_image
  path: `d0a25775_p41_i5.png`

- **asset_id**: 1606c31e-ae46-4edc-9a95-ade043ff5ffd
  source: slides-05a-ooa
  page: 41
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 52df0730-082b-48e8-8193-3ad0a7c8a625
  source: slides-05a-ooa
  page: 42
  type: embedded_image
  path: `d0a25775_p42_i0.png`

- **asset_id**: 92990cb8-3947-4733-b40d-a22840fdb922
  source: slides-05a-ooa
  page: 42
  type: embedded_image
  path: `d0a25775_p42_i1.png`

- **asset_id**: 1790bcdb-2381-4f9b-be3e-c43677cbeb66
  source: slides-05a-ooa
  page: 42
  type: embedded_image
  path: `d0a25775_p42_i2.png`

- **asset_id**: e25a404a-bb72-4773-8f49-6a10ba84b189
  source: slides-05a-ooa
  page: 42
  type: embedded_image
  path: `d0a25775_p42_i3.png`

- **asset_id**: 258e1250-9c02-4c32-a0ac-b38476bd62ca
  source: slides-05a-ooa
  page: 42
  type: embedded_image
  path: `d0a25775_p42_i4.png`

- **asset_id**: 761b7f81-b343-44ce-a2f7-6ddc86a9532d
  source: slides-05a-ooa
  page: 42
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b5f991a0-398a-4197-86a5-af1b8846be13
  source: slides-05a-ooa
  page: 43
  type: embedded_image
  path: `d0a25775_p43_i0.png`

- **asset_id**: 54f59401-8f1f-44c6-8f13-22669b23ef3a
  source: slides-05a-ooa
  page: 43
  type: embedded_image
  path: `d0a25775_p43_i1.png`

- **asset_id**: 7a70713e-7819-497e-be2a-9d8315b11b65
  source: slides-05a-ooa
  page: 43
  type: embedded_image
  path: `d0a25775_p43_i2.png`

- **asset_id**: db4d7f3c-8d3c-4e52-9c13-128b41a45101
  source: slides-05a-ooa
  page: 43
  type: embedded_image
  path: `d0a25775_p43_i3.png`

- **asset_id**: a8450d59-0376-4436-a4b8-b16156c7a11b
  source: slides-05a-ooa
  page: 43
  type: embedded_image
  path: `d0a25775_p43_i4.png`

- **asset_id**: 1311cfff-c307-4a70-9884-da41b6b78efc
  source: slides-05a-ooa
  page: 43
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 1bebf4d7-456c-4a7d-9995-ce5fc82c872e
  source: slides-05a-ooa
  page: 44
  type: embedded_image
  path: `d0a25775_p44_i0.png`

- **asset_id**: 81b016c2-0d92-4f03-9624-215372d32602
  source: slides-05a-ooa
  page: 44
  type: embedded_image
  path: `d0a25775_p44_i1.png`

- **asset_id**: 93b08176-8cf4-44ce-a516-8d1613e8135e
  source: slides-05a-ooa
  page: 44
  type: embedded_image
  path: `d0a25775_p44_i2.png`

- **asset_id**: 09d43f96-e954-4b1c-b53d-2073110e048e
  source: slides-05a-ooa
  page: 44
  type: embedded_image
  path: `d0a25775_p44_i3.png`

- **asset_id**: 036be980-0269-4f11-acbd-6b22e8324b06
  source: slides-05a-ooa
  page: 44
  type: embedded_image
  path: `d0a25775_p44_i4.png`

- **asset_id**: 9fe422a9-07a6-40cb-8033-89f34bbba051
  source: slides-05a-ooa
  page: 44
  type: embedded_image
  path: `d0a25775_p44_i5.png`

- **asset_id**: c71cf5af-6a96-4eb2-8f92-cdb3068ded14
  source: slides-05a-ooa
  page: 44
  type: embedded_image
  path: `d0a25775_p44_i6.png`

- **asset_id**: f73accf3-6a7c-4fc5-91ff-f531ad6a8ad1
  source: slides-05a-ooa
  page: 44
  type: embedded_image
  path: `d0a25775_p44_i7.png`

- **asset_id**: a0b90845-63f1-4418-bab6-769a7fea7d32
  source: slides-05a-ooa
  page: 44
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 2964c500-4ca8-4cf2-9e89-f60ead4c6138
  source: slides-05a-ooa
  page: 45
  type: embedded_image
  path: `d0a25775_p45_i0.png`

- **asset_id**: 000ad95e-9e77-443c-a747-f8830a11c8af
  source: slides-05a-ooa
  page: 45
  type: embedded_image
  path: `d0a25775_p45_i1.png`

- **asset_id**: 6d6fb1f3-6e0d-4fe1-ab6d-d08f85bcf594
  source: slides-05a-ooa
  page: 45
  type: embedded_image
  path: `d0a25775_p45_i2.png`

- **asset_id**: f2c2b202-c566-4109-bddd-1442d20c0bd0
  source: slides-05a-ooa
  page: 45
  type: embedded_image
  path: `d0a25775_p45_i3.png`

- **asset_id**: 75df4523-c7fd-4a96-ab6c-8f5de33848cb
  source: slides-05a-ooa
  page: 45
  type: embedded_image
  path: `d0a25775_p45_i4.png`

- **asset_id**: 4905d423-c418-406a-a7e3-cb898a7a8d89
  source: slides-05a-ooa
  page: 45
  type: embedded_image
  path: `d0a25775_p45_i5.png`

- **asset_id**: 0c861c47-e740-488b-9933-830466a194e0
  source: slides-05a-ooa
  page: 45
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 8e65505f-8f6e-41a6-9252-a17325714e92
  source: slides-05a-ooa
  page: 46
  type: embedded_image
  path: `d0a25775_p46_i0.png`

- **asset_id**: c2d08c0b-6902-4102-a242-2ec039331831
  source: slides-05a-ooa
  page: 46
  type: embedded_image
  path: `d0a25775_p46_i1.png`

- **asset_id**: 14b61dc8-4f42-4028-b427-97f05cd64369
  source: slides-05a-ooa
  page: 46
  type: embedded_image
  path: `d0a25775_p46_i2.png`

- **asset_id**: ef46edf9-7fde-4787-a83c-d40b95035aca
  source: slides-05a-ooa
  page: 46
  type: embedded_image
  path: `d0a25775_p46_i3.png`

- **asset_id**: 3e7a18ef-7883-4d0a-b693-79f6e6ac6c77
  source: slides-05a-ooa
  page: 46
  type: embedded_image
  path: `d0a25775_p46_i4.png`

- **asset_id**: ee83d7e9-5953-41a8-9733-0317c836d1b2
  source: slides-05a-ooa
  page: 46
  type: embedded_image
  path: `d0a25775_p46_i5.png`

- **asset_id**: 3cbc048c-066f-474e-971b-acddc69bc359
  source: slides-05a-ooa
  page: 46
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 0b0eeb27-8404-4c30-8db0-989b76ebfd3f
  source: slides-05a-ooa
  page: 47
  type: embedded_image
  path: `d0a25775_p47_i0.png`

- **asset_id**: e5957739-4900-4bfb-b7ef-6f00bf6565bc
  source: slides-05a-ooa
  page: 47
  type: embedded_image
  path: `d0a25775_p47_i1.png`

- **asset_id**: 11824775-71e0-43ca-b433-7bdd62a2f1d6
  source: slides-05a-ooa
  page: 47
  type: embedded_image
  path: `d0a25775_p47_i2.png`

- **asset_id**: f57f4580-0157-4fdc-8262-916a883c4ba8
  source: slides-05a-ooa
  page: 47
  type: embedded_image
  path: `d0a25775_p47_i3.png`

- **asset_id**: 2c36b569-00cc-4bb9-8eff-8e9205d79910
  source: slides-05a-ooa
  page: 47
  type: embedded_image
  path: `d0a25775_p47_i4.png`

- **asset_id**: 28f24cc4-2ad0-4657-b1b0-7efb3ab541d1
  source: slides-05a-ooa
  page: 47
  type: embedded_image
  path: `d0a25775_p47_i5.png`

- **asset_id**: 35baf75e-74d1-40cd-9e32-033cc883e941
  source: slides-05a-ooa
  page: 47
  type: embedded_image
  path: `d0a25775_p47_i6.jpeg`

- **asset_id**: eba408d4-c737-474b-a129-9743274a4627
  source: slides-05a-ooa
  page: 47
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 1b406d28-3da9-48ff-8890-e37f08835e81
  source: slides-05a-ooa
  page: 48
  type: embedded_image
  path: `d0a25775_p48_i0.png`

- **asset_id**: 815db369-af31-4c6a-b4e4-d271a15aa250
  source: slides-05a-ooa
  page: 48
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 4c8f5869-8102-4486-956e-ba8ef30f3b45
  source: slides-05a-ooa
  page: 49
  type: embedded_image
  path: `d0a25775_p49_i0.png`

- **asset_id**: dc50b844-6411-453e-a798-bcbf38d82372
  source: slides-05a-ooa
  page: 49
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 78940c60-99f9-4985-b22c-c10c2cc4fff9
  source: slides-05a-ooa
  page: 50
  type: embedded_image
  path: `d0a25775_p50_i0.png`

- **asset_id**: a0df1ce6-2f80-4081-8663-81da121b513b
  source: slides-05a-ooa
  page: 50
  type: embedded_image
  path: `d0a25775_p50_i1.png`

- **asset_id**: 93a8e1a4-b8b3-4279-a00b-a6493888dfa4
  source: slides-05a-ooa
  page: 50
  type: embedded_image
  path: `d0a25775_p50_i2.png`

- **asset_id**: f13c731a-4660-4083-b1be-f5340c65fbfd
  source: slides-05a-ooa
  page: 50
  type: embedded_image
  path: `d0a25775_p50_i3.png`

- **asset_id**: 559ff744-2335-4042-8072-62551702ba37
  source: slides-05a-ooa
  page: 50
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 73123603-ccc5-4a38-8b43-cace881219ef
  source: slides-05a-ooa
  page: 51
  type: embedded_image
  path: `d0a25775_p51_i0.png`

- **asset_id**: 3caa8717-d1e2-4fbd-b3fe-8fcccfdca1aa
  source: slides-05a-ooa
  page: 51
  type: embedded_image
  path: `d0a25775_p51_i1.png`

- **asset_id**: 1fc41ac6-4ac9-46f8-9729-12d20c80e3f1
  source: slides-05a-ooa
  page: 51
  type: embedded_image
  path: `d0a25775_p51_i2.png`

- **asset_id**: dcd33e34-644b-42b7-ab30-2a3ff4b3ba35
  source: slides-05a-ooa
  page: 51
  type: embedded_image
  path: `d0a25775_p51_i3.png`

- **asset_id**: 8b0d487f-fca2-437a-8306-17f8657fe19f
  source: slides-05a-ooa
  page: 51
  type: embedded_image
  path: `d0a25775_p51_i4.png`

- **asset_id**: 60f21b10-fa8d-457e-a858-7e2f01c457eb
  source: slides-05a-ooa
  page: 51
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 76594a97-1170-4866-8b3b-2efd1eb87007
  source: slides-05a-ooa
  page: 52
  type: embedded_image
  path: `d0a25775_p52_i0.png`

- **asset_id**: fae79548-ed32-49f2-93f0-9befb0e3e69c
  source: slides-05a-ooa
  page: 52
  type: embedded_image
  path: `d0a25775_p52_i1.png`

- **asset_id**: 5dd5d784-1972-4156-841d-a9074ebff8a9
  source: slides-05a-ooa
  page: 52
  type: embedded_image
  path: `d0a25775_p52_i2.png`

- **asset_id**: bce1a252-6778-4292-ac76-3292c6c9bd71
  source: slides-05a-ooa
  page: 52
  type: embedded_image
  path: `d0a25775_p52_i3.png`

- **asset_id**: 58908af6-fca2-4185-bc58-4e0840e16984
  source: slides-05a-ooa
  page: 52
  type: embedded_image
  path: `d0a25775_p52_i4.png`

- **asset_id**: fe5f367a-4960-45ea-b268-303fb47dfb0c
  source: slides-05a-ooa
  page: 52
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 4e27a8c3-a22f-4576-8c60-f73d1dd888a5
  source: slides-05a-ooa
  page: 53
  type: embedded_image
  path: `d0a25775_p53_i0.png`

- **asset_id**: 1379e4c7-9e3b-4b1e-b6f7-f6aae9b412d6
  source: slides-05a-ooa
  page: 53
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: a0775c97-d7ea-46d4-ab7d-b74040f3ea14
  source: slides-05a-ooa
  page: 54
  type: embedded_image
  path: `d0a25775_p54_i0.png`

- **asset_id**: 0b1fb308-b5d3-45da-ae88-368d49887518
  source: slides-05a-ooa
  page: 54
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 94c05899-0537-4d10-a8ee-c820c110606c
  source: slides-05a-ooa
  page: 55
  type: embedded_image
  path: `d0a25775_p55_i0.png`

- **asset_id**: f30296ce-af8d-4c19-b827-235f950ddff2
  source: slides-05a-ooa
  page: 55
  type: embedded_image
  path: `d0a25775_p55_i1.png`

- **asset_id**: 85a0f13b-8a7f-46a4-be0e-73a554285bde
  source: slides-05a-ooa
  page: 55
  type: embedded_image
  path: `d0a25775_p55_i2.png`

- **asset_id**: 5553b79e-1464-48c2-90cb-d5d94043fd5b
  source: slides-05a-ooa
  page: 55
  type: embedded_image
  path: `d0a25775_p55_i3.png`

- **asset_id**: 654b7f50-c03f-4d85-8604-9da1fb663b93
  source: slides-05a-ooa
  page: 55
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 20c8912d-f266-427b-baa7-f386e0e2b934
  source: slides-05a-ooa
  page: 56
  type: embedded_image
  path: `d0a25775_p56_i0.png`

- **asset_id**: 30fe1dab-9e24-42b5-b7dc-84134650d10f
  source: slides-05a-ooa
  page: 56
  type: embedded_image
  path: `d0a25775_p56_i1.png`

- **asset_id**: b6f6de06-9e4d-4dbe-977a-fd3e5bf1c211
  source: slides-05a-ooa
  page: 56
  type: embedded_image
  path: `d0a25775_p56_i2.png`

- **asset_id**: 9e077405-3534-4b8d-887f-9b859a69c3cb
  source: slides-05a-ooa
  page: 56
  type: embedded_image
  path: `d0a25775_p56_i3.png`

- **asset_id**: c0a713f5-c4af-4a61-862e-2fd97973cbdd
  source: slides-05a-ooa
  page: 56
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 55789832-23a8-4546-b040-f0a1b2e135a4
  source: slides-05a-ooa
  page: 57
  type: embedded_image
  path: `d0a25775_p57_i0.png`

- **asset_id**: 8bbe941e-e7ba-4e84-855c-090227d85a2b
  source: slides-05a-ooa
  page: 57
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: e26f4dcc-a781-4383-8a7a-02ccd5e81417
  source: slides-05a-ooa
  page: 58
  type: embedded_image
  path: `d0a25775_p58_i0.png`

- **asset_id**: 7be5f52c-7147-4d49-88eb-e483c1a77077
  source: slides-05a-ooa
  page: 58
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 7d0a78d7-ec7f-4758-b27a-41a8196e7a76
  source: slides-05a-ooa
  page: 59
  type: embedded_image
  path: `d0a25775_p59_i0.png`

- **asset_id**: 45f4f36e-039b-4c47-bce6-58ebc4684c8c
  source: slides-05a-ooa
  page: 59
  type: embedded_image
  path: `d0a25775_p59_i1.png`

- **asset_id**: ebf22978-639a-4f98-b57d-235c5451bf15
  source: slides-05a-ooa
  page: 59
  type: embedded_image
  path: `d0a25775_p59_i2.png`

- **asset_id**: baf46f13-661e-470a-9649-4a6c78783422
  source: slides-05a-ooa
  page: 59
  type: embedded_image
  path: `d0a25775_p59_i3.png`

- **asset_id**: 92212e0d-be5e-4ee5-a183-6325c32d33f9
  source: slides-05a-ooa
  page: 59
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 0840527a-4ac3-4211-915a-03f567ca7fe2
  source: slides-05a-ooa
  page: 60
  type: embedded_image
  path: `d0a25775_p60_i0.png`

- **asset_id**: 7a2aed37-30cc-49f2-af8e-d6320fe709b0
  source: slides-05a-ooa
  page: 60
  type: embedded_image
  path: `d0a25775_p60_i1.png`

- **asset_id**: bde9d735-0a3a-40db-bab9-5552d068a327
  source: slides-05a-ooa
  page: 60
  type: embedded_image
  path: `d0a25775_p60_i2.png`

- **asset_id**: f171529f-48f3-4234-a4e0-4f3bb4d57849
  source: slides-05a-ooa
  page: 60
  type: embedded_image
  path: `d0a25775_p60_i3.png`

- **asset_id**: ed9868bd-2c39-47c2-ae16-788d4aaccf7a
  source: slides-05a-ooa
  page: 60
  type: embedded_image
  path: `d0a25775_p60_i4.png`

- **asset_id**: dccd00fb-2b6a-4a34-8613-fb7a4da6ca33
  source: slides-05a-ooa
  page: 60
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 0ab04be5-f9da-40d3-906e-70c21acb97b6
  source: slides-05a-ooa
  page: 61
  type: embedded_image
  path: `d0a25775_p61_i0.png`

- **asset_id**: ac5c86f9-b80a-4fd4-804f-1757853cac8c
  source: slides-05a-ooa
  page: 61
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: bc56afab-548b-40a4-9b8d-1d8b114dec83
  source: slides-05a-ooa
  page: 62
  type: embedded_image
  path: `d0a25775_p62_i0.png`

- **asset_id**: 5da36ff4-69aa-47cf-9a17-34d2bff4ef23
  source: slides-05a-ooa
  page: 62
  type: embedded_image
  path: `d0a25775_p62_i1.png`

- **asset_id**: 6eaaf72c-4866-41b4-8d92-b3006099d9e8
  source: slides-05a-ooa
  page: 62
  type: embedded_image
  path: `d0a25775_p62_i2.png`

- **asset_id**: f0240f4e-d145-4907-ac95-06a5cde65fcd
  source: slides-05a-ooa
  page: 62
  type: embedded_image
  path: `d0a25775_p62_i3.png`

- **asset_id**: 667d8121-4c28-439e-95b9-1b7888530b59
  source: slides-05a-ooa
  page: 62
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

