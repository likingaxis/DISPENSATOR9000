# Metodologie Agile e Scrum

## Metodi Agile

### Origine e caratteristiche

Nei primi anni 2000 è emersa una forte reazione contro l'importanza attribuita ai processi software accuratamente pianificati. Tali processi, infatti, erano considerati troppo restrittivi e burocratici per gli sviluppatori, rallentando l'innovazione e la capacità di adattamento ai cambiamenti.

Il termine *agile method* nasce quindi per estendere il concetto originario di sviluppo iterativo e incrementale. L'approccio Agile non è un singolo modello di sviluppo rigido, ma un insieme di principi e valori che guidano un modo di lavorare incentrato su flessibilità, collaborazione e consegna rapida di valore.

L'approccio Agile include aspetti fondamentali quali:
* comunicazione intensiva all'interno del progetto;
* feedback rapido da parte dei clienti;
* poche regole esterne sul modo di lavorare, lasciando autonomia ai team.

Questi valori e principi comuni sono riassunti nell'**Agile Manifesto**.

![[assets/4f64ac69_p5_i0.png]]

### L'Agile Manifesto

Creato nel 2001, l'Agile Manifesto definisce i concetti di base dell'Agile development. Il Manifesto precisa che, pur riconoscendo valore agli elementi tradizionali (posti a destra nei confronti), si attribuisce un'importanza decisamente maggiore ad altri aspetti fondamentali (posti a sinistra).

I 4 valori principali del Manifesto sono:
1. **Individui e interazioni** più di *processi e strumenti*.
2. **Software funzionante** più di *documentazione esaustiva*.
3. **Collaborazione col cliente** più di *negoziazione contrattuale*.
4. **Risposta al cambiamento** più di *seguire un piano*.

Oltre a questi valori, l'Agile Manifesto contiene **12 principi Agile** che forniscono indicazioni pratiche aggiuntive, orientate alla consegna continua di software funzionante, alla collaborazione attiva con i clienti e all'accoglienza dei cambiamenti nei requisiti.

## Scrum

**Scrum** è uno dei framework più popolari nell'ambito dell'approccio Agile. È progettato come una struttura organizzativa leggera e iterativa pensata specificamente per gestire progetti complessi. 

L'obiettivo principale di Scrum è consegnare valore in modo iterativo e incrementale, permettendo ai team di adattarsi rapidamente e continuamente ai cambiamenti nelle esigenze dei clienti e nel contesto del progetto.

### Ruoli Scrum

Scrum definisce tre ruoli fondamentali, ognuno con responsabilità chiare e distinte per il successo del progetto:

* **Scrum Master**:
  * Assicura che la metodologia sia compresa e correttamente implementata dal team.
  * Supporta il team aiutando gli elementi esterni a interagire secondo le regole Scrum.
  * Rimuove gli ostacoli che potrebbero impedire il progresso e protegge il team dalle interferenze esterne.
* **Product Owner**:
  * Gestisce e contribuisce a prioritizzare i requisiti da implementare, che sono documentati e mantenuti aggiornati nel *Product Backlog*.
* **Development Team**:
  * È responsabile dello sviluppo vero e proprio del prodotto e di tutte le attività rilevanti (progettazione, codifica, testing).
  * Lavora in gruppo per produrre gli incrementi di software funzionante.

![[assets/4f64ac69_p8_i0.png]]

### Artefatti Scrum

Per gestire il lavoro e monitorare il progresso, Scrum utilizza tre artefatti principali:

* **Product Backlog**: Una lista prioritizzata che contiene tutte le funzionalità, i miglioramenti e le attività da realizzare in futuro.
* **Sprint Backlog**: Contiene gli elementi specifici selezionati dal Product Backlog per essere sviluppati durante lo sprint corrente.
* **Incremento**: È il risultato effettivo del lavoro dello sprint, comprendente le funzionalità e le attività che sono state completate.

### Sprint ed Eventi Scrum

Scrum organizza il lavoro in cicli ripetitivi chiamati **Sprint**. Questa organizzazione iterativa permette al team di adattarsi ai cambiamenti e di ricevere feedback regolare.

* Uno sprint dura tipicamente da 2 a 4 settimane.
* Lo scopo di ogni sprint è consegnare un nuovo **incremento di software funzionante**.

Il ciclo di vita di uno sprint prevede 4 eventi principali:
1. **Sprint Planning**: Si tiene all'inizio dello sprint. Il team trasferisce gli elementi da sviluppare dal Product Backlog allo Sprint Backlog.
2. **Daily Scrum** (o *stand-up meeting*): Brevi incontri giornalieri del development team per sincronizzare il lavoro e affrontare eventuali problemi.
3. **Sprint Review**: Alla fine dello sprint, l'incremento di software prodotto viene presentato al Product Owner e agli stakeholder.
4. **Sprint Retrospective**: Incontro conclusivo per identificare e pianificare miglioramenti nel processo lavorativo per lo sprint successivo.

![[assets/4f64ac69_p9_i0.png]]

### Definition of Done (DoD)

Scrum richiede rigorosamente una **Definition of Done** (Definizione di Fatto). Questo aiuta a garantire che il lavoro consegnato sia di alta qualità e soddisfi gli standard stabiliti dal progetto.

Il development team definisce autonomamente cosa significa che un work item sia considerato *done* prima che possa essere integrato nel main branch di sviluppo.

I requisiti minimi tipici di una DoD includono:
* Un numero adeguato di test case superati.
* La verifica dell'integrazione del nuovo codice, per assicurarsi che non interrompa o corrompa il main development branch.
* Codice documentato adeguatamente (è il team stesso a stabilire cosa significhi "adeguata").

![[assets/4f64ac69_p10_i0.png]]
![[assets/4f64ac69_p10_i1.png]]

## User Stories ed Epiche

Le **User Stories** sono una pratica molto comune nello sviluppo Agile (spesso usate in combinazione con Scrum, sebbene non siano formalmente definite nella Scrum Guide). Mirano a focalizzare l'attenzione sui bisogni reali degli utenti finali.

Una user story è un formato per descrivere un requisito utente sotto forma di una storia, descritta dal punto di vista dell'utente stesso. Deve essere molto breve, tipicamente composta da una sola frase.

* **Template comune**: `As a <role>, I want <goal> so that <benefit>`.
* *Esempio*: As a process engineer, I want to see the dependencies between different process steps so that I can easily verify and validate them.

Le **Epics** (epiche) sono user stories molto grandi e complesse, che vengono successivamente suddivise in storie più piccole e gestibili durante lo sviluppo.

![[assets/4f64ac69_p11_i0.png]]
