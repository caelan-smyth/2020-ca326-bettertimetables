from flask import Flask, jsonify

app = Flask(__name__)

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

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/test')
def get_test():
    return jsonify({'test_data' : test_data})

if __name__ == '__main__':
    app.run(debug=True)
