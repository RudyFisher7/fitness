import sqlite3
from python.database_utilities.util import execute_script_from_file

# the order of this list is important
tables: list[str] = [
    "user",
    "exercise",
    "exercise_demo",
    "routine",
    "routine_exercise",
]

def upgrade(connection: sqlite3.Connection) -> bool:
    result: bool = True
    fstring: str = "sql/v1/%s/create_table_%s.sql"

    for table in tables:
        execute_script_from_file(connection, fstring % (table, table))

    return result


def downgrade(connection: sqlite3.Connection) -> bool:
    result: bool = True
    fstring: str = "sql/v1/%s/drop_table_%s.sql"
    
    for table in tables:
        execute_script_from_file(connection, fstring % (table, table))

    return result