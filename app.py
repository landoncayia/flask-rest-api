from flask import Flask, request, jsonify
from flask_cors import CORS
import db

app = Flask(__name__)
# Allow access to endpoints from any IP address
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/pokemon', methods=['GET'])
def api_get_all_pokemon():
    # We use jsonify so that we are returning JSON objects rather than Python dictionaries
    return jsonify(db.get_all_pokemon())

@app.route('/api/pokemon/<pokedex_no>', methods=['GET'])
def api_get_pokemon_by_dex(pokedex_no):
    return jsonify(db.get_pokemon_by_dex(pokedex_no))

@app.route('api/pokemon/add', methods=['POST'])
def api_add_pokemon():
    pokemon = request.get_json()
    return jsonify(db.insert_pokemon(pokemon))

@app.route('api/pokemon/update', methods=['PUT'])
def api_update_pokemon():
    pokemon = request.get_json()
    return jsonify(db.update_pokemon(pokemon))

@app.route('api/pokemon/delete/<pokedex_no>', methods=['DELETE'])
def api_delete_pokemon(pokedex_no):
    return jsonify(db.delete_pokemon(pokedex_no))

if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run() # run Flask app
