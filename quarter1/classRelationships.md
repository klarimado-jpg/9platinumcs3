# Class Relationships: Association and Multiplicity

## Previous Work

[Part I - Classes and Objects](classObjectUML.md)

[Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class

Class: StudyPlanner

Description: A StudyPlanner represents a personal study plan that helps a student organize a subject, schedule, and completion status for a study task.

## New Related Class
Class: StudySession 

Description: A StudySession represents a study plan that allocates a specific block of time dedicated to studying. It contains attributes like start time, end time, duration, and breaks. It helps students assign different subjects to learn in different time intervals (pomodoro method).

## Association
Relationship: StudyPlanner HAS-A StudySession.

Explanation: A StudyPlanner can contain and manage multiple StudySession objects. Each study session represents a specific time interval that can be used for studying different subjects or tasks.

## Multiplicity
Multiplicity: 1 : 0..*

Explanation: One StudyPlanner can have zero or more StudySession objects. A student can create a study planner before adding any study sessions, and they can add multiple study sessions to organize their study schedule.

## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)

## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
![Relationship Test Run](images/relationshipTestRun.png)

## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)

## Analysis

### What is the association between your two classes?
The association between StudyPlanner and StudySession is a HAS-A relationship. A StudyPlanner has StudySession objects that help organize the student's study schedule. The StudyPlanner can manage several study sessions for different study periods.

### What multiplicity did you choose and why?
I chose a onte-to-many relationship with a multiplicity of 1 : 0..*. One StudyPlanner can have zero or more StudySession objects. This fits the system because a student can have one study planner with several study sessions for different subjects or time intervals.

### How did you implement the relationship in Python?
I implemented the relationship by creating a list called study_sessions inside the StudyPlanner class. This list stores the actual StudySession objects. I also created an add_session() method that adds a StudySession object to the list.

### Why did you store an object reference instead of copying its data?
I stored it so that the StudyPlanner can access the actual StudySession object and its information. For example, the planner can access the start time or duration of a session without copying those values into the StudyPlanner.

### If your relationship uses many, why is a list appropriate?
A list is appropriate because one StudyPlanner can contain multiple StudySession objects. The list stores the actual StudySession objects, which allows the StudyPLanner to keep track of all its study sessions.
