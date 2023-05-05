"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa7f67avj5o48b95i0-a.oregon-postgres.render.com",
        database="todo_yzc8",
        user="todo_yzc8_user",
        password="TVNYsAJC3a9Afi9HgukVoglAtKJFBe20")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
