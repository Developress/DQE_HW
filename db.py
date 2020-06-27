import csv
import sqlite3
import sys

# set the connection to database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Project;")

# create the first table with appropriate columns
cursor.execute("CREATE TABLE IF NOT EXISTS Project ("
               "name text,"
               "description text,"
               "deadline date)")

cursor.execute("DROP TABLE IF EXISTS Tasks;")

# create the second table with appropriate columns
cursor.execute("CREATE TABLE IF NOT EXISTS Tasks ("
               "id integer NOT NULL,"
               "priority integer,"
               "details text,"
               "status text,"
               "deadline date,"
               "completed date,"
               "project text)")

# first command line argument is the file with data for the first table
with open(sys.argv[1]) as f:
    # read csv file
    reader = csv.DictReader(f)
    for row in reader:
        # read row by row and insert values to database
        cursor.execute(f"INSERT INTO Project (name, description, deadline) VALUES ('{row['name']}', "
                       f"'{row['description']}', {row['deadline']});")

# second command line argument is the file with data for the second table
with open(sys.argv[2]) as f:
    # read csv file
    reader = csv.DictReader(f)
    for row in reader:
        # read row by row and insert values to database
        cursor.execute(f"INSERT INTO Tasks (id, priority, details, status, deadline, completed, project)"
                       f"VALUES ({row['id']}, {row['priority']}, '{row['details']}',"
                       f"'{row['status']}', {row['deadline']}, {row['completed']},'{row['project']}');")

# enter parameter for select query
name = input("Enter name of project:")

cursor.execute(f"SELECT * FROM Tasks "
               f"WHERE project = '{name}';")

# display results
for line in cursor.fetchall():
    print(line)

conn.commit()
conn.close()
