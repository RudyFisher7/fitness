import sqlite3

def execute_script_from_file(connection: sqlite3.Connection, path: str) -> bool:
    result: bool = True

    with open(path, "r") as file:
        script = file.read()
        connection.executescript(script)
    
    return result