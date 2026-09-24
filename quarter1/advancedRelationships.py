class StudyPlanner:
    def __init__(self, subject, schedule, completion_status):
        self.subject = subject
        self.schedule = schedule
        self.completion_status = completion_status
        self.study_sessions = []

    def add_session(self, session):
        self.study_sessions.append(session)

    def displayPlanner(self):
        print("Subject:", self.subject)
        print("Schedule:", self.schedule)
        print("Completion Status:", self.completion_status)


class StudySession:
    def __init__(self, start_time, end_time, duration, breaks):
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.breaks = breaks

    def displaySession(self):
        print("Start Time:", self.start_time)
        print("End Time:", self.end_time)
        print("Duration:", self.duration, "minutes")
        print("Breaks:", self.breaks)


class PomodoroSession(StudySession):
    def __init__(self, start_time, end_time, duration, breaks, cycles):
        super().__init__(start_time, end_time, duration, breaks)
        self.cycles = cycles

    def displaySession(self):
        super().displaySession()
        print("Pomodoro Cycles:", self.cycles)

# test run ko tohh
planner = StudyPlanner("Chemistry", "7:00 PM - 9:00 PM", "In Progress")

session1 = StudySession("7:00 PM", "7:50 PM", 50, "10 minutes")
session2 = PomodoroSession("8:00 PM", "8:50 PM", 50, "10 minutes", 2)

planner.add_session(session1)
planner.add_session(session2)

print("=== INHERITANCE TEST ===")
print("Child class:", type(session2).__name__)
print("Inherited duration:", session2.duration)
print("Inherited breaks:", session2.breaks)
print("Additional attribute - cycles:", session2.cycles)

print("\n=== AGGREGATION TEST ===")
print("Planner contains", len(planner.study_sessions), "study sessions.")
print("Session 1:", type(session1).__name__)
print("Session 2:", type(session2).__name__)

print("\n=== PLANNER TEST ===")
planner.displayPlanner()

print("\n=== POMODORO SESSION TEST ===")
session2.displaySession()
