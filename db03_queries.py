import sqlite3
import pathlib
import pandas as pd
import matplotlib.pyplot as plt

# Define paths to database and SQL queries
db_file_path = pathlib.Path("project.db")
queries_folder = pathlib.Path("sql_queries")

# Function to execute a query and return the result as a DataFrame
def execute_sql_query(db_path, sql_file_path):
    try:
        with sqlite3.connect(db_path) as conn:
            with open(sql_file_path, "r") as file:
                sql_query = file.read()
            df = pd.read_sql_query(sql_query, conn)
            print(f"Executed {sql_file_path.name} query successfully!")
            return df
    except sqlite3.Error as e:
        print(f"Error executing {sql_file_path.name}: {e}")
        return None

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
    agg_df = execute_sql_query(db_file_path, queries_folder.joinpath("query_aggregation.sql"))
    if agg_df is not None:
        print("\nAggregation Results:")
        print(agg_df)

    # Run filtering query
    filter_df = execute_sql_query(db_file_path, queries_folder.joinpath("query_filter.sql"))
    if filter_df is not None:
        print("\nFiltered Results:")
        print(filter_df)

    # Run sorting query
    sort_df = execute_sql_query(db_file_path, queries_folder.joinpath("query_sorting.sql"))
    if sort_df is not None:
        print("\nSorted Results:")
        print(sort_df)

    # Run grouping query
    group_df = execute_sql_query(db_file_path, queries_folder.joinpath("query_group_by.sql"))
    if group_df is not None:
        print("\nGrouped Results:")
        print(group_df)
        plot_query_results(group_df, "Number of Books Per Author")

    # Run join query
    join_df = execute_sql_query(db_file_path, queries_folder.joinpath("query_join.sql"))
    if join_df is not None:
        print("\nJoin Results:")
        print(join_df)

def main():
    execute_and_display_queries()

if __name__ == "__main__":
    main()
