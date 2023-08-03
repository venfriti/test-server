from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/dropdata', methods=['GET'])
def handle_data():
    param_a = request.args.get('a')
    param_b = request.args.get('b')
    param_c = request.args.get('c')
    param_d = request.args.get('d')
    param_e = request.args.get('e')
    param_f = request.args.get('f')

    response_data = {'message': f'Received parameter a={param_a}, b={param_b}, c={param_c}, d={param_d}, e={param_e}, f={param_f}'}

    print(f'Received parameter a={param_a}, b={param_b}, c={param_c}, d={param_d}, e={param_e}, f={param_f}')

    # Return an empty response (optional)
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
