 # Class Attributes and Methods

## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)

## Design Revision
- I kept the StudyPlanner class and its original attributes and methods
- I made duration private because the study time should be controlled and should not be changed into an invalid value
- I added getDuration() so the duration can be safely viewed without directly accessing the private attribute

## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| subject | string | public | it can be accessed normally because the subject is basic information about the study plan |
| task | string | public | it can be accessed normally because |
| duration | int | private | |
| completed | boolean | public | |

## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)

## Python Implementation
[View Python Source](classImplementation.py)!

## Test Run
![Test Run](images/classTestRun.png)

## Object Diagram
![Object Diagram](images/objectDiagram.png)

## Analysis

### Why did you make your chosen attribute private?
 I made my chosen attribute private because the study time should be protected from incorrect changes. If another part of the program directly changed, it could accidentally give the study plan an invalid value, such as a negative number. Keeping it private allows the class to control how the study duration is accessed or changed. This makes the StudyPlanner more organized and safer to use. 

### Which method changes the state of your object?
The markCompleted() method changes the completed attribute from False to True. In my test run, Object 1 changed from incomplete to completeed after the method was called. Object 2 was not affected.

### How did your two objects demonstrate that instances are independent?
I created two StudyPlanner objects with different subjects, tasks, and durations. When I called markCompleted on Object 1, only Object 1 changed its completed value to True. Object 2 remained False, showing that each objects keep its own state.

### What is the difference between your class diagram and your object diagram?


