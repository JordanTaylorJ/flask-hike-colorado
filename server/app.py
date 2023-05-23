from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
#from models import 

# Views go here!

if __name__ == '__main__':
    app.run(port=5555, debug=True)