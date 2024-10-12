import csv
from cs50 import SQL

# SQL command to create the people table
#CREATE TABLE people (
    #id INTEGER PRIMARY KEY AUTOINCREMENT,
    #names TEXT UNIQUE
#);

# Open database
db = SQL("sqlite:///cl_madrid_2024_eliminatoria.db")

# List of tables to insert data from
#tables = ["eliminatoria_adulto", "eliminatoria_juvenil", "eliminatoria_single_a","eliminatoria_single_b"]  # Replace these with your actual table names

tables = ["people_separated"]

# Loop over each table and insert names into 'people'
for table in tables:
    try:
        # Execute the INSERT INTO ... SELECT query
        db.execute("INSERT OR IGNORE INTO people (names) SELECT names FROM ?", table)
        print(f"Names from '{table}' inserted into 'people'.")
    except Exception as e:
        # Handle the exception (e.g., log it or print an error message)
        print(f"Error inserting from '{table}': {e}")

print(f"Completed insertion from {len(tables)} tables.")
