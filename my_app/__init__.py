import os
from flask import Flask, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = Flask(__name__)

#load main config
app.config.from_pyfile('../config.py') 
db = SQLAlchemy(app)
socketio = SocketIO(app)


import my_app.views
import my_app.models

db.create_all()