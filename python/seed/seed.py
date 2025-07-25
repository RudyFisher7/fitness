import sys
import sqlite3
import python.database_utilities.util as util
from types import ModuleType

args: list[str] = ["v1", "upgrade"]

arg_len: int = len(sys.argv)
for i in range(len(args)):
    args[i] = sys.argv[i + 1] if arg_len > (i + 1) else args[i]

# the order of this list is important
modules: list[ModuleType] = []

modules.append(util.import_seed_module(args[0], "m002_seed_exercise"))
modules.append(util.import_seed_module(args[0], "m003_seed_exercise_demo"))
modules.append(util.import_seed_module(args[0], "m004_seed_user"))

connection: sqlite3.Connection = sqlite3.connect("database.db")

if (args[1] == "downgrade"):
    for module in reversed(modules):
        module.downgrade(connection)
else:
    for module in modules:
        module.upgrade(connection)

connection.close()