import sqlite3
import pathlib
import pandas as pd
import matplotlib.pyplot as plt

# Define paths to database and SQL queries
db_file_path = pathlib.Path("project.db")
queries_folder = pathlib.Path("sql_queries")

def execute_sql_query(db_file_path, sql_file_path):
    try:
        with sqlite3.connect(db_file_path) as conn:
            with open(sql_file_path, 'r') as f:
                sql_query = f.read()
                print("Executing SQL query:", sql_query)  # Debugging output
                df = pd.read_sql_query(sql_query, conn)
                print("Query executed successfully")  # Debugging output
                return df
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")


import sqlite3
import pathlib
import pandas as pd
import matplotlib.pyplot as plt

# Define paths to database and SQL queries
db_file_path = pathlib.Path("project.db")
queries_folder = pathlib.Path("sql_queries")

# Function to execute a single SQL query and return the result as a DataFrame
def execute_sql_query(db_path, sql_query):
    try:
        with sqlite3.connect(db_path) as conn:
            df = pd.read_sql_query(sql_query, conn)
            print(f"Executed query successfully!")
            return df
    except sqlite3.Error as e:
        print(f"Error executing query: {e}")
        return None

# Function to read and split queries in the SQL file
def read_sql_file(sql_file_path):
    try:
        with open(sql_file_path, "r") as file:
            sql_query = file.read().strip()
            # Split the queries based on the semicolon delimiter
            queries = [query.strip() for query in sql_query.split(';') if query.strip()]
            return queries
    except Exception as e:
        print(f"Error reading SQL file {sql_file_path}: {e}")
        return []

# Function to plot the results of a query (for aggregation and grouping)
def plot_query_results(df, title):
    try:
        df.plot(kind='bar', x=df.columns[0], y=df.columns[1:], legend=True)
        plt.title(title)
        plt.xlabel(df.columns[0])
        plt.ylabel('Count')
        plt.show()
    except Exception as e:
        print(f"Error plotting results: {e}")

# Function to execute and display the query results
def execute_and_display_queries():
    # Run aggregation query
    aggregation_queries = read_sql_file(queries_folder.joinpath("query_aggregation.sql"))
    for query in aggregation_queries:
        agg_df = execute_sql_query(db_file_path, query)
        if agg_df is not None:
            print("\nAggregation Results:")
            print(agg_df)

    # Run filtering query
    filtering_queries = read_sql_file(queries_folder.joinpath("query_filter.sql"))
    for query in filtering_queries:
        filter_df = execute_sql_query(db_file_path, query)
        if filter_df is not None:
            print("\nFiltered Results:")
            print(filter_df)

    # Run sorting query
    sorting_queries = read_sql_file(queries_folder.joinpath("query_sorting.sql"))
    for query in sorting_queries:
        sort_df = execute_sql_query(db_file_path, query)
        if sort_df is not None:
            print("\nSorted Results:")
            print(sort_df)

    # Run grouping query
    grouping_queries = read_sql_file(queries_folder.joinpath("query_group_by.sql"))
    for query in grouping_queries:
        group_df = execute_sql_query(db_file_path, query)
        if group_df is not None:
            print("\nGrouped Results:")
            print(group_df)
            plot_query_results(group_df, "Number of Books Per Author")

    # Run join query
    joining_queries = read_sql_file(queries_folder.joinpath("query_join.sql"))
    for query in joining_queries:
        join_df = execute_sql_query(db_file_path, query)
        if join_df is not None:
            print("\nJoin Results:")
            print(join_df)

def main():
    execute_and_display_queries()

if __name__ == "__main__":
    main()
