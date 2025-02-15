import sqlite3
import pathlib
import pandas as pd
import matplotlib.pyplot as plt

# Define paths to database and SQL queries
db_file_path = pathlib.Path("project.db")
queries_folder = pathlib.Path("sql_queries")

def verify_table_columns(db_file_path):
    with sqlite3.connect(db_file_path) as conn:
        cursor = conn.execute("PRAGMA table_info(authors);")
        columns = cursor.fetchall()
        print("Authors table columns:", columns)  # Debugging output

