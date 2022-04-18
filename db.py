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
        