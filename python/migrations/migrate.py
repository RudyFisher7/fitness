import sys
import os
import sqlite3
import python.database_utilities.util as util
from types import ModuleType

args: list[str] = ["v1", "upgrade"]
database_file_path: str = "database.db"

arg_len: int = len(sys.argv)
for i in range(len(args)):
    args[i] = sys.argv[i + 1] if arg_len > (i + 1) else args[i]

# the order of this list is important
modules: list[ModuleType] = []

modules.append(util.import_migration_module(args[0], "m001_create_tables"))

if args[1] == "upgrade":
    if not os.path.exists(database_file_path):
        with open(database_file_path, "w") as file:
            pass

connection: sqlite3.Connection = sqlite3.connect(database_file_path)

if args[1] == "downgrade":
    for module in reversed(modules):
        module.downgrade(connection)
else:
    for module in modules:
        module.upgrade(connection)

connection.close()

if args[1] == "downgrade":
    if os.path.exists(database_file_path):
        os.remove(database_file_path)