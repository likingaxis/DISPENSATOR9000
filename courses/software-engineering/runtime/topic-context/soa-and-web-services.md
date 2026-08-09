# Topic Context

**topic_id**: soa-and-web-services
**title**: Service Oriented Architecture (SOA) e Web Services

## Retrieval Metadata
- Primary fragments: 862
- Secondary fragments: 10
- Visual assets candidate: 206
- Estimated context tokens: ~10670

## 1. Primary Evidence (Official Coverage)

### Source: slides-09-ood (`official-slides\II parte ISW\09-OOD.pdf`)
#### Page 22
> Service Oriented Architecture (SOA)

> • A SOA is a distributed software architecture that  consists of multiple autonomous services • The services are distributed such that they can  execute on different nodes with different service  providers • With a SOA, the goal is to develop software  applications that are composed of distributed  services, such that individual services can  execute on different platforms and be  implemented in different languages

> © UniRoma2 - Ingegneria del Software 23

#### Page 23
> SOA protocols

> • Standard Internet-based protocols are provided to  allow services to communicate with each other  and to exchange information • Each service has a service description, which  allows applications to discover and communicate  with the service • The service description defines the name of the  service, the location of the service, and its data  exchange requirements

> © UniRoma2 - Ingegneria del Software 24

#### Page 24
> Service providers and consumers

> • A service provider supports services used by  multiple clients  • Unlike client/server architectures, SOAs build on  the concept of loosely coupled services that can  be discovered and linked to by clients (also  referred to as service consumers or service  requesters) with the assistance of service brokers

> © UniRoma2 - Ingegneria del Software 25

#### Page 25
> SOA design concepts

> • An important goal of SOA is to design services as  autonomous reusable components • Services are intended to be self-contained and  loosely coupled, meaning that dependencies between  services are kept to a minimum • Instead of one service depending on another,  coordination services are provided in situations in  which multiple services need to be accessed and  access to them needs to be sequenced • Several software architectural patterns are described  for service-oriented applications:

> – Broker patterns, including Service Registration, Service

> Brokering, and Service Discovery – Transaction patterns, including Two-Phase Commit,

> Compound, and Long-Living Transaction patterns – and Negotiation patterns

> © UniRoma2 - Ingegneria del Software 26

#### Page 26
> Services Design Principles

> • Loose coupling

> • Service contract

> • Autonomy

> • Abstraction

> • Reusability

> • Composability

> • Statelessness

> • Discoverability

> © UniRoma2 - Ingegneria del Software 27

#### Page 27
> Software Architectural Broker Patterns

> • In a SOA, object brokers act as intermediaries  between clients and services • In the Broker pattern (which is also known as the  Object Broker or Object Request Broker pattern),  the broker acts as an intermediary between the  clients and services • Services register with the broker • Clients locate services through the broker • After the broker has brokered the connection  between client and service, communication  between client and service can be direct or via the  broker

> © UniRoma2 - Ingegneria del Software 28

#### Page 28
> Transparency

> • The broker provides both location transparency  and platform transparency • Location transparency means that if the service  is moved to a different location, clients are  unaware of the move and only the broker needs  to be notified • Platform transparency means that each service  can execute on a different hardware/software  platform and does not need to maintain  information about the platforms that other services  execute on

> © UniRoma2 - Ingegneria del Software 29

#### Page 29
> Brokered communication

> • With brokered communication, instead of a client  having to know the location of a given service, the  client queries the broker for services provided • First, the service must register with a broker as  described by the Service Registration pattern

> © UniRoma2 - Ingegneria del Software 30

#### Page 30
> Service Registration Pattern

> • The service needs to register service information  with the broker, including the service name, a  description of the service, and the location at  which the service is provided  • Message sequence: 1. the service sends a register service request to the  broker 2. the broker registers the service in the service registry  and sends a registration acknowledgment to the  service.

> © UniRoma2 - Ingegneria del Software 31

#### Page 31
> Service Registration Pattern

> © UniRoma2 - Ingegneria del Software 32

#### Page 32
> Broker Fowarding Pattern (white pages)

> 1. A client sends a message identifying the service  required – for example, to withdraw cash from a  given bank 2. The broker receives the client request,  determines the location of the service (the ID of  the node the service resides on), and forwards  the message to the service at the specific  location 3. The message arrives at the service, and the  requested service is invoked 4. The broker receives the service response and  forwards it back to the client

> © UniRoma2 - Ingegneria del Software 33

#### Page 33
> Broker Fowarding Pattern (white pages)

> © UniRoma2 - Ingegneria del Software 34

#### Page 34
> Broker Handle Pattern (white pages)

> • The Broker Handle pattern keeps the benefit of  location transparency while adding the advantage  of reducing message traffic • Instead of forwarding each client message to the  service, the broker returns a service handle to the  client, which is then used for direct  communication between client and service • This pattern is particularly useful when the client  and service are likely to have a dialog and  exchange several messages between them.

> © UniRoma2 - Ingegneria del Software 35

#### Page 35
> Broker Handle Pattern (white pages)

> © UniRoma2 - Ingegneria del Software 36

#### Page 36
> Service Discovery Pattern (yellow pages)

> • In white pages brokering the client knows the service  required but not the location • A different brokering pattern is yellow pages  brokering, analogous to the yellow pages of the  telephone directory, in which the client knows the type  of service required but not the specific service • Also known as the Service Discovery pattern  because it allows the client to discover new services:

> 1. The client sends a query request to the broker, requesting  all services of a given type 2. The broker responds with a list of all services that match  the client’s request 3. The client, possibly after consultation with the user, selects  a specific service 4. The broker returns the service handle, which the client  uses for communicating directly with the service

> © UniRoma2 - Ingegneria del Software 37

#### Page 37
> Service Discovery Pattern (yellow pages)

> © UniRoma2 - Ingegneria del Software 38

#### Page 38
> Technology Support for SOA

> • Although SOAs are conceptually platform- independent, they are currently provided very  successfully on Web Services technology  platforms • A web service is a service that is accessed using  standard Internet and XML-based protocols

> © UniRoma2 - Ingegneria del Software 39

#### Page 39
> Web Service Protocols

> • Application clients and services need to have a  communication protocol for inter-component communication • Extensible Markup Language (XML) is a technology that  allows different systems to interoperate through exchange of  data and text • The Simple Object Access Protocol (SOAP), which is a  lightweight protocol developed by the World Wide Web  Consortium (W3C), builds on XML and HTTP to permit  exchange of information in a distributed environment • SOAP defines a unified approach for sending XML-encoded  data and consists of three parts:

> – an envelope that defines a framework for describing what is in a

> message and how to process it – a set of encoding rules for expressing instances of application-

> defined data types, and – a convention for representing remote procedure calls and responses

> © UniRoma2 - Ingegneria del Software 40

#### Page 40
> Web Services

> • Applications provide services for clients • One example of application services is Web  services, which use the World Wide Web for  application-to-application communication • From a software perspective, Web services are the  application programming interfaces (APIs) that  provide a standard means of communication among  different software applications on the World Wide  Web • From a business application perspective, a Web  service is business functionality provided by a  company in the form of an explicit service over the  Internet for other companies or programs to use • A Web service is provided by a service provider and  may be composed of other services to form new  services and applications.

> © UniRoma2 - Ingegneria del Software 41

#### Page 41
> Web Service example

> © UniRoma2 - Ingegneria del Software 42

#### Page 42
> Registration Services

> • A registration service is provided for services to make their  services available to clients • Services register their services with a registration service  – a process referred to as publishing or registering the  service • Most brokers, such as CORBA and Web service brokers,  provide a registration service • For Web services, a service registry is provided to allow  services to be published and located via the World Wide  Web.  • Service providers register their services together with  service descriptions in a service registry • Clients searching for a service can look up the service  registry to find a suitable service • The Web Services Description Language (WSDL) is an  XML-based language used to describe what a service  does, where it resides, and how to invoke it

> © UniRoma2 - Ingegneria del Software 43

#### Page 43
> Brokering and Discovery Services

> • In a distributed environment, an object broker is an  intermediary in interactions between clients and  services • An example of brokering technology is a Web  services broker • Information about a Web service can be defined by  the Universal Description, Discovery, and  Integration (UDDI) framework for Web services  integration • A UDDI specification consists of several related  documents and an XML schema that defines a  SOAP-based protocol for registering and discovering  Web services • A Web services broker can use the UDDI framework  to provide a mechanism for clients to dynamically find  services on the Web

> © UniRoma2 - Ingegneria del Software 44

#### Page 44
> Web Service Broker Example

> © UniRoma2 - Ingegneria del Software 45

#### Page 45
> Web Service Protocols and Standards

> © UniRoma2 - Ingegneria del Software 46

> 1. Client queries UDDI  registry to locate service 2. Registry refers client to  WSDL document 3. Client accesses WSDL  document 4. WSDL provides data to  interact with web service 5. Client sends SOAP- message request 6. Web service returns  SOAP-message response

> WSDL  Document UDDI Registry

> Web Service

> Client

> 1

> 2

> 3

> 4

> 5

> 6

#### Page 46
> WSDL

> © UniRoma2 - Ingegneria del Software 47

> Operations Ports and Bindings

> service

> messages

> resource

> input output

> operation

> service

> operation operation operation

> portType

> operation operation operation

> portType

> URI URI URI ports

> TCP HTTP SMTP

> messages

> resource

> bindings

#### Page 47
> © UniRoma2 - Ingegneria del Software 48

> Q-WSDL(1)

> (QoS-enabled WSDL) • A lightweight and automated WSDL extension  for the description of QoS characteristics of a  web service, such as:

> – performance

> – reliability

> – availability

> – security

> – etc.

> (1) D'Ambrogio A., A model-driven WSDL extension for describing the QoS of web services, Proceedings IEEE

> International Conference on Web Services (ICSW 2006), pp. 789 – 796. Sept 18-22, 2006, Chicago (IL), USA.

#### Page 48
> © UniRoma2 - Ingegneria del Software 49

> Extension Process (2)

> WSDL

> XML  Schema

> WSDL Metamodel

> Q-WSDL Metamodel

> Q-WSDL

> XML  Schema

> WSDL

> XML  Document

> Q-WSDL

> XML  Document

> Metamodel Transformation XMI XMI

> Metamodel layer

> Model layer

> WSDL

> Model

> Q-WSDL

> Model

> MOF Model

> Meta-metamodel layer

> <<instance of>>

#### Page 49
> © UniRoma2 - Ingegneria del Software 50

> WSDL metamodel

> +name +targetNamespace

> Definition

> +name

> Message

> +name

> Binding

> +name +location

> Port

> +name

> Operation +name

> Part

> +name

> Service

> +name

> PortType

> output

> fault

> * 0..* 1..*

> 1

> 1

> 1

> 1..*

> 1..*

> 1..*

> 1..*

> 1..*

> 0..1

> 0..1

> 1..*

> 1

> +namespace +location

> Import

> 1..*

> Types

> 0..1

> is_located_on

> is_acceded_by

#### Page 50
> © UniRoma2 - Ingegneria del Software 51

> WSDL model (portion)

> name = 'TranslateService'

> s : Service name = 'TranslateServiceSoap' location = 'http://www.sel.uniroma2.it/ TranslateServiceSoap'

> p : Port

> name = 'TranslateServiceSoap'

> pt : PortType

> name = 'TranslateServiceSoap'

> b : Binding

> name = 'Translate'

> o : Operation

#### Page 51
> © UniRoma2 - Ingegneria del Software 52

> QoS Profile

> • A standard specialization of general UML concepts to  provide UML models with QoS-oriented annotations • A QoS characteristic is a quantified aspect of the QoS, for  example latency, throughput, reliability, availability, etc. • QoS characteristics are grouped into QoS categories, for  example performance (for latency and throughput  characteristics) and dependability (for reliability and  availability characteristics) • A QoS characteristic is quantified by use of QoS  dimensions • Examples dimensions for reliability are: – MTBF (mean time between failures), – MTTR (mean time to repair) – number of failures supported

#### Page 52
> © UniRoma2 - Ingegneria del Software 53

> QoS characteristics

> • The QoS profile introduces a catalog of general  QoS characteristics within a structured collection  of modeling concepts, denoted as QoS modeling  framework

> • Different domains usually requires different  catalogs of QoS characteristics, and thus the  QoS modeling framework provides enough  flexibility to either specialize the QoS  characteristics for a given application domain or  introduce new characteristics.

#### Page 53
> © UniRoma2 - Ingegneria del  Software 54

> Q-WSDL QoS characteristics

> QoS Characteristic QoS Dimension

> OperationLatency ServiceTime TurnAround OperationDemand ArrivalRate

> Network

> BitRate Delay Jitter PacketLoss ServiceAccessControl Policy

> MessageEncryption EncryptionProtocol KeyType

> ServiceAvailability

> TimeToRepair TimeBetweenFailure ExpAvailability

> ServiceReliability TimeBetweenFailure ExpFailures

#### Page 54
> © UniRoma2 - Ingegneria del Software 55

> Q-WSDL  Metamodel (overall view)

> +name +targetNamespace

> Definition

> +name

> Message

> +name

> Binding

> +name +location

> Port

> +name

> Operation +name

> Part

> +name

> Service

> +name

> PortType

> input

> output

> fault

> * 0..* 1..*

> 1

> 1

> 1

> 1..*

> 1..*

> 1..*

> 1..*

> 1..*

> 0..1

> 0..1

> 0..1

> 1..*

> 1..*

> 1

> +namespace +location

> Import

> 1..*

> Types

> 0..1

> is_located_on

> is_acceded_by

> +qualification +isOffered

> MessageEncryption

> QoSCharacteristic

> +value +unit +source

> Protocol

> +value +unit +source

> KeyType

> QoSDimension QoSDimension

> +qualification +isOffered

> OperationDemand +qualification +isOffered

> OperationLatency

> +qualification +isOffered

> Network

> +qualification +isOffered

> AccessControl

> +qualification +isOffered

> Reliability +qualification +isOffered

> Availability

> +value +unit = 'msec' +type +direction = 'decreasing' +source

> ServiceTime

> +value +unit = 'msec' +type +direction = 'decreasing' +source

> TurnAround

> +value +unit = 'requests/sec' +type +direction +source

> ArrivalRate

> +value +unit = 'Mbit/sec' +type +direction = 'increasing' +source

> BitRate

> +value +unit = 'msec' +type +direction = 'decreasing' +source

> Delay

> +value +unit = 'msec' +type +direction = 'decreasing' +source

> Jitter

> +value +unit = '%' +type +direction = 'decreasing' +source

> PacketLoss

> +value +unit = 'hours' +type +direction = 'decreasing' +source

> TimeToRepair

> +value +unit = 'hours' +type +direction = 'increasing' +source

> TimeBetweenFailure

> +value +unit = 'failures/year' +type +direction = 'decreasing' +source

> ExpFailures

> +value +unit +source

> Policy

> QoSCharacteristic QoSCharacteristic

> QoSCharacteristic

> QoSCharacteristic QoSCharacteristic

> QoSCharacteristic

> QoSDimension QoSDimension QoSDimension

> QoSDimension QoSDimension

> QoSDimension

> QoSDimension

> QoSDimension

> QoSDimension

> QoSDimension

> QoSDimension

> 0..1 0..1 0..1

> 0..1

> 0..1

> 0..1 0..1

> 1 0..1

> 1 0..1 1

> 1 0..1

> 0..1

> 0..1

> 1

> 1 0..1 0..1

> +value +unit = '%' +type +direction = 'increasing' +source

> ExpAvailability

> QoSDimension

> 1

> QoSDimension

> 0..1

#### Page 55
> © UniRoma2 - Ingegneria del Software 56

> Q-WSDL XML schema (portion)

> <element name="operation" type="qwsdl:operationType"/>

> <complexType name="operationType">

> <complexContent>

> <extension base="qwsdl:documented">

> <choice>

> <group ref="qwsdl:one-way-operation"/>

> <group ref="qwsdl:request-response-operation"/>

> <group ref="qwsdl:solicit-response-operation"/>

> <group ref="qwsdl:notification-operation"/> </choice>

> <sequence>

> <element ref="qwsdl:OperationLatency"

> minOccurs="0" maxOccurs="1"/>

> </sequence>

> <attribute name="name" type="NCName"

> use="required"/>

> </extension>

> </complexContent>

> </complexType>

> <element name="OperationLatency"

> type="qwsdl:OperationLatencyType"/> <complexType name="OperationLatencyType">

> <sequence>

> <element name="ServiceTime"

> type="qwsdl:ServiceTimeType"

> minOccurs="1" maxOccurs="1"/>

> <element name="TurnAround"

> type="qwsdl:TurnAroundType"

> minOccurs="1" maxOccurs="1"/> </sequence>

> <attribute name="Qualification"

> type="QualificationType"/>

> <attribute name="Offered" type="boolean"/>

> </complexType>

> <complexType name="ServiceTimeType">

> <attribute name="value" type="float"/>

> <attribute name="unit" type="string" fixed="sec"/>

> <attribute name="qualifier"

> type="qwsdl:QualifierType"/>

> <attribute name="direction"

> type="qwsdl:DirectionType" fixed="decreasing"/> <attribute name="source" type="qwsdl:SourceType"/>

> </complexType>

> <complexType name="TurnAround">

> <attribute name="value" type="float"/>

> <attribute name="unit" type="string" fixed='sec'/>

> <attribute name="qualifier"

> type="qwsdl:QualifierType"/>

> <attribute name="direction"

> type="qwsdl:DirectionType" fixed="decreasing"

> <attribute name="source" type="qwsdl:SourceType"/>

> </complexType>

#### Page 56
> © UniRoma2 - Ingegneria del Software 57

> Q-WSDL applications

> • to specify QoS requirements of web services; • to add QoS characteristics when querying registries of  web services (e.g., UDDI); • to define service level specifications (SLS) when  establishing service level agreements (SLA); • to enable the QoS-aware composition of web services; • to ease the derivation of models that predict the QoS of  web services; • to support the automated mapping from WSDL documents  to Q-WSDL ones; • to support the automated mapping from UML models (e.g.,  UML models of BPEL processes) to services in Q-WSDL.

#### Page 57
> © UniRoma2 - Ingegneria del Software 58

> Example Q-WSDL application

> name = 'TranslateService'

> s : Service name = 'TranslateServiceSoap' location = 'http://www.sel.uniroma2.it/ TranslateServiceSoap'

> p : Port

> name = 'TranslateServiceSoap'

> pt : PortType

> name = 'TranslateServiceSoap'

> b : Binding

> name = 'Translate'

> o : Operation

> qualification = 'none' isOffered = false

> od : OperationDemand

> qualification = 'threshold best-effort' isOffered = false

> ol : OperationLatency

> qualification = 'best-effort' isOffered = true

> a : Availability

> qualification = 'best-effort' isOffered = true

> r : Reliability

> value = 98 unit = '%' type = 'mean' direction = 'increasing' source = 'measured'

> ea : ExpAvailability

> value = 2 unit = 'failures/year' type = 'mean' direction = 'decreasing' source = 'measured'

> ef : ExpFailures

> value = 800 unit = 'msec' type = 'maximum' direction = 'decreasing' source = 'required'

> rt : ServiceTime

> value = 2000 unit = 'msec' type = 'maximum' direction = 'decreasing' source = 'required'

> ta : TurnAround

> value = 10 unit = 'requests/sec' type = 'mean' direction = 'none' source = 'assumed'

> ar : ArrivalRate

#### Page 58
> REST

> • REST stands for Representational State Transfer • REST is a term coined by Roy T. Fielding to describe an  architecture style of networked systems • RESTful API – A resource-based API that uses the HTTP protocol

> © UniRoma2 - Ingegneria del Software 59

#### Page 59
> REST-based network characteristics

> • Client-Server: a pull-based interaction style • Stateless: the client-server communication is constrained  by no client context being stored on the server • Cache: clients and intermediaries can cache responses • Uniform interface: all resources are accessed with a  generic interface (e.g., HTTP GET, POST, PUT,  DELETE), thus simplifying and decoupling the architecture • Named resources: the system is comprised of resources  which are named using a URL (or URI) • Interconnected resource representations: the  representations of the resources are interconnected using  URLs, thereby enabling a client to progress from one state  to another

> © UniRoma2 - Ingegneria del Software 60

#### Page 60
> Resources

> • Resources – every distinguishable entity

> is a resource. – a resource may be a Web

> site, an HTML page, an  XML document, a Web  service, a physical device,  etc. • URLs Identify Resources – Resources are is uniquely

> identified by a URL (Axiom  0 of Tim Berners-Lee Web  Design)

> © UniRoma2 - Ingegneria del Software 61

#### Page 61
> RESTful API

> • The RESTful API uses the available HTTP verbs  to perform CRUD operations based on the  “context”:

> – Collection: A set of items (e.g.: /users) – Item: A specific item in a collection (e.g.: /users/{id})

> © UniRoma2 - Ingegneria del Software 62

#### Page 62
> Conventional vs. REST-based design

> • Example scenario – an airline wants to provide a Web reservation service

> for customers to make flight reservations through the  Web. – the airline wants to ensure that its premier members get

> immediate service, its frequent flyer members get  expedited service, all others get regular service. • Two main approaches to design and implement  the Web reservation service

> – Single URL approach: based on conventional web  service design – Multiple URLs approach: exploits REST-based design

> © UniRoma2 - Ingegneria del Software 63

#### Page 63
> Single URL approach

> • The Web service is responsible for examining  incoming client requests to determine their priority  and process them accordingly

> © UniRoma2 - Ingegneria del Software 64

> Premier Members

> Frequent Flyer Members

> Regular Members

> Web  Reservation

> Service

> Determine

> Priority

> Premier Customer

> F.F. Customer

> Regular Customer

> client

> client

> client

#### Page 64
> Single URL approach disadvantages

> • Clients must learn the rule for expressing  priorities, and the Web service application must  be written to understand the rule  • Based upon the incorrect assumption that a URL  is "expensive" and that their use must be rationed • The Web service is a central point of failure and a  bottleneck

> – Load balancing is a challenge • It violates Axiom 0 of Tim Berners-Lee Web  Design

> © UniRoma2 - Ingegneria del Software 65

#### Page 65
> Multiple URLs approach

> • One URL for premier members, a different URL  for frequent flyers, and still another for regular  customers

> © UniRoma2 - Ingegneria del Software 66

> Premier Members

> Frequent Flyer Members

> Regular Members

> client

> client

> client

> http://www.kings-air/reservations/premier

> http://www.kings-air/reservations/frequent-flyer

> http://www.kings-air/reservations/regular

> Premier Member Reservation

> Service

> Frequent

> Flyer Reservation

> Service

> Regular Member Reservation

> Service

#### Page 66
> Multiple URLs approach advantages

> • It's easy to understand what each service does  simply by examining the URL • There is no need to introduce rules

> – Priorities are elevated to the level of a URL.  "What you

> see is what you get" • It's easy to implement high priority

> – simply assign a fast machine at the premier member

> URL. • There is no bottleneck and no central point of  failure • Consistent with Axiom 0

> © UniRoma2 - Ingegneria del Software 67

#### Page 67
> Software Architectural Transaction Patterns

> • A service often encapsulates data or provides  access to data that need to be read or updated by  clients • Many services need to provide coordinated  update operations • A transaction is a request from a client to a  service that consists of two or more operations  that perform a single logical function and that  must be completed in its entirety or not at all

> © UniRoma2 - Ingegneria del Software 68

#### Page 68
> Transaction properties

> • Transactions have the following properties,  sometimes referred to as ACID properties:

> – Atomicity (A). A transaction is an indivisible unit of

> work. It is either entirely completed (committed) or  aborted (rolled back) – Consistency (C). After the transaction executes, the

> system must be in a consistent state – Isolation (I). A transaction’s behavior must not be

> affected by other transactions – Durability (D). Changes are permanent after a

> transaction completes. These changes must survive  system failures. This is also referred to as persistence

> © UniRoma2 - Ingegneria del Software 69

#### Page 69
> Example Banking Transaction

> (Transfer) • Consider a transfer transaction between two  accounts – for example, from a savings account  to a checking account – in which the accounts are  maintained at two separate banks (services) • In this case, it is necessary to debit the savings  account and credit the checking account • Therefore, the transfer transaction consists of two  operations that must be atomic – a debit operation  and a credit operation – and the transfer  transaction must bre either committed or aborted:

> – Committed. Both credit and debit operations occur – Aborted. Neither the credit nor the debit operation

> occurs

> © UniRoma2 - Ingegneria del Software 71

#### Page 70
> Two-Phase Commit Protocol

> • The Two-Phase Commit Protocol pattern addresses the  problem of managing atomic transactions in distributed  systems, by synchronizing updates on different nodes

> • Coordination of the transaction is provided by the  CommitCoordinator

> • There is one participant service for each node

> • There are two participants in the bank transfer transaction:

> – firstBankService, which maintains the account from which money  is being transferred (from Account), and

> – secondBankService, which maintains the account to which money is  being transferred (to Account)

> © UniRoma2 - Ingegneria del Software 72

#### Page 71
> First Phase

> © UniRoma2 - Ingegneria del Software 73

#### Page 72
> Second Phase

> © UniRoma2 - Ingegneria del Software 74

#### Page 73
> Compound Transaction Pattern

> • The previous bank transfer transaction is an example of a  flat transaction, which has an “all-or-nothing” characteristic • A compound transaction, in contrast, might need only a  partial rollback • The Compound Transaction pattern can be used when  the client’s transaction requirement can be broken down  into smaller flat atomic transactions, in which each atomic  transaction can be performed separately and rolled back  separately • For example, if a travel agent makes an airplane  reservation, followed by a hotel reservation and a rental  car reservation, it is more flexible to treat this reservation  as consisting of three flat transactions. Treating the  transaction as a compound transaction allows part of a  reservation to be changed or canceled without the other  parts of the reservation being affected.

> © UniRoma2 - Ingegneria del Software 75

#### Page 74
> Example Compound Transaction Pattern

> © UniRoma2 - Ingegneria del Software 76

#### Page 75
> Long-Living Transaction Pattern

> • A long-living transaction is a transaction that has

> a human in the loop and that could take a long

> and possibly indefinite time to execute, because

> individual human behavior is unpredictable

> • The Long-Living Transaction pattern splits a

> long-living transaction into two or more separate

> transactions (usually two) so that human decision

> making takes place between the successive pairs

> (such as first and second) of transactions.

> © UniRoma2 - Ingegneria del Software 77

#### Page 76
> Example Long-Living Transaction

> • Consider an airline reservation with human  involvement in the transaction • First a query transaction displays the available seats • The query transaction is followed by a reserve  transaction • With this approach, it is necessary to recheck seat  availability before the reservation is made • A seat available at query time might no longer be  available at reservation time because several agents  might be querying the same flight at the same time • If only one seat is available, the first agent will get the  seat but not the others

> © UniRoma2 - Ingegneria del Software 78

#### Page 77
> Example Long-Living Transaction Pattern

> © UniRoma2 - Ingegneria del Software 79

#### Page 78
> Negotiation Pattern

> • In some SOAs, the coordination between services  involves negotiations between software agents so that  they can cooperatively make decisions • In the Negotiation pattern (also known as the Agent- Based Negotiation or Multi-Agent Negotiation pattern), a  client agent acts on behalf of the user and makes a  proposal to a service agent • The service agent attempts to satisfy the client’s proposal,  which might involve communication with other services • Having determined the available options, the service agent  then offers the client agent one or more options that come  closest to matching the original client agent proposal • The client agent may then request one of the options,  propose further options, or reject the offer • If the service agent can satisfy the client agent request, it  accepts the request; otherwise, it rejects the request

> © UniRoma2 - Ingegneria del Software 80

#### Page 79
> Negotiation Services

> • The client agent, who acts on behalf of the client, may do  any of the following:

> – Propose a service. The client agent proposes a service to the

> service agent. This proposed service is negotiable, meaning that  the client agent is willing to consider counteroffers – Request a service. The client agent requests a service from the

> service agent. This requested service is nonnegotiable, meaning  that the client agent is not willing to consider counteroffers – Reject a service offer. The client agent rejects an offer made by

> the service agent  • The service agent, who acts on behalf of the service, may  do any of the following:

> – Offer a service. In response to a client proposal, a service agent

> offers a counter- proposal  – Reject a client request/proposal. The service agent rejects the

> client agent’s proposed or requested service  – Accept a client request/proposal. The service agent accepts the

> client agent’s proposed or requested service

> © UniRoma2 - Ingegneria del Software 81

#### Page 80
> Example Negotiation Pattern

> © UniRoma2 - Ingegneria del Software 82

#### Page 81
> Service Interface Design in SOA

> • New services are initially designed by using class  structuring criteria • During dynamic interaction modeling, the  interaction between client objects and service  objects is determined • The approach taken for designing service  operations is similar to that used in class interface  design • The messages arriving at a service form the basis  for designing the service operations. The  messages are analyzed to determine the name of  the operation, as well as to determine the input  and output parameters

> © UniRoma2 - Ingegneria del Software 83

#### Page 82
> Service Coordination in SOA

> • In SOA applications that involve multiple services,  coordination of these services is usually required • To ensure loose coupling among the services, it is  often better to separate the details of the  coordination from the functionality of the individual  services • In SOA, different types of coordination are  provided, including orchestration and  choreography

> © UniRoma2 - Ingegneria del Software 84

#### Page 83
> Orchestration and Choreography

> • Orchestration consists of centrally controlled  workflow coordination logic for coordinating  multiple participant services

> – This allows the reuse of existing services by incorpo-

> rating them into new service applications • Choreography provides distributed coordination  among services, and it can be used when  coordination is needed between different business  organizations

> – Thus, choreography can be used for collaboration

> between services from different service providers  provided by different business organizations – Whereas orchestration is centrally controlled,

> choreography involves distributed control

> © UniRoma2 - Ingegneria del Software 85

#### Page 84
> Coordination

> • Because the terms orchestration and  choreography are often used interchangeably, the  more general term coordination is used to  describe the control and sequencing of different  services as needed by a SOA application,  whether they are centrally controlled or involve  distributed control.  • Transaction patterns can also be used for service  coordination

> © UniRoma2 - Ingegneria del Software 86

### Source: slides-09a-soa (`official-slides\II parte ISW\09a-SOA_casestudy.pdf`)
#### Page 0
> © UniRoma2 - Ingegneria del Software

> Designing SOA

> Case Study(*)

> 1

> (*) Hassan Gomaa, Software Modeling and Design: UML, Use Cases, Patterns, and  Software Architectures, Cambridge Press.

#### Page 1
> © UniRoma2 - Ingegneria del Software

> Web-based Online Shopping System

> • In the Web-based Online Shopping System, customers  can request to purchase one or more items from the  supplier • The customer provides personal details, such as address  and credit card information • This information is stored in a customer account • If the credit card is valid, then a delivery order is created  and sent to the supplier • The supplier checks the available inventory, confirms the  order, and enters a planned shipping date • When the order is shipped, the customer is notified, and  the customer’s credit card account is charged

> 2

#### Page 2
> © UniRoma2 - Ingegneria del Software

> Use Case Modeling

> 3

#### Page 3
> © UniRoma2 - Ingegneria del Software

> Use Case Diagram

> 4

#### Page 4
> © UniRoma2 - Ingegneria del Software

> Activity diagram for Browse Catalog UC

> 5

#### Page 5
> © UniRoma2 - Ingegneria del Software

> Activity diagram for Make Order Request UC

> 6

#### Page 6
> © UniRoma2 - Ingegneria del Software

> Activity diagram for Process Delivery Order UC

> 7

#### Page 7
> © UniRoma2 - Ingegneria del Software

> Activity diagram for Confirm Shipment and Bill Customer UC

> 8

#### Page 8
> © UniRoma2 - Ingegneria del Software

> Activity diagram for View Order UC

> 9

#### Page 9
> © UniRoma2 - Ingegneria del Software

> Static Modeling

> 10

#### Page 10
> © UniRoma2 - Ingegneria del Software

> Software System Context Class Diagram

> 11

#### Page 11
> © UniRoma2 - Ingegneria del Software

> Entity Class Diagram

> 12

#### Page 12
> © UniRoma2 - Ingegneria del Software

> Entity Classes

> 13

#### Page 13
> © UniRoma2 - Ingegneria del Software

> Class Structuring

> • The entity classes determined in the previous  section are integrated into a service-oriented  architecture by means of service classes • Catalog Service, Customer Account Service,  Delivery Order Service, and Inventory Service  are service classes that provide access to the  entity classes

> 14

#### Page 14
> © UniRoma2 - Ingegneria del Software

> Service and Entity Classes

> 15

#### Page 15
> © UniRoma2 - Ingegneria del Software

> Other classes

> • There is also a service class, Credit Card Service, which  deals with credit card authorization and charging • Another service class is Email Service, which enables the  Online Shopping System to send email messages to  customers.  • User interaction classes are needed to interact with the  external users – in particular, Customer Interaction and  Supplier Interaction, which correspond to the actors in  the use cases • In addition, to coordinate and sequence the customer  and supplier access to the online shopping services, two  coordinator classes, Customer Coordinator and Supplier  Coordinator, are provided,. A third autonomous  coordinator, Billing Coordinator, is needed to deal with  billing customers.

> 16

#### Page 16
> © UniRoma2 - Ingegneria del Software

> Class Structuring

> «software system» OnlineShoppingSystem

> «user interaction»

> Customer Interaction

> «coordinator»

> Customer Coordinator

> «coordinator»

> Supplier Coordinator

> «user interaction»

> Supplier Interaction

> «service»

> Email Service

> «service» CreditCard

> Service

> «service» CustomerAccount

> Service

> «service»

> Catalog

> Service

> «service» DeliveryOrder

> Service

> «service» Inventory

> Service

> «coordinator»

> Billing Coordinator

> 17

#### Page 17
> © UniRoma2 - Ingegneria del Software

> Dynamic Modeling

> 18

#### Page 18
> © UniRoma2 - Ingegneria del Software

> Communication diagram for the Browse Catalog UC

> 19

#### Page 19
> © UniRoma2 - Ingegneria del Software

> Communication diagram for the Make Order Request UC

> 20

#### Page 20
> © UniRoma2 - Ingegneria del Software

> Communication diagram for the Process Delivery Order UC

> 21

#### Page 21
> © UniRoma2 - Ingegneria del Software

> Communication diagram for the Confirm Shipment and Bill Customer UC

> 22

#### Page 22
> © UniRoma2 - Ingegneria del Software

> Communication diagram

> for the View Order UC

> 23

#### Page 23
> © UniRoma2 - Ingegneria del Software

> Design Modeling

> 24

#### Page 24
> © UniRoma2 - Ingegneria del Software

> Design Modeling Overview

> • The Online Shopping System is designed as a layered  architecture based on the Layers of Abstraction architecture  pattern • The software architecture consists of three layers – a (data)  service layer, a coordinator layer, and a user interaction layer • Furthermore, because this system needs to be highly flexible  and distributed, the decision is made to design a service- oriented architecture, in which distributed components can  discover services and communicate with them • Each component is depicted with the component stereotype  (what kind of component it is, as specified by the component  structuring criteria) • The design of the component and service interfaces are  determined by analysis of the communication diagrams for  each use case

> 25

#### Page 25
> © UniRoma2 - Ingegneria del Software

> Layered Architecture

> «user interaction»

> «component»

> Supplier  Interaction

> «coordinator»

> «component»

> Supplier Coordinator

> «service» DeliveryOrder

> Service

> «service» Inventory

> Service

> «service»

> Catalog

> Service

> «service» CustomerAccount

> Service

> {Layer 3}

> {Layer 2}

> {Layer 1}

> «user interaction»

> «component»

> Customer  Interaction

> «coordinator»

> «component»

> Customer Coordinator

> «coordinator»

> «component»

> Billing Coordinator

> «service» CreditCard

> Service

> «service»

> Email Service

> «layer» UserLayer

> «layer» CoordinationLayer

> «layer» ServiceLayer

> 26

#### Page 26
> © UniRoma2 - Ingegneria del Software

> Architectural Communication Patterns

> • Synchronous Message Communication with  Reply

> • Broker Handle

> • Service Discovery

> • Bidirectional Asynchronous Message  Communication

> • Two-Phase Commit

> 27

#### Page 27
> © UniRoma2 - Ingegneria del Software

> Concurrent Software Design

> • To keep the design simple, the Synchronous  Message Communication with Reply pattern has  been widely used in this case study • This approach has the disadvantage of suspending  the client while it awaits a response from the  service • An alternative design to avoid suspending the client  is to use the Asynchronous Message  Communication with Callback pattern • The Bidirectional Asynchronous Communication  pattern is used for Supplier Coordinator and Billing  Coordinator to communicate with each other in  both directions

> 28

#### Page 28
> © UniRoma2 - Ingegneria del Software

> Concurrent Communication Diagram

> Customer

> Request

> Query,

> Select

> Select, Update Store, Update,  Request Check, Reserve,

> Commit

> Supplier

> Request

> Delivery

> Order Authorization

> Request Authorization

> Response

> Store,  Update, Request

> Customer  Coordinator

> Response

> Supplier  Coordinator

> Response

> Ready For Shipment

> «user interaction»

> «component»

> : Customer Interaction

> «coordinator»

> «component»

> : Customer Coordinator

> «service» : CreditCard

> Service

> «service»

> : Catalog

> Service

> «service» : Customer

> Account

> Service

> «service» : DeliveryOrder

> Service

> «service» : Inventory

> Service

> «user interaction»

> «component»

> : Supplier  Interaction

> «coordinator»

> «component»

> : Supplier Coordinator

> Inventory

> Info Account Info Catalog

> Info

> Delivery

> Order

> «coordinator»

> «component»

> : Billing Coordinator

> Commit

> Invoice

> Request Account

> Info

> Commit

> Charge

> «service»

> : Email Service

> Send

> Send

> Charge Committed

> Account Billed

> 29

#### Page 29
> © UniRoma2 - Ingegneria del Software

> Component Ports and Interfaces for Services

> 30

#### Page 30
> © UniRoma2 - Ingegneria del Software

> Service Interface for Catalog Service

> 31

#### Page 31
> © UniRoma2 - Ingegneria del Software

> Service Interface for Customer Account Service

> 32

#### Page 32
> © UniRoma2 - Ingegneria del Software

> Service Interface for Delivery Order Service

> 33

#### Page 33
> © UniRoma2 - Ingegneria del Software

> Service Interface for Inventory Service

> 34

#### Page 34
> © UniRoma2 - Ingegneria del Software

> Service Interface for Credit Card and Email services

> 35

#### Page 35
> © UniRoma2 - Ingegneria del Software

> Service-Oriented Software Architecture

> «user interaction»

> «component»

> Customer Interaction

> «coordinator»

> «component»

> Customer Coordinator

> «user interaction»

> «component»

> Supplier  Interaction

> «coordinator»

> «component»

> Supplier Coordinator

> «service» Inventory

> Service

> «service» DeliveryOrder

> Service

> «service» CustomerAccount

> Service

> «service»

> Catalog

> Service

> «service» CreditCard

> Service

> PSupplierCoordinator

> RCustomerCoordinator

> PCustomerCoordinator

> RCreditCard

> Service

> PCustAccountService

> RCustAccount

> Service

> PCreditCardService

> PCatalogService

> RCatalog

> Service

> PDOService PInventoryService

> RInventoryService RDOService

> RSupplierCoordinator

> RDOService

> RInterCoordinator

> PInterCoordinator

> «coordinator»

> «component»

> Billing Coordinator

> RDOService RCustAccount

> Service

> «service»

> Email Service

> REmail Service

> REmail Service

> RCreditCard

> Service

> PEmailService

> 36

#### Page 36
> © UniRoma2 - Ingegneria del Software

> Component ports and interfaces for Customer Interaction and Supplier Interaction

> 37

#### Page 37
> © UniRoma2 - Ingegneria del Software

> Component ports and interfaces for

> Customer Coordinator

> 38

#### Page 38
> © UniRoma2 - Ingegneria del Software

> Component ports and interfaces for

> Supplier Coordinator

> 39

#### Page 39
> © UniRoma2 - Ingegneria del Software

> Component ports and interfaces for

> Billing Coordinator

> 40

#### Page 40
> © UniRoma2 - Ingegneria del Software

> Service Reuse

> • With the SOA paradigm, once the services have  been designed and their interfaces specified, the  service interface information can be registered with  a service broker • Services can be composed into new applications • This case study has described an Online Shopping  System • However, other electronic commerce systems could  be designed that would reuse the services provided  by the Online Shopping System, such as Catalog  Service, Delivery Order Service, and Inventory  Service

> 41

## 2. Secondary Evidence (BM25 Lexical + Concepts)

### Source: theory-summary (`teoria.pdf`)
#### Page 0 (BM25: 34.04)
> ▪3. Component-Based Architectures ▪4. Service Oriented Architecture (SOA) ◦Design Patterns

#### Page 18 (BM25: 34.04)
> è pensare in termini di assemblaggio, più che di scrittura da zero. 4. Service Oriented Architecture (SOA) La SOA è un'architettura software distribuita che consiste in molteplici servizi. I

#### Page 19 (BM25: 19.41)
> vengono fornite con grande successo su piattaforme tecnologiche di Web Services. Da un punto di vista di SW, i Web Services sono le API che forniscono i metodi standard di comunicazione. Da un punto di vista business, i

#### Page 20 (BM25: 18.68)
> forma di servizio esplicito di Internet. I Web Services sono quindi il fulcro dell'implmentazione SOA, e sfruttano vari protocolli per far comunicare i servizi fra di loro. Tra questi troviamo:

#### Page 19 (BM25: 18.21)
> forniscono i metodi standard di comunicazione. Da un punto di vista business, i Web Services sono funzionalità di business fornite da una compagnia nella

#### Page 20 (BM25: 16.68)
> localizzare e identificare i servizi disponibili su una rete. • WSDL (Web Services Description Language): Linguaggio basato su XML per descrivere le interfacce dei servizi in un architettura SOA.

#### Page 19 (BM25: 16.58)
> In un ambiente SOA, i servizi possono essere registrati e scoperti dinamicamente. Il pattern Service Broker si occupa di gestire la comunicazione tra client e servizi in modo disaccopiato e flessibile. In pratica fa da

#### Page 21 (BM25: 15.92)
> non vadano persi • Il Two-Phase Commit Protocol è un meccanismo che serve a garantire l’atomicità delle transazioni distribuite, cioè a sincronizzare correttamente

#### Page 19 (BM25: 15.19)
> Ci sono diversi pattern architetturali tra cui: 1. Broker Patterns In un ambiente SOA, i servizi possono essere registrati e scoperti

#### Page 19 (BM25: 15.04)
> ridurre la complessità e aumentare la flessibilità. Un requisito fondamentale è che ogni servizio si registri presso il broker (come previsto dal pattern Service Registration). Solo così il broker può fare da "centralino" per la scoperta e la

## 3. Visual Assets Candidates

- **asset_id**: 527d9939-41be-4249-9344-38be45f3078b
  source: slides-09-ood
  page: 22
  type: embedded_image
  path: `603d78f4_p22_i0.png`

- **asset_id**: 143c1245-a40a-4195-ac20-05da96b35c9a
  source: slides-09-ood
  page: 22
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: f0dfe4db-481c-4ac7-92da-7833eab9398c
  source: slides-09-ood
  page: 23
  type: embedded_image
  path: `603d78f4_p23_i0.png`

- **asset_id**: cae08c7b-edb8-4d0b-80d4-dfdd66172cb1
  source: slides-09-ood
  page: 23
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: fbabe319-7926-4adc-8013-2f5ebff884be
  source: slides-09-ood
  page: 24
  type: embedded_image
  path: `603d78f4_p24_i0.png`

- **asset_id**: 3eca06d1-e89c-4779-be19-4ade68a8bc6d
  source: slides-09-ood
  page: 24
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 738136df-b13f-4a98-b0a7-0fbe67af8295
  source: slides-09-ood
  page: 25
  type: embedded_image
  path: `603d78f4_p25_i0.png`

- **asset_id**: 35b24b5f-4de1-4531-a2ea-e922a6efb30b
  source: slides-09-ood
  page: 25
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: d3faa9dc-f53e-4d63-a288-9b129fb3ef42
  source: slides-09-ood
  page: 26
  type: embedded_image
  path: `603d78f4_p26_i0.png`

- **asset_id**: 0da7f353-ac44-49a5-9e49-384254e5d90d
  source: slides-09-ood
  page: 26
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: c5a47292-0340-411e-a151-a9133ae1b1ba
  source: slides-09-ood
  page: 27
  type: embedded_image
  path: `603d78f4_p27_i0.png`

- **asset_id**: c2a1743e-ddf3-4265-abab-d3fc7a8bf87a
  source: slides-09-ood
  page: 27
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b4bc6095-8a4a-4906-ab4b-88381ba1730f
  source: slides-09-ood
  page: 28
  type: embedded_image
  path: `603d78f4_p28_i0.png`

- **asset_id**: 2c4bda1c-7e78-457b-8369-b45b62d1b198
  source: slides-09-ood
  page: 28
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 232e8ca1-873a-472f-a3ab-946b071b14cc
  source: slides-09-ood
  page: 29
  type: embedded_image
  path: `603d78f4_p29_i0.png`

- **asset_id**: a2510b32-9de3-4196-85fe-fd3c161ac06d
  source: slides-09-ood
  page: 29
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 0e74a43d-f9e9-4798-99b7-72296f670402
  source: slides-09-ood
  page: 30
  type: embedded_image
  path: `603d78f4_p30_i0.png`

- **asset_id**: 8449186d-1ff6-4136-8da3-fe5acd529c2d
  source: slides-09-ood
  page: 30
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: ea380786-2010-4c1f-9bd1-a44727969a66
  source: slides-09-ood
  page: 31
  type: embedded_image
  path: `603d78f4_p31_i0.png`

- **asset_id**: a51d8a7c-0ae9-4410-a0a5-103d034e4cfa
  source: slides-09-ood
  page: 31
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 6d85d5ef-2bd1-4d93-8319-7493d8ee40ae
  source: slides-09-ood
  page: 32
  type: embedded_image
  path: `603d78f4_p32_i0.png`

- **asset_id**: e9d33079-1ba0-4695-bf8d-ef8161d48c7e
  source: slides-09-ood
  page: 32
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 2c7f780a-5659-4774-8954-79c749d6bef2
  source: slides-09-ood
  page: 33
  type: embedded_image
  path: `603d78f4_p33_i0.png`

- **asset_id**: 9737f6d1-6c24-4ef2-be74-069163195afe
  source: slides-09-ood
  page: 33
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 175fe64d-7a9f-459c-b546-c63d52b49833
  source: slides-09-ood
  page: 34
  type: embedded_image
  path: `603d78f4_p34_i0.png`

- **asset_id**: cf6c59cc-bc44-4eee-9cda-3488e57cf08c
  source: slides-09-ood
  page: 34
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 447875ba-39f0-4424-a8e7-ea82e584d3cb
  source: slides-09-ood
  page: 35
  type: embedded_image
  path: `603d78f4_p35_i0.png`

- **asset_id**: c002c80c-6d08-4b51-9ff9-cd2a897c273a
  source: slides-09-ood
  page: 35
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: e7586eba-b3e6-4169-8f03-3d141e2593b4
  source: slides-09-ood
  page: 36
  type: embedded_image
  path: `603d78f4_p36_i0.png`

- **asset_id**: 143fe4d4-f7d8-4f91-b533-0f4f420e8240
  source: slides-09-ood
  page: 36
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 2bdb8a62-2a5a-4bfd-9425-e6a5abe2604e
  source: slides-09-ood
  page: 37
  type: embedded_image
  path: `603d78f4_p37_i0.png`

- **asset_id**: ec7258a6-4dd1-4e63-980e-c0067eddf778
  source: slides-09-ood
  page: 37
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: d85fb12e-8d9e-452f-994d-105c4e99b74d
  source: slides-09-ood
  page: 38
  type: embedded_image
  path: `603d78f4_p38_i0.png`

- **asset_id**: 9e626285-d0d4-4530-9ea3-84c1a7728672
  source: slides-09-ood
  page: 38
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 4180bc85-d102-4ae5-9754-9c4658ad653d
  source: slides-09-ood
  page: 39
  type: embedded_image
  path: `603d78f4_p39_i0.png`

- **asset_id**: 135943dc-2126-4175-8a82-0cc7ddaff9fe
  source: slides-09-ood
  page: 39
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: e0aa5d29-17d0-4979-be7b-a3cffe773186
  source: slides-09-ood
  page: 40
  type: embedded_image
  path: `603d78f4_p40_i0.png`

- **asset_id**: 6c54ba89-e612-43e0-a992-f3d0a14b24c9
  source: slides-09-ood
  page: 40
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 6741417c-32de-4ed2-8881-d9419f6a01dd
  source: slides-09-ood
  page: 41
  type: embedded_image
  path: `603d78f4_p41_i0.png`

- **asset_id**: d409832e-4da4-43a2-9093-f6b16eb29ff2
  source: slides-09-ood
  page: 41
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 00ecb301-4a8d-4e75-bc3d-25657cbc56a1
  source: slides-09-ood
  page: 42
  type: embedded_image
  path: `603d78f4_p42_i0.png`

- **asset_id**: f2f05f26-deb2-4aef-a769-6fe487873898
  source: slides-09-ood
  page: 42
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: d6f0af91-f409-44e1-a049-fe08785e1e6b
  source: slides-09-ood
  page: 43
  type: embedded_image
  path: `603d78f4_p43_i0.png`

- **asset_id**: b6fe30a3-6fd1-4707-a63c-a2724efc48bc
  source: slides-09-ood
  page: 43
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 2f70e0a7-0246-48ed-a7ea-a5b4e316d021
  source: slides-09-ood
  page: 44
  type: embedded_image
  path: `603d78f4_p44_i0.png`

- **asset_id**: 9c28160d-78e1-4be4-841a-4022d0531208
  source: slides-09-ood
  page: 44
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: a2040199-896f-43f0-8c61-6223db1d3253
  source: slides-09-ood
  page: 45
  type: embedded_image
  path: `603d78f4_p45_i0.png`

- **asset_id**: 7260a464-faf0-4199-971a-d4db01fcae2c
  source: slides-09-ood
  page: 45
  type: embedded_image
  path: `603d78f4_p45_i1.png`

- **asset_id**: 6e3709f8-9ab1-49b7-a1cb-8c52a83c79d0
  source: slides-09-ood
  page: 45
  type: embedded_image
  path: `603d78f4_p45_i2.png`

- **asset_id**: 64c25773-900e-48d6-a5a0-c64ce5cf2317
  source: slides-09-ood
  page: 45
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 4e0eb6c0-b9f7-4e0c-8010-da214747ec4c
  source: slides-09-ood
  page: 46
  type: embedded_image
  path: `603d78f4_p46_i0.png`

- **asset_id**: c4ebdd3b-d6cf-4097-ac67-5a4b210adafb
  source: slides-09-ood
  page: 46
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 401b6f38-0272-45ae-8400-8d0c9f678334
  source: slides-09-ood
  page: 47
  type: embedded_image
  path: `603d78f4_p47_i0.png`

- **asset_id**: aa36c3ed-b28d-438c-90ed-4ea1cb6ab129
  source: slides-09-ood
  page: 47
  type: embedded_image
  path: `603d78f4_p47_i1.png`

- **asset_id**: e3aae209-b40e-456c-84eb-cce9e330c4cc
  source: slides-09-ood
  page: 47
  type: embedded_image
  path: `603d78f4_p47_i2.png`

- **asset_id**: 1b510def-8238-4ffc-a2b7-ed58e10785d1
  source: slides-09-ood
  page: 47
  type: embedded_image
  path: `603d78f4_p47_i3.png`

- **asset_id**: bad199cd-db05-4a91-ab53-9eefc3121a8b
  source: slides-09-ood
  page: 47
  type: embedded_image
  path: `603d78f4_p47_i4.png`

- **asset_id**: b33f3c23-5d71-4886-b4c2-38eb7bd6e279
  source: slides-09-ood
  page: 47
  type: embedded_image
  path: `603d78f4_p47_i5.png`

- **asset_id**: 3ce9ab60-bb0b-4e6e-a7de-3e7b7f342bb8
  source: slides-09-ood
  page: 47
  type: embedded_image
  path: `603d78f4_p47_i6.png`

- **asset_id**: ac32b4e0-3e6b-4aca-be4c-bdd14936c3c9
  source: slides-09-ood
  page: 47
  type: embedded_image
  path: `603d78f4_p47_i7.png`

- **asset_id**: 01fa457b-2d46-466f-a38e-d8f7da68a46f
  source: slides-09-ood
  page: 47
  type: embedded_image
  path: `603d78f4_p47_i8.png`

- **asset_id**: 8ff314d4-c519-4d47-96fa-3c73dedf1793
  source: slides-09-ood
  page: 47
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 6712d363-633e-4c94-af4e-1e2e11261843
  source: slides-09-ood
  page: 48
  type: embedded_image
  path: `603d78f4_p48_i0.png`

- **asset_id**: c082c1b5-9f7c-4982-a6fb-a72fd0611291
  source: slides-09-ood
  page: 48
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 16ba05a3-ff60-4733-b15c-35aca3083c94
  source: slides-09-ood
  page: 49
  type: embedded_image
  path: `603d78f4_p49_i0.png`

- **asset_id**: f405ef6c-d961-4d5a-acb6-d21fc0e2b41a
  source: slides-09-ood
  page: 49
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 02e2057d-6a9d-4984-8c71-cd5933859a8c
  source: slides-09-ood
  page: 50
  type: embedded_image
  path: `603d78f4_p50_i0.png`

- **asset_id**: d5fe38f6-fc98-46f2-9e81-43c8b18f941d
  source: slides-09-ood
  page: 50
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 91767bb9-40a6-4e41-a050-1b39ca0f31b4
  source: slides-09-ood
  page: 51
  type: embedded_image
  path: `603d78f4_p51_i0.png`

- **asset_id**: bb879283-3c88-4c2f-ada6-d1149c59395e
  source: slides-09-ood
  page: 51
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b797e06b-7aa7-4beb-bb1f-2ada7c1a684e
  source: slides-09-ood
  page: 52
  type: embedded_image
  path: `603d78f4_p52_i0.png`

- **asset_id**: 90d34e34-fc4f-4d49-b8c7-4c2679c8fba5
  source: slides-09-ood
  page: 52
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: d8a51624-5804-414a-ac6a-ac970d681ce5
  source: slides-09-ood
  page: 53
  type: embedded_image
  path: `603d78f4_p53_i0.png`

- **asset_id**: 3a6bb1b1-a7c1-4b69-84a7-9718f0d85201
  source: slides-09-ood
  page: 53
  type: embedded_image
  path: `603d78f4_p53_i1.png`

- **asset_id**: dba99caa-1d92-493e-ac7b-12ff85ab4243
  source: slides-09-ood
  page: 53
  type: embedded_image
  path: `603d78f4_p53_i2.png`

- **asset_id**: ca4dfc6b-8fc6-4d75-844f-4311aa3fd7d1
  source: slides-09-ood
  page: 53
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: f0486107-34fd-4e65-b04d-6452dde1514a
  source: slides-09-ood
  page: 54
  type: embedded_image
  path: `603d78f4_p54_i0.png`

- **asset_id**: 83120a2c-1b46-478e-904b-eab724f3aaa4
  source: slides-09-ood
  page: 54
  type: embedded_image
  path: `603d78f4_p54_i1.png`

- **asset_id**: 0fb698f8-8f5c-419a-8bb7-3423676cad4b
  source: slides-09-ood
  page: 54
  type: embedded_image
  path: `603d78f4_p54_i2.png`

- **asset_id**: 2dd9a7ee-141f-47e9-957a-78e39e6ab7eb
  source: slides-09-ood
  page: 54
  type: embedded_image
  path: `603d78f4_p54_i3.png`

- **asset_id**: 97dc5ef1-76c4-41c6-b9a2-4f33e1447727
  source: slides-09-ood
  page: 54
  type: embedded_image
  path: `603d78f4_p54_i4.png`

- **asset_id**: bc01f30e-8f0c-42f8-85ac-5f99d2a7ad76
  source: slides-09-ood
  page: 54
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 8c564ed1-dede-4d4b-8925-6a04a344145a
  source: slides-09-ood
  page: 55
  type: embedded_image
  path: `603d78f4_p55_i0.png`

- **asset_id**: 926c2f96-cc81-48bd-8e19-1045c7748702
  source: slides-09-ood
  page: 55
  type: embedded_image
  path: `603d78f4_p55_i1.png`

- **asset_id**: d065e58c-5abc-4397-97c4-9d5c076304c3
  source: slides-09-ood
  page: 55
  type: embedded_image
  path: `603d78f4_p55_i2.png`

- **asset_id**: a7f99797-5d4a-4b01-9f9e-379dd7ca8ec1
  source: slides-09-ood
  page: 55
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 8b997f78-f1ed-4661-87f5-954513322b96
  source: slides-09-ood
  page: 56
  type: embedded_image
  path: `603d78f4_p56_i0.png`

- **asset_id**: c9ae7d1e-8b1f-4d00-b449-5564b02a5983
  source: slides-09-ood
  page: 56
  type: embedded_image
  path: `603d78f4_p56_i1.png`

- **asset_id**: f8006473-715a-402c-a32d-2d949e5bf8c3
  source: slides-09-ood
  page: 56
  type: embedded_image
  path: `603d78f4_p56_i2.png`

- **asset_id**: 79bdd751-fcda-49dc-ae59-19179aa15c2b
  source: slides-09-ood
  page: 56
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 643e5814-8188-403b-81dc-75d2cfc690d5
  source: slides-09-ood
  page: 57
  type: embedded_image
  path: `603d78f4_p57_i0.png`

- **asset_id**: 49f06ecc-0c1d-4d86-b8ee-f4bb333ac6ec
  source: slides-09-ood
  page: 57
  type: embedded_image
  path: `603d78f4_p57_i1.png`

- **asset_id**: b12b3b25-2ced-4530-a640-40cd0ffc67b9
  source: slides-09-ood
  page: 57
  type: embedded_image
  path: `603d78f4_p57_i2.png`

- **asset_id**: 0f1ba702-27bd-430d-900d-cd9ca7278408
  source: slides-09-ood
  page: 57
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: a361318f-33e2-4c5a-8cd4-3f20174478f8
  source: slides-09-ood
  page: 58
  type: embedded_image
  path: `603d78f4_p58_i0.png`

- **asset_id**: 91e59b09-cad1-4469-81e9-398ade7873ca
  source: slides-09-ood
  page: 58
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: e431b9d7-c8ce-4216-b983-e3c38eb7d029
  source: slides-09-ood
  page: 59
  type: embedded_image
  path: `603d78f4_p59_i0.png`

- **asset_id**: f5a20f57-9309-4235-8347-b951af167ced
  source: slides-09-ood
  page: 59
  type: embedded_image
  path: `603d78f4_p59_i1.png`

- **asset_id**: 8ccb3107-ebb5-46c0-8b52-028c53358d0b
  source: slides-09-ood
  page: 59
  type: embedded_image
  path: `603d78f4_p59_i2.png`

- **asset_id**: ca8f3a10-d77b-488f-8590-569101d35cf6
  source: slides-09-ood
  page: 59
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 0d54960b-d8c3-48c1-8733-bdb5ebe00552
  source: slides-09-ood
  page: 60
  type: embedded_image
  path: `603d78f4_p60_i0.png`

- **asset_id**: 9ffd1677-794f-4fb9-b23f-57bf812867ba
  source: slides-09-ood
  page: 60
  type: embedded_image
  path: `603d78f4_p60_i1.png`

- **asset_id**: ffe6f4d6-2d63-4ffb-be87-e98fe94e6e4c
  source: slides-09-ood
  page: 60
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: f598a406-ecb8-4586-89b0-f50f4131e76e
  source: slides-09-ood
  page: 61
  type: embedded_image
  path: `603d78f4_p61_i0.png`

- **asset_id**: 7114a7b2-f01a-4beb-953a-d9ec8ab01ae9
  source: slides-09-ood
  page: 61
  type: embedded_image
  path: `603d78f4_p61_i1.png`

- **asset_id**: 83fdbf83-9da0-4790-96c5-948396463eee
  source: slides-09-ood
  page: 61
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 5c212d5e-0fc6-49c1-8a2d-ee3d9980ff10
  source: slides-09-ood
  page: 62
  type: embedded_image
  path: `603d78f4_p62_i0.png`

- **asset_id**: d2729bf6-3068-4d80-b830-28e29d5773db
  source: slides-09-ood
  page: 62
  type: embedded_image
  path: `603d78f4_p62_i1.png`

- **asset_id**: 011cc339-9198-4983-be0f-a6b834120d44
  source: slides-09-ood
  page: 62
  type: embedded_image
  path: `603d78f4_p62_i2.png`

- **asset_id**: 0235c5e5-3338-4e3a-9eba-241219b957d6
  source: slides-09-ood
  page: 62
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 87af6a97-6453-43ca-9a26-0e87ffdd3ce3
  source: slides-09-ood
  page: 63
  type: embedded_image
  path: `603d78f4_p63_i0.png`

- **asset_id**: ce28b02a-24e2-46f6-8710-588fdc70930d
  source: slides-09-ood
  page: 63
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 228f4ea0-9a49-4891-b06e-1d043efdfbb4
  source: slides-09-ood
  page: 64
  type: embedded_image
  path: `603d78f4_p64_i0.png`

- **asset_id**: ae66cc55-9c4b-4293-9f3b-5179a1783938
  source: slides-09-ood
  page: 64
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: cbffb805-bdc3-458a-b93e-f23c6ad8ee2f
  source: slides-09-ood
  page: 65
  type: embedded_image
  path: `603d78f4_p65_i0.png`

- **asset_id**: 5e63c28b-53e4-47ae-b438-3a748fe4935e
  source: slides-09-ood
  page: 65
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: ee11032d-d79d-44bc-a3b9-ac7bdc111010
  source: slides-09-ood
  page: 66
  type: embedded_image
  path: `603d78f4_p66_i0.png`

- **asset_id**: 7af5d8ae-dd47-423b-90ba-eba34f71e5c5
  source: slides-09-ood
  page: 66
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 99ec9dc6-af45-41dd-9f87-c56271e2b45d
  source: slides-09-ood
  page: 67
  type: embedded_image
  path: `603d78f4_p67_i0.png`

- **asset_id**: 11ed0be9-b3d5-4fff-a394-8d2b36090d79
  source: slides-09-ood
  page: 67
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 92db14da-05cb-4c3c-bc57-926c6d2b4ca6
  source: slides-09-ood
  page: 68
  type: embedded_image
  path: `603d78f4_p68_i0.png`

- **asset_id**: daf8f26f-c09e-45f7-bfa1-2dda8c388e88
  source: slides-09-ood
  page: 68
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 4b969d9f-4ee7-44dc-90b5-fe32cf260b5f
  source: slides-09-ood
  page: 69
  type: embedded_image
  path: `603d78f4_p69_i0.png`

- **asset_id**: 8773a6e8-269a-4342-b230-61827b0669bc
  source: slides-09-ood
  page: 69
  type: embedded_image
  path: `603d78f4_p69_i1.png`

- **asset_id**: eac7a1fd-f7c9-45b1-8dc8-49004f203339
  source: slides-09-ood
  page: 69
  type: embedded_image
  path: `603d78f4_p69_i2.png`

- **asset_id**: 326a2948-b533-4072-96e3-1d4b99c29c8e
  source: slides-09-ood
  page: 69
  type: embedded_image
  path: `603d78f4_p69_i3.png`

- **asset_id**: 3429f184-9a1f-4666-8878-c420f7acbf80
  source: slides-09-ood
  page: 69
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: ed562915-1eb0-4b7e-ba8f-283da185dc37
  source: slides-09-ood
  page: 70
  type: embedded_image
  path: `603d78f4_p70_i0.png`

- **asset_id**: 2301acf9-ef81-4de4-a1bb-1861ff075d5c
  source: slides-09-ood
  page: 70
  type: embedded_image
  path: `603d78f4_p70_i1.png`

- **asset_id**: fb3ac7fd-f539-4d4a-9159-30e7317c3cdd
  source: slides-09-ood
  page: 70
  type: embedded_image
  path: `603d78f4_p70_i2.png`

- **asset_id**: 88946acc-2fe2-48ab-9bca-aec933b6289e
  source: slides-09-ood
  page: 70
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 13efe99f-9c19-4528-9c3e-18f268477ce1
  source: slides-09-ood
  page: 71
  type: embedded_image
  path: `603d78f4_p71_i0.png`

- **asset_id**: 4d95d293-bbad-4910-8268-a7f1d9918704
  source: slides-09-ood
  page: 71
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: c57ead2a-19b8-46ec-a5ca-42ed844601f5
  source: slides-09-ood
  page: 72
  type: embedded_image
  path: `603d78f4_p72_i0.png`

- **asset_id**: 31ccb5eb-6b44-426f-ba30-3811ea76da2a
  source: slides-09-ood
  page: 72
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 95659e42-3fe3-4cc4-b2f9-21cb80a8fa7f
  source: slides-09-ood
  page: 73
  type: embedded_image
  path: `603d78f4_p73_i0.png`

- **asset_id**: b7dabb74-a64f-4b7d-b5fe-bedaa8f417ca
  source: slides-09-ood
  page: 73
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: c1914cb4-a1d0-4a1b-b960-ced6676497d2
  source: slides-09-ood
  page: 74
  type: embedded_image
  path: `603d78f4_p74_i0.png`

- **asset_id**: ae2b5be3-df1a-485d-a5ff-a780c395e6ee
  source: slides-09-ood
  page: 74
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: fa0d267a-6d82-4f6f-be8b-19d4668ed847
  source: slides-09-ood
  page: 75
  type: embedded_image
  path: `603d78f4_p75_i0.png`

- **asset_id**: 48166fd2-9c1e-414c-921a-6b5e34c88df0
  source: slides-09-ood
  page: 75
  type: embedded_image
  path: `603d78f4_p75_i1.png`

- **asset_id**: 5d350f0f-97df-49a4-b1ed-5f6339af7038
  source: slides-09-ood
  page: 75
  type: embedded_image
  path: `603d78f4_p75_i2.png`

- **asset_id**: f42d859e-b007-4d40-8f8a-fc69a54865e0
  source: slides-09-ood
  page: 75
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 31169e9d-be96-49a3-bbf2-90b8b9c30b0d
  source: slides-09-ood
  page: 76
  type: embedded_image
  path: `603d78f4_p76_i0.png`

- **asset_id**: f25984a5-1211-4ad6-aeb0-746fb1774607
  source: slides-09-ood
  page: 76
  type: embedded_image
  path: `603d78f4_p76_i1.png`

- **asset_id**: f66bc7a9-fe9b-40b8-bbd6-49f69f1142b3
  source: slides-09-ood
  page: 76
  type: embedded_image
  path: `603d78f4_p76_i2.png`

- **asset_id**: f37b58b0-94e0-4761-b1d7-c2c11f355912
  source: slides-09-ood
  page: 76
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 71f7404c-024a-473e-98f8-f5b776e48bfc
  source: slides-09-ood
  page: 77
  type: embedded_image
  path: `603d78f4_p77_i0.png`

- **asset_id**: 78ea29a1-d261-4aa0-8b02-26c7149165bd
  source: slides-09-ood
  page: 77
  type: embedded_image
  path: `603d78f4_p77_i1.png`

- **asset_id**: 1900d74b-aab6-4aca-8422-a0795b0f33d8
  source: slides-09-ood
  page: 77
  type: embedded_image
  path: `603d78f4_p77_i2.png`

- **asset_id**: d80e7949-03b0-4ee7-b0c0-57766e5fa5a5
  source: slides-09-ood
  page: 77
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 6b9463ae-05f7-4aa3-bb68-bd593a3849cb
  source: slides-09-ood
  page: 78
  type: embedded_image
  path: `603d78f4_p78_i0.png`

- **asset_id**: 2e391540-b498-45fb-9975-e531de8a486a
  source: slides-09-ood
  page: 78
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 598a0a52-f4d8-442a-978f-6a067a377d5e
  source: slides-09-ood
  page: 79
  type: embedded_image
  path: `603d78f4_p79_i0.png`

- **asset_id**: e289075f-9f30-4be0-9526-2d83ee31ab75
  source: slides-09-ood
  page: 79
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 675648e8-019b-48c0-9486-c646139924b9
  source: slides-09-ood
  page: 80
  type: embedded_image
  path: `603d78f4_p80_i0.png`

- **asset_id**: a8bcf0fd-9755-4ff5-8fcf-174f0e71fcea
  source: slides-09-ood
  page: 80
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 48e50b48-8eb8-4fb8-984a-3cebfe8d7d39
  source: slides-09-ood
  page: 81
  type: embedded_image
  path: `603d78f4_p81_i0.png`

- **asset_id**: 15803c78-ad7f-49d9-9280-992752716729
  source: slides-09-ood
  page: 81
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 94eeef0f-f4be-4602-9079-718d5f9fbea4
  source: slides-09-ood
  page: 82
  type: embedded_image
  path: `603d78f4_p82_i0.png`

- **asset_id**: aa0ae330-aa78-471c-a750-f0bc1da8d901
  source: slides-09-ood
  page: 82
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 8d90c146-2d51-46fd-839b-2a4df271d201
  source: slides-09-ood
  page: 83
  type: embedded_image
  path: `603d78f4_p83_i0.png`

- **asset_id**: f8d24f29-8e94-420e-873e-1fbeac582dad
  source: slides-09-ood
  page: 83
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: ed3f9e17-1498-4f4d-90fc-82ec144d5f0f
  source: slides-09-ood
  page: 84
  type: embedded_image
  path: `603d78f4_p84_i0.png`

- **asset_id**: 1e983d24-bef8-493e-befa-6dff097912cf
  source: slides-09-ood
  page: 84
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: e58e4ca0-48f4-40e3-ae85-07183c6174b7
  source: slides-09a-soa
  page: 0
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 99b06cde-af8b-454e-936f-55b15576e98b
  source: slides-09a-soa
  page: 1
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 44e26a47-b47e-4a48-bd79-01c1f4c4b3fc
  source: slides-09a-soa
  page: 2
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: f4165f44-d6d4-4fe9-b404-0278089af662
  source: slides-09a-soa
  page: 3
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 1bb75595-9227-4bf9-bbc2-b7a9e4576c52
  source: slides-09a-soa
  page: 4
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 72bccd8d-fbd6-4150-8ddc-3feeb7477402
  source: slides-09a-soa
  page: 5
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 8a9e69fd-6a13-4d96-8cd0-58c8b1ad3e7c
  source: slides-09a-soa
  page: 6
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: a3189c62-a809-4512-a0b6-1ea82ff9c11a
  source: slides-09a-soa
  page: 7
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 5e73900a-bbc7-4baa-ba8d-92725e99a3b4
  source: slides-09a-soa
  page: 8
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 4fca4d1f-0fcd-4bc8-81e2-ea551a5d68c5
  source: slides-09a-soa
  page: 9
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 4db882a5-c98a-4d2e-a7cd-3d392c4f7fa4
  source: slides-09a-soa
  page: 10
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 9e61a145-3adb-424a-8d26-ad78ec8ab37a
  source: slides-09a-soa
  page: 11
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 17ceaf95-fb73-4bca-91c9-1173280c9e60
  source: slides-09a-soa
  page: 12
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b5d95b65-0cb3-4acf-b7a7-efd9ab7ca2fe
  source: slides-09a-soa
  page: 13
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: aaae982d-958c-4062-83da-d920463af571
  source: slides-09a-soa
  page: 14
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 9ce6a563-ef4d-4630-8157-06de24564353
  source: slides-09a-soa
  page: 15
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 19d37fe2-d4e0-475c-8b93-c58b35546cbb
  source: slides-09a-soa
  page: 16
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: f64c02e7-3894-45a5-81ac-18642709a009
  source: slides-09a-soa
  page: 17
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 05ae7ecc-373f-49ab-be68-b73db51c6789
  source: slides-09a-soa
  page: 18
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 22288635-7f4f-43b8-ab48-175986751a1a
  source: slides-09a-soa
  page: 19
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 6e8d31dd-95b0-440d-99b8-c2f326b3b302
  source: slides-09a-soa
  page: 20
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 5804a893-7c2a-4ff5-b24d-05ad8995c7c9
  source: slides-09a-soa
  page: 21
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 576e5ff1-6b6d-403d-aeb7-d195ae655933
  source: slides-09a-soa
  page: 22
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 0c4abe4d-a823-4d55-929b-10448b997e00
  source: slides-09a-soa
  page: 23
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 8fef8772-9e95-4524-9612-3306ddba3559
  source: slides-09a-soa
  page: 24
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 132357b0-964c-4bc4-8f2e-42167ed0c84b
  source: slides-09a-soa
  page: 25
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 412653ba-f94b-4161-b94f-1f77bb4be3da
  source: slides-09a-soa
  page: 26
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 9b61b7c8-a896-48fd-a11b-2b3baf1e2622
  source: slides-09a-soa
  page: 27
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 51007054-3284-4ce2-9c34-a3f80e2a1e25
  source: slides-09a-soa
  page: 28
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: f87f0f8e-857b-4320-b234-eea6b6e3a162
  source: slides-09a-soa
  page: 29
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 648bcaab-ba87-4b1f-a3c2-d8879ec6b772
  source: slides-09a-soa
  page: 30
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 55d16dbb-0a17-4de7-9631-6f9c73710c85
  source: slides-09a-soa
  page: 31
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 24e53fdd-5ea9-4596-8c76-35422cb693f9
  source: slides-09a-soa
  page: 32
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: f9a1f61a-6fde-442c-9c20-ff135d611ed4
  source: slides-09a-soa
  page: 33
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 62b9220c-c912-4109-8daa-554f7a30ce49
  source: slides-09a-soa
  page: 34
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: cde0ef60-c322-46b9-b5fd-317764b73b75
  source: slides-09a-soa
  page: 35
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 8fb6d68d-75f1-4a0f-a2c5-8712a68b8442
  source: slides-09a-soa
  page: 36
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 8a9444ca-5d88-4e44-949b-3d090f4eed78
  source: slides-09a-soa
  page: 37
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 080710ae-da89-4706-bc73-8b704d0fb6ea
  source: slides-09a-soa
  page: 38
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: e616743c-c03a-41aa-aaff-b86b4a9d90d1
  source: slides-09a-soa
  page: 39
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 4e9a1adf-a03e-48ec-8253-6108eacb6985
  source: slides-09a-soa
  page: 40
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

