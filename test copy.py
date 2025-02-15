import sqlite3
import pathlib
import pandas as pd
import matplotlib.pyplot as plt

# Define paths to database and SQL queries
db_file_path = pathlib.Path("project.db")
queries_folder = pathlib.Path("sql_queries")

def read_sql_file(sql_file_path):
    try:
        with open(sql_file_path, 'r') as f:
            sql_query = f.read()
            print("SQL Query from file:", sql_query)  # Debugging output
            return sql_query
    except FileNotFoundError:
        print(f"Error: {sql_file_path} not found.")


