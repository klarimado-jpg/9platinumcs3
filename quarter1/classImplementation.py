class StudyPlanner:
    def __init__(self, subject, task, duration):
        self.subject = subject
        self.task = task
        self.__duration = duration
        self.completed = False

    def displayPlan(self):
        print("Subject:", self.subject)
        print("Task:", self.task)
        print("Duration:", self.__duration, "minutes")
        print("Completed:", self.completed)

    def markCompleted(self):
        self.completed = True

    def getDuration(self):
        return self.__duration

study1 = StudyPlanner("Mathematics", "Review Polynomials", 60)
study2 = StudyPlanner("Biology", "Study Cell Structure", 45)

print("--- BEFORE ---")

print("\nObject 1:")
study1.displayPlan()

print("\nObject 2:")
study2.displayPlan()

print("\nMarking Object 1 as completed...")
study1.markCompleted()

print("\n--- AFTER ---")

print("\nObject 1:")
study1.displayPlan()

print("\nObject 2:")
study2.displayPlan()
