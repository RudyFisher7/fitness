import sqlite3
from python.migrations.v1.m001_create_tables import upgrade


connection: sqlite3.Connection = sqlite3.connect("database.db")

upgrade(connection)

connection.close()