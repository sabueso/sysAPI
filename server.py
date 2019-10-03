#!/usr/bin/env python


from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

import sysapi_users

app = Flask(__name__)
api = Api(app)

class Users_list(Resource):
    def get(self):
        list_all_users=sysapi_users.list_users()
        return {'users': list_all_users} # Fetches first column that is Employee ID

api.add_resource(Users_list, '/users_list') # Route_1


if __name__ == '__main__':
     app.run(port='5002')