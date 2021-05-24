import os
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS
import sqlalchemy

import models
from routes import apply_routes

load_dotenv()
app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
models.db.init_app(app)

def root():
  return { "message": "ok" }
app.route('/', methods=["GET"])(root)

apply_routes(app)

if __name__ == '__main__':
  port = os.environ.get('PORT') or 5000
  app.run(port=port, debug=True)