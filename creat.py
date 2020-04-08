import os

from flask import Flask, render_template, request
from models import *
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Flask
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:20001003@localhost:5432/test"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

#sqlAlchemy
engine = create_engine('postgresql://postgres:20001003@localhost:5432/test', echo = True)
metadata = MetaData
Base = declarative_base()
Session = sessionmaker(bind = engine)

def main():
    #creat database table
    db.metadata.create_all(engine)

if __name__ == "__main__":
    with app.app_context():
        main()
