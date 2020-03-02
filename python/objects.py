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

    def slot_to_json(self):
        return {
            "isvalid" : 1,
            "code" : self.code,
            "loc": self.location,
            "title": self.title,
            "weeks": self.weeks
        }



class timetableDay(object):
    def __init__(self, day, timeslots=list()):
        self.day = day
        self.timeslots = timeslots[:]

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
    
    def day_to_json(self):
        d = {
            "day" : self.day,
            "timeslots" : []
        }

        for slot in self.timeslots:
            if slot:
                d["timeslots"].append(slot.slot_to_json())
            else:
                d["timeslots"].append({"isvalid":0})
        return d


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

    # TODO: to_json method to populate db objects !important
    def week_to_json(self):
        d = {
            "code" : self.course_code,
            "year" : self.year,
            "sem" : self.semester,
            "days" : []
        }
        for day in self.days:
            d["days"].append(day.day_to_json())
        return d

