import sys
import importlib
import sqlite3

args: list[str] = ["v1", "upgrade"]

arg_len: int = len(sys.argv)
for i in range(len(args)):
    args[i] = sys.argv[i + 1] if arg_len > (i + 1) else args[i]

m1_path: str = f"python.migrations.{args[0]}.m001_create_tables"
m1 = importlib.import_module(m1_path)

m2_path: str = f"python.migrations.{args[0]}.m002_seed_exercise"
m2 = importlib.import_module(m2_path)

connection: sqlite3.Connection = sqlite3.connect("database.db")

if (args[1] == "downgrade"):
    m2.downgrade(connection)
    m1.downgrade(connection)
else:
    m1.upgrade(connection)
    m2.upgrade(connection)

connection.close()