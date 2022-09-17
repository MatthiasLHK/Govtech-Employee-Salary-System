from functions.Employee import Employee
import sys

def readFile(filepath):
    file = open(filepath, "r")
    lines = file.readlines()
    line_count = 0
    employees = []
    for line in lines:
        line = line.strip()
        entry = line.split(',')
        if line_count == 0:
            line_count += 1
            continue
        if entry[0][0] == "#":
            line_count += 1
            continue
        try:
            employee = Employee(entry[0], entry[1], entry[2], float(entry[3]))
            employees.append(employee)
            line_count += 1
        except:
            raise Exception(f"Invalid entry [{entry}], please follow this format the each row: id, login, name, salary")
    print(employees, file=sys.stderr)
    return employees

# readFile("C:\\Users\\dracu\OneDrive\\Desktop\\GovTech TAP Assessment\\govtech-employee\\test\\test.csv")