from flask import Flask, request, jsonify
from flask_cors import CORS
from test import decompose as func

app = Flask(__name__)
CORS(app)

@app.route('/decompose', methods=['POST'])
def decompose():
    sentence = request.json['sentence']
    res = func(sentence)
    decomposed_string = res[0]
    #res[1].draw()
    return jsonify({'result': decomposed_string})

if __name__ == '__main__':
    app.run()