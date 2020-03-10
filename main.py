# import datetime

from flask import Flask, render_template, request
from google.cloud import datastore
# from pynubank import Nubank


# Stuff for Flask
app = Flask(__name__)
# Stuff for DataStore
datastore_client = datastore.Client()
# Stuff for Nubank
# nu = Nubank()

# Creates new user
def store_new_user(id, key, value):
    # Try to get
    # If found, update
    # Else, create
    
    kind = 'user'
    name = id
    user_key = datastore_client.key(kind, name)
    user = datastore.Entity(key = user_key)
    user[key] = value
    datastore_client.put(user)

    return True

# Returns a user
def fetch_user(cpf):
    user_key = datastore_client.key('user', cpf)
    user = datastore_client.get(user_key)
    return user


@app.route('/davi')
def davi():
    return "10"


@app.route('/new/<int:cpf>/<name>')
def store_user(cpf, name):
    result = store_new_user(cpf, 'name', name)
    if result:
        return 'Success! Stored '+ str(cpf) + ', ' + str(name)
    else:
        return 'Failed. Try again'


@app.route('/fetch_user/<int:cpf>')
def get_user(cpf):
    return fetch_user(cpf)

@app.route('/fetch_user_info/<int:cpf>/<field>')
def get_user_field(cpf, field):
    return fetch_user(cpf)[field]

@app.route('/update_user_info/<int:cpf>/<field>/<value>')
def update_user_info(cpf, field, value):
    user = fetch_user(cpf)
    user[field] = value
    datastore_client.put(user)
    return "Success"



if __name__ == '__main__':
    
    app.run(host='127.0.0.1', port=8080, debug=True)