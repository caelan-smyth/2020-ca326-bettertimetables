from flask import Flask, jsonify, request, Response, abort
from flask_restful import Resource, Api, reqparse
from timetable_getter import get_timetable
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
api = Api(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'timetables.db')
db = SQLAlchemy(app)

class Timetable(db.Model):
    code = db.Column(db.String, primary_key=True)
    year = db.Column(db.Integer)
    semester = db.Column(db.Integer)
    jsontable = db.Column(db.Text)

    def __repr__(self):
        return "course {}, year {}, semester {}".format(self.code, self.year, self.semester)







test_data =     {
        "code" : "CASE",
        "year" : 2,
        "sem" : 1,
        "days" : [
            {
                "day" : "Monday",
                "timeslots" : [
                    {"isvalid" : 0},
                    {"isvalid" : 0},
                    {"isvalid" : 0},
                    {"isvalid" : 0},
                    {"isvalid" : 0},
                    {"isvalid" : 0},
                    {
                        "isvalid" : 1,
                        "code" : "CA266",
                        "title" : "Probstats",
                        "loc" : "GLA.LG25"
                    },
                    {
                        "isvalid" : 1,
                        "code" : "CA266",
                        "title" : "Probstats",
                        "loc" : "GLA.LG25"
                    },
                    {"isvalid" : 0},
                    {"isvalid" : 0},
                    {
                        "isvalid" : 1,
                        "code" : "CA269",
                        "title" : "Prog 4",
                        "loc" : "GLA.LG25"
                    },
                                        {
                        "isvalid" : 1,
                        "code" : "CA269",
                        "title" : "Prog 4",
                        "loc" : "GLA.LG25"
                    },
                    {
                        "isvalid" : 1,
                        "code" : "CA269",
                        "title" : "Prog 4",
                        "loc" : "GLA.LG25"
                    },
                                        {
                        "isvalid" : 1,
                        "code" : "CA269",
                        "title" : "Prog 4",
                        "loc" : "GLA.LG25"
                    },
                    {"isvalid" : 0},
                    {"isvalid" : 0},
                    {"isvalid" : 0},
                    {"isvalid" : 0}

                ]
            }
        ]

    }

@app.after_request
def after_request(response):
	'''
	Allows for Cross Origin Requests.
	'''
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
	return response


@app.route('/hello') # test top level route
def index():
    return "Hello, World!"

@app.route("/table") 
def table():
    return get_timetable("http://oisin.site/timetable")

# this will be the route that handles everything. get request with dynamic route params will pull from DB
@app.route("/timetable/<string:course>/<string:year>/<string:semester>", methods=['GET'])
def handle_timetable(course, year, semester):
    return jsonify(course, year, semester)
    
    





if __name__ == '__main__':
    app.run(debug=True)
