from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/dropdata', methods=['GET'])
def handle_data():
    param_a = request.args.get('a')

    response_data = {'message': f'Received parameter a={param_a}'}

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='192.168.43.23', port=80)  
