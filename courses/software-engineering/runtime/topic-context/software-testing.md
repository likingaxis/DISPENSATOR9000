# Topic Context

**topic_id**: software-testing
**title**: Tecniche di Testing

## Retrieval Metadata
- Primary fragments: 500
- Secondary fragments: 10
- Visual assets candidate: 654
- Estimated context tokens: ~6951

## 1. Primary Evidence (Official Coverage)

### Source: slides-14-testing (`official-slides\II parte ISW\14-Testing.pdf`)
#### Page 0
> © UniRoma2 - Ingegneria del Software 1

> Verification and Validation

> • Assuring that a software system conforms to its  specification and meets the user's needs

> • Verification:    "Are we building the product right?"

> i.e., the software should conform to its  specification

> • Validation:    "Are we building the right product?"

> i.e., the software should do what the user really  requires

#### Page 1
> © UniRoma2 - Ingegneria del Software 2

> • Is a whole life-cycle process - V&V must be  applied at each stage in the software process.

> • Has two principal objectives

> – The discovery of defects in a system

> – The assessment of whether or not the system is  usable in an operational situation

> • V&V should be independent, which means that  the development team and the SQA team should  be separate teams (different managers and  different members)

> The V&V process

#### Page 2
> © UniRoma2 - Ingegneria del Software 3

> • Software inspections  Concerned with analysis of

> the static system representation to discover

> problems (static techniques)

> – May be supplemented by tool-based document and

> code analysis

> • Software testing  Concerned with exercising and

> observing product behaviour (dynamic

> techniques)

> – The system is executed with test data and its

> operational behaviour is observed

> V&V techniques

#### Page 3
> © UniRoma2 - Ingegneria del Software 4

> Static and dynamic V&V

> Formal specification High-level

> design Requirements

> specification

> Detailed

> design Program

> Prototype Dynamic validation

> Static verification

> (or testing)

> (or software inspections)

#### Page 4
> © UniRoma2 - Ingegneria del Software 5

> • Can reveal the presence of defects NOT their  absence

> • A successful test is a test which discovers one  or more defects

> • The only validation technique for non-functional  user requirements

> – Dynamic validation of non-executable artifacts can be carried out  using simulation-based approached

> • Should be used in conjunction with static  verification to provide full V&V coverage

> – Static techniques can only check the correspondence between a  program and its specification (verification); they cannot  demonstrate that the software is operationally useful (validation)

> Dynamic validation (testing)

#### Page 5
> © UniRoma2 - Ingegneria del Software 6

> • Validation testing

> – Tests intended to demonstrate that a system meets  its user requirements

> – A successful validation test requires the system to  perform correctly using given acceptance test cases

> • Defect testing

> – Tests designed to discover system defects

> – A successful defect test is one which reveals the  presence of defects in a system

> • Statistical testing

> – Tests designed to reflect the frequency of user inputs

> – Used for reliability estimation

> Types of testing

#### Page 6
> © UniRoma2 - Ingegneria del Software 7

> V&V goals • V&V should establish confidence that the  software is fit for purpose • This does NOT mean that the system must be  completely free of defects, but good enough for  its intended use and the type of use will  determine the degree of confidence that is  needed, which depends on:

> – System’s purpose

> • The level of confidence depends on how critical the software  is to an organisation – User expectations

> • Users may have low expectations of certain kinds of software – Marketing environment

> • Getting a product to market early may be more important  than finding defects in the program

#### Page 7
> © UniRoma2 - Ingegneria del Software 8

> • Defect testing and debugging are distinct  processes

> • Verification and validation is concerned with  establishing the existence of defects in a  program

> • Debugging is concerned with locating and  repairing these defects

> • Debugging involves formulating a hypothesis  about program behaviour then testing these  hypotheses to find the system defect

> Testing vs. debugging

#### Page 8
> © UniRoma2 - Ingegneria del Software 9

> The debugging process

> Locate

> error

> Design error repair

> Repair

> error

> Re-test program

> Test results Specification Test cases

#### Page 9
> © UniRoma2 - Ingegneria del Software 10

> The testing process

> Sub-system

> testing

> Module

> testing

> Unit testing

> System

> testing

> Acceptance

> testing

> Component

> testing

> Integration testing User testing

#### Page 10
> © UniRoma2 - Ingegneria del Software 11

> Testing stages • Unit testing

> – Individual components are tested • Module testing

> – Related collections of dependent components are  tested • Sub-system testing

> – Modules are integrated into sub-systems and tested.  The focus here should be on interface testing • System testing

> – Testing of the system as a whole. Testing of emergent  properties • Acceptance testing

> – Testing with customer data to check that it is  acceptable

#### Page 11
> © UniRoma2 - Ingegneria del Software 12

> • Careful planning is required to get the most  out of testing and inspection processes

> • Planning should start early in the  development process

> • The plan should identify the balance  between static verification and testing

> • Test planning is about defining standards  for the testing process rather than  describing product tests

> V&V planning

#### Page 12
> © UniRoma2 - Ingegneria del Software 13

> The V-model of development

> Requirements

> specification

> System specification

> System

> design

> Detailed

> design

> Module and

> unit code

> and tess

> Sub-system

> integration

> test plan

> System integration

> test plan

> Acceptance

> test plan

> Service Acceptance

> test

> System integration test

> Sub-system integration test

#### Page 13
> © UniRoma2 - Ingegneria del Software 14

> The structure of a software test plan

> • The testing process

> • Requirements traceability

> • Tested items

> • Testing schedule

> • Test recording procedures

> • Hardware and software requirements

> • Constraints

#### Page 14
> © UniRoma2 - Ingegneria del Software 15

> Software inspections

> • Involve people examining the source  representation with the aim of discovering  anomalies and defects • Do not require execution of a system so may be  used before implementation • May be applied to any representation of the  system (requirements, design, test data, etc.) • Very effective technique for discovering defects:

> – Fagan (1986) reported that more than 60% of the  defects in a program can be detected using software  inspections – Mills et al. (1987) suggest that a more formal  approach, using mathematical verification, can detect  more than 90% of the defects in a program

#### Page 15
> © UniRoma2 - Ingegneria del Software 16

> Inspections and testing

> • Inspections and testing are complementary  and not opposing verification techniques • Both should be used during the V&V  process • Inspections can check conformance with a  specification but not conformance with the  customer’s real requirements • Inspections cannot check non-functional  characteristics such as performance,  usability, etc.

#### Page 16
> © UniRoma2 - Ingegneria del Software 17

> Program inspections

> • Formalised approach to document reviews

> • Intended explicitly for defect DETECTION

> (not correction)

> • Defects may be logical errors, anomalies in

> the code that might indicate an erroneous

> condition (e.g. a not-initialised variable) or

> non-compliance with standards

#### Page 17
> © UniRoma2 - Ingegneria del Software 18

> Inspection pre-conditions • A precise specification must be available • Team members must be familiar with the  organisation standards • Syntactically correct code must be  available • A defect checklist should be prepared • Management must accept that inspection  will increase costs early in the software  process • Management must not use inspections for  staff appraisal

#### Page 18
> © UniRoma2 - Ingegneria del Software 19

> The inspection process

> Inspection

> meeting

> Individual preparation

> Overview

> Planning

> Rework

> Follow-up

#### Page 19
> © UniRoma2 - Ingegneria del Software 20

> Inspection procedure • System overview presented to inspection  team

> • Code and associated documents are  distributed to inspection team in advance

> • Inspection takes place and discovered  defects are noted

> • Modifications are made to repair  discovered defects

> • Re-inspection may or may not be required

#### Page 20
> © UniRoma2 - Ingegneria del Software 21

> Inspection teams

> • Made up of at least 4 members – Author: of the code being inspected – Inspector: who  finds defects,

> omissions and inconsistencies  – Reader: who reads the code to the

> team – Moderator: who chairs the meeting and

> notes discovered defects – Other roles are Scribe and  Chief

> moderator

#### Page 21
> © UniRoma2 - Ingegneria del Software 22

> Inspection checklists

> • Checklist of common defects should be

> used to  drive the inspection

> • Defects checklist is programming language

> dependent

> • The 'weaker' the type checking, the larger

> the checklist

> • Examples: Initialisation, constant naming,

> loop termination, array bounds, etc.

#### Page 22
> © UniRoma2 - Ingegneria del Software 23

> Inspection

> checks

> Fault class Inspection check Data faults Are all program variables initialised before their  values are used? Have all constants been named? Should the lower bound of arrays be 0, 1, or something else?   Should the upper bound of arrays be equal to the size of the array or Size -1? If character strings are  used, is a delimiter explicitly assigned?   Control faults For each conditional statement, is the condition correct? Is each loop certain to terminate? Are compound statements correctly bracketed? In case statements, are all possible cases accounted for? Input/output faults Are all input variables used? Are all output variables assigned a value before they are output? Interface faults Do all function and procedure calls have the correct number of parameters? Do formal and actual parameter types match?   Are the parameters in the right order?   If components access shared memory, do they have  the same model of the shared memory structure? Storage management faults

> If a linked structure is modified,  have all links been correctly reassigned? If dynamic storage is used, has space been allocated correctly? Is space explicitly de-allocated after it  is no longer required? Exception management faults

> Have all possible error conditions been taken  into account?

#### Page 23
> © UniRoma2 - Ingegneria del Software 24

> Inspection rate

> • 500 statements/hour during overview

> • 125 source statements/hour during

> individual preparation

> • 100-125 statements/hour can be inspected

> • Inspection is therefore an expensive

> process

> • Inspecting 500 statements costs about 40

> man/hours of effort

#### Page 24
> © UniRoma2 - Ingegneria del Software 25

> Automated static analysis

> • Static analysers are software tools for  source text processing

> • They parse the program text and try to  discover potentially erroneous conditions  and bring these to the attention of the V&V  team

> • Very effective as an aid to inspections. A  supplement to but not a replacement for  inspections

#### Page 25
> © UniRoma2 - Ingegneria del Software 26

> Static analysis checks

> Fault class Static analysis check Data faults Variables used before initialisation Variables declared but never used Variables assigned twice but never used between assignments Possible array bound violations   Undeclared variables Control faults Unreachable code Unconditional branches into loops Input/output faults Variables output twice with no intervening assignment Interface faults Parameter type mismatches Parameter number mismatches Non-usage of the results of functions Uncalled functions and procedures Storage  management faults

> Unassigned pointers Pointer arithmetic

#### Page 26
> © UniRoma2 - Ingegneria del Software 27

> Stages of static analysis

> • Control flow analysis.  Checks for loops  with multiple exit or entry points, finds  unreachable code, etc.

> • Data use analysis.  Detects not-initialised  variables, variables assigned twice without  an intervening assignment, variables which  are declared but never used, etc.

> • Interface analysis.  Checks the consistency  of routine and procedure declarations and  their use

#### Page 27
> © UniRoma2 - Ingegneria del Software 28

> Stages of static analysis

> • Information flow analysis.  Identifies the  dependencies of output variables. Does not  detect anomalies itself but highlights  information for code inspection or review • Path analysis.  Identifies paths through the  program and sets out the statements  executed in that path. Again, potentially  useful in the review process • Both these stages generate vast amounts  of information. Must be used with care.

#### Page 28
> © UniRoma2 - Ingegneria del Software 29

> LINT static analysis

> >> more lint_ex.c

> #include <stdio.h> printarray (Anarray)   int Anarray; {   printf(“%d”,Anarray); } main () {   int Anarray[5]; int i; char c;   printarray (Anarray, i, c);   printarray (Anarray) ; }

> >> cc lint_ex.c >> lint lint_ex.c

> lint_ex.c(10): warning: c may be used before set lint_ex.c(10): warning: i may be used before set printarray: variable # of args. lint_ex.c(4) :: lint_ex.c(10) printarray, arg. 1 used inconsistently lint_ex.c(4) :: lint_ex.c(10) printarray, arg. 1 used inconsistently lint_ex.c(4) :: lint_ex.c(11) printf returns value which is always ignored

#### Page 29
> © UniRoma2 - Ingegneria del Software 30

> Use of static analysis

> • Particularly valuable when a language such

> as C is used which has weak typing and

> hence many defects are undetected by the

> compiler

> • Less cost-effective for languages like Java

> that have strong type checking and can

> therefore detect many defects during

> compilation

#### Page 30
> © UniRoma2 - Ingegneria del Software 31

> • The name is derived from the 'Cleanroom'  process in semiconductor fabrication. The  philosophy is defect avoidance rather than  defect removal • Software development process based on:

> – Incremental development – Formal specification – Static verification using correctness

> arguments – Statistical testing to determine program

> reliability

> Cleanroom software development

#### Page 31
> © UniRoma2 - Ingegneria del Software 32

> The Cleanroom process

> Construct structured

> program

> Define software increments

> Formally

> verify

> code

> Integrate increment

> Formally

> specify system

> Develop operational

> profile

> Design statistical

> tests

> Test integrated

> system

> Error rework

#### Page 32
> © UniRoma2 - Ingegneria del Software 33

> Cleanroom process characteristics

> • Formal specification using a state  transition model

> • Incremental development

> • Structured programming - limited control  and abstraction constructs are used

> • Static verification using rigorous  inspections

> • Statistical testing of the system

#### Page 33
> © UniRoma2 - Ingegneria del Software 34

> Incremental development

> Formal specification

> Develop s/w

> increment Establish rerquirements

> Deliver software

> Frozen specification

> Requirements change request

#### Page 34
> © UniRoma2 - Ingegneria del Software 35

> Formal specification and inspections

> • The state based model is a system  specification and the inspection process  checks the program against this model

> • Programming approach is defined so that  the correspondence (transformation)  between the model and the system is clear

> • Mathematical arguments (not proofs) are  used to increase confidence in the  inspection process

#### Page 35
> © UniRoma2 - Ingegneria del Software 36

> • Specification team.  Responsible for developing  and maintaining the system specification

> • Development team.  Responsible for  developing and verifying the software.  The  software is NOT executed or even compiled  during this process

> • Certification team.  Responsible for developing a  set of statistical tests to exercise the software  after development. Reliability growth models are  used to determine when to stop testing (i.e.,  when reliability is acceptable)

> Cleanroom process teams

#### Page 36
> © UniRoma2 - Ingegneria del Software 37

> • Results in IBM have been very impressive  with few discovered faults in delivered  systems • Independent assessment shows that the  process is no more expensive than other  approaches • Fewer defects than in a 'traditional'  development process • Not clear how this approach can be  transferred to an environment with less  skilled or less highly motivated engineers

> Cleanroom process evaluation

#### Page 37
> © UniRoma2 - Ingegneria del Software 38

> • Validation testing

> – Tests intended to demonstrate that a system meets  its user requirements

> – A successful validation test requires the system to  perform correctly using given acceptance test cases

> • Defect testing

> – Tests designed to discover system defects

> – A successful defect test is one which reveals the  presence of defects in a system

> • Statistical testing

> – Tests designed to reflect the frequency of user inputs

> – Used for reliability estimation

> Types of testing

> We focus on this

#### Page 38
> © UniRoma2 - Ingegneria del Software 39

> Defect testing • The goal of defect testing is to discover  defects in programs • This contrast with validation testing which is  intended to demonstrate that a system meets  its user requirements • Validation testing requires the system to  perform correctly using given acceptance test  cases • A successful defect test is a test which causes  a program to behave in an anomalous way • Tests show the presence not the absence of  defects

#### Page 39
> © UniRoma2 - Ingegneria del Software 40

> Defect testing phases

> Component

> testing

> Integration

> testing

> Software developer Independent testing team • Component testing (unit and module testing)

> – Testing of individual program components – Usually the responsibility is of the component developer (except sometimes

> for critical systems) – Tests are derived from the developer’s experience • Integration testing (sub-system and system testing)

> – Testing of groups of components integrated to create a system or sub-

> system – The responsibility is of an independent testing team – Tests are based on a system specification • User testing (validation or acceptance testing) is not part of the defect  testing process

#### Page 40
> © UniRoma2 - Ingegneria del Software 41

> • Only exhaustive testing can show that a  program is free from defects. However,  exhaustive testing is impossible • Testing must be based on a subset of  possible test cases, according to policies  which should be devised by the V&V team  (and not by the development team) • Tests should exercise a system's  capabilities rather than its components • Testing typical situations is more important  than boundary value cases

> Testing policies

#### Page 41
> © UniRoma2 - Ingegneria del Software 42

> • Test cases

> – Inputs to test the system and the predicted

> outputs from these inputs if the system  operates according to its specification – Test cases are usually generated manually

> (because it is not easy to automatically derive  test output from informal specifications) • Test data

> – Inputs which have been devised to test the

> system – Test data can be generated automatically

> Test cases and test data

#### Page 42
> © UniRoma2 - Ingegneria del Software 43

> The defect testing process

> Design test

> cases

> Prepare test

> data

> Run program with test data

> Compare results

> to test cases

> Test cases

> Test data

> Test results

> Test reports

#### Page 43
> © UniRoma2 - Ingegneria del Software 44

> Black-box testing • An approach to testing where the program is  considered as a black-box • The program test cases are derived from the  system specification  • The tester presents inputs to the component  or system and examines the corresponding  output • If the outputs are not those specified then the  test has successfully detected a problem with  the software • Also called functional testing because the  tester is only concerned with the functionality  and not the implementation of the software

#### Page 44
> © UniRoma2 - Ingegneria del Software 45

> Black-box testing

> I e Input test data

> Oe Output test results

> System

> Inputs causing anomalous behaviour

> Outputs which reveal the presence of defects

> Ie

#### Page 45
> © UniRoma2 - Ingegneria del Software 46

> Equivalence partitioning

> • Input data and output results often fall into

> different classes where all members of a

> class are related

> • Each of these classes is an equivalence

> partition where the program behaves in an

> equivalent way for each class member

> • Test cases should be chosen from each

> partition

#### Page 46
> © UniRoma2 - Ingegneria del Software 47

> Equivalence partitioning

> System

> Outputs

> Invalid inputs Valid inputs

#### Page 47
> © UniRoma2 - Ingegneria del Software 48

> • Partition system inputs and outputs into  ‘equivalence partitions’

> – If input is a 5-digit integer between 10,000

> and 99,999, equivalence partitions are < 10,000 | 10,000-99,999 | > 99,999

> • Choose test cases at the boundary of  these partitions plus cases close to the  mid-point of the partitions with valid inputs

> – 09999, 10000, 50000, 99999, 100000

> Equivalence partitioning

#### Page 48
> © UniRoma2 - Ingegneria del Software 49

> Equivalence partitions

> Between 10000 and 99999 Less than 10000 More than 99999

> 9999 10000 50000 100000 99999

> Input values

> Between 4 and 10 Less than 4 More than 10

> 3 4 7 11 10

> Number of input values

#### Page 49
> © UniRoma2 - Ingegneria del Software 50

> Search routine specification

> procedure Search (Key : ELEM ; T: ELEM_ARRAY;        Found : in out BOOLEAN; L: in out ELEM_INDEX) ;

> Pre-condition   -- the array has at least one element   T’FIRST <= T’LAST  Post-condition   -- the element is found and is referenced by L   ( Found and T (L) = Key)  or    -- the element is not in the array   ( not Found and         not (exists i, T’FIRST >= i <= T’LAST, T (i) = Key ))

#### Page 50
> © UniRoma2 - Ingegneria del Software 51

> • Inputs which conform to the pre- conditions

> • Inputs where a pre-condition does not  hold

> • Inputs where the key element is a  member of the array

> • Inputs where the key element is not a  member of the array

> Search routine - input partitions

#### Page 51
> © UniRoma2 - Ingegneria del Software 52

> Testing guidelines (sequences)

> • Test software with sequences which have

> only a single value

> • Use sequences of different sizes in

> different tests

> • Derive tests so that the first, middle and

> last elements of the sequence are

> accessed

> • Test with sequences of zero length

#### Page 52
> © UniRoma2 - Ingegneria del Software 53

> Search routine  Example input partitions and test cases

> Array  Element  Single value  In sequence  Single value  Not in sequence  More than 1 value  First element in sequence  More than 1 value  Last element in sequence  More than 1 value  Middle element in sequence  More than 1 value  Not in sequence      Input sequence (T)  Key (Key)  Output (Found, L)  17  17  true, 1  17  0  false, ??  17, 29, 21, 23  17  true, 1  41, 18, 9, 31, 30, 16, 45  45  true, 7  17, 18, 21, 23, 29, 41, 38  23  true, 4  21, 23, 29, 33, 38   25  false, ??

#### Page 53
> © UniRoma2 - Ingegneria del Software 54

> • Sometimes called white-box testing

> • Test cases are derived from the program

> structure

> • Knowledge of the program is used to

> identify additional test cases

> • Objective is to exercise all program

> statements (not all path combinations)

> Structural testing

#### Page 54
> © UniRoma2 - Ingegneria del Software 55

> White-box testing

> Component

> code

> Test outputs

> Test data

> Derives Tests

#### Page 55
> © UniRoma2 - Ingegneria del Software 56

> Binary search

> (Java)

> class BinSearch {    // This is an encapsulation of a binary search function that takes an array of  // ordered objects and a key and returns an object with 2 attributes namely   // index - the value of the array index   // found - a boolean indicating whether or not the key is in the array  // An object is returned because it is not possible in Java to pass basic types by   // reference to a function and so return two values  // the key is -1 if the element is not found        public static void search ( int key, int [] elemArray, Result r )    {      int bottom = 0 ;      int top = elemArray.length - 1 ;      int mid ;      r.found = false ; r.index = -1 ;      while ( bottom <= top )      {        mid = (top + bottom) / 2 ;        if (elemArray [mid] == key)        {          r.index = mid ;           r.found = true ;          return ;        } // if part        else        {          if (elemArray [mid] < key)            bottom = mid + 1 ;          else            top = mid - 1 ;        }      } //while loop    } // search  } //BinSearch

#### Page 56
> © UniRoma2 - Ingegneria del Software 57

> Binary search equiv. partitions

> Mid-point

> Elements < Mid Elements > Mid

> Equivalence class boundaries

#### Page 57
> © UniRoma2 - Ingegneria del Software 58

> • Pre-conditions satisfied, key element in  array • Pre-conditions satisfied, key element not  in array • Pre-conditions unsatisfied, key element in  array • Pre-conditions unsatisfied, key element  not in array • Input array has a single value • Input array has an even number of values • Input array has an odd number of values

> Binary search - equiv. partitions

#### Page 58
> © UniRoma2 - Ingegneria del Software 59

> Binary search Example test cases

> Input array (T) Key (Key) Output (Found, L) 17 17 true, 1 17 0 false, ?? 17, 21, 23, 29 17 true, 1 9, 16, 18, 30, 31, 41, 45 45 true, 7 17, 18, 21, 23, 29, 38, 41 23 true, 4 17, 18, 21, 23, 29, 33, 38 21 true, 3 12, 18, 21, 23, 32 23 true, 4 21, 23, 29, 33, 38 25 false, ??

#### Page 59
> © UniRoma2 - Ingegneria del Software 60

> Path testing

> • The objective of path testing is to ensure that the set of

> test cases is such that each path through the program

> (and thus each statement) is executed at least once

> • The number of paths through a program is usually

> proportional to its size. As modules are integrated into

> systems, it becomes unfeasible to use path testing

> techniques, that are therefore mostly used at unit or

> module testing stages

> • The starting point for path testing is a program flow graph

> that shows nodes representing program decisions and

> arcs representing the flow of control

#### Page 60
> © UniRoma2 - Ingegneria del Software 61 Binary search flow graph

> 1

> 2

> 3

> 4

> 6 5

> 7

> while bottom <= top

> if (elemArray [mid] == key

> (if (elemArray [mid]< key 8

> 9

> bottom > top

#### Page 61
> © UniRoma2 - Ingegneria del Software 62

> • 1, 2, 3, 8, 9

> • 1, 2, 3, 4, 6, 7, 2

> • 1, 2, 3, 4, 5, 7, 2

> • 1, 2, 3, 4, 6, 7, 2, 8, 9

> • Test cases should be derived so that all of  these paths are executed

> • Dynamic program analysers or profilers  may be used to check that paths have  been executed

> Independent paths

#### Page 62
> © UniRoma2 - Ingegneria del Software 63

> Integration testing

> • Tests complete systems or subsystems

> composed of integrated components

> • Integration testing should be black-box

> testing with test cases derived from the

> specification

> • Main difficulty is localising defects

> • Incremental integration testing reduces this

> problem

#### Page 63
> © UniRoma2 - Ingegneria del Software 64

> Incremental integration testing

> T3

> T2

> T1

> T4

> T5

> A

> B

> C

> D

> T2

> T1

> T3

> T4

> A

> B

> C

> T1

> T2

> T3

> A

> B

> Test sequence

> 1 Test sequence

> 2 Test sequence

> 3

## 2. Secondary Evidence (BM25 Lexical + Concepts)

### Source: theory-summary (`teoria.pdf`)
#### Page 52 (BM25: 32.24)
> risultati. Testing La fase di testing si assicura che un sistema software sia conforme alle sue

#### Page 54 (BM25: 27.69)
> sistema o un sottosistema. L'obiettivo è verificare che le componenti collaborino corretamente. È un tipo di testing black box , perché si testa l'integrazione a livello funzionale, senza entrare nel dettaglio del codice.

#### Page 7 (BM25: 18.64)
> Le caratteristiche principali sono: • Sviluppo software e testing eseguiti in parallelo. • Features prioritizzate e integrate in 3-4 sottoprogetti cardine.

#### Page 53 (BM25: 17.71)
> quando cliente e sviluppatore non coincidono. Per la fase di testing si seguono delle politiche, ovvero: • Solo test esaustivi possono mostrare che il programma sia libero di difetti

#### Page 53 (BM25: 16.64)
> • Testare situazioni tipiche è più importante che testare casi limite. Parliamo adesso dei due approcci che esistono nel testing software: • Black-box testing: si concentra sul comportamento esterno del software. Il

#### Page 53 (BM25: 15.99)
> soddisfa i requisiti del cliente. In genere viene eseguito dall'utente finale o il cliente, infatti questa fase di testing viene fatta nei software a contratto, quando cliente e sviluppatore non coincidono.

#### Page 54 (BM25: 15.52)
> ogni operazione della classe in tutti i modi possibili, cercando di capire ogni combinazione significativa di stato/azione. È anch'esso ovviamente white box . • Scenario Based Testing: È un tipo di testing che deriva dai casi d'uso. Si

#### Page 3 (BM25: 15.25)
> definizione e/o produzione al suo interno. Durante ogni fase si procede ad efettuare il testing di quanto prodotto, mediante opportune techine di verifica e validazione. Ci sono vari tipo di manutenzione:

#### Page 53 (BM25: 15.02)
> sistema o sottosistema. • User testing: Anche noto come validation testing o acceptance testing, in questa fase non si cercano difetti nel codice, ma si verifica se il software

#### Page 52 (BM25: 14.58)
> Testing La fase di testing si assicura che un sistema software sia conforme alle sue specifiche e che soddisfi le esigenze dell'utente. In particolare andremo a parlare di

## 3. Visual Assets Candidates

- **asset_id**: 6e3b8e07-145a-422f-b10d-c786f974c584
  source: slides-14-testing
  page: 0
  type: embedded_image
  path: `c4f92be1_p0_i0.png`

- **asset_id**: c2d86c3a-6a95-48d2-9445-471303577ca2
  source: slides-14-testing
  page: 0
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 94e68f4d-393f-4ed0-971e-555e424e325f
  source: slides-14-testing
  page: 1
  type: embedded_image
  path: `c4f92be1_p1_i0.png`

- **asset_id**: 200fb1bd-9ca6-4bd7-b3b3-ff0050600af1
  source: slides-14-testing
  page: 1
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: a3290d9a-9bb2-4331-8588-5dbb960d416a
  source: slides-14-testing
  page: 2
  type: embedded_image
  path: `c4f92be1_p2_i0.png`

- **asset_id**: 9d2e87f4-e0a3-4b7f-93c4-3832239b0349
  source: slides-14-testing
  page: 2
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: ac9a34e7-fb89-42d0-be08-7fef901035f6
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i0.png`

- **asset_id**: a4608a8f-43fa-4dea-80bc-53fdcbea9c40
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i1.png`

- **asset_id**: 36457650-06a2-4e9f-8698-b23261c60376
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i2.png`

- **asset_id**: c4d3df23-e797-4b85-9311-cebca504e2c1
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i3.png`

- **asset_id**: db405e57-b6bb-4ad5-bc92-a35c589abd68
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i4.png`

- **asset_id**: e477f3c9-88d9-4680-9668-e3bd6ce02df0
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i5.png`

- **asset_id**: 8250f39e-3728-4694-9cf9-452d9138e86f
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i6.png`

- **asset_id**: ea1c8736-d80b-49aa-aed5-0944ee0b349b
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i7.png`

- **asset_id**: 77a6bef4-2dee-4336-bbf8-c6426f963b47
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i8.png`

- **asset_id**: 24398431-111c-4bf5-b522-8fe076f5368c
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i9.png`

- **asset_id**: 42d47ccd-4c4d-45d6-9332-b11a42004933
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i10.png`

- **asset_id**: 97d01339-563e-4187-a59c-9a967f909743
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i11.png`

- **asset_id**: 56202435-07ba-4a5d-bb08-7d6d38d8f664
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i12.png`

- **asset_id**: c299f36f-fb66-4a31-811b-e6177e667ca7
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i13.png`

- **asset_id**: 609aae35-a286-458c-9f62-f5f582ba48cc
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i14.png`

- **asset_id**: 3ec95814-80fa-42b3-9be8-a2e0655d57f7
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i15.png`

- **asset_id**: 6a960d95-adf7-4656-a9b5-2728ad417596
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i16.png`

- **asset_id**: 58162376-674c-495f-9603-00ad6eec0e0e
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i17.png`

- **asset_id**: 8fece02d-9293-46f0-84d4-092d023ca4d9
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i18.png`

- **asset_id**: 3d72e107-ead0-4471-a0ed-3e6e89f2240c
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i19.png`

- **asset_id**: fdb1b525-e960-4bb6-a472-d3e3880b052e
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i20.png`

- **asset_id**: 1a659d51-5166-42ad-b6f2-12869f4b0de7
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i21.png`

- **asset_id**: 30c380aa-2974-47fd-a1f0-df9e8950f4c5
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i22.png`

- **asset_id**: 18261d0a-4864-4e4e-adba-0ef90d4f4e59
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i23.png`

- **asset_id**: f9f64d38-95ae-4cb4-9951-661b3ce463ec
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i24.png`

- **asset_id**: 994d0b1c-c97e-457b-9362-f497503ade8e
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i25.png`

- **asset_id**: 8db4278f-4810-475d-9391-23fc516f42a0
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i26.png`

- **asset_id**: 90c8cd7b-c77a-4f58-99f0-04f67d46a5a1
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i27.png`

- **asset_id**: bcf62b73-fdb8-43a7-9848-b67e92f2bc75
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i28.png`

- **asset_id**: d01a9b7d-bb94-4da9-aaaf-5f11b44c5cda
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i29.png`

- **asset_id**: f98d3d50-e3c7-427c-9fac-03ea7f9921bd
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i30.png`

- **asset_id**: a2394cde-fcc6-404f-807e-ea2804f8791b
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i31.png`

- **asset_id**: a666caca-a566-409c-bddf-b9d6e4591a13
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i32.png`

- **asset_id**: e9262618-605c-45d6-a3d2-a5432340f82a
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i33.png`

- **asset_id**: 5086cfac-8900-4e9d-a4b0-9a288b5abec4
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i34.png`

- **asset_id**: 4a9b084c-fe1b-4cfd-9dcd-cbcfd71fcfc6
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i35.png`

- **asset_id**: 0b0dc7f6-45f2-465f-9bf1-fe3ee0493828
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i36.png`

- **asset_id**: b4155f95-3946-4b2b-b9e8-ac2b7ecc9f67
  source: slides-14-testing
  page: 3
  type: embedded_image
  path: `c4f92be1_p3_i37.png`

- **asset_id**: 9f4c534e-8f6e-4f46-b04e-ff6c4734387f
  source: slides-14-testing
  page: 3
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 39883d90-4763-4288-ae45-06325a8a5e00
  source: slides-14-testing
  page: 4
  type: embedded_image
  path: `c4f92be1_p4_i0.png`

- **asset_id**: d1dcbe06-2c68-4dd9-b22b-b0828de5c293
  source: slides-14-testing
  page: 4
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 2aac8be7-be28-4950-a46a-ead9c8484d15
  source: slides-14-testing
  page: 5
  type: embedded_image
  path: `c4f92be1_p5_i0.png`

- **asset_id**: 87ac829b-d002-454a-8e7a-18f04cb9c978
  source: slides-14-testing
  page: 5
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 94a4e4e3-adee-4057-a9ac-c7818e84c187
  source: slides-14-testing
  page: 6
  type: embedded_image
  path: `c4f92be1_p6_i0.png`

- **asset_id**: dbe2f9bf-dc2c-4e1d-8fd0-0b3e2da23dd4
  source: slides-14-testing
  page: 6
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 97587ce3-cdda-4266-a885-608f6fbf2aaa
  source: slides-14-testing
  page: 7
  type: embedded_image
  path: `c4f92be1_p7_i0.png`

- **asset_id**: 2cba5ce9-573e-46af-bc76-529a7973e709
  source: slides-14-testing
  page: 7
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: ad803083-cce9-4066-946b-546db5527e4b
  source: slides-14-testing
  page: 8
  type: embedded_image
  path: `c4f92be1_p8_i0.png`

- **asset_id**: 9b02e607-c2f8-421c-adc7-68b1464cd3b8
  source: slides-14-testing
  page: 8
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: dba71e26-9bd3-45c3-9267-124de3c4ffe2
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i0.png`

- **asset_id**: 35dbed4d-f521-423c-b8fa-af3fbf0b0007
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i1.png`

- **asset_id**: b45c98b5-d397-4020-a465-175eed8f5284
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i2.png`

- **asset_id**: 2323ab08-b5ac-4d57-a02e-1b37a9244361
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i3.png`

- **asset_id**: 4f10be32-4430-4ac4-a78c-a6dd48a620ff
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i4.png`

- **asset_id**: 69805241-a9d9-4ac7-a617-8008ef712f42
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i5.png`

- **asset_id**: a04a7437-0403-4e08-a9c5-43eb06c259e3
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i6.png`

- **asset_id**: a9e42c87-c906-4371-9f31-f5d19eb86897
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i7.png`

- **asset_id**: 98b6dd82-6320-49e7-9cbf-782677a1a06c
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i8.png`

- **asset_id**: 943dcb20-e48d-4f66-9db1-ab7e88f1e6ee
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i9.png`

- **asset_id**: fa452cdb-f76c-4f11-9b9c-dd9662a10f2b
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i10.png`

- **asset_id**: b0904ac0-7399-4177-a280-54e7496c5b56
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i11.png`

- **asset_id**: ce2d05b1-4fb8-4e49-b888-4abfe9e32d2b
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i12.png`

- **asset_id**: 7e59183a-9770-444d-94dd-bca5b4e7caef
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i13.png`

- **asset_id**: 682dd609-9473-4d00-8deb-6fa18ee6ced9
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i14.png`

- **asset_id**: f822df9a-9194-45ed-b08d-ec9225020a69
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i15.png`

- **asset_id**: 20027d1d-348a-412e-8485-de2aa57921e2
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i16.png`

- **asset_id**: 1528215f-ea20-406f-b2f7-eb24423c3564
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i17.png`

- **asset_id**: 4bd50a5c-30ea-492a-b0e6-f8d10c5e7435
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i18.png`

- **asset_id**: cef366cd-da34-4150-a063-24220a6fa5ef
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i19.png`

- **asset_id**: 76ef86db-a2a3-485c-b606-b68558eecb33
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i20.png`

- **asset_id**: 5a6462a1-4451-4a69-9402-81862ff0b7bd
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i21.png`

- **asset_id**: d8e652da-60e1-4761-acad-cf1423cc33bc
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i22.png`

- **asset_id**: c34b1a7c-0ca9-4ca6-a58f-91b99b29c6fb
  source: slides-14-testing
  page: 9
  type: embedded_image
  path: `c4f92be1_p9_i23.png`

- **asset_id**: 5a390d12-d45a-44b6-a05f-2f03beb1bb98
  source: slides-14-testing
  page: 9
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: d19b3672-3012-461f-b7c4-e2f8d80ddfc5
  source: slides-14-testing
  page: 10
  type: embedded_image
  path: `c4f92be1_p10_i0.png`

- **asset_id**: 98e69895-50e6-44a2-9a6d-da17821a4420
  source: slides-14-testing
  page: 10
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 70e4905a-58f6-4390-bab0-49e33c3e2d43
  source: slides-14-testing
  page: 11
  type: embedded_image
  path: `c4f92be1_p11_i0.png`

- **asset_id**: cca8bbbf-29fc-40e9-8f21-b098a9a5ee3f
  source: slides-14-testing
  page: 11
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 62c4817a-18ab-4aa6-830c-0fd079fc9e62
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i0.png`

- **asset_id**: df95c459-c93d-425a-94c0-cb2ca14fdd19
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i1.png`

- **asset_id**: 86cee373-a47a-4f5e-9e93-d884794c1c57
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i2.png`

- **asset_id**: 554262c5-789c-4b3c-98c4-678519d4a62e
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i3.png`

- **asset_id**: 7afb51a0-6bb7-4db9-8a1d-820e1142db28
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i4.png`

- **asset_id**: 99370695-8861-45f2-a706-307097d3841c
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i5.png`

- **asset_id**: 4d992306-8027-474e-9882-1c4f54035f8a
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i6.png`

- **asset_id**: 073b64da-56c2-4c0f-80d0-77db6d38fbb9
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i7.png`

- **asset_id**: 10460f4e-9158-4271-9007-10ba4b22ea39
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i8.png`

- **asset_id**: c77b8dc4-7b22-4c62-a37b-4ed4f5913da3
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i9.png`

- **asset_id**: fe3ded68-44d6-4141-956b-ca17d3a26609
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i10.png`

- **asset_id**: 16e6c569-376e-41d5-b774-93f1050550e1
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i11.png`

- **asset_id**: ae462827-6415-447a-bb99-eddfd9806162
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i12.png`

- **asset_id**: 9cbd118e-a444-454c-b4dc-7f44bb076f6a
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i13.png`

- **asset_id**: 71053213-eaed-46cc-9ab3-139c0d601c06
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i14.png`

- **asset_id**: dad200f1-0fe0-4326-98ed-70484e99570d
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i15.png`

- **asset_id**: eef43d59-cb9d-460e-a877-1fe991a23ce7
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i16.png`

- **asset_id**: 0e73ce0f-ab48-48d6-ae0e-10b77249a51b
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i17.png`

- **asset_id**: 48212805-2a75-4128-ac05-19ac1ee88a5a
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i18.png`

- **asset_id**: cddbbad2-3d7d-4b6b-ad8a-8a7342c69a6d
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i19.png`

- **asset_id**: dc0f6de6-9051-4a4f-bc19-b5870373c0ca
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i20.png`

- **asset_id**: 59d88471-f9db-4a61-a357-f6d0bd8c59b4
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i21.png`

- **asset_id**: a8573b0e-aeea-48e0-b8e1-70e89d6f7508
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i22.png`

- **asset_id**: e44b33a1-0a0b-43a0-8ada-95ae00f13907
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i23.png`

- **asset_id**: 11fc1a2b-4bf8-4ec6-a75e-d9ab92369ae1
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i24.png`

- **asset_id**: 28d06404-5081-4523-8523-1415a3c6d12c
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i25.png`

- **asset_id**: 1c098d6a-9b89-4f1f-8e87-a32570828475
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i26.png`

- **asset_id**: 86e5df6d-d95b-46e9-b1e2-15015dec1568
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i27.png`

- **asset_id**: 7c085d72-1dac-4ac7-b078-ea953f97ac43
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i28.png`

- **asset_id**: 52d16e62-f916-47d0-ae9c-1d3ce54bdbcf
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i29.png`

- **asset_id**: dc39ace7-6215-49eb-b716-e8482c9edbe4
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i30.png`

- **asset_id**: ac4c45d2-8b1c-4829-933c-344f2642335c
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i31.png`

- **asset_id**: 7236e966-a3b3-4162-bf6d-40c1bf654386
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i32.png`

- **asset_id**: 20c39971-2d4a-4f6e-a046-47965d0db185
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i33.png`

- **asset_id**: 81773a37-8ce0-4207-82fe-004d7e9e696b
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i34.png`

- **asset_id**: 3a484bec-7a11-4065-9567-c34504f85a4e
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i35.png`

- **asset_id**: 53f2288e-56d9-409f-839f-93b039cbace1
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i36.png`

- **asset_id**: 980b16b1-38ea-4345-9d17-6ed5226e11d6
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i37.png`

- **asset_id**: de9b9ddd-4948-4903-819c-f800c9c6a3ab
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i38.png`

- **asset_id**: 064d0a23-8682-4b7f-97fe-eeb90d561bac
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i39.png`

- **asset_id**: 54cb729d-14ce-4ebf-906b-0189c1b5a9a8
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i40.png`

- **asset_id**: 64fce89b-fdad-4925-9c2c-5d086fc3e5d7
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i41.png`

- **asset_id**: e35d3155-9086-492b-b351-59f0c51aba8e
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i42.png`

- **asset_id**: a5e8dcc7-eae0-4e64-84bd-e6bac4bdd868
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i43.png`

- **asset_id**: a53dab47-0e8a-4d8f-9036-08f5bba2df5b
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i44.png`

- **asset_id**: 7c0f5499-d236-4f81-8129-286556f851a4
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i45.png`

- **asset_id**: 971f417f-a201-417d-a052-59c9e7fdd03b
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i46.png`

- **asset_id**: d825df7a-ca0b-4743-9607-97fcce71c414
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i47.png`

- **asset_id**: 8e5300c7-0da8-4540-b591-6fbe56e7fff5
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i48.png`

- **asset_id**: b7d0a938-50ea-4b0e-a820-ec0ce37b9e41
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i49.png`

- **asset_id**: 4467ce96-b739-493d-a936-bd5ead4b8e63
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i50.png`

- **asset_id**: e3fa8ca5-ee46-4eb3-a67f-e48c48184ec6
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i51.png`

- **asset_id**: 6113b005-0bc8-4f51-8da0-af39c134d17b
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i52.png`

- **asset_id**: 03f393e9-8592-4399-866c-d555715b7868
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i53.png`

- **asset_id**: 1b685037-7b5f-4a07-8c79-8274bb74cc2f
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i54.png`

- **asset_id**: a9e552bd-93a6-4d72-8f6e-b88fbf7dce5a
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i55.png`

- **asset_id**: 77a51c1b-2813-48ec-ab4d-2970a0227f75
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i56.png`

- **asset_id**: 137dc15d-f82c-46cc-b41d-3f3567b70820
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i57.png`

- **asset_id**: dcbffa1e-51c8-4917-91cc-3eb0e09bf642
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i58.png`

- **asset_id**: 1beed0d2-1e43-4bad-828f-16532132af20
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i59.png`

- **asset_id**: d0846752-47fe-4e24-bb50-5613640d537c
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i60.png`

- **asset_id**: 3cf35de5-ab6d-4ded-8b62-21352ca9d3d1
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i61.png`

- **asset_id**: 2b1becfc-396a-4fa7-9022-d6999048e867
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i62.png`

- **asset_id**: 471d78b2-a9ef-4326-8108-eca80d5a69b7
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i63.png`

- **asset_id**: 1a4dcb23-baf9-4bb3-9a82-bdaa31fc4582
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i64.png`

- **asset_id**: 9d72506b-a496-43f8-84c2-b3b22c508932
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i65.png`

- **asset_id**: 36e7feaa-a95b-4e32-8267-81b91557311e
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i66.png`

- **asset_id**: cd60c5c4-a0a1-43c7-baa0-a4488361af54
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i67.png`

- **asset_id**: f3072e61-8baa-4c27-9181-98028a5f0527
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i68.png`

- **asset_id**: 2eb06c4d-0ff9-41ca-ad02-67183440eec5
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i69.png`

- **asset_id**: 582e5486-844e-43e6-aba8-26a0ee3df433
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i70.png`

- **asset_id**: 24dee04d-f432-4fb6-9a11-ec5f5ab049cb
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i71.png`

- **asset_id**: 7dc26ccf-16c7-4cf4-a7f8-f92a6284f8c0
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i72.png`

- **asset_id**: b1580fc8-4497-4d10-a6c3-6df30ae5a122
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i73.png`

- **asset_id**: 6b1f8afc-b640-400c-90ad-c1663b8fd09d
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i74.png`

- **asset_id**: 4f505166-b342-46b4-a333-fa95f6525aae
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i75.png`

- **asset_id**: bb838fbb-e3a9-409f-8475-f3c3c7ed4c91
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i76.png`

- **asset_id**: 2f9737e3-c518-4797-ba54-274b01bdcd01
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i77.png`

- **asset_id**: bee4d472-a1ad-4b70-93fc-f4783a3f88a2
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i78.png`

- **asset_id**: 2a90dd41-6e0c-4729-8d74-bcc2124e481d
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i79.png`

- **asset_id**: 10e2a7f7-a988-43bb-b3fd-927fa20165b1
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i80.png`

- **asset_id**: b0ca84d4-67ba-4ad9-a38b-45f86add3bd8
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i81.png`

- **asset_id**: 26a26da9-333a-46cd-b82f-5d6087f7c931
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i82.png`

- **asset_id**: 96b616bb-7f2f-4c65-87ac-f2ac42184b1b
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i83.png`

- **asset_id**: a76f9f4e-b0d4-4d86-b2f6-a8a6080ef83e
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i84.png`

- **asset_id**: c30bb53e-5489-4960-93bb-a7a020542047
  source: slides-14-testing
  page: 12
  type: embedded_image
  path: `c4f92be1_p12_i85.png`

- **asset_id**: e425cea0-18af-4eed-ac5c-9a278f39ff06
  source: slides-14-testing
  page: 12
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 5909b26b-e428-4e8c-8810-b8837b6c10a6
  source: slides-14-testing
  page: 13
  type: embedded_image
  path: `c4f92be1_p13_i0.png`

- **asset_id**: 7de0c412-f66a-4ea1-81b6-5851479b7088
  source: slides-14-testing
  page: 13
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 30d3f9e6-ee58-4cf1-bc54-6d97aeb1cf87
  source: slides-14-testing
  page: 14
  type: embedded_image
  path: `c4f92be1_p14_i0.png`

- **asset_id**: c67f37fd-0b6d-4b15-85bf-0c7eb87c599d
  source: slides-14-testing
  page: 14
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: ffd5a778-4062-4057-990a-61700034306e
  source: slides-14-testing
  page: 15
  type: embedded_image
  path: `c4f92be1_p15_i0.png`

- **asset_id**: 3904e4cf-5b6f-44f8-b3a1-a5eceaa652ff
  source: slides-14-testing
  page: 15
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: c28d4319-68cb-42e4-8953-24fb96625712
  source: slides-14-testing
  page: 16
  type: embedded_image
  path: `c4f92be1_p16_i0.png`

- **asset_id**: dacba66b-9eac-41d8-8e61-26b317c33486
  source: slides-14-testing
  page: 16
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 9128b141-aea7-4e8d-b8bc-e35e75e7f323
  source: slides-14-testing
  page: 17
  type: embedded_image
  path: `c4f92be1_p17_i0.png`

- **asset_id**: 4b0b6d62-4540-4a63-829e-41a0d298236c
  source: slides-14-testing
  page: 17
  type: embedded_image
  path: `c4f92be1_p17_i1.png`

- **asset_id**: c91dabae-21ba-4132-9b54-59536bc1363f
  source: slides-14-testing
  page: 17
  type: embedded_image
  path: `c4f92be1_p17_i2.png`

- **asset_id**: e7bc81e3-9d4b-46db-adda-9d87c8051e3c
  source: slides-14-testing
  page: 17
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 5ec91102-53e8-4fab-bd16-30b89b1b5762
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i0.png`

- **asset_id**: 6cbbe7cd-f832-4192-a752-1b29e7c26d69
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i1.png`

- **asset_id**: 3d8de624-2e54-4331-a255-038142f53742
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i2.png`

- **asset_id**: 8297c5e3-4af6-4c03-97fa-62dec9991bf2
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i3.png`

- **asset_id**: 4425d01c-338d-4b39-b58f-96ba0470b093
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i4.png`

- **asset_id**: 1e2a2acb-413b-4c32-9d1b-e3c3fe19abd2
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i5.png`

- **asset_id**: f6e0c224-840f-471a-a46b-75b92ce6da32
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i6.png`

- **asset_id**: 381736d5-70df-4adc-8f18-6ca4d59e8c17
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i7.png`

- **asset_id**: 75e8ca2a-ae72-4cc8-858a-b6597df39953
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i8.png`

- **asset_id**: 246287b5-04ad-4549-a0d2-0c34f8454e10
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i9.png`

- **asset_id**: a123292f-63d9-4e23-b072-300005f9e16a
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i10.png`

- **asset_id**: e3c8704b-c2e8-49c9-b3dc-77c2220780f1
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i11.png`

- **asset_id**: 4290a365-222e-42c7-8468-1e07681f64b0
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i12.png`

- **asset_id**: 0937f6dd-d1f2-4223-8a2c-69d3cd8f0439
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i13.png`

- **asset_id**: 10854a3d-c28f-41b6-a08d-32f54646c516
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i14.png`

- **asset_id**: 35c47494-2633-46e1-b08d-abfc3ab4d682
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i15.png`

- **asset_id**: fc10964f-082c-4c0b-a9af-86419c45b5f6
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i16.png`

- **asset_id**: 65ee76a5-ceca-44e5-bf7f-1daa19048cc4
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i17.png`

- **asset_id**: bdf629d4-1ab2-4b69-a746-83b320040434
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i18.png`

- **asset_id**: a260ae98-fd0c-465e-b725-69ef3a380193
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i19.png`

- **asset_id**: f5649365-ac73-46d7-8b7c-aee751bdc038
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i20.png`

- **asset_id**: 2971affb-173e-41bd-bc5f-0469fee5eb1e
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i21.png`

- **asset_id**: 29b65697-83c5-4f23-b304-1340c044a64c
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i22.png`

- **asset_id**: 0357358b-79de-42cd-bc9a-9fcc6132bace
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i23.png`

- **asset_id**: 262b39f2-eee8-46b5-9e04-85efd463de5d
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i24.png`

- **asset_id**: b4281737-890e-4281-b59b-60efee781b5c
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i25.png`

- **asset_id**: 207c9839-fc57-4df6-93be-83589165b32e
  source: slides-14-testing
  page: 18
  type: embedded_image
  path: `c4f92be1_p18_i26.png`

- **asset_id**: 0f0b9872-592d-4958-b7f9-13ae4ca8b69c
  source: slides-14-testing
  page: 18
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 8fb8c88d-82c2-4cd7-bbd3-7da846b9faf7
  source: slides-14-testing
  page: 19
  type: embedded_image
  path: `c4f92be1_p19_i0.png`

- **asset_id**: baa2616f-8920-4d15-9797-d216fdca9042
  source: slides-14-testing
  page: 19
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 8c552f82-bef4-4a65-96d0-906ce26bfcaf
  source: slides-14-testing
  page: 20
  type: embedded_image
  path: `c4f92be1_p20_i0.png`

- **asset_id**: 87d20d5a-527f-48c9-bf73-ccc48621472c
  source: slides-14-testing
  page: 20
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 577c8285-3c8d-4ec6-998a-b8c62eff5835
  source: slides-14-testing
  page: 21
  type: embedded_image
  path: `c4f92be1_p21_i0.png`

- **asset_id**: b87da351-612d-4bb1-94e2-06faaa2d464d
  source: slides-14-testing
  page: 21
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: be2c08fc-9233-4409-9c46-21585aab29a2
  source: slides-14-testing
  page: 22
  type: embedded_image
  path: `c4f92be1_p22_i0.png`

- **asset_id**: 73cf66a8-d672-4b14-b9fa-59804c1e4796
  source: slides-14-testing
  page: 22
  type: embedded_image
  path: `c4f92be1_p22_i1.png`

- **asset_id**: e179c464-0352-44b2-aecd-072c0f4bb791
  source: slides-14-testing
  page: 22
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: aa4cdb4b-40f6-4130-afeb-a87b1dbba291
  source: slides-14-testing
  page: 23
  type: embedded_image
  path: `c4f92be1_p23_i0.png`

- **asset_id**: 4f8a8c7a-080a-42bc-9dd8-5c1bebaf654f
  source: slides-14-testing
  page: 23
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 716b3523-bf21-419a-ab3c-bb53bb06fa2d
  source: slides-14-testing
  page: 24
  type: embedded_image
  path: `c4f92be1_p24_i0.png`

- **asset_id**: 228ef791-8795-4be8-8a7e-105613d4be73
  source: slides-14-testing
  page: 24
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 3ad4c47c-e763-498b-aeae-50522d2c85b8
  source: slides-14-testing
  page: 25
  type: embedded_image
  path: `c4f92be1_p25_i0.png`

- **asset_id**: 1949740a-52f8-412d-95a6-0442b52f36b6
  source: slides-14-testing
  page: 25
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 54741e74-1c0d-491c-90cb-d6586ec0fb26
  source: slides-14-testing
  page: 26
  type: embedded_image
  path: `c4f92be1_p26_i0.png`

- **asset_id**: 55ae2274-afec-4c82-af14-93b41d61394e
  source: slides-14-testing
  page: 26
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 475502ca-3437-4a8c-b719-685b48134fdf
  source: slides-14-testing
  page: 27
  type: embedded_image
  path: `c4f92be1_p27_i0.png`

- **asset_id**: d94be00e-c162-4293-97ee-58195e1608c4
  source: slides-14-testing
  page: 27
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 3e66c37b-d32e-4956-a122-77113f06cf30
  source: slides-14-testing
  page: 28
  type: embedded_image
  path: `c4f92be1_p28_i0.png`

- **asset_id**: 2c2fd710-47ba-4bba-a313-42867eb512b9
  source: slides-14-testing
  page: 28
  type: embedded_image
  path: `c4f92be1_p28_i1.png`

- **asset_id**: a621ea76-19c6-453f-99c0-4e3a33594ede
  source: slides-14-testing
  page: 28
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: da12e6bb-416a-4962-bf14-42d342e52a99
  source: slides-14-testing
  page: 29
  type: embedded_image
  path: `c4f92be1_p29_i0.png`

- **asset_id**: 2c0a1ead-e360-4b86-b0a6-b9782e7f3e98
  source: slides-14-testing
  page: 29
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 413730cf-3c9b-4986-8069-ccffef4cce3c
  source: slides-14-testing
  page: 30
  type: embedded_image
  path: `c4f92be1_p30_i0.png`

- **asset_id**: cce97f56-04e6-467a-96e7-076f43b12826
  source: slides-14-testing
  page: 30
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 88cb2505-f421-4e40-9570-f5364f369f4e
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i0.png`

- **asset_id**: 3be35571-2239-44d7-8d2e-e1b5fef3312b
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i1.png`

- **asset_id**: c1a1e908-5542-4b72-aea2-9dfba24a1b26
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i2.png`

- **asset_id**: 3ca5a21a-3fa7-4856-a49c-dbde3b592688
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i3.png`

- **asset_id**: a23f7b0c-ca1a-4868-b3b4-c581f7a5e908
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i4.png`

- **asset_id**: 114978bc-2edf-479d-81c6-2a00f60cfa6d
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i5.png`

- **asset_id**: 4471ff45-cccb-45b2-af01-c04a6f8cf65f
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i6.png`

- **asset_id**: fa30e304-139f-41c6-aee0-f1a634abf235
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i7.png`

- **asset_id**: 1954dcc9-f7ac-4f90-95ff-075c9d4d8065
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i8.png`

- **asset_id**: 2d4678e3-8c13-4c2a-8064-6631e27d7b5f
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i9.png`

- **asset_id**: 09f88074-031b-41fa-8ed0-95e7ec09cbc5
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i10.png`

- **asset_id**: 97d404eb-de44-4270-a696-3f00826e87d8
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i11.png`

- **asset_id**: acb71586-3365-41a6-9159-96ddbbf0c9e9
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i12.png`

- **asset_id**: bdfc5c5d-898a-44fa-8d26-118daae35a15
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i13.png`

- **asset_id**: efad37d9-8179-4c9b-b310-fb0af1f8702f
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i14.png`

- **asset_id**: 9ee1f39d-c96b-4cba-8e8c-57fe913d703c
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i15.png`

- **asset_id**: 68856f3b-1c0b-45cd-ac2a-cc494bd976c8
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i16.png`

- **asset_id**: f2fdf089-1dd1-4aa1-a6b2-30483c42948b
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i17.png`

- **asset_id**: d20de8ed-f43a-43d0-abef-6a2568a0c4d4
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i18.png`

- **asset_id**: ceb444b4-0567-4afa-b826-cb2f5044290e
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i19.png`

- **asset_id**: 711f2f99-ef8f-443c-94ca-64252735aa33
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i20.png`

- **asset_id**: dd76d8b6-c370-479e-9ca2-37a26aebd2a9
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i21.png`

- **asset_id**: 6bb37834-edde-4f76-b6ac-321101440eef
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i22.png`

- **asset_id**: c4d0981d-d3e5-478c-937a-73c6aa613616
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i23.png`

- **asset_id**: a9c5db67-3974-4f7b-a52e-81eccd3220d2
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i24.png`

- **asset_id**: 7c9cd85f-1e65-42a0-8086-0f7ba45b2b33
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i25.png`

- **asset_id**: 8bc9298f-4ca6-4d51-a493-dba2bffec434
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i26.png`

- **asset_id**: e43e379d-fecc-4ddd-aed7-2e918626dc24
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i27.png`

- **asset_id**: 285fc0a5-6880-421d-a905-14af67a3d7e1
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i28.png`

- **asset_id**: 147a242f-0f16-4c60-a4b2-efcc256ccb1b
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i29.png`

- **asset_id**: 53b968d7-406b-4da2-9ed2-bde235f3f8cc
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i30.png`

- **asset_id**: 4c1f3dda-b751-43da-a40d-ffe0f1386f5b
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i31.png`

- **asset_id**: ba8dfd01-3df2-46d3-94f6-184a5434ec7e
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i32.png`

- **asset_id**: 9ccca4dd-4fe0-495c-bf77-58cd13535e55
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i33.png`

- **asset_id**: 31f1293d-7e64-40ba-952f-bb27a0497046
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i34.png`

- **asset_id**: d7e34200-e9b5-4b66-954e-3221e44d1950
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i35.png`

- **asset_id**: 05103b89-2c99-48eb-86bc-30d4093f1904
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i36.png`

- **asset_id**: 105eeca5-6b13-408f-bdae-e6494ecc219e
  source: slides-14-testing
  page: 31
  type: embedded_image
  path: `c4f92be1_p31_i37.png`

- **asset_id**: fe5b5c8c-3e1b-4356-972e-7c4844879129
  source: slides-14-testing
  page: 31
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: afb6dad8-224f-4f8a-849e-e740bd68baff
  source: slides-14-testing
  page: 32
  type: embedded_image
  path: `c4f92be1_p32_i0.png`

- **asset_id**: 3c386a2c-c67f-4e63-b932-1f5fb832f105
  source: slides-14-testing
  page: 32
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 4c67b01b-14ca-43aa-bf82-9c6462978134
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i0.png`

- **asset_id**: a9c9ad95-146b-4cef-ab1b-9b218ba3b258
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i1.png`

- **asset_id**: 51d39812-149e-4f6b-b847-a098793165f7
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i2.png`

- **asset_id**: d5df8a55-cf39-4d8e-a720-ad00597bf297
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i3.png`

- **asset_id**: 952628d5-3b9a-435a-8dbc-0dfca27b99e7
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i4.png`

- **asset_id**: 62ddd724-c79b-42f9-bdd4-6bc742459b93
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i5.png`

- **asset_id**: a42d22c2-ec0b-4605-b128-f562956c44ea
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i6.png`

- **asset_id**: 17e3b1ec-f2be-4a0c-9e0b-a0a689ca0fff
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i7.png`

- **asset_id**: 24bddff1-1a2e-479b-83e7-4a6eedd3621d
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i8.png`

- **asset_id**: bfb680d0-5a77-4db8-8e6b-7dab5ccb5c63
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i9.png`

- **asset_id**: 3a976659-17d2-4c85-aa7a-37a2aba94c25
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i10.png`

- **asset_id**: 479c0197-7100-4a0c-bcba-01ea81341457
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i11.png`

- **asset_id**: 8abcff0b-2ec4-4b75-aaac-9350eabfccad
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i12.png`

- **asset_id**: 76228fcc-66b3-4d6b-9d28-930805bf26a0
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i13.png`

- **asset_id**: c3bf2a7f-4f72-4fec-b07f-b85483cad47e
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i14.png`

- **asset_id**: 36c30d99-e941-4920-91e7-67b1d10ed701
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i15.png`

- **asset_id**: 2f96df4c-31e7-49e3-9601-90a1ea42434d
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i16.png`

- **asset_id**: 1e2112ab-df83-4309-95d7-db63757bdd64
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i17.png`

- **asset_id**: ef2bd7b3-0d46-4e94-8d9d-cca40dbd71a5
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i18.png`

- **asset_id**: b13a4c5c-9bfd-425d-a86a-108650849327
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i19.png`

- **asset_id**: d5f395ae-fed9-492b-ad98-5e2adda0cdba
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i20.png`

- **asset_id**: 19682d57-b9f7-4fac-9a86-27bf1ff2e8f2
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i21.png`

- **asset_id**: d0e5ba8d-95b5-445a-80f0-b9a75c93e0b3
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i22.png`

- **asset_id**: a251b3ce-5147-4509-93d6-dbd0ce22bd61
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i23.png`

- **asset_id**: 97f13c08-ae2f-4805-b50e-3141b692a8f5
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i24.png`

- **asset_id**: 977d629c-f99d-4d2b-ae4a-7cd5c7fa016b
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i25.png`

- **asset_id**: fbc11859-9dde-450c-a52d-8c42e1cdafec
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i26.png`

- **asset_id**: e4fedc49-797a-4cea-83da-fbbd3cce7c4d
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i27.png`

- **asset_id**: 2d7032e6-e4be-4f78-8eec-041a346e9767
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i28.png`

- **asset_id**: 15b862c3-eb31-4cac-9135-5a9066be1cea
  source: slides-14-testing
  page: 33
  type: embedded_image
  path: `c4f92be1_p33_i29.png`

- **asset_id**: 10c7602c-b693-4852-b7b5-bf802f37c21e
  source: slides-14-testing
  page: 33
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 744cb04b-1093-4cb1-8559-17b3b6367285
  source: slides-14-testing
  page: 34
  type: embedded_image
  path: `c4f92be1_p34_i0.png`

- **asset_id**: bf39c149-9efc-4e8d-ab45-330279d4b61c
  source: slides-14-testing
  page: 34
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: f78b0fb2-0e9e-4c98-95be-0deb7cef64c3
  source: slides-14-testing
  page: 35
  type: embedded_image
  path: `c4f92be1_p35_i0.png`

- **asset_id**: 45ecb036-6015-422a-af7d-305554e34f95
  source: slides-14-testing
  page: 35
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 77355bed-9cf5-497f-8018-dda428f7e40f
  source: slides-14-testing
  page: 36
  type: embedded_image
  path: `c4f92be1_p36_i0.png`

- **asset_id**: 55faa076-3634-40b1-a9bc-053daf0bacdc
  source: slides-14-testing
  page: 36
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 6b0680e7-1acc-4622-b043-7fc0e9d02845
  source: slides-14-testing
  page: 37
  type: embedded_image
  path: `c4f92be1_p37_i0.png`

- **asset_id**: caada6e3-f609-4f1a-943e-cfa41da7f5a6
  source: slides-14-testing
  page: 37
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 36ecf953-b3d0-417a-8947-c06ae775dab1
  source: slides-14-testing
  page: 38
  type: embedded_image
  path: `c4f92be1_p38_i0.png`

- **asset_id**: f021f384-64b8-436e-9a48-2db54cad4314
  source: slides-14-testing
  page: 38
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 7fc46dec-8ae8-4849-92d4-b889b2599a2a
  source: slides-14-testing
  page: 39
  type: embedded_image
  path: `c4f92be1_p39_i0.png`

- **asset_id**: 709ed0ee-fb03-4701-9cdb-5dcb2e6915fa
  source: slides-14-testing
  page: 39
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 4be8b9ad-034b-480d-b18e-34abae618f9a
  source: slides-14-testing
  page: 40
  type: embedded_image
  path: `c4f92be1_p40_i0.png`

- **asset_id**: a2d62575-dd17-4a87-b9d4-e5db3e79cb1d
  source: slides-14-testing
  page: 40
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 9010bb6f-a255-46ad-a89c-8e925e662ca7
  source: slides-14-testing
  page: 41
  type: embedded_image
  path: `c4f92be1_p41_i0.png`

- **asset_id**: 1998f10c-f1a1-4d9e-9e21-64d01c2c16d3
  source: slides-14-testing
  page: 41
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: f6704667-a80d-4234-bbaf-51e554b1fcf4
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i0.png`

- **asset_id**: a870be23-eec0-42ab-913a-641551cce2ab
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i1.png`

- **asset_id**: fca903ff-9ca4-4c9b-946f-111c2d42760d
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i2.png`

- **asset_id**: 34331355-a16a-465b-b6be-71a293d213cc
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i3.png`

- **asset_id**: f830a58b-a2fc-4908-ad4b-4a0b6328b4c0
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i4.png`

- **asset_id**: a8b5f6de-ff52-49ec-b9bd-cfa4b24475c8
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i5.png`

- **asset_id**: 2a89d249-2d1d-462c-8fdf-3498ad64e0f6
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i6.png`

- **asset_id**: e9fd8133-aee7-4a13-a875-6246edf2ff2d
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i7.png`

- **asset_id**: 1a0a0f3c-053f-4776-affb-a7c82be3ef25
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i8.png`

- **asset_id**: b3d57797-d432-4444-8aea-6588c171236d
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i9.png`

- **asset_id**: 78c156c3-6bf0-46a4-b1f4-448f3524ab13
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i10.png`

- **asset_id**: 490534ad-b835-4800-a04f-31ebb131b88a
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i11.png`

- **asset_id**: 182afcf9-7f2b-48b9-81cd-ce774a7c8c35
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i12.png`

- **asset_id**: f9cf3c7a-1e07-4e66-b6da-56e20b984a7f
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i13.png`

- **asset_id**: 5b50452f-e854-4ac6-8941-c63e4a572aec
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i14.png`

- **asset_id**: a1b8639b-63d2-49b1-bfc8-585c589092dd
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i15.png`

- **asset_id**: 2cae6d12-abee-479f-8329-76aae20e9995
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i16.png`

- **asset_id**: c2d4b253-6d86-405e-a63c-a20b968166cc
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i17.png`

- **asset_id**: 80ec4e00-a418-4f2a-8821-26a4563cee1b
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i18.png`

- **asset_id**: dba36b7c-430c-4a15-afb4-246c5b7c19e9
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i19.png`

- **asset_id**: 86577e4b-0c0d-40a9-bef1-59ab277dcd05
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i20.png`

- **asset_id**: 0208df2a-7821-42cc-a0c4-61e806d20591
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i21.png`

- **asset_id**: 89884560-c39e-4140-a4b4-46ac5e364e58
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i22.png`

- **asset_id**: 1fbfe379-eeee-44d2-a0d3-a70dabb5ed62
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i23.png`

- **asset_id**: a65f72c9-d788-4f89-b23c-58d57dad7216
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i24.png`

- **asset_id**: a103ce66-d431-4839-83f5-889930806d9e
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i25.png`

- **asset_id**: a6fd678d-f26c-4aa0-8d97-60c290e58bae
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i26.png`

- **asset_id**: d9d5341a-9ea2-484e-8ec3-3ca8b1fe13ec
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i27.png`

- **asset_id**: 60e6933f-2714-4000-97cc-2aa54ee84dce
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i28.png`

- **asset_id**: f609d125-ac64-4627-88bc-ad1f787cfe45
  source: slides-14-testing
  page: 42
  type: embedded_image
  path: `c4f92be1_p42_i29.png`

- **asset_id**: b577d113-fc82-4218-8b1e-2b955a28b1ce
  source: slides-14-testing
  page: 42
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 52cdd515-dd0c-4b6d-9d54-471b14bafe55
  source: slides-14-testing
  page: 43
  type: embedded_image
  path: `c4f92be1_p43_i0.png`

- **asset_id**: b1e42a68-5f29-4e29-9c9b-394eb4c25a0b
  source: slides-14-testing
  page: 43
  type: embedded_image
  path: `c4f92be1_p43_i1.png`

- **asset_id**: a37e40de-85c9-4cee-96fb-ee88e61f5826
  source: slides-14-testing
  page: 43
  type: embedded_image
  path: `c4f92be1_p43_i2.png`

- **asset_id**: f48abc26-fb46-4f12-81a4-b6b2aa0d8c56
  source: slides-14-testing
  page: 43
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 11dc5185-bbe3-4e9d-937b-b392e4cf7d26
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i0.png`

- **asset_id**: ad01aa4d-2c79-4d8a-b4d7-ae0147dc20b7
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i1.png`

- **asset_id**: 799049b7-c739-44da-b843-19a5a3aa4d41
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i2.png`

- **asset_id**: c222d3f1-ee6d-4d0e-9936-e0f583093af9
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i3.png`

- **asset_id**: cb2bf9ae-5846-40a4-a21c-2b8fac047565
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i4.png`

- **asset_id**: 7b7fb62e-4a02-4553-a27d-267a14d590ec
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i5.png`

- **asset_id**: 9e0abf3c-4021-4892-bded-40eea52252a2
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i6.png`

- **asset_id**: bf86c36f-276f-44fa-9a17-7ad88fd5cb1e
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i7.png`

- **asset_id**: d8041325-04af-4bea-8c67-4c8921bf61d4
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i8.png`

- **asset_id**: 8e2c315f-6c4a-47f4-ab6f-d82961d8ff8a
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i9.png`

- **asset_id**: 9c04748a-3219-46ec-8e7c-769bd52daf10
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i10.png`

- **asset_id**: 243d0656-257e-4d60-a1a2-88b118d9565d
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i11.png`

- **asset_id**: 48a9962b-e8d2-48f5-bd21-e5998d301e5b
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i12.png`

- **asset_id**: 0c800820-ade1-4058-9e53-bd6542e94df6
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i13.png`

- **asset_id**: c675a538-d576-48d6-87b3-92bc11ffe1a3
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i14.png`

- **asset_id**: fe219faf-c61c-4ce7-9ba0-a4ac104737e4
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i15.png`

- **asset_id**: 4f458a4d-526b-460f-917f-5d1a5f79ae3a
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i16.png`

- **asset_id**: dd17c5eb-d99a-44f3-abe1-9680ddc66480
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i17.png`

- **asset_id**: 74532759-f6fe-43d0-9302-76da0dd02d36
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i18.png`

- **asset_id**: c7471c2a-9e68-4a8c-9e0f-4a88a500aae2
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i19.png`

- **asset_id**: d9c3f07d-0a27-42e2-b861-3a4831d2f074
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i20.png`

- **asset_id**: aec2957d-28f2-443f-8944-fdabd193dac1
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i21.png`

- **asset_id**: 47194d77-6bbc-43f4-9450-9b07f0b4a676
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i22.png`

- **asset_id**: c1be6624-c603-4acf-8984-ed524e0d37e9
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i23.png`

- **asset_id**: b718376b-c6e7-4615-b6bf-d153ef07a56a
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i24.png`

- **asset_id**: 4f802459-415b-4be4-a479-341171f4523e
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i25.png`

- **asset_id**: 32b86403-1bcc-474b-bbb6-b0b7511925d8
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i26.png`

- **asset_id**: 8379453b-a9d5-4ec4-913a-1a8553ff551b
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i27.png`

- **asset_id**: c3bb121e-7006-4708-94e4-48049b0a840d
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i28.png`

- **asset_id**: ada30634-6995-4ede-8a2b-fced28c09994
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i29.png`

- **asset_id**: bf6316a6-274e-4415-8e97-55cc063c0967
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i30.png`

- **asset_id**: 3de8bf15-6211-4da6-aedf-ea0076523551
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i31.png`

- **asset_id**: 38d5f039-5656-40f8-ba32-9b27bc89b513
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i32.png`

- **asset_id**: e0e44625-0c2e-4d0b-95ea-94834b729ee6
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i33.png`

- **asset_id**: 6c5c738d-6020-4f6a-8d9c-6c20f4615a35
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i34.png`

- **asset_id**: 2641238f-c404-424b-92d5-26415ef622a2
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i35.png`

- **asset_id**: 6ad25020-4cbd-4ec8-aa0e-e163689589ba
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i36.png`

- **asset_id**: 6e3dfdce-6623-48b1-af6e-15163c47b9ec
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i37.png`

- **asset_id**: b8782627-0d0f-4d11-b84f-7a67b0507b12
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i38.png`

- **asset_id**: 09b02c9c-4be9-42ff-8266-e9420243a79f
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i39.png`

- **asset_id**: 5c4b52be-9db4-4734-a96f-b63531953c9b
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i40.png`

- **asset_id**: fd7c9eb3-abe6-4fd3-b38a-9fcdbe50ae0c
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i41.png`

- **asset_id**: f2fa83f1-f217-405f-baf5-b184292ed294
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i42.png`

- **asset_id**: 711b523f-bd34-4b3f-8496-abaccc075ba1
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i43.png`

- **asset_id**: 796cf3bc-c35d-4bad-89dd-e7ea56454d13
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i44.png`

- **asset_id**: cd2353d0-a824-4dbf-9591-8561d350acc7
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i45.png`

- **asset_id**: 89babe37-0a6c-4e10-930d-578302f23697
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i46.png`

- **asset_id**: 08184c9e-e192-40c5-aa04-6fba269b1b6b
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i47.png`

- **asset_id**: 924690af-2bef-4693-91e5-9b8f50bdfb71
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i48.png`

- **asset_id**: 9a48c95d-5596-4a53-ba15-481565f878a9
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i49.png`

- **asset_id**: b451c8c8-9ce9-4547-a475-2ca31a203c5f
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i50.png`

- **asset_id**: 134adcb6-2a03-4915-bec7-778f28c24f39
  source: slides-14-testing
  page: 44
  type: embedded_image
  path: `c4f92be1_p44_i51.png`

- **asset_id**: d102b81f-6b24-48ca-ab7f-1a6ae7c4a035
  source: slides-14-testing
  page: 44
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 37dd17c9-86e6-4755-b51c-f70e34c1ec02
  source: slides-14-testing
  page: 45
  type: embedded_image
  path: `c4f92be1_p45_i0.png`

- **asset_id**: de6930cb-67dd-4e8b-a58a-600ea999ccb9
  source: slides-14-testing
  page: 45
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 14c69819-535f-494b-a710-48beea180480
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i0.png`

- **asset_id**: b45e4120-b257-48e4-8bf1-851d43af7d45
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i1.png`

- **asset_id**: 2ab10b0a-1879-4e49-8126-05b21aead9f6
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i2.png`

- **asset_id**: 5422e5dc-b245-4ba5-9b76-f4b0f04490db
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i3.png`

- **asset_id**: f04d8fe9-6af2-471c-bf6a-6da6d52cf527
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i4.png`

- **asset_id**: d05bd167-edb0-4cb5-afd0-fd1dd353bfb2
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i5.png`

- **asset_id**: 8e3fe05f-0a46-4d92-a919-1941c83aa823
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i6.png`

- **asset_id**: d9df3ad2-5bdd-4fcc-b6f4-743c77f7f39b
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i7.png`

- **asset_id**: 034fc293-b5eb-4c4d-a37c-65649c87e5a7
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i8.png`

- **asset_id**: 2f41b298-7974-4ca7-8816-3a85429506be
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i9.png`

- **asset_id**: 8556ab0c-558c-490b-b341-6502303c770e
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i10.png`

- **asset_id**: 2e4ca9b7-0368-4316-9051-8ce8fe0eace7
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i11.png`

- **asset_id**: 891b8355-f8c6-4139-a12c-2ed9eab23c6f
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i12.png`

- **asset_id**: 0ab87324-11a3-46d4-86d8-ef71d63de84f
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i13.png`

- **asset_id**: b50d4466-23fb-4183-b185-5468f25d87a5
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i14.png`

- **asset_id**: c7e594a7-0945-4e44-bb43-157ddb17175d
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i15.png`

- **asset_id**: 7b794f6a-6ef4-49fa-a45c-174d0d305013
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i16.png`

- **asset_id**: 7b53fa14-6dfb-427f-812f-b7e814baf476
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i17.png`

- **asset_id**: cc13a180-52a6-43a6-a246-e6a1fed3840d
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i18.png`

- **asset_id**: 78295694-593c-4458-afab-b14651ccd772
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i19.png`

- **asset_id**: eb852e6c-f96b-457d-b72c-4faed6241628
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i20.png`

- **asset_id**: 0d6e2609-7c65-480e-bef7-bd1a414358d6
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i21.png`

- **asset_id**: 094673d7-86a5-4b8c-85ad-557926755a22
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i22.png`

- **asset_id**: 1e84c9c4-231a-47f9-be8a-503fb6d513ae
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i23.png`

- **asset_id**: 10836b3d-a4b9-43ea-9403-3d9b5b8219cd
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i24.png`

- **asset_id**: 785c54e7-4128-467e-aa7d-5941cb655033
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i25.png`

- **asset_id**: bdaacd01-bbac-4e4b-98ad-c73be36d2161
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i26.png`

- **asset_id**: bef64da1-0b1c-4890-bb3c-8a9802c44b12
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i27.png`

- **asset_id**: 3badbfd9-2ecf-4be2-843a-b10fa08f42b8
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i28.png`

- **asset_id**: 51c12384-d2cf-437f-9a3b-ce8ab848c4f0
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i29.png`

- **asset_id**: 0eeb8a84-47a6-4cc6-aebb-8d467412166d
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i30.png`

- **asset_id**: 9ee58294-9db4-46aa-9a63-132d6a49d272
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i31.png`

- **asset_id**: c129f4cb-accb-450c-8d5e-b2d5177bda0b
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i32.png`

- **asset_id**: b11c111a-ac05-4607-8bfb-196a46e5a76a
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i33.png`

- **asset_id**: a4407846-e026-447f-a1f1-1e17f78a6a79
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i34.png`

- **asset_id**: 9c02bbbb-e52a-4bfe-8d0b-dce6c2a841b1
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i35.png`

- **asset_id**: 77b0d731-fbc6-4db9-85a6-d9b1dde7e56b
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i36.png`

- **asset_id**: 5071fded-ff76-450a-8a82-9d33a49feaf2
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i37.png`

- **asset_id**: e3e4fb86-1aca-4c9c-8ebe-8ed6d5058b53
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i38.png`

- **asset_id**: 79ff07f2-1fd6-441f-96c5-dd64681f8527
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i39.png`

- **asset_id**: d6f0af87-3794-4d2c-8993-1f50aa9a008d
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i40.png`

- **asset_id**: 2e15eb82-9f6c-475b-8a11-14f54cb8845f
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i41.png`

- **asset_id**: 6a2fd6cc-a36b-4c7e-904f-1407fe1af260
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i42.png`

- **asset_id**: 7b929132-6553-4dd9-84a2-872c4173b45e
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i43.png`

- **asset_id**: 50811270-97d3-41c6-a039-f1ba14e4c3d4
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i44.png`

- **asset_id**: c0d3dd96-47d9-4411-be05-b84adcf26ba8
  source: slides-14-testing
  page: 46
  type: embedded_image
  path: `c4f92be1_p46_i45.png`

- **asset_id**: f64e1b95-8226-4ec7-a132-188e66f9b4a2
  source: slides-14-testing
  page: 46
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 1e0e0e40-1c03-4fa9-aaf6-e3bfdb3cdab8
  source: slides-14-testing
  page: 47
  type: embedded_image
  path: `c4f92be1_p47_i0.png`

- **asset_id**: 3bdaa19b-6906-4ebe-8212-c51df3610bdb
  source: slides-14-testing
  page: 47
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 5e47b924-a8c7-415a-8d66-6b5725e96241
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i0.png`

- **asset_id**: 28d7b02d-44fe-4e97-ad79-3c30de359d59
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i1.png`

- **asset_id**: 58398f31-240e-4abd-9fcd-f098c25411b8
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i2.png`

- **asset_id**: b4a8bd2d-47ce-4412-86ce-b43bdf90d22e
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i3.png`

- **asset_id**: 06b98fc5-4f69-4c30-817e-8b7574521acf
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i4.png`

- **asset_id**: 0e56930b-85f3-4a14-8c61-48031f947170
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i5.png`

- **asset_id**: 67644df8-937c-4c2b-83fc-ed7be2195bb3
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i6.png`

- **asset_id**: 1c0577e3-6c9b-479a-969b-a50cd03ed78c
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i7.png`

- **asset_id**: d0319c39-2a4f-47f9-9d26-d8395fcfb620
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i8.png`

- **asset_id**: ad10479a-cdc3-4901-a429-86a508578d6f
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i9.png`

- **asset_id**: 2c623ff8-87ee-4d1a-85a8-55f69e3003c6
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i10.png`

- **asset_id**: 301edd82-ba3d-4722-8c18-8995679e1f74
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i11.png`

- **asset_id**: 827bbef2-1723-4e9b-a54b-cd7a83dc9bd2
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i12.png`

- **asset_id**: dd0ef2f4-9e07-4a69-b031-f9e275e600ed
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i13.png`

- **asset_id**: 723a6e64-a6b8-41d4-b6a1-df9f14118d99
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i14.png`

- **asset_id**: a9ca3c58-8ae1-4d06-b10e-297f8636a190
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i15.png`

- **asset_id**: ac92f93d-500b-435a-b66a-19011b79c892
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i16.png`

- **asset_id**: 57aca45f-af70-4406-b646-0ba8f4a9333b
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i17.png`

- **asset_id**: 1d0027aa-6b31-467d-8b0e-dcace72ef18d
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i18.png`

- **asset_id**: 6bea43ad-7a26-41ce-b373-985c4ea45b28
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i19.png`

- **asset_id**: 4a374e7c-86d1-418d-adb0-682e16312281
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i20.png`

- **asset_id**: af5d1b4d-2878-4103-b711-b61195f9bbc1
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i21.png`

- **asset_id**: 1584d9b3-9db1-4b3d-ab37-9e6da177036e
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i22.png`

- **asset_id**: e71c9c00-79d8-4378-a886-dd15c68ee383
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i23.png`

- **asset_id**: 01f3bcde-20b8-410e-a5a2-4d505967b034
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i24.png`

- **asset_id**: 29d0ec46-9ce1-4529-8215-03781ec9c8bf
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i25.png`

- **asset_id**: f8d46299-6393-4952-82a7-78102f9c4f91
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i26.png`

- **asset_id**: e1f1f60d-b3e1-4b54-ace8-c025768afc0e
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i27.png`

- **asset_id**: 35aea3e9-68d4-410b-8cb5-72e5f207320a
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i28.png`

- **asset_id**: 38d8ac88-4d0b-48fe-896c-00158a93a716
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i29.png`

- **asset_id**: dd5cb2bd-15e2-49fc-ba12-5a3af9c19085
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i30.png`

- **asset_id**: 37002f18-ab2b-41e8-95ab-7e7e4188cafd
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i31.png`

- **asset_id**: a0c3a4ba-94f3-42e5-97a6-f564f31b7fa2
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i32.png`

- **asset_id**: 0c40eeec-be3e-49df-aa3f-cfdc3a47bcc4
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i33.png`

- **asset_id**: cea0c3ec-1ed6-4799-ab69-338127556133
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i34.png`

- **asset_id**: f2072c8e-c913-4c10-b17f-7b8a90e35711
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i35.png`

- **asset_id**: 8ef33e07-f3d3-4a39-8a33-8b34f68245e7
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i36.png`

- **asset_id**: 55437d5b-dc85-420a-8f3b-675e6ee18905
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i37.png`

- **asset_id**: 9350e027-a8f1-46e0-905f-b9d8e49d8373
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i38.png`

- **asset_id**: 2f74e280-7ad1-4402-8699-128aebf133fb
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i39.png`

- **asset_id**: 06c20552-5762-4d07-b9f5-8e2f9e4d98ec
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i40.png`

- **asset_id**: 7022ba01-c0cc-4bb0-9ada-b532e309756f
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i41.png`

- **asset_id**: 9bc8756d-bcf3-43df-8d4d-78dd57c62ca5
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i42.png`

- **asset_id**: f6d61a59-9c2f-4e51-9e60-e76bd7f4b003
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i43.png`

- **asset_id**: e09b3797-2f04-4e99-96b6-a9d913aec80e
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i44.png`

- **asset_id**: cc17fc8b-05ff-4d12-b0b4-e3c370f0a1f6
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i45.png`

- **asset_id**: d4f3abed-698d-45d4-a889-312ad94dfbac
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i46.png`

- **asset_id**: 7f8c6869-f6a4-42e9-a8a6-011da77cba2a
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i47.png`

- **asset_id**: 16e91d61-e7f3-4eba-ae72-b4e8266b7e1c
  source: slides-14-testing
  page: 48
  type: embedded_image
  path: `c4f92be1_p48_i48.png`

- **asset_id**: 4f7cbff5-4acc-4e23-a259-677dbdfc71b2
  source: slides-14-testing
  page: 48
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 899a6ed9-2a02-403f-8cbc-632eff503ec7
  source: slides-14-testing
  page: 49
  type: embedded_image
  path: `c4f92be1_p49_i0.png`

- **asset_id**: a48c9bfd-ad95-4c97-9056-7de54657bada
  source: slides-14-testing
  page: 49
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: e9ae8817-e12c-4115-94c6-049f384b1e85
  source: slides-14-testing
  page: 50
  type: embedded_image
  path: `c4f92be1_p50_i0.png`

- **asset_id**: 42909485-540c-4533-ac17-5daefec44835
  source: slides-14-testing
  page: 50
  type: embedded_image
  path: `c4f92be1_p50_i1.png`

- **asset_id**: d87c5769-be8a-42d2-b685-ebad3f87291b
  source: slides-14-testing
  page: 50
  type: embedded_image
  path: `c4f92be1_p50_i2.png`

- **asset_id**: f92226d7-84fb-47ff-80a0-0110addb7153
  source: slides-14-testing
  page: 50
  type: embedded_image
  path: `c4f92be1_p50_i3.png`

- **asset_id**: 0da93a25-98d3-40db-8d5e-15bc28a9ef2a
  source: slides-14-testing
  page: 50
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: d5408874-2ed4-43eb-9e3f-b74f5e3d9b71
  source: slides-14-testing
  page: 51
  type: embedded_image
  path: `c4f92be1_p51_i0.png`

- **asset_id**: 38686b31-727d-4516-a894-0e6bb5837c19
  source: slides-14-testing
  page: 51
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: a5ed2435-6908-49d2-9210-46654180060e
  source: slides-14-testing
  page: 52
  type: embedded_image
  path: `c4f92be1_p52_i0.png`

- **asset_id**: 2395a542-ae08-4d3f-a9ff-3002a53e0f18
  source: slides-14-testing
  page: 52
  type: embedded_image
  path: `c4f92be1_p52_i1.png`

- **asset_id**: f1e37af6-89b1-45c5-b1d2-beaf7d7b0f3b
  source: slides-14-testing
  page: 52
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 133aace6-7ba7-4df7-baa1-1761bb19d26a
  source: slides-14-testing
  page: 53
  type: embedded_image
  path: `c4f92be1_p53_i0.png`

- **asset_id**: b1d2144d-a0d8-45eb-bcdc-a3a125b64d4b
  source: slides-14-testing
  page: 53
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 53c95ef9-1427-4de6-b83e-f228a075653c
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i0.png`

- **asset_id**: 8d3ca30a-ede3-4c67-93fa-56111f78b31c
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i1.png`

- **asset_id**: 96ba9f94-f1a6-407a-8663-2f5e985516f9
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i2.png`

- **asset_id**: 64f99c66-84f1-4a09-aa99-1d88750ed5f3
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i3.png`

- **asset_id**: 65a63784-84c3-47ab-a32a-fdba41847f8a
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i4.png`

- **asset_id**: 355f2e4d-5142-4755-b4ab-f7b87062470c
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i5.png`

- **asset_id**: 93bcf65b-30ba-4a62-9d9a-cc5362a16bbd
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i6.png`

- **asset_id**: 20b5566a-4bb9-4aed-b179-373a13d77ede
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i7.png`

- **asset_id**: 120171d8-cb0d-49dc-ba86-bd9ea7856766
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i8.png`

- **asset_id**: c3933892-dff2-428a-bab6-f25bdd99b6ca
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i9.png`

- **asset_id**: 6085bcdb-9dd5-47f3-b615-717a5cc135e0
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i10.png`

- **asset_id**: 618cce44-ad88-44cb-823e-09f2d55ac8a1
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i11.png`

- **asset_id**: bbfbb849-dd5a-414f-8e91-3a3b644e2cd5
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i12.png`

- **asset_id**: 3d9d6691-d688-4edd-86dc-7bc78e04d63a
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i13.png`

- **asset_id**: 5386f62a-610b-40d7-bb52-ee4fae2688e1
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i14.png`

- **asset_id**: 9845cd6a-caf6-4341-ae2b-1050e85e9e74
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i15.png`

- **asset_id**: fbcda85d-a377-4970-a7e9-57bb0d9223bd
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i16.png`

- **asset_id**: d836e31e-0b61-42bb-9f3b-6e6cf6c8d1ac
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i17.png`

- **asset_id**: b90ab0b1-6e33-402c-9f5a-c0381ef3cf2e
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i18.png`

- **asset_id**: b082ce65-5552-4c43-8cc7-f7155915ea64
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i19.png`

- **asset_id**: f3691c26-a5ca-42ce-8cf0-b211ea442646
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i20.png`

- **asset_id**: fc937a93-f739-42cf-9820-78800180a4db
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i21.png`

- **asset_id**: a7374469-93d1-4ccc-8b30-f7355cdffde6
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i22.png`

- **asset_id**: 974ecb20-6192-47ac-ac52-1f9b7feed0d6
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i23.png`

- **asset_id**: f656da06-4ad2-42ec-918e-4b49a671505a
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i24.png`

- **asset_id**: 5e238442-e9aa-435d-87a9-2a41eca47545
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i25.png`

- **asset_id**: 08590a9d-6669-4ab9-9d42-3208d8a598c5
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i26.png`

- **asset_id**: b82c45f0-8e19-4c02-a737-3d95ea38b49a
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i27.png`

- **asset_id**: 36bcfc9e-cc6c-4a9e-87ba-267bbfa80e5c
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i28.png`

- **asset_id**: 2cc75d08-48c7-447c-81c3-a30488e44e7a
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i29.png`

- **asset_id**: 605c393a-8558-4fe9-8373-3570fab53823
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i30.png`

- **asset_id**: 44cbc892-b97c-42e1-b057-36cb48d89c79
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i31.png`

- **asset_id**: cf881372-0301-4496-ab07-84e785865486
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i32.png`

- **asset_id**: 476aef27-d846-485b-bbe1-0da2ad5f3dbd
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i33.png`

- **asset_id**: 8f3f3192-c59e-4f8f-940d-733c7c07c2af
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i34.png`

- **asset_id**: 6bef4cde-67d6-4d0f-9171-9b8f0e612efc
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i35.png`

- **asset_id**: 5980fc7a-2375-4bdb-b95a-255f0da003fa
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i36.png`

- **asset_id**: ffe4654b-278e-47bf-9691-5bd4baae50a8
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i37.png`

- **asset_id**: ee46e77d-2067-4596-8b58-2b3d43240292
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i38.png`

- **asset_id**: 684d2db5-1951-4b3f-a716-6581a07fbf29
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i39.png`

- **asset_id**: 1c4205c1-47db-427e-bc5f-70daf35b90b2
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i40.png`

- **asset_id**: dca0813e-c8cb-491c-8013-76c0bf49cc8c
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i41.png`

- **asset_id**: 7edc0d7c-acc3-4843-959f-f6ce5e1b1b7c
  source: slides-14-testing
  page: 54
  type: embedded_image
  path: `c4f92be1_p54_i42.png`

- **asset_id**: 99748cbc-651a-4471-bd2f-ab2840501070
  source: slides-14-testing
  page: 54
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 8cd53bf1-08e8-4884-a4bf-cd1bf7746c5f
  source: slides-14-testing
  page: 55
  type: embedded_image
  path: `c4f92be1_p55_i0.png`

- **asset_id**: fc18a6b8-376d-4a08-aab1-340789b6699f
  source: slides-14-testing
  page: 55
  type: embedded_image
  path: `c4f92be1_p55_i1.png`

- **asset_id**: 3f85e4e7-6e37-42eb-9bf4-ad619eecae85
  source: slides-14-testing
  page: 55
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 7b59679e-66a0-4603-92fc-af56734bb574
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i0.png`

- **asset_id**: 535103d1-8eab-41d8-ba64-a089efcd83ad
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i1.png`

- **asset_id**: 408f432d-f433-4ee4-8a8c-394c51901b80
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i2.png`

- **asset_id**: a6ab9cf7-0bce-4645-ba40-c83023c6858d
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i3.png`

- **asset_id**: 0d869b4a-d23d-4e99-936e-9607aac763e1
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i4.png`

- **asset_id**: 72d633bf-4737-4f48-94e9-69f6f4e714b5
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i5.png`

- **asset_id**: 8510157b-8360-409f-8317-2ed24671a24b
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i6.png`

- **asset_id**: 4ff24625-04a5-4900-8af4-e2fba70fa593
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i7.png`

- **asset_id**: a6d9e6d5-a6cf-488b-a1ee-31343a66f426
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i8.png`

- **asset_id**: 71811407-611d-497d-afb2-4e7e41be5626
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i9.png`

- **asset_id**: 01ab5fcd-deac-4e2b-a2ed-21f753e0f096
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i10.png`

- **asset_id**: 61113c0e-7386-4bed-b9ee-f4f68eecc39d
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i11.png`

- **asset_id**: f8d79687-6ee4-4b00-81d0-cd3740af39f6
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i12.png`

- **asset_id**: 5d2d19c2-59dc-41d1-a153-1b7f97708d2a
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i13.png`

- **asset_id**: 659d89a6-bf1d-40f1-a9c1-c9c9a70aec38
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i14.png`

- **asset_id**: 64b1b026-00c1-479f-9b96-172e7666ac3f
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i15.png`

- **asset_id**: fa425eaa-bae9-409e-b368-547df65c0d85
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i16.png`

- **asset_id**: 5dcbd1e0-5e4b-4561-8745-bd0056d1c4f9
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i17.png`

- **asset_id**: dbfec011-9460-45c6-8c24-b9eb1b273bcf
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i18.png`

- **asset_id**: 22e26fef-daf0-456c-8db4-9edeadf4c010
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i19.png`

- **asset_id**: 7ff8f7f4-ac02-4d2a-a6e0-5b4db01da2af
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i20.png`

- **asset_id**: f601e565-7f11-4c3b-a434-2c789db24f33
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i21.png`

- **asset_id**: 92f56070-7453-42d0-b2f9-814ac5db5ff8
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i22.png`

- **asset_id**: 35392158-24d4-44c6-9937-886f39435835
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i23.png`

- **asset_id**: f0d28cbf-b10f-4b16-b713-a0259ba4ca48
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i24.png`

- **asset_id**: 9bc51211-158b-4afe-bfb1-6664e077f0dd
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i25.png`

- **asset_id**: 7409235a-1c19-4c82-abea-d31f8864077a
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i26.png`

- **asset_id**: fc666578-3b36-45d5-ace4-3206178622d5
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i27.png`

- **asset_id**: f9ca23b6-0ec6-45f3-8352-0c64281214da
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i28.png`

- **asset_id**: 270051ba-45d3-42a8-af32-65abd9900244
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i29.png`

- **asset_id**: 0bc5094d-2181-4bc3-aaab-845689447629
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i30.png`

- **asset_id**: 8a948790-d6db-459a-856f-d7a94e6fe9f6
  source: slides-14-testing
  page: 56
  type: embedded_image
  path: `c4f92be1_p56_i31.png`

- **asset_id**: 672f5c93-2a5d-4064-8357-23f8ec715a52
  source: slides-14-testing
  page: 56
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 11179f97-e09f-4455-9b9d-e2d8c385e5c8
  source: slides-14-testing
  page: 57
  type: embedded_image
  path: `c4f92be1_p57_i0.png`

- **asset_id**: 8621174b-109f-4f8f-bd61-89a7af9fa3d9
  source: slides-14-testing
  page: 57
  type: embedded_image
  path: `c4f92be1_p57_i1.png`

- **asset_id**: 0f5b8c10-7b35-4f71-8550-87310ebb9e92
  source: slides-14-testing
  page: 57
  type: embedded_image
  path: `c4f92be1_p57_i2.png`

- **asset_id**: f441ef62-4c5f-47f4-a104-3e3458920227
  source: slides-14-testing
  page: 57
  type: embedded_image
  path: `c4f92be1_p57_i3.png`

- **asset_id**: 90acd4d2-fcf9-408a-875c-82d070bbad16
  source: slides-14-testing
  page: 57
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 5a95cdd1-3a0e-4c0d-b008-2dfe0821797b
  source: slides-14-testing
  page: 58
  type: embedded_image
  path: `c4f92be1_p58_i0.png`

- **asset_id**: 3624bad8-8500-4103-8ac5-900141814c75
  source: slides-14-testing
  page: 58
  type: embedded_image
  path: `c4f92be1_p58_i1.png`

- **asset_id**: 818c8771-0fa6-4cf8-87d1-016be21c87e2
  source: slides-14-testing
  page: 58
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: d42b7e55-17a4-4c98-8a4f-f70f0d3388ac
  source: slides-14-testing
  page: 59
  type: embedded_image
  path: `c4f92be1_p59_i0.png`

- **asset_id**: e1cdaeff-6293-42d6-a871-47175cefdbd6
  source: slides-14-testing
  page: 59
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 4ba7b392-963f-4704-bff8-fd84696b8420
  source: slides-14-testing
  page: 60
  type: embedded_image
  path: `c4f92be1_p60_i0.png`

- **asset_id**: 89679664-d4fa-493a-8d38-2e2fbc789b11
  source: slides-14-testing
  page: 60
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 7df501ba-e94a-45ff-80f3-1b2fb6d0aaca
  source: slides-14-testing
  page: 61
  type: embedded_image
  path: `c4f92be1_p61_i0.png`

- **asset_id**: 9c0732e4-2ae3-4a86-b1f4-09e654220f0d
  source: slides-14-testing
  page: 61
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: 6d5f064e-2cd9-4e03-852e-8bb96ae3757e
  source: slides-14-testing
  page: 62
  type: embedded_image
  path: `c4f92be1_p62_i0.png`

- **asset_id**: 4ce9bcce-a9c7-4fa3-9f30-2dadb7202f43
  source: slides-14-testing
  page: 62
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

- **asset_id**: daaeda05-59d9-4c82-9455-981fcbdf8cf1
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i0.png`

- **asset_id**: 2bf2be77-8e18-4d0d-b2b5-4fd01e502346
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i1.png`

- **asset_id**: dcad26e0-b70e-4969-971a-0304e5969cc5
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i2.png`

- **asset_id**: 628f794e-5a92-4af9-aa64-05d91fc9d69d
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i3.png`

- **asset_id**: fd545265-a173-468e-baa2-114ec288a251
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i4.png`

- **asset_id**: d2a83e6d-9067-43e4-80b7-5012f6452112
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i5.png`

- **asset_id**: 7d003f9d-3aab-4016-80e6-d13d697dc3cd
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i6.png`

- **asset_id**: 35f27f9a-3b98-4cc0-8284-9c66ca9a3e35
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i7.png`

- **asset_id**: ca1a7255-6d00-4c4a-919a-e408ddaed1e4
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i8.png`

- **asset_id**: f4855e85-eeb9-40aa-b296-4774d073f7bf
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i9.png`

- **asset_id**: 90069cf0-f3f1-48d4-8065-996cde263fe0
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i10.png`

- **asset_id**: 71467a75-2c56-4658-9821-83e0bb9777b7
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i11.png`

- **asset_id**: 0878711e-1f9d-4de9-977b-a3db05de3c98
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i12.png`

- **asset_id**: ae8bf43d-4dac-4d6d-b8a4-c7466766f3db
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i13.png`

- **asset_id**: 694dba69-bd00-499b-8acb-3aea62997559
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i14.png`

- **asset_id**: 7cb6694b-c07e-4d78-959f-bca2d90057a3
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i15.png`

- **asset_id**: 343a3131-031a-47ce-8bfb-c38faaa1f007
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i16.png`

- **asset_id**: 5f8cf366-8ecb-4a14-aeb8-6c3e6a07c617
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i17.png`

- **asset_id**: d56e7f2d-2735-4db8-a974-9606df07d706
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i18.png`

- **asset_id**: 34933fdf-67f4-4a72-80a9-33952d59aa8f
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i19.png`

- **asset_id**: 713131b3-ee9c-4d17-8c0e-d99228c3c79c
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i20.png`

- **asset_id**: c617955d-e3d6-4859-82ac-275de5c7fe30
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i21.png`

- **asset_id**: e262aed3-d670-4ccc-a41e-96a89d17a995
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i22.png`

- **asset_id**: f694c709-2371-406f-a752-3e88c66a4872
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i23.png`

- **asset_id**: 4e12b308-d125-4330-b221-ff95ea7c5eb7
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i24.png`

- **asset_id**: 89986781-f57c-4714-bd28-0b236b734f85
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i25.png`

- **asset_id**: 40bee148-f4af-444b-b2a2-49bb2b906125
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i26.png`

- **asset_id**: 79c190ba-d341-4418-aae4-041372eaa844
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i27.png`

- **asset_id**: 7ac81735-870d-4fb3-b0c2-88a55c498f84
  source: slides-14-testing
  page: 63
  type: embedded_image
  path: `c4f92be1_p63_i28.png`

- **asset_id**: 625f1256-b07d-4cd0-bc22-21b539e94eb5
  source: slides-14-testing
  page: 63
  type: vector_diagram_region
  path: `VIRTUAL_RENDER_REQUIRED`

