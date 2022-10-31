from flask import Flask
from flask_restful import Api

import resources

app = Flask(__name__)
api = Api(app)
api.add_resource(resources.HelloWorld, "/")

if __name__ == "__main__":
    app.run(debug=True)
