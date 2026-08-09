# Topic Context

**topic_id**: bpmn-notation
**title**: Business Process Model and Notation (BPMN)

## Retrieval Metadata
- Primary fragments: 197
- Secondary fragments: 0
- Visual assets candidate: 136
- Estimated context tokens: ~3161

## 1. Primary Evidence (Official Coverage)

### Source: slides-16-bpmn (`official-slides\II parte ISW\16-BPMN.pdf`)
#### Page 0
> BPMN Business Process Model

> and Notation

#### Page 1
> Modeling Language Components

> • A modeling language consists of three parts: • Syntax

> • Set of modeling elements and rules to combine them • BPMN syntax includes activities, events, gateways, sequence  ﬂows • Semantics

> • Bind syntactical elements with textual descriptions to a precise  meaning

> • Behavior of BPMN elements • Notation

> • Defines graphical symbols for elements

#### Page 2
> Business Process Model and

> Notation (BPMN)

> • Object Management Group (OMG) standard • http://www.omg.org • http://www.omg.org/specs/bpmn • version 1.0 (2006) • version 1.1 (2007) • version 1.2 (2009) • version 2.0 (2011)

> • Provide a notation to describe Business Process  understandable by:

> • BP analysts • IT developers • BP workers and managers

#### Page 3
> Why BPMN

> • Business people are very comfortable with  visualizing Business Processes in a flow-chart  format

> • BPMN execution semantics is fully formalized

> • BPMN 2.0 has a formal definition (metamodel) • Precise definition of the constructs and rules for creating  models

#### Page 4
> BPMN Metamodel

> • Metamodeling has the following benefits • Formalization of models and entities • Formalization of relationship between elements • Interoperability

> • It is not necessary for the modeler to handle the  metamodel

> • Is the modeling tool that ensures the model is  compliant with metamodel

#### Page 5
> BPMN Metamodel (partial)

#### Page 6
> BPMN Semantic

> • To describe how the BPMN elements behave, the theoretical concept of  token is used

> • The “simulated” behavior of elements can be defined by describing how they  interact with a token • The token is not part of the BPMN specification • BPMN modeling tools are not required to implement any form of token

> • The token will traverse the sequence flows and pass through the  elements in the process

> • Token traverse sequence flows instantaneously, so there is no time associated  with them • When arrives at an element, the token may continue instantaneously or can be  delayed depending on the element

> • We use this notation for tokens T

#### Page 7
> Sequence Flow

> • Sequence flow connects model elements showing their  order of execution

> • Each sequence flow has only one source and only one  target

> • Model elements can have one or more incoming sequence  flow and one or more outgoing sequence flow but usually  they have one

> • Source and target can be activities, events, gateways

> Sequence Flow

#### Page 8
> Start Event

> • Beginning of the process • It has no incoming flows

> • A process may have zero, one or more start events • If not present, all activities without incoming flows start  together • If an end event is present, at least one start event is  mandatory

#### Page 9
> End Event

> • Where the flow of the process ends • It has no outgoing flows

> • A process may have zero, one or more end events • If not present, all activities that do not have any outgoing  flows mark the end of a process path

> • In this case, the Process ends when all parallel paths have  completed

> • If a start event is present, at least one end event is  mandatory

#### Page 10
> Task

> • Unit of work (atomic activity), the job to be  performed

> • A task is used when the work in the process cannot  be broken down to a finer level of detail

#### Page 11
> Our First BPMN Model

> • A simple BPMN model generally has 1. A start point 2. An end point 3. Some activities 4. Connections between activities

> Get shipment

> address Purchase order confirmed

> Ship product Receive payment

> Order fulfilled

#### Page 12
> Gateway

> • Used to control how sequence flows interact as they  converge and diverge within a process

> • Split gateway  • Point where the process flow diverges • Has one incoming sequence flow and multiple outgoing sequence  flows

> • Merging gateway • Point where the process flow converges • Has multiple incoming sequence flows and one outgoing sequence  flow

#### Page 13
> Exclusive Gateway

> • Diverging Exclusive Gateway • Creates alternative paths within a process flow • The decision is considered as a question with a defined set of  alternative answers • Only one of the paths can be taken (XOR) • The default path (if defined) is taken if none of the  conditional expressions evaluate to true

> false

> true T

#### Page 14
> Exclusive Gateway

> • Converging Exclusive Gateway • Used to merge alternative paths • Each incoming token is routed to the outgoing sequence  flow without synchronization

> T

> T

> T

> Done!

#### Page 15
> Exclusive Gateway Example

> • Order shipment • When a purchase order is received, check stock  availability. If the item is available, confirm order and  ship product, otherwise reject order.

#### Page 16
> Exclusive Gateway Example

> • Order shipment • When a purchase order is received, check stock  availability. If the item is available, confirm order and  ship product, otherwise reject order

#### Page 17
> Parallel Gateway

> • Diverging Parallel Gateway • Creates parallel paths without checking any conditions • Each outgoing sequence flow receives a token

> T T

#### Page 18
> Parallel Gateway

> • Converging Parallel Gateway • Used to synchronize (combine) parallel flows and to  create parallel flows • Waits for all incoming flows before routing the token to  the outgoing flows (AND)

> T

> T

#### Page 19
> Parallel Gateway Example

> • Boarding security check • Having the boarding pass, go to security check for  luggage and security screening. When passed both go to  boarding

#### Page 20
> Parallel Gateway Example

> • Boarding security check • Having the boarding pass, go to security check for  luggage and security screening. When passed both go to  boarding

#### Page 21
> Inclusive Gateway

> • Diverging Inclusive Gateway

> • Used to create alternative but also parallel paths within a process flow • Unlike the exclusive gateway, all condition expressions are evaluated • All Sequence Flows with a true evaluation will be traversed by a token (OR) • The default path (if defined) is taken if none of the conditional expressions  evaluate to true

> true

> true T T

#### Page 22
> Inclusive Gateway

> • Converging Inclusive Gateway

> • Used to merge a combination of alternative and parallel paths • Token arriving at an inclusive gateway may be synchronized with  some other tokens that arrive later at the gateway

> • When all the expected tokens have arrived the token moves to the  outgoing sequence flow

> T

> T

#### Page 23
> Inclusive Gateway Example

> • Order decomposition • When an order is received, get product of type A from  warehouse A and products of type B from warehouse B.

#### Page 24
> Inclusive Gateway Example

> • Order decomposition • When an order is received, get product of type A from  warehouse A and products of type B from warehouse B.

> Suborder to  warehouse A

> Suborder to  warehouse B

#### Page 25
> Resource Modeling

> • Organizational resource are mapped in pools and lanes

> • Pools  • Independent organizational entities (do not share any  common system that allows them to communicate implicitly)

> • Customer is independent from the Supplier

> • Lanes  • Multiple resource classes in the same organization (share  common systems)

> • Sales department and marketing Department

#### Page 26
> Pools and Lanes

#### Page 27
> Message Flow

> • Used to show the flow of messages between two  participants

> • Participants are prepared to send and receive the  messages

> • Message flow only connects two separate pools • Message flow can be attached to pools, activities, or  message events • Message flow cannot connect two objects within the  same pool

#### Page 28
> Artifacts

> • Additional information that is not directly related to  the sequence flows or message flows

> • Associations, groups, text annotations

> • Association is used to associate artifacts with  process elements

> Association

#### Page 29
> Text Annotation

> • Provides additional information for the reader of a  BPMN diagram

> • Does not affect the flow of the process

#### Page 30
> Data Objects

> • Represent data and document exchanged in the  process

> • Can be used to show input and output of activities

> • BPMN defines 5 kind of data objects

#### Page 31
> Data Objects

> • Data object • Information traversing the process (email, letters, documents)

> • Collection data object • Collection of information

> • Data input • External input necessary to start the activity

> • Data output • Outcome of the activity or the process

> • Data store • Place where the process can read and write data (database)

> Data Store

#### Page 32
> BPMN Process Type

> • Orchestration

> • Collaborations

> • Choreographies

> • BPMN uses the terms collaboration and  choreography when modeling the interaction  between processes

#### Page 33
> Orchestration Example

> • BP internal to a specific organization

> • Generally called workflow or BPM process

> Image from “Business Process Model and Notation (BPMN)”, http://www.omg.org/spec/BPMN/2.0

#### Page 34
> Collaboration

> • Collaboration shows interactions between two or  more participants

> • A pool represents one of the participants in the  collaboration

> • Collaboration can be shown as two or more  processes communicating with each other

> • The message exchanged between the participants is  shown by a message flow

#### Page 35
> Collaboration Example

> Image from “Business Process Model and Notation (BPMN)”, http://www.omg.org/spec/BPMN/2.0

#### Page 36
> Specialized Task

> • Send/Receive message • Task that send/receive a message to/from an  external participant (within the process) • User activity • Task performed by a human with the assistance of  a software application • Manual activity • Task performed without the aid of any application • Service calling • Task that uses some sort of external service  identified with an URI • Script • Task performed by a business process engine

#### Page 37
> Event Definition

> • The “Event” is the composition of • Position

> • Start, Intermediate, End • Nature • Catch, Throw • Impact • Interrupting, Non-Interrupting • Type

> • Message, Timer, etc.

#### Page 38
> Event Symbol

> Single, double or filled

> outer circle Define the position of the  event (start, intermediate,

> end)

> Dashed or solid circle Define the impact of the  event (interrupting, non-

> interrupting)

> Filled or unfilled marker Define the nature of event

> (throw, catch) Internal marker Define the type of the  event (message, timer,

> etc.)

#### Page 39
> Event Position

> • Start event • initial point of execution flow

> • Intermediate event • may occur between start and  end of the execution flow

> • End event • stop of the execution flow

#### Page 40
> Event Nature

> • Catch event • All start events and some intermediate events • When the event is triggered, the token is generated

> • Throw event • All end events and some intermediate events are  throwing events that may eventually be caught by  another event • Typically, the trigger carries information from the scope  where the throw event occurred into the scope of the  catching events

#### Page 41
> Events Definition

#### Page 42
> Events Definition

#### Page 43
> Events Definition

#### Page 44
> Event-Based Gateway

> • Alternative paths are based on events that occur, rather  than the evaluation of expressions

> • Usually the receipt of a message determines the path that will be  taken

> • When the first event is triggered, then the corresponding  path is activated

> • All remaining paths will no longer be valid • The event gateway is thus a race condition where the first event  that is triggered wins

> • Event gateways can be used to start the process according  to the event occurred

#### Page 45
> Event-Based Gateway

#### Page 46
> Demo - Shipment Process of a

> Hardware Retailer

> • When goods are ready to be sent, the warehouse  worker starts packaging the goods and a clerk decides if  this is a normal postal or a special shipment.

> • If a special shipment is required, the clerk selects a  carrier and prepares the paperwork.

> • Otherwise a normal post shipment is fine and in this  case the clerk checks if an extra insurance is necessary.

> • If the extra insurance is required, the logistics manager  prepares that insurance. In any case, the clerk has to fill  in a postal label for the shipment.

#### Page 47
> Demo - Shipment Process of a

> Hardware Retailer

> • When goods are ready to be sent, the warehouse  worker starts packaging the goods and a clerk decides if  this is a normal postal or a special shipment.

> • If a special shipment is required, the clerk selects a  carrier and prepares the paperwork.

> • Otherwise a normal post shipment is fine and in this  case the clerk checks if an extra insurance is necessary.

> • If the extra insurance is required, the logistics manager  prepares that insurance. In any case, the clerk has to fill  in a postal label for the shipment.

> Participants

#### Page 48
> Demo - Shipment Process of a

> Hardware Retailer

> • When goods are ready to be sent, the warehouse  worker starts packaging the goods and a clerk decides if  this is a normal postal or a special shipment.

> • If a special shipment is required, the clerk selects a  carrier and prepares the paperwork.

> • Otherwise a normal post shipment is fine and in this  case the clerk checks if an extra insurance is necessary.

> • If the extra insurance is required, the logistics manager  prepares that insurance. In any case, the clerk has to fill  in a postal label for the shipment.

> Activities

#### Page 49
> Demo - Shipment Process of a

> Hardware Retailer

## 2. Secondary Evidence (BM25 Lexical + Concepts)

*No secondary evidence found.*

## 3. Visual Assets Candidates

- **asset_id**: 29490f9d-6b20-401b-a122-82db74a36e3c
  source: slides-16-bpmn
  page: 0
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b9a35e28-90a0-4d8c-90cc-74d3a38956e6
  source: slides-16-bpmn
  page: 1
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 08d35083-f766-4635-96a6-420aa3cea32d
  source: slides-16-bpmn
  page: 2
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 58108a18-d8d5-493b-b339-42feb2632842
  source: slides-16-bpmn
  page: 3
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 0be606f9-68c8-459c-af6f-95973cb227e7
  source: slides-16-bpmn
  page: 4
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 0308fdf4-296b-4f6a-9c89-618a348e8f18
  source: slides-16-bpmn
  page: 5
  type: embedded_image
  path: `4277faaa_p5_i0.jpeg`

- **asset_id**: 71f7c128-957e-462e-8126-d31a5a15b92c
  source: slides-16-bpmn
  page: 5
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 4606df50-3f39-466b-bc52-18199e88a6f4
  source: slides-16-bpmn
  page: 6
  type: embedded_image
  path: `4277faaa_p6_i0.png`

- **asset_id**: d0f62236-a129-48fc-a9ed-753cb40f60e5
  source: slides-16-bpmn
  page: 6
  type: embedded_image
  path: `4277faaa_p6_i1.png`

- **asset_id**: f0f38031-cc88-4175-88d5-94e49f5696b0
  source: slides-16-bpmn
  page: 6
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 6c1035c7-c7be-4ad5-879f-0d02e12033f5
  source: slides-16-bpmn
  page: 7
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 7292df48-442f-4870-a656-484ca7045125
  source: slides-16-bpmn
  page: 8
  type: embedded_image
  path: `4277faaa_p8_i0.png`

- **asset_id**: ad36acb5-f74a-433e-8580-54d83ff29d72
  source: slides-16-bpmn
  page: 8
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 578e20e8-9b2f-42ca-9896-05bce240c5e6
  source: slides-16-bpmn
  page: 9
  type: embedded_image
  path: `4277faaa_p9_i0.png`

- **asset_id**: 072c483b-7447-45fb-9b11-614b9377b1db
  source: slides-16-bpmn
  page: 9
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: c57d72f0-f917-47aa-b4ba-c79646f73f9c
  source: slides-16-bpmn
  page: 10
  type: embedded_image
  path: `4277faaa_p10_i0.jpeg`

- **asset_id**: d2ac2ea5-1257-4e14-9359-252aee02e140
  source: slides-16-bpmn
  page: 10
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b989d696-2b75-411f-a15c-e0a498b2d930
  source: slides-16-bpmn
  page: 11
  type: embedded_image
  path: `4277faaa_p11_i0.png`

- **asset_id**: 4177f24d-2293-44e1-b749-914e17ac327e
  source: slides-16-bpmn
  page: 11
  type: embedded_image
  path: `4277faaa_p11_i1.png`

- **asset_id**: 11d892d1-f302-4b89-ac9e-90b9ad652a18
  source: slides-16-bpmn
  page: 11
  type: embedded_image
  path: `4277faaa_p11_i2.png`

- **asset_id**: 95719a77-d61d-4d71-80dc-f876bcfeb7cd
  source: slides-16-bpmn
  page: 11
  type: embedded_image
  path: `4277faaa_p11_i3.png`

- **asset_id**: a7328922-3f34-44ec-a371-a2846e42822f
  source: slides-16-bpmn
  page: 11
  type: embedded_image
  path: `4277faaa_p11_i4.png`

- **asset_id**: 7f3a4fc0-d1c7-475c-9053-2147cbabc935
  source: slides-16-bpmn
  page: 11
  type: embedded_image
  path: `4277faaa_p11_i5.png`

- **asset_id**: 3d691eaa-1043-426b-93e9-fb16c5f9d08f
  source: slides-16-bpmn
  page: 11
  type: embedded_image
  path: `4277faaa_p11_i6.png`

- **asset_id**: 4302ed31-e260-453a-945f-9fde47c061b9
  source: slides-16-bpmn
  page: 11
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: f250825b-36fb-483e-9d65-60a4a5de2b8f
  source: slides-16-bpmn
  page: 12
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 37bc8487-8246-4965-9abe-a4edeb279a74
  source: slides-16-bpmn
  page: 13
  type: embedded_image
  path: `4277faaa_p13_i0.png`

- **asset_id**: 57fceb19-f09e-4dc7-bb15-dbc355c17736
  source: slides-16-bpmn
  page: 13
  type: embedded_image
  path: `4277faaa_p13_i1.png`

- **asset_id**: 8dd72129-b9df-41f2-9721-add6e6562ef6
  source: slides-16-bpmn
  page: 13
  type: embedded_image
  path: `4277faaa_p13_i2.png`

- **asset_id**: f917a274-8987-43ce-92ba-9c69db77c8bd
  source: slides-16-bpmn
  page: 13
  type: embedded_image
  path: `4277faaa_p13_i3.png`

- **asset_id**: 79fbd228-5c70-42b0-9ca6-b8fe1ac426e0
  source: slides-16-bpmn
  page: 13
  type: embedded_image
  path: `4277faaa_p13_i4.png`

- **asset_id**: 765dbe55-6356-4d68-9f27-757c3bbd37a6
  source: slides-16-bpmn
  page: 13
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: b630a0c6-9123-4410-8d16-5c75ad775fab
  source: slides-16-bpmn
  page: 14
  type: embedded_image
  path: `4277faaa_p14_i0.png`

- **asset_id**: fb929f9a-981b-4650-8b6c-563e1533b64c
  source: slides-16-bpmn
  page: 14
  type: embedded_image
  path: `4277faaa_p14_i1.png`

- **asset_id**: 6f0a5a55-5402-4090-9686-7500bb8f6ef4
  source: slides-16-bpmn
  page: 14
  type: embedded_image
  path: `4277faaa_p14_i2.png`

- **asset_id**: c5f8b539-5c90-4824-927e-c77a8169f392
  source: slides-16-bpmn
  page: 14
  type: embedded_image
  path: `4277faaa_p14_i3.png`

- **asset_id**: 7aedfad1-f4d7-49cf-8f52-bf1af13bc3d0
  source: slides-16-bpmn
  page: 14
  type: embedded_image
  path: `4277faaa_p14_i4.png`

- **asset_id**: dc00ba9e-c843-44da-8b60-1ca193d40ac9
  source: slides-16-bpmn
  page: 14
  type: embedded_image
  path: `4277faaa_p14_i5.png`

- **asset_id**: 3404fcdb-d4a5-47d1-bdee-f75e38718eaa
  source: slides-16-bpmn
  page: 14
  type: embedded_image
  path: `4277faaa_p14_i6.png`

- **asset_id**: a0b9e52e-6fea-42fb-944b-3c9407e1c147
  source: slides-16-bpmn
  page: 14
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 9a3d0683-2d37-4708-b868-1a5457775fdb
  source: slides-16-bpmn
  page: 15
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 7cd848c1-1843-4253-b8c3-ee1f340f6e78
  source: slides-16-bpmn
  page: 16
  type: embedded_image
  path: `4277faaa_p16_i0.png`

- **asset_id**: 2e29f10e-7a8f-47d1-86bf-abaa67d342a2
  source: slides-16-bpmn
  page: 16
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: c46e5ed4-eb34-4faf-abaa-ffdc009656f7
  source: slides-16-bpmn
  page: 17
  type: embedded_image
  path: `4277faaa_p17_i0.png`

- **asset_id**: 07b41129-817a-4e27-aacb-6f2deec1be4e
  source: slides-16-bpmn
  page: 17
  type: embedded_image
  path: `4277faaa_p17_i1.png`

- **asset_id**: 68a84a35-12d4-47cd-8027-57a9a9c4cbff
  source: slides-16-bpmn
  page: 17
  type: embedded_image
  path: `4277faaa_p17_i2.png`

- **asset_id**: ae63de6e-2050-4fdd-86f9-0af054e2920e
  source: slides-16-bpmn
  page: 17
  type: embedded_image
  path: `4277faaa_p17_i3.png`

- **asset_id**: 16e6833d-a274-47e2-959e-bbab5cc10751
  source: slides-16-bpmn
  page: 17
  type: embedded_image
  path: `4277faaa_p17_i4.png`

- **asset_id**: 8bb6117b-cf49-4b28-ba48-fa3b94cb37d7
  source: slides-16-bpmn
  page: 17
  type: embedded_image
  path: `4277faaa_p17_i5.png`

- **asset_id**: 5897ddeb-bc73-49e4-a5f9-aa5731d37394
  source: slides-16-bpmn
  page: 17
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 772c83c8-a3e8-4c9d-8c76-06a00eec1700
  source: slides-16-bpmn
  page: 18
  type: embedded_image
  path: `4277faaa_p18_i0.png`

- **asset_id**: 2672a751-07ca-454b-807d-2dee36348492
  source: slides-16-bpmn
  page: 18
  type: embedded_image
  path: `4277faaa_p18_i1.png`

- **asset_id**: a585937b-f738-443a-8272-60cee6111618
  source: slides-16-bpmn
  page: 18
  type: embedded_image
  path: `4277faaa_p18_i2.png`

- **asset_id**: 29b6fff6-1e36-4156-a3ca-0b065a731717
  source: slides-16-bpmn
  page: 18
  type: embedded_image
  path: `4277faaa_p18_i3.png`

- **asset_id**: 3d92087e-d479-459e-a528-b628912a16ae
  source: slides-16-bpmn
  page: 18
  type: embedded_image
  path: `4277faaa_p18_i4.png`

- **asset_id**: b8f6ea7d-33ef-416f-aa0e-db6c6d2cae72
  source: slides-16-bpmn
  page: 18
  type: embedded_image
  path: `4277faaa_p18_i5.png`

- **asset_id**: 544a8e4f-b510-429d-9f6e-c4bfdf8dd529
  source: slides-16-bpmn
  page: 18
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 6556e12f-fb2d-4682-be15-023de638b74b
  source: slides-16-bpmn
  page: 19
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 7e469aa8-0401-43cc-a843-165bbbb1ade6
  source: slides-16-bpmn
  page: 20
  type: embedded_image
  path: `4277faaa_p20_i0.png`

- **asset_id**: 964e8e15-0ca4-4c7e-a3ba-0a0b089b8f41
  source: slides-16-bpmn
  page: 20
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 4519ac32-3f4e-4e35-aad3-ab9deb2e4463
  source: slides-16-bpmn
  page: 21
  type: embedded_image
  path: `4277faaa_p21_i0.png`

- **asset_id**: 068c8ae3-478b-47fb-9911-fa1645bc5b95
  source: slides-16-bpmn
  page: 21
  type: embedded_image
  path: `4277faaa_p21_i1.png`

- **asset_id**: 4c7efa30-7483-436e-92b8-c0c262613ae4
  source: slides-16-bpmn
  page: 21
  type: embedded_image
  path: `4277faaa_p21_i2.png`

- **asset_id**: 22b75cf1-d3a5-46c0-9f25-562832bbb124
  source: slides-16-bpmn
  page: 21
  type: embedded_image
  path: `4277faaa_p21_i3.png`

- **asset_id**: b78fa83d-a3a6-4a0a-87aa-1c677dce49f0
  source: slides-16-bpmn
  page: 21
  type: embedded_image
  path: `4277faaa_p21_i4.png`

- **asset_id**: dc3d3c5c-8e6f-45ac-8f97-daabc0d7c2e1
  source: slides-16-bpmn
  page: 21
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: fc62b3f6-59e7-478b-a478-9258f0930511
  source: slides-16-bpmn
  page: 22
  type: embedded_image
  path: `4277faaa_p22_i0.png`

- **asset_id**: 101af697-ac6a-4a23-87d4-2de70afca129
  source: slides-16-bpmn
  page: 22
  type: embedded_image
  path: `4277faaa_p22_i1.png`

- **asset_id**: b9dba53d-1995-4187-8ccb-949a0e2e3d68
  source: slides-16-bpmn
  page: 22
  type: embedded_image
  path: `4277faaa_p22_i2.png`

- **asset_id**: 38ba29d2-671b-4b9f-b91a-205dbfc4e60e
  source: slides-16-bpmn
  page: 22
  type: embedded_image
  path: `4277faaa_p22_i3.png`

- **asset_id**: b462168b-bf33-4e5d-a89b-5eb858cff2a4
  source: slides-16-bpmn
  page: 22
  type: embedded_image
  path: `4277faaa_p22_i4.png`

- **asset_id**: 95acb567-ec4c-497a-8232-08b19326da20
  source: slides-16-bpmn
  page: 22
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: ec052a60-7453-45a1-9c3c-6138545d346f
  source: slides-16-bpmn
  page: 23
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: e348d220-b5cf-4724-b43a-a6352b473f0a
  source: slides-16-bpmn
  page: 24
  type: embedded_image
  path: `4277faaa_p24_i0.png`

- **asset_id**: 69bf5b9e-e61a-49d6-8b46-4d42f39be1be
  source: slides-16-bpmn
  page: 24
  type: embedded_image
  path: `4277faaa_p24_i1.png`

- **asset_id**: f4827b52-f9a7-4cbf-964c-2c388c87cda0
  source: slides-16-bpmn
  page: 24
  type: embedded_image
  path: `4277faaa_p24_i2.png`

- **asset_id**: 99c7684c-8858-4193-9779-1dafa04d7dfc
  source: slides-16-bpmn
  page: 24
  type: embedded_image
  path: `4277faaa_p24_i3.png`

- **asset_id**: ea115dcd-6135-49c2-a270-63db31c181ec
  source: slides-16-bpmn
  page: 24
  type: embedded_image
  path: `4277faaa_p24_i4.png`

- **asset_id**: 50680a68-6a10-4aa1-9e39-3b42df371f66
  source: slides-16-bpmn
  page: 24
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 0950004b-de1f-4007-b3fa-65f67c30dfb8
  source: slides-16-bpmn
  page: 25
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: ad60f07b-745d-4cb1-b3d5-2ff3c149582b
  source: slides-16-bpmn
  page: 26
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 2787eb0d-002a-4752-b39d-6aafe0a5e708
  source: slides-16-bpmn
  page: 27
  type: embedded_image
  path: `4277faaa_p27_i0.png`

- **asset_id**: c58e1202-0989-45e0-ae9c-ab868f73c160
  source: slides-16-bpmn
  page: 27
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: d0c17a1b-e9ff-4a26-b532-96259cbce948
  source: slides-16-bpmn
  page: 28
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: fd9c46e5-2a7d-4b6d-ab03-ed7321ffddbc
  source: slides-16-bpmn
  page: 29
  type: embedded_image
  path: `4277faaa_p29_i0.jpeg`

- **asset_id**: 8e975f8a-8cb7-4e87-b36f-d682c89c3c75
  source: slides-16-bpmn
  page: 29
  type: embedded_image
  path: `4277faaa_p29_i1.png`

- **asset_id**: 161d489c-ace4-4862-b848-039f419c6582
  source: slides-16-bpmn
  page: 29
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: e6850dd6-eb67-41c7-8d9b-ef49e24798ab
  source: slides-16-bpmn
  page: 30
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: d3bc3a9f-aa8e-4ef0-ad00-931ff2b03bbb
  source: slides-16-bpmn
  page: 31
  type: embedded_image
  path: `4277faaa_p31_i0.png`

- **asset_id**: bf9b9e95-8b36-4623-9303-d9072edbc312
  source: slides-16-bpmn
  page: 31
  type: embedded_image
  path: `4277faaa_p31_i1.png`

- **asset_id**: acfa01d9-900f-4efb-abf8-909cb68b56dd
  source: slides-16-bpmn
  page: 31
  type: embedded_image
  path: `4277faaa_p31_i2.png`

- **asset_id**: 4b7ac4c9-9c53-4ecb-810b-6afffce1f60e
  source: slides-16-bpmn
  page: 31
  type: embedded_image
  path: `4277faaa_p31_i3.png`

- **asset_id**: f22a11cc-44d4-440a-ae07-f3ec3dcce079
  source: slides-16-bpmn
  page: 31
  type: embedded_image
  path: `4277faaa_p31_i4.png`

- **asset_id**: 39f12014-8791-493d-91be-76fb4599b9d8
  source: slides-16-bpmn
  page: 31
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 9cde34ea-19d4-4a20-98b8-0b8fa70d7e02
  source: slides-16-bpmn
  page: 32
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 8d709e55-d9ef-403b-9452-591fe20b2671
  source: slides-16-bpmn
  page: 33
  type: embedded_image
  path: `4277faaa_p33_i0.png`

- **asset_id**: 6690c805-0dd1-4ce1-9ad0-a63e1cfbbb37
  source: slides-16-bpmn
  page: 33
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: c27e444e-36af-4cd8-a51e-61a491e0dec9
  source: slides-16-bpmn
  page: 34
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 336b72fc-4dcf-4641-ab92-f0f74c8e60f5
  source: slides-16-bpmn
  page: 35
  type: embedded_image
  path: `4277faaa_p35_i0.png`

- **asset_id**: 37b2e3e5-28f7-4be5-bb5f-145d11340d8b
  source: slides-16-bpmn
  page: 35
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 3cf0f736-e0f3-4547-9f01-14ecc7070342
  source: slides-16-bpmn
  page: 36
  type: embedded_image
  path: `4277faaa_p36_i0.jpeg`

- **asset_id**: 2c1ae4d5-2f09-4380-b1ca-c354b50e0368
  source: slides-16-bpmn
  page: 36
  type: embedded_image
  path: `4277faaa_p36_i1.jpeg`

- **asset_id**: d170cbc6-1f03-4e45-8dd9-9ac1efb0bced
  source: slides-16-bpmn
  page: 36
  type: embedded_image
  path: `4277faaa_p36_i2.jpeg`

- **asset_id**: 0742c763-ea99-4cc0-b08b-9d23bcff0371
  source: slides-16-bpmn
  page: 36
  type: embedded_image
  path: `4277faaa_p36_i3.jpeg`

- **asset_id**: 13f2893e-82b7-4333-8b68-569bc9b50682
  source: slides-16-bpmn
  page: 36
  type: embedded_image
  path: `4277faaa_p36_i4.jpeg`

- **asset_id**: fe68dbc5-acd1-4777-9242-a5d56f9933a2
  source: slides-16-bpmn
  page: 36
  type: embedded_image
  path: `4277faaa_p36_i5.jpeg`

- **asset_id**: e6273d14-6d68-479d-af94-b0ff7f0f7a8d
  source: slides-16-bpmn
  page: 36
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 79140a9c-ef7a-4f20-a1b7-45eed9f7cc0b
  source: slides-16-bpmn
  page: 37
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 92374880-d754-4e1c-a587-f2ff805175ea
  source: slides-16-bpmn
  page: 38
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: bca224a6-6aa3-4d16-93e4-5daceca3058f
  source: slides-16-bpmn
  page: 39
  type: embedded_image
  path: `4277faaa_p39_i0.png`

- **asset_id**: fedf7a27-b3b2-4226-a05e-5f0af7f98d58
  source: slides-16-bpmn
  page: 39
  type: embedded_image
  path: `4277faaa_p39_i1.png`

- **asset_id**: 395d6f70-a0d8-4b29-8139-b97a1fa21aed
  source: slides-16-bpmn
  page: 39
  type: embedded_image
  path: `4277faaa_p39_i2.png`

- **asset_id**: e98215c3-1d02-4918-b5cd-ede481b1620c
  source: slides-16-bpmn
  page: 39
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: f8f5b90e-09e7-44c8-84c7-e7641d045abd
  source: slides-16-bpmn
  page: 40
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: ab3e9cd7-665b-424d-8798-5f7185088f57
  source: slides-16-bpmn
  page: 41
  type: embedded_image
  path: `4277faaa_p41_i0.png`

- **asset_id**: e48bc5bd-a685-4eda-8b85-f569938e9897
  source: slides-16-bpmn
  page: 41
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: f107c240-563c-49f7-ac23-1a2d17c4cc31
  source: slides-16-bpmn
  page: 42
  type: embedded_image
  path: `4277faaa_p42_i0.png`

- **asset_id**: 7358b828-04ee-4d2b-bce8-8bfd3e792914
  source: slides-16-bpmn
  page: 42
  type: embedded_image
  path: `4277faaa_p42_i1.png`

- **asset_id**: 47949ae6-28f9-4016-ae22-8679418913e3
  source: slides-16-bpmn
  page: 42
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 3e83aadc-4937-419c-9d1f-2dbbbb3815c8
  source: slides-16-bpmn
  page: 43
  type: embedded_image
  path: `4277faaa_p43_i0.png`

- **asset_id**: 9357109f-73ad-4b74-ae1f-c0236066b360
  source: slides-16-bpmn
  page: 43
  type: embedded_image
  path: `4277faaa_p43_i1.png`

- **asset_id**: bed70a32-4b8a-4867-ad7f-46e307c5e42d
  source: slides-16-bpmn
  page: 43
  type: embedded_image
  path: `4277faaa_p43_i2.png`

- **asset_id**: 05667a6c-496a-4454-a8fc-f5a671be7ee0
  source: slides-16-bpmn
  page: 43
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: ca1266d4-0e05-48e0-bc8e-7f663a1f97d5
  source: slides-16-bpmn
  page: 44
  type: embedded_image
  path: `4277faaa_p44_i0.png`

- **asset_id**: 1034f50b-102b-4299-a8e7-5d3df4f95a7d
  source: slides-16-bpmn
  page: 44
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 6d50a320-4626-4e3f-8aff-6b682e278780
  source: slides-16-bpmn
  page: 45
  type: embedded_image
  path: `4277faaa_p45_i0.png`

- **asset_id**: d2a043f7-4ed8-4b71-baa7-ca240aa75230
  source: slides-16-bpmn
  page: 45
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 24dfe619-717f-4083-b9de-31ad879e3359
  source: slides-16-bpmn
  page: 46
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 9faa61b7-bf63-4e32-a580-f526c875c3c1
  source: slides-16-bpmn
  page: 47
  type: embedded_image
  path: `4277faaa_p47_i0.png`

- **asset_id**: 334199af-471d-40c9-9962-397d36d84210
  source: slides-16-bpmn
  page: 47
  type: embedded_image
  path: `4277faaa_p47_i1.png`

- **asset_id**: b2c03001-b31b-4af9-9d2d-7097cbf72fdb
  source: slides-16-bpmn
  page: 47
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 8fe711ce-3453-4611-85da-841941c30a3b
  source: slides-16-bpmn
  page: 48
  type: embedded_image
  path: `4277faaa_p48_i0.png`

- **asset_id**: 3f2d4354-d36f-461d-bede-ca87f7864414
  source: slides-16-bpmn
  page: 48
  type: embedded_image
  path: `4277faaa_p48_i1.png`

- **asset_id**: 352fc8a1-0f99-49e0-a46f-47a15e629667
  source: slides-16-bpmn
  page: 48
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 750d2cf3-a3d8-4738-85da-e276fe12fe49
  source: slides-16-bpmn
  page: 49
  type: embedded_image
  path: `4277faaa_p49_i0.jpeg`

- **asset_id**: 78fd67e7-9969-4c71-a619-9ab63b4662dc
  source: slides-16-bpmn
  page: 49
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

