from flask import Flask
from flask_restful import Api

import resources

app = Flask(__name__)
api = Api(app)
api.add_resource(resources.ArgsResource, "/api/data_in_args")
api.add_resource(resources.ParamsResource, "/api/data_in_params/<name>/<place>")
api.add_resource(resources.FormResource, "/api/data_in_form")

if __name__ == "__main__":
    app.run(debug=False)
