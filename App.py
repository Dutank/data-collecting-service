from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"
@app.route('/machinelearning')
def machine_learning():
    retJson = {
        'Algorithm': 'Random Forest',
        'Parameter': [
            {
                'Company': 'circular tree',
                'Author': 'dlee'
            },
            {
                'Company': 'ipoint',
                'Author': 'gwalden'
            }
        ]
    }
    return jsonify(retJson)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)