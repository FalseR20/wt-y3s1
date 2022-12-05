#!/usr/bin/env python

from flask import Flask, Blueprint
from flask_restful import Api

from resources import example

app = Flask(__name__)
api = Api(app)
app.register_blueprint(api_blueprint := Blueprint("/api", __name__))
api.add_resource(example.ArgsResource, "/api/data_in_args")
api.add_resource(example.ParamsResource, "/api/data_in_params/<name>/<place>")
api.add_resource(example.FormResource, "/api/data_in_form")

if __name__ == "__main__":
    app.run(debug=False)
