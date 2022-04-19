#!/usr/bin/python
import sqlite3
import csv

def connect_to_db():
    """ Establish a connection to the database file.
    :return: the connection object for the database file
    """
    conn = sqlite3.connect('database.db')
    return conn

def create_db_table():
    """ Attempt to create the Pokemon table in the database file,
    with error handling.
    """
    try:
        conn = connect_to_db()
        conn.execute('''
            CREATE TABLE pokemon (
                pokedex_number integer PRIMARY KEY NOT NULL,
                name text NOT NULL,
                type1 text NOT NULL,
                type2 text,
                generation integer NOT NULL,
                abilities text NOT NULL
            );
        ''')

        conn.commit()
        print("Pokemon table create successfully")
    except:
        print("Pokemon table creation failed")
    finally:
        conn.close()

def csv_to_db():
    """ Read the data from the .csv file into the database
    """
    try:
        conn = connect_to_db()
        try:
            with open('pokemon.csv') as pkm_csv:
                # Create csv reader object
                reader = csv.reader(pkm_csv)

                # Extract field row at top of csv file
                fields = next(reader)

                # Read the data from the csv file, row by row, insert into the database
                for row in reader:
                    sql = '''INSERT INTO pokemon (pokedex_number, name, type1, type2, generation, abilities) 
                            VALUES (?, ?, ?, ?, ?, ?);
                    '''
                    val = (int(row[32]), row[30], row[36], row[37], int(row[39]), row[0])
                    cur = conn.cursor()
                    cur.execute(sql, val)
        except:
            conn.rollback()
            print("Error reading csv data into database, rolling back")
    except:
        print("CSV reading failed")
    finally:
        conn.close()

def insert_pokemon(pokemon):
    """ Implements the 'Create' in CRUD - inserts a Pokemon into the database
    :param pokemon: the pokemon to be inserted
    :return: the Pokemon that was inserted
    """
    inserted_pokemon = {}
    try:
        conn = connect_to_db()
        # Cursor object is used to execute CRUD operations
        cur = conn.cursor()
        # SQL 'INSERT INTO' statement inserts new records into a database
        # See the README for an example of what the parameter 'pokemon' should be formatted as
        cur.execute("INSERT INTO pokemon (pokedex_number, name, type1, type2, generation, abilities) \
                        VALUES (?, ?, ?, ?, ?, ?)", (pokemon['pokedex_number'], pokemon['name'], pokemon['type1'],
                        pokemon['type2'], pokemon['generation'], pokemon['abilities']))
        # Changes must be committed to the database
        conn.commit()
        inserted_pokemon = get_pokemon_by_dex(cur.lastrowid)
    except:
        # If an error occurs, roll back and state which function the error occurred in
        conn.rollback()
        print("Error inserting new Pokemon into the database")
    
    finally:
        # Always remember to close the connection when done
        conn.close()
    
    return insert_pokemon
        
def get_all_pokemon():
    """ Partially implements the 'Retrieve' in CRUD - retrieves ALL Pokemon from the database
    :return: all the Pokemon in the database
    """
    all_pokemon = []
    try:
        conn = connect_to_db()
        # row_factory = Row makes it so that name-based access to columns are possible rather than just indexed like with tuples
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        # SQL SELECT statement to retrieve everything from the database
        cur.execute("SELECT * FROM pokemon")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            pokemon = {}
            pokemon['pokedex_number'] = i['pokedex_number']
            pokemon['name'] = i['name']
            pokemon['type1'] = i['type1']
            pokemon['type2'] = i['type2']
            pokemon['generation'] = i['generation']
            pokemon['abilities'] = i['abilities']
            all_pokemon.append(pokemon)
            
    except:
        pokemon = []
        print("Error retrieving all Pokemon from the database")
    
    finally:
        conn.close()
    
    return all_pokemon

def get_pokemon_by_dex(pokedex_no):
    """ Partially implements the 'Retrieve' in CRUD - retrieves a single Pokemon from the database by Pokedex no.
    :param pokedex_no: the Pokedex no. of the Pokemon to be retrieved
    :return: the specified Pokemon's database entry
    """
    pokemon = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        # SQL SELECT statement along with WHERE to retrieve a Pokemon with a certain Pokedex no. from the database
        cur.execute("SELECT * FROM pokemon WHERE pokedex_number = ?", (pokedex_no,))
        row = cur.fetchone()

        # convert row object to dictionary
        pokemon['pokedex_number'] = row['pokedex_number']
        pokemon['name'] = row['name']
        pokemon['type1'] = row['type1']
        pokemon['type2'] = row['type2']
        pokemon['generation'] = row['generation']
        pokemon['abilities'] = row['abilities']
    
    except:
        pokemon = {}
        print("Error retrieving single Pokemon from the database with no:", pokedex_no)
    
    finally:
        conn.close()

    return pokemon

def update_pokemon(pokemon):
    """ Implements the 'Update' in CRUD - updates a single Pokemon in the database
    :param pokemon: the Pokemon to be updated (identified by Pokedex no.)
    :return: the Pokemon that was updated
    """
    updated_pokemon = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        # SQL UPDATE statement along with WHERE to update a Pokemon with a certain Pokedex no. in the database
        cur.execute("UPDATE pokemon SET name = ?, type1 = ?, type2 = ?, generation = ?, abilities = ?\
                     WHERE pokedex_number = ?", pokemon['name'], pokemon['type1'], pokemon['type2'],
                     pokemon['generation'], pokemon['abilities'], pokemon['pokedex_number'])
        conn.commit()
        # return the Pokemon
        updated_pokemon = get_pokemon_by_dex(pokemon['pokedex_number'])
    
    except:
        conn.rollback()
        updated_pokemon = {}
        print("Error updating the pokemon:", pokemon)
    
    finally:
        conn.close()
    
    return updated_pokemon

def delete_pokemon(pokedex_no):
    """ Implements the 'Delete' in CRUD - deletes a single Pokemon in the database
    :param pokedex_no: the Pokedex no. of the Pokemon to be delete
    :return: a success/failure message
    """
    message = {}
    try:
        conn = connect_to_db()
        # SQL DELETE statement along with WHERE to delete a Pokemon with a certain Pokedex no. from the database
        conn.execute("DELETE from pokemon WHERE pokedex_number = ?", (pokedex_no,))
        conn.commit()
        message['status'] = "Pokemon deleted successfully"
    except:
        conn.rollback()
        message['status'] = "Cannot delete Pokemon"
    finally:
        conn.close()
    
    return message

