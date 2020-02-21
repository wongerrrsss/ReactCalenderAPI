# set up virtual environment
# set up flask boilerplate 
#set up sqlachemy 
#set up flask routes for each class table

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS 
from flask_marshmallow import Marshmallow 
from flask_heroku import Heroku 

app = Flask(__name__)
CORS(app)
heroku = Heroku(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

app.config["SQLALCHEMY_DATABASE_URI"] = ""



if __name__ == "__main__":
    app.debug = True
    app.run()