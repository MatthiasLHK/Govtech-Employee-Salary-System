import sys
from functions.StartDbConnection import startConnection

def insertEmployeesToDb(employees):
    conn = startConnection()
    cursor = conn.cursor()
    print("Inserting into Employess table", file=sys.stderr)
    for employee in employees:
        print(employee.name,file=sys.stderr)
        insertQuery = f"INSERT INTO Employees (id, login, name, salary) VALUES ('{employee.id}', '{employee.login}', '{employee.name}', {employee.salary})"
        updateQuery = f"UPDATE Employees SET id = '{employee.id}', login = '{employee.login}', name = '{employee.name}', salary = {employee.salary} WHERE id = '{employee.id}'"
        exists = checkIfEmployeeExists(cursor, employee.id)
        if exists:
            print("User already exists", file=sys.stderr)
            cursor.execute(updateQuery)
        else:
            print("Creating new user", file=sys.stderr)
            cursor.execute(insertQuery)
    conn.commit()
    conn.close()
        

def checkIfEmployeeExists(cursor, id):
    print(id,file=sys.stderr)
    query = f"SELECT 1 FROM Employees WHERE id = '{id}'"
    cursor.execute(query)
    value = cursor.fetchall()
    print(value,file=sys.stderr)
    print(len(value),file=sys.stderr)
    if len(value) == 0:
        return False
    else:
        return True


