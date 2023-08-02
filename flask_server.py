from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/dropdata', methods=['GET'])
def handle_data():
    param_a = request.args.get('a')
    param_b = request.args.get('b')

    response_data = {'message': f'Received parameter a={param_a}, b={param_b}'}

    print(f'Received parameter a={param_a}, b={param_b}')

    # Return an empty response (optional)
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='192.168.0.102', port=80)  
