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
db_url = os.environ.get("DATABASE_URL")
if os.environ.get("ENV") == 'dev':
    db_url = db_url.replace('postgres', 'postgresql')
    db_url = db_url.replace('username', 'postgres')
elif os.environ.get("ENV") == 'prod':
    db_url = db_url.replace('postgres', 'postgresql')
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
models.db.init_app(app)

def root():
  return { "message": "ok" }
app.route('/', methods=["GET"])(root)

apply_routes(app)

if __name__ == '__main__':
  port = int(os.environ.get('PORT') or 5000)
  app.run(host='0.0.0.0', port=port, debug=True)