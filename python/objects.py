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
        s = "-----\n"
        s += ("Day: {}\n".format(self.day))
        s += ("Time: {}\n".format(self.time))
        s += ("Type: {}\n".format(self.slot_type))
        s += ("Location: {}\n".format(self.location))
        s += ("Title: {} {}\n".format(self.code, self.title))
        s += ("Weeks: {}".format(self.weeks))

        return s

