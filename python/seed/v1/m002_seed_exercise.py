import sqlite3
import python.database_utilities.util as util

def upgrade(connection: sqlite3.Connection) -> bool:
    result: bool = True

    result = util.seed_from_csv(
        connection,
        '''
        INSERT INTO exercise (name, description, muscle_groups, work_types, equipment)
        VALUES (?, ?, ?, ?, ?);
        ''',
        "data/seed_exercise.csv",
    )

    return result


def downgrade(connection: sqlite3.Connection) -> bool:
    result: bool = True

    connection.execute("DELETE FROM exercise;")
    connection.commit()

    return result