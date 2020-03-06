import re
def cleanup(s):
    s = s.replace("|", "")
    s = s.replace("---", "")
    s = s.replace("![]", "")
    s = s.replace('<img height="1" src="http://www.dcu.ie/images/space.gif" width="1"/>', "emptySlot\n")
    s = s.replace('<td style="border-bottom:3px solid #000000;"><img height="1" src="http://www.dcu.ie/images/space.gif" width="1"/></td>', 'emptySlot\n')
    s = re.sub(r"\<(.*?)\>", "", s)
    s = s.split("17:30")[1]
    s = s.split("Sat")[0]
    s = s.replace(", ", ",")
    s = s.replace(",\n", "")
    s = s.replace("  ", "\n")
    s = s.replace("   ", "\n")
    s = s.replace("\n ", "\n")
    s = re.sub(r"\n+", "\n\n", s) # double newline is purely for readability by humans
    s = re.sub(r"\((.*?)\n", "", s)
    s = re.sub(r"\[(.*?)\n", "\n", s)
    s = s.replace("\n\n", "\n")
    return s

