from objects import Timeslot, timetableDay, courseTimetable
from flask import jsonify
import copy

def make_lists(data): # splits the long string of plaintext timetable info into a token for each day
    day_strings = data.replace("Mon", "splitplaceholder").replace("Tue", "splitplaceholder").replace("Wed", "splitplaceholder").replace("Thu", "splitplaceholder").replace("Fri", "splitplaceholder").split("splitplaceholder")

    mon, tue, wed, thu, fri = day_strings[1], day_strings[2], day_strings[3], day_strings[4], day_strings[5]
    return [mon, tue, wed, thu, fri]

def parse_daylist(s, day): # pass one daystring at a time. returns a populated Day object.
    s = s.strip()
    keys = s.split("\n")
    keys = keys[2:]
    output_day = timetableDay(day)
    start_strings = ["Prac.", "Lec.", "Tut."]
    i = 0
    while i < len(keys):
        if keys[i] == "emptySlot":
            output_day.add_timeslot(None)
            i += 1
        elif keys[i].strip() in start_strings:
            if keys[i+4][0].isdigit():
                typ = keys[i]
                loc = keys[i+1]
                code = keys[i+3]
                title = keys[i+3]
                weeks = keys[i+4]
                i += 1
            else:
                typ = keys[i]
                loc = keys[i+1]
                title = keys[i+3]
                code = keys[i+4]
                weeks = keys[i+5]
                i += 1
            output_day.add_timeslot(Timeslot(day, typ, loc, title, code, weeks))
        else:
            i += 1
    return output_day

# returns a fully populated timetable week object given the plaintext string and some more info
def timetableify(s, code, year, sem, rowspan, colspan): # pass me cleaned up soup
    final_timetable = courseTimetable(code, year, sem)
    
    days = make_lists(s)
    week = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    for i in range(5):
        final_timetable.add(parse_daylist(days[i], week[i]))
    non_empty = [day.non_empty() for day in final_timetable]
    durations = [] 
    tmpcolspan = colspan[:] # trick to force a deep copy instead of reference
    for key in non_empty: # assembling a list for each day representing the durations of each non empty slot
        if key !=0:
            durations.append(tmpcolspan[:key])
            tmpcolspan = tmpcolspan[key:]
        else:
            durations.append([])
    # durations is a list of list representing dur of non empty slots for each day.
    # now use setters and getters, build a new list with duped slots and replace.
    # result is to normalise each slot to be 30mins and each row to have an even no of slots - less work on frontend
    currentday = 0
    for day in final_timetable:
        slots = day.get_timeslots()
        newslots = []
        current_durations = durations[currentday]
        nonemptycounter = 0
        for slot in slots:
            if slot is None:
                newslots.append(None)
            else:
                for i in range(current_durations[nonemptycounter]):
                    newslots.append(slot)                
                nonemptycounter += 1
        newnewslots = newslots[:18]
        if len(newslots) > 18:
            restrows = newslots[18:]
            list_rest_rows = [restrows[i:i+20] for i in range(0, len(restrows), 20)]
            for row in list_rest_rows:
                newnewslots += row[2:]
        day.set_timeslots(newnewslots)
        currentday += 1
    return final_timetable





    