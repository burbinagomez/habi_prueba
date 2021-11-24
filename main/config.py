"""
This file containes all the configuration instances
"""
import os
from sqlalchemy import create_engine
from flask import Flask
from dotenv import load_dotenv
load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")
user = os.getenv("USER_DB")
pwd = os.getenv("PASS")
schema = os.getenv("SCHEMA")

db_engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@{host}:{port}/{schema}")
app = Flask(__name__)
