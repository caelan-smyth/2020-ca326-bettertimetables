from flask import Flask, jsonify, request, Response, abort
from flask_restful import Resource, Api, reqparse
from timetable_getter import get_timetable

app = Flask(__name__)
api = Api(app)




test_data = [
    {
        "name": "Programming",
        "day": "monday",
        "loc": "CG12",
        "dur": "1"
    },
    {
        "name": "Operating Systems",
        "day": "tuesday",
        "loc": "LG27",
        "dur": "2"
    }
]


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')


class Test(Resource):
    def get(self):
        return jsonify(test_data)

api.add_resource(Test, '/test')

@app.route('/hello') # test top level route
def index():
    return "Hello, World!"


@app.route("/", methods = ['POST']) # opting for a top level POST of json with all form info.
def get_data(): # timetable getter will probably just get called here, but not sure where the DB will fit in.
    if not request.json:
        abort(400)
    data = request.json

@app.route("/table")
def table():
    return get_timetable("http://oisin.site/timetable")
    
    



# @app.route('/test') # test first layer route
# def get_test():
#     return jsonify({'test_data' : test_data})

# @app.route()
# def find_route(route):
#     if route == "hello":
#         return "hello"


if __name__ == '__main__':
    app.run(debug=True)
