#!/usr/bin/python
import sqlite3

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