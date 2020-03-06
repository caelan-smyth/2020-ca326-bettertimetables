from flask import Flask, jsonify, request, Response, abort
from timetable_getter import get_timetable
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from parser import timetableify
import os
import datetime
import json

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'timetables.db')
db = SQLAlchemy(app)
# list of urls from our dummy server. These could handily be replaced/consolidated with the actual legacy timetable
# urls and be added into the database successfully.
urls = [["CA", 1, 1, "http://student.computing.dcu.ie/~smythc45/ca11.html"],
        ["CA", 1, 2, "http://student.computing.dcu.ie/~smythc45/ca12.html"],
        ["CASE", 2, 1, "http://student.computing.dcu.ie/~smythc45/case21.html"],
        ["CASE", 2, 2, "http://student.computing.dcu.ie/~smythc45/case22.html"],
        ["CASE", 3, 1, "http://student.computing.dcu.ie/~smythc45/case31.html"],
        ["CASE", 3, 2, "http://student.computing.dcu.ie/~smythc45/case32.html"],
        ["CASE", 4, 1, "http://student.computing.dcu.ie/~smythc45/case41.html"],
        ["CASE", 4, 2, "http://student.computing.dcu.ie/~smythc45/case42.html"],
        ["DS", 1, 1, "http://student.computing.dcu.ie/~smythc45/ds11.html"],
        ["DS", 1, 2, "http://student.computing.dcu.ie/~smythc45/ds12.html"],
        ["DS", 2, 1, "http://student.computing.dcu.ie/~smythc45/ds21.html"],
        ["DS", 2, 2, "http://student.computing.dcu.ie/~smythc45/ds22.html"],
        ["DS", 3, 1, "http://student.computing.dcu.ie/~smythc45/ds31.html"],
        ["EC", 1, 1, "http://student.computing.dcu.ie/~smythc45/ec11.html"],
        ["EC", 1, 2, "http://student.computing.dcu.ie/~smythc45/ec12.html"],
        ["EC", 2, 1, "http://student.computing.dcu.ie/~smythc45/ec21.html"],
        ["EC", 2, 2, "http://student.computing.dcu.ie/~smythc45/ec22.html"],
        ["EC", 3, 1, "http://student.computing.dcu.ie/~smythc45/ec31.html"],
        ["EC", 4, 1, "http://student.computing.dcu.ie/~smythc45/ec41.html"],
        ["EC", 4, 2, "http://student.computing.dcu.ie/~smythc45/ec42.html"]
        ]

# ORM class for insertion into database.        
class Timetable(db.Model):
    code = db.Column(db.String) # course code
    year = db.Column(db.Integer)    # year of study
    semester = db.Column(db.Integer)    # semester
    jsontable = db.Column(db.Text, primary_key=True) # json representation of timetable for interpretation by react app
    creationdate = db.Column(db.DateTime, default=datetime.datetime.utcnow) # auto creation date column

    def __repr__(self): # purely for human debugging
        return "course {}, year {}, semester {}".format(self.code, self.year, self.semester)

    def get_json(self): # returns json data of timetable
        return self.jsontable


def url_to_database(urllist): # takes a url and calls parser functions to return an ORM object, fully populated, for insertion into DB
    url = urllist[3]    #[course code, year, semester, url]
    course_code = urllist[0]
    year = urllist[1]
    semester = urllist[2]
    tokens = get_timetable(url) # returns a list with the timetable data and some duration data of populated slots
    timetable_object = timetableify(tokens[0], course_code, year, semester, 0, tokens[1]) # create a true timetable object in memory and then pass its data to an ORM
    # ORM timetable object for insertion
    db_timetable = Timetable(code=course_code, year=year, semester=semester, jsontable=timetable_object.week_to_json())
    return db_timetable # return ORM object



@app.after_request
def after_request(response):
	'''
	Allows for Cross Origin Requests.
	'''
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
	return response


# this will be the route that handles everything. get request with dynamic route params will pull from DB
@app.route("/<string:course>/<string:year>/<string:semester>", methods=['GET'])
def handle_timetable(course, year, semester):
    # query DB with parameters passed by GET request.
    data = Timetable.query.filter_by(code=course, year=year, semester=semester).first().get_json()
    # no error handling here - handled on frontend in case of no response!
    return jsonify(json.loads(data))

# route to update the database automatically from the list of URLs.
# idea is that this could easily be automated (cron job every 24hrs would be a simple way)
@app.route("/update")
def update_db():
    for token in urls:
        entry = url_to_database(token)
        exists = db.session.query(Timetable).filter_by(code=token[0], year=token[1], semester=token[2]).scalar() is not None
        if not exists:    
            db.session.add(entry)
            db.session.commit()
        else:
            old_entry = db.session.query(Timetable).filter_by(code=token[0], year=token[1], semester=token[2]).first()
            if entry.jsontable != old_entry.jsontable:
                db.session.delete(old_entry)
                db.session.add(entry)
                db.session.commit()

    return "updated db"


if __name__ == '__main__':
    app.run(debug=True)                