# Flask Rest API

This is a REST API that connects to a Flask app, intended for use by CS275 students at the University of Vermont.

### Database C.R.U.D. operations

* **C**reate new database entries.
* **R**ead database entries.
* **U**pdate database entries.
* **D**elete database entries.

### Python modules used

* flask
  * Flask
  * request
  * jsonify
* db (package name is db_sqlite3)
* flask_cors
  * CORS

## How to Use

### REST API endpoints

This table describes our REST API "endpoints" - these are the URLs that will define how we can perform operations on our sqlite3 database.

| # | Endpoints                                             | HTTP Method | Description                                 |
|---|-------------------------------------------------------|-------------|---------------------------------------------|
| 1 | http://localhost:5000/api/pokemon                     | GET         | Get the list of all Pokemon in the database |
| 2 | http://localhost:5000/api/pokemon/<pokedex_no>        | GET         | Get a single Pokemon by its Pokedex no.     |
| 3 | http://localhost:5000/api/pokemon/add                 | POST        | Create a new Pokemon record                 |
| 4 | http://localhost:5000/api/pokemon/update              | PUT         | Update a Pokemon record                     |
| 5 | http://localhost:5000/api/pokemon/delete/<pokedex_no> | DELETE      | Delete a Pokemon record                     |

### Setup on UVM Silk

As currently implemented, getting this program to work on UVM's Silk server is a bit of a pain. This might be improved in the future, but it's what we've got for now. Here is what you need to do:
1. In Silk, create a directory called `api` withing your `www-root` directory (so that you have `api/www-root`).
2. Within the `api` directory, create the following files/directories:
   1. my_api.py
   2. public/
   3. wsgi.py
3. For each route (URL) that you wish to set up, you need to create a route in my_api.py. Contained within this repository is an example using Pokemon data.
4. Once you have your routes set up, edit `www-root/.silk.ini` with each route. Again, an example of my `.silk.ini` for this Pokemon example can be found within this repository.
5. Once you have your routes added to `.silk.ini`, run the following command from `www-root` on Silk: `silk site <url> update`. For <url>, simply insert the URL you wish to use. I just used `<netid>.w3.uvm.edu`.
6. Finally, run `silk app <url>/<path> load # for uri = /<path>` ***FOR EACH*** path you set up. You cannot run this command only once, or you will get 404 errors.
7. You are all set—your site should work as designed. Please note that, in my example, the POST and PUT requests require data to be supplied in JSON form in the request body. [Postman](https://www.postman.com/) is an excellent tool for this.

#### Sample Pokemon object
```json
pokemon = {
    "name": "Houndoom",
    "type1": "dark",
    "type2": "fire",
    "generation": 2,
    "abilities": [
                    'Early Bird',
                    'Flash Fire',
                    'Unnerve'
                 ]
}
```

## Resources used
* https://levelup.gitconnected.com/full-stack-web-app-with-python-react-and-bootstrap-backend-8592baa6e4eb
* Pokemon dataset: https://www.kaggle.com/datasets/rounakbanik/pokemon
* Postman API Platform for testing: https://www.postman.com/