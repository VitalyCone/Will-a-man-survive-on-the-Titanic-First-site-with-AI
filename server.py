from flask import Flask, request, jsonify
from ii_model.main_model import send_model

app = Flask(__name__)

@app.route('/request', methods=['POST'])
def process_data():
    data = request.json['data']
    model_return = send_model(data)
    return jsonify(model_return)

if __name__ == '__main__':
    app.run(debug=True,port=5501)