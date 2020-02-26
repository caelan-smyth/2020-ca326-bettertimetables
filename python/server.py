from flask import Flask, jsonify, request, Response, abort
from flask_restful import Resource, Api, reqparse
from timetable_getter import get_timetable

app = Flask(__name__)
api = Api(app)





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

@app.route('/test', methods=['GET'])
def send_test_data():
    return jsonify(test_data)


@app.route("/", methods = ['POST']) # opting for a top level POST of json with all form info.
def get_data(): # timetable getter will probably just get called here, but not sure where the DB will fit in.
    if not request.json:
        abort(400)
    data = request.json
    return data

@app.route("/table") 
def table():
    return get_timetable("http://oisin.site/timetable")


@app.route("/timetable/<string:course>/<string:year>/<string:semester>", methods=['GET'])
def handle_timetable(course, year, semester):
    return jsonify(course, year, semester)
    
    



# @app.route('/test') # test first layer route
# def get_test():
#     return jsonify({'test_data' : test_data})

# @app.route()
# def find_route(route):
#     if route == "hello":
#         return "hello"


if __name__ == '__main__':
    app.run(debug=True)
