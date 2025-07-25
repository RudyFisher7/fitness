import sqlite3
import csv
from python.database_utilities.util import execute_script_from_file

def upgrade(connection: sqlite3.Connection) -> bool:
    result: bool = True

    with open("data/seed_exercise.csv") as file:
        reader = csv.DictReader(file)
        rows = [tuple(row.values()) for row in reader]

        connection.executemany('''
            INSERT INTO exercise (name, description, muscle_groups, work_types, equipment)
            VALUES (?, ?, ?, ?, ?)
        ''', rows)

        connection.commit()

    return result


def downgrade(connection: sqlite3.Connection) -> bool:
    result: bool = True

    connection.execute("DELETE FROM exercise;")
    connection.commit()

    return result