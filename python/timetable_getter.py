from bs4 import BeautifulSoup
import requests, sys
from cleaner import cleanup
import csv
from flask import jsonify
import objects


def get_timetable(url): # get a bs4 object from a url to be passed to cleaner function.
    html = requests.get(url, verify=False)
    soup = BeautifulSoup(html.content, 'html.parser')
    oldsoup = soup
    soup = str(soup) # must be a string for cleaner function
    tables = get_tables(oldsoup)
    colspan = colspan_getter(tables)
    return [cleanup(soup), colspan]


def get_tables(soup): # extracts html tables from soup. needed to extract rowspan and colspan
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

def rowspan_getter(tables): # returns the rows occupied by each day, in order. deprecated.
    keys = tables.split("td rowspan")
    keys = keys[1:6]
    values = []
    for key in keys:
        values.append(int(key[2]))
    return values


