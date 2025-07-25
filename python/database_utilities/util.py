import sqlite3
import csv
import importlib
from types import ModuleType

def execute_script_from_file(connection: sqlite3.Connection, path: str) -> bool:
    result: bool = True

    with open(path, "r") as file:
        script = file.read()
        connection.executescript(script)
    
    return result

def load_rows_from_csv(file_path: str) -> list[tuple]:
    result: list[tuple] = []

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        result = [tuple(row.values()) for row in reader]
    
    return result

def seed_from_csv(connection: sqlite3.Connection, sql_query: str, csv_path: str,) -> bool:
    result: bool = True

    rows = load_rows_from_csv(csv_path)

    connection.executemany(sql_query, rows)

    connection.commit()

    return result

def import_migration_module(version: str, suffix: str) -> ModuleType:
    path: str = f"python.migrations.{version}.{suffix}"
    result: ModuleType = importlib.import_module(path)
    return result

def import_seed_module(version: str, suffix: str) -> ModuleType:
    path: str = f"python.seed.{version}.{suffix}"
    result: ModuleType = importlib.import_module(path)
    return result