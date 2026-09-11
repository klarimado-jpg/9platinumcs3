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
