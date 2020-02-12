from bs4 import BeautifulSoup
import requests, sys
from cleaner import cleanup
import csv

def main():
    print(get_timetable("http://oisin.site/timetable"))

def get_timetable(url):
    html = requests.get(url, verify=False)
    soup = BeautifulSoup(html.content, 'html.parser')
    oldsoup = soup
    soup = str(soup)
    # print(cleanup(soup))
    f = open("soup.txt", "w+")
    f.write(cleanup(soup))

    tables = get_tables(oldsoup)
    print(colspan_getter(tables))
    print(rowspan_getter(tables))


def get_tables(soup): # extracts tables from soup. needed to extract rowspan and colspan
    raw_html = ""
    for table in soup.find_all("td"):
        raw_html += str(table)
    return raw_html

def colspan_getter(tables): # returns the duration of every non-empty slot in order
    keys = tables.split("colspan")
    keys = keys[21:]
    values = []
    for key in keys:
        values.append(int(key[2]))
    return values

def rowspan_getter(tables): # returns the rows occupied by each day, in order
    keys = tables.split("td rowspan")
    keys = keys[1:6]
    values = []
    for key in keys:
        values.append(int(key[2]))
    return values


if __name__ == "__main__":
    main()



