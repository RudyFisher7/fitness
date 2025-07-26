import sqlite3
import python.database_utilities.util as util

def upgrade(connection: sqlite3.Connection) -> bool:
    result: bool = True

    result = util.seed_from_csv(
        connection,
        '''
        INSERT INTO routine (time_started, duration_seconds, name, description, user_id)
        VALUES (?, ?, ?, ?, ?);
        ''',
        "data/seed_routine.csv",
    )

    return result


def downgrade(connection: sqlite3.Connection) -> bool:
    result: bool = True

    connection.execute("DELETE FROM routine;")
    connection.commit()

    return result