# Flask Rest API

This is a REST API that connects to a Flask app, intended for use by CS275 students at the University of Vermont.

## Background on REST APIs

## The C.R.U.D. operations

* **C**reate:
* **R**etrieve:
* **U**pdate:
* **D**elete:

## Modules used

* Flask
* db-sqlite3

## REST API endpoints

This table describes our REST API "endpoints" - these are the URLs that will define how we can perform operations on our sqlite3 database.

| # | Endpoints                                             | HTTP Method | Description                                 |
|---|-------------------------------------------------------|-------------|---------------------------------------------|
| 1 | http://localhost:5000/api/pokemon                     | GET         | Get the list of all Pokemon in the database |
| 2 | http://localhost:5000/api/pokemon/<pokedex_no>        | GET         | Get a single Pokemon by its Pokedex no.     |
| 3 | http://localhost:5000/api/pokemon/add                 | POST        | Create a new Pokemon record                 |
| 4 | http://localhost:5000/api/pokemon/update              | PUT         | Update a Pokemon record                     |
| 5 | http://localhost:5000/api/pokemon/delete/<pokedex_no> | DELETE      | Delete a Pokemon record                     |

## Resources used
* https://levelup.gitconnected.com/full-stack-web-app-with-python-react-and-bootstrap-backend-8592baa6e4eb
* Pokemon dataset: https://www.kaggle.com/datasets/rounakbanik/pokemon