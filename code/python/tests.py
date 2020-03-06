import unittest
from server import *
from parser import *
from timetable_getter import *
import requests
from bs4 import BeautifulSoup


class TestTesting(unittest.TestCase):

    def test_test(self): # basic test to proc CI/CD and make sure all is working
        self.assertEqual('foo'.upper(), 'FOO')
        print("test!")
    

class TestServer(unittest.TestCase):

    def test_url_to_db(self):
        url = ["CA", 1, 1, "http://student.computing.dcu.ie/~smythc45/ca11.html"]
        entry = url_to_database(url)
        self.assertIsInstance(entry, Timetable)

    def test_return_json(self):
        url = ["CA", 1, 1, "http://student.computing.dcu.ie/~smythc45/ca11.html"]
        entry = url_to_database(url)
        jsontable = entry.get_json()
        self.assertIsInstance(jsontable, str)
        self.assertIsInstance(repr(entry), str)

class TestParser(unittest.TestCase):
    f = open("soup.txt", "r")
    s = f.read()
    lists = make_lists(s)

    def test_make_lists(self):
        self.assertEqual(len(TestParser.lists), 5)

    def test_make_lists_type(self):
        self.assertIsInstance(TestParser.lists[0], str)
             
    def test_parse_daylist(self):
        day = parse_daylist(TestParser.lists[0], "Monday")
        self.assertIsInstance(day, timetableDay)

    def test_timetableify(self):
        colspan = [2, 2, 2, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 4]
        week = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        finaltable = timetableify(TestParser.s, "CASE", 2, 2, 2, colspan)
        self.assertIsInstance(finaltable, courseTimetable)

    
class TestCleaner(unittest.TestCase):

    def test_deletion(self):
        self.assertEqual(cleanup("17:30|---![],\n"), "")

    def test_emptyslot(self):
        self.assertEqual(cleanup('17:30<img height="1" src="http://www.dcu.ie/images/space.gif" width="1"/>'), "emptySlot\n")

    def test_emptyslot2(self):
        self.assertEqual(cleanup('17:30<td style="border-bottom:3px solid #000000;"><img height="1" src="http://www.dcu.ie/images/space.gif" width="1"/></td>'), "emptySlot\n")

    def test_regex(self):
        self.assertEqual(cleanup("17:30<dlnwaldnawldknlawknd>"), "")

    def test_regex2(self):
        self.assertEqual(cleanup("17:30[dwlkadnlawnda\n").strip(), "")

    def test_regex3(self):
        self.assertEqual(cleanup("17:30(nwdnjwndjwndjwd\n").strip(), "")
    
    def test_split(self):
        self.assertEqual(cleanup("17:30fooSatjndjsnjdsn"), "foo")


class TestGetter(unittest.TestCase):
    url = "http://oisin.site/timetable"
    html = requests.get(url, verify=False)
    soup = BeautifulSoup(html.content, 'html.parser')
    def test_get_timetable(self):
        tokens = get_timetable(TestGetter.url)
        self.assertIsInstance(tokens, list)

    def test_get_types(self):
        tokens = get_timetable(TestGetter.url)
        self.assertIsInstance(tokens[0], str)
        self.assertIsInstance(tokens[1], list)

    def test_get_tables(self):
        tables = get_tables(TestGetter.soup)
        self.assertIsInstance(tables, str)

    def test_colspan(self):
        tables = get_tables(TestGetter.soup)
        colspans = colspan_getter(tables)
        self.assertIsInstance(colspans, list)

# class TestObjects(unittest.TestCase):






if __name__ == "__main__":
    unittest.main()