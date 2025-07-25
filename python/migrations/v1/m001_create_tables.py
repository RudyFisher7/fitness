import sqlite3
from python.database_utilities.util import execute_script_from_file

def upgrade(connection: sqlite3.Connection) -> bool:
    result: bool = True
    fstring: str = "sql/v1/%s/create_table_%s.sql"

    execute_script_from_file(connection, fstring % ("user", "user"))
    execute_script_from_file(connection, fstring % ("exercise", "exercise"))
    execute_script_from_file(connection, fstring % ("exercise_demo", "exercise_demo"))

    return result


def downgrade(connection: sqlite3.Connection) -> bool:
    result: bool = True
    fstring: str = "sql/v1/%s/drop_table_%s.sql"
    
    execute_script_from_file(connection, fstring % ("user", "user"))
    execute_script_from_file(connection, fstring % ("exercise", "exercise"))
    execute_script_from_file(connection, fstring % ("exercise_demo", "exercise_demo"))

    return result