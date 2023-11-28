from flask import Flask, request, jsonify

app = Flask(__name__)

# Almacenar datos de posición de los agentes
agent_positions = {}
agent_states = {}

#Routes--------------------------------------------
@app.route('/update_positions', methods=['POST'])
def update_positions():
    data = request.json
    agent_positions.update(data)
    return jsonify({"status": "success"})

@app.route('/agent', methods=['GET'])
def get_positions():
    # Convertir el diccionario en una lista de objetos para que Unity pueda procesarlo
    positions_list = [{"id": key, "position": value} for key, value in agent_positions.items()]
    return jsonify(positions_list)

@app.route('/update_estados', methods=['POST'])
def update_states():
    data = request.json
    agent_states.update(data)
    return jsonify({"status": "success State"})

@app.route('/agentState', methods=['GET'])
def get_states():
    # Convertir el diccionario en una lista de objetos para que Unity pueda procesarlo
    states_list = [{"id": key, "state": value} for key, value in agent_states.items()]
    return jsonify(states_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)