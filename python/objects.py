class Timeslot(object):
    def __init__(self, day, slot_type, location, title, code, weeks, time=None):
        self.day = day
        self.time = time
        self.slot_type = slot_type
        self.location = location
        self.title = title
        self.code = code
        self.weeks = weeks
    
    def __str__(self):
        s = "\n-----\n"
        s += ("Day: {}\n".format(self.day))
        s += ("Time: {}\n".format(self.time))
        s += ("Type: {}\n".format(self.slot_type))
        s += ("Location: {}\n".format(self.location))
        s += ("Title: {} {}\n".format(self.code, self.title))
        s += ("Weeks: {}\n-----\n".format(self.weeks))

        return s


class timetableDay(object):
    def __init__(self, day, timeslots=list()):
        self.day = day
        self.timeslots = timeslots[:]

    # def __str__(self):
    #     print(self.day)
    #     for timeslot in self.timeslots:
    #         print(timeslot)

    def __iter__(self):
        for slot in self.timeslots:
            yield slot 

    def __str__(self):
        s = ""
        for slot in self.timeslots:
            if slot:
                s += str(slot)
            else:
                s += "None\n"
            # s += "slot\n"
        return s

    def daylength(self):
        return len(self.timeslots)


    def add_timeslot(self, timeslot):
        self.timeslots.append(timeslot)

    def non_empty(self):
        return len([i for i in self.timeslots if i is not None])


class courseTimetable(object):
    def __init__(self, course_code, year, semester, days=list()):
        self.course_code = course_code
        self.year = year
        self.semester = semester
        self.days = days

    def __iter__(self):
        for day in self.days:
            yield day

    def __str__(self):
        s = ""
        for day in self.days:
            s += str(day)
        return s
    
    def add(self, day):
        self.days.append(day)
    
    def getdays(self):
        return self.days

    def dayslength(self):
        return len(self.days)


