from objects import Timeslot, timetableDay, courseTimetable
from flask import jsonify
import copy

def make_lists(data): # pass me cleanup(soup)
    day_strings = data.replace("Mon", "splitplaceholder").replace("Tue", "splitplaceholder").replace("Wed", "splitplaceholder").replace("Thu", "splitplaceholder").replace("Fri", "splitplaceholder").split("splitplaceholder")

    mon, tue, wed, thu, fri = day_strings[1], day_strings[2], day_strings[3], day_strings[4], day_strings[5]
    return [mon, tue, wed, thu, fri]

def parse_daylist(s, day): # pass one daystring at a time. returns a list of timeslot objects
    s = s.strip()
    keys = s.split("\n")
    keys = keys[2:]
    output_day = timetableDay(day)
    start_strings = ["Prac.", "Lec.", "Tut."]
    i = 0
    while i < len(keys):
        if keys[i] == "emptySlot":
            # output_list.append(None)
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
            # output_list.append(Timeslot(day, typ, loc, title, code, weeks))
            output_day.add_timeslot(Timeslot(day, typ, loc, title, code, weeks))
        else:
            i += 1

    # return output_list
    # print(output_day.daylength())
    return output_day


def timetableify(s, code, year, sem, rowspan, colspan): # pass me cleaned up soup
    final_timetable = courseTimetable(code, year, sem)
    
    days = make_lists(s)
    week = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    for i in range(5):
        final_timetable.add(parse_daylist(days[i], week[i]))
    # TODO: normalise slots to 30mins here. cross ref durations and dupe long slots
    # each list should be the same length or 2x.
    non_empty = [day.non_empty() for day in final_timetable]
    durations = [] 
    print(non_empty)
    # if len(durations) == 0:
    tmpcolspan = colspan[:]
    for key in non_empty:
        durations.append(tmpcolspan[:key])
        tmpcolspan = tmpcolspan[key:]
    durations = [i for i in durations if len(i) > 0]
    # durations is a list of list representing dur of non empty slots for each day.
    # now use setters and getters, build a new list with duped slots and replace.
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

        if len(newslots) > 18:
            newslots = newslots[:18] + newslots[20:]
        day.set_timeslots(newslots)
        currentday += 1
    return final_timetable




def main():
    f = open("soup.txt", "r")
    s = f.read()
    colspan = [2, 2, 2, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 4]
    table = timetableify(s, "case", 2, 2, 0, colspan)
    # print(table.week_to_json())
    # for day in table:
    #     print(day.non_empty())
    # print(table)
    f = open("tablestring.txt", "w")
    f.write(str(table))
    for day in table:
        print(day.daylength())





if __name__ == "__main__":
    main()






    