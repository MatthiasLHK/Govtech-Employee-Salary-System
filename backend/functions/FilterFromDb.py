from functions.StartDbConnection import startConnection
from functions.Employee import Employee

def filterMinMax(min, max, option):
    conn = startConnection()
    cursor = conn.cursor()
    if option == 1:
        query = f"SELECT * FROM Employees WHERE salary >= {min} AND salary <= {max} ORDER BY id ASC, name ASC, login ASC, salary ASC LIMIT 30"
    elif option == 2:
        query = f"SELECT * FROM Employees WHERE salary >= {min} AND salary <= {max} ORDER BY name ASC, id ASC, login ASC, salary ASC LIMIT 30"
    elif option == 3:
        query = f"SELECT * FROM Employees WHERE salary >= {min} AND salary <= {max} ORDER BY login ASC, id ASC, name ASC, salary ASC LIMIT 30"
    elif option == 4:
        query = f"SELECT * FROM Employees WHERE salary >= {min} AND salary <= {max} ORDER BY salary ASC, id ASC, name ASC, login ASC LIMIT 30"
    elif option == 5:
        query = f"SELECT * FROM Employees WHERE salary >= {min} AND salary <= {max} ORDER BY id DESC, name ASC, login ASC, salary ASC LIMIT 30"
    elif option == 6:
        query = f"SELECT * FROM Employees WHERE salary >= {min} AND salary <= {max} ORDER BY name DESC, id ASC, login ASC, salary ASC LIMIT 30"
    elif option == 7:
        query = f"SELECT * FROM Employees WHERE salary >= {min} AND salary <= {max} ORDER BY login DESC, id ASC, name ASC, salary ASC LIMIT 30"
    elif option == 8:
        query = f"SELECT * FROM Employees WHERE salary >= {min} AND salary <= {max} ORDER BY salary DESC, id ASC, name ASC, login ASC LIMIT 30"
    else:
        raise Exception("Invalid sorting order detected.")
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        employees = []
        for entry in data:
            employee = Employee(list(entry))
            employees.append(employee)
        conn.commit()
        conn.close()
        return employees
    except:
        raise Exception("Error trying to get all employees that fit the min and max salary.")