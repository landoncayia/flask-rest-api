from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import db

# Create the Pokemon table in the database file
#db.create_db_table()
# Add the data from the Pokemon csv to the database
#db.csv_to_db()

app = Flask(__name__)
# Allow access to endpoints from any IP address
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def home():
    return """Welcome to the Pokemon REST API. Here are the utilities available to you:<br>
    \t* /api/pokemon: Return all Pokemon using a GET request<br>
    \t* /api/pokemon/<pokedex_no>: Return a single Pokemon using a GET request (via Pokedex number)<br>
    \t* /api/pokemon/add: Add a Pokemon using a POST request (new data should be in JSON form)<br>
    \t* /api/pokemon/update: Update a Pokemon using a PUT request (updates made by linking Pokedex numbers)<br>
    \t* /api/pokemon/delete/<pokedex_no>: Delete a Pokemon using a DELETE request (via Pokedex number)<br>
    """

@app.route('/api/pokemon', methods=['GET'])
def api_get_all_pokemon():
    # We use jsonify so that we are returning JSON objects rather than Python dictionaries
    return jsonify(db.get_all_pokemon())

@app.route('/api/pokemon/<pokedex_no>', methods=['GET'])
def api_get_pokemon_by_dex(pokedex_no):
    return jsonify(db.get_pokemon_by_dex(pokedex_no))

@app.route('/api/pokemon/add', methods=['POST'])
def api_add_pokemon():
    pokemon = request.get_json()
    result = db.insert_pokemon(pokemon)
    return jsonify(result)

@app.route('/api/pokemon/update', methods=['PUT'])
def api_update_pokemon():
    pokemon = request.get_json()
    result = db.update_pokemon(pokemon)
    return jsonify(result)

@app.route('/api/pokemon/delete/<pokedex_no>', methods=['DELETE'])
def api_delete_pokemon(pokedex_no):
    return jsonify(db.delete_pokemon(pokedex_no))

if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run() # run Flask app
