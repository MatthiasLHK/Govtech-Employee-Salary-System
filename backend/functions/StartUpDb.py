from tabnanny import check
from functions.StartDbConnection import startConnection
import sys

def createAllTables():
    conn = startConnection()
    cursor = conn.cursor()
    isCreated = checkTableExists(cursor)
    print(f"Table exists: {isCreated}", file=sys.stderr)
    if isCreated == False:
        createEmployeesTable(cursor)
        print("Tables created", file=sys.stderr)
    else:
        print("Tables already exists", file=sys.stderr)
    conn.commit()
    conn.close()
    

def createEmployeesTable(cursor):
    print("Creating Employess table", file=sys.stderr)
    query = "DROP TABLE IF EXISTS Employees"
    cursor.execute(query)
    query2 = "CREATE TABLE Employees (id VARCHAR(255) PRIMARY KEY, login VARCHAR(255) UNIQUE NOT NULL, name VARCHAR(255), salary DECIMAL)"
    try:
        cursor.execute(query2)
    except:
        raise Exception("Error trying to create Employees table")

def checkTableExists(cursor):
    print("Creating Employess table", file=sys.stderr)
    print("Checking if employees table exists", file=sys.stderr)
    query = "SELECT EXISTS (SELECT FROM pg_tables WHERE schemaname = 'public' AND tablename  = 'employees');"
    cursor.execute(query)
    value = cursor.fetchall()[0][0]
    print(value, file=sys.stderr)
    if value == False:
        return False
    else:
        return True
