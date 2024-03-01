from flask import Flask, jsonify, request
from model.cost_estimation import run_model

app = Flask(__name__)

@app.route('/cost', methods=['GET'])
def cost():
    area = request.args.get('area', type=float)
    depth = request.args.get('depth', type=float)
    result = run_model(area, depth) 
    return jsonify({'price': result.tolist()})

if __name__ == '__main__':
    app.run()