import sqlite3
import python.database_utilities.util as util

def upgrade(connection: sqlite3.Connection) -> bool:
    result: bool = True

    result = util.seed_from_csv(
        connection,
        '''
        INSERT INTO routine_exercise_set (routine_id, exercise_id, index_in_routine, equipment, duration, distance, reps, resistance)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        ''',
        "data/seed_routine_exercise_set.csv",
    )

    return result


def downgrade(connection: sqlite3.Connection) -> bool:
    result: bool = True

    connection.execute("DELETE FROM routine_exercise_set;")
    connection.commit()

    return result