import sqlite3
import python.database_utilities.util as util

def upgrade(connection: sqlite3.Connection) -> bool:
    result: bool = True

    result = util.seed_from_csv(
        connection,
        '''
        INSERT INTO user (display_name, first_name, last_name, date_of_birth)
        VALUES (?, ?, ?, ?);
        ''',
        "data/seed_user.csv",
    )

    return result


def downgrade(connection: sqlite3.Connection) -> bool:
    result: bool = True

    connection.execute("DELETE FROM user;")
    connection.commit()

    return result