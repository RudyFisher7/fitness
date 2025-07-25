import sqlite3
import python.database_utilities.util as util

def upgrade(connection: sqlite3.Connection) -> bool:
    result: bool = True

    result = util.seed_from_csv(
        connection,
        '''
        INSERT INTO exercise_demo (exercise_id, cues, video_url)
        VALUES (?, ?, ?);
        ''',
        "data/seed_exercise_demo.csv",
    )

    return result


def downgrade(connection: sqlite3.Connection) -> bool:
    result: bool = True

    connection.execute("DELETE FROM exercise_demo;")
    connection.commit()

    return result