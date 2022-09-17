from flask import Flask, request, render_template, make_response
from flask_cors import CORS, cross_origin
import os
from functions.FileReader import readFile
from functions.StartUpDb import createAllTables
import sys
from functions.InsertIntoDb import insertEmployeesToDb
from functions.FilterFromDb import filterMinMax

app = Flask(__name__, static_folder='frontend/build', static_url_path='')
CORS(app)

@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
@cross_origin()
def uploadCSV():
    target=os.path.join("./",'test_docs')
    if not os.path.isdir(target):
        os.mkdir(target)
    file = request.files['file']
    filename = file.filename
    destination="/".join([target, filename])
    file.save(destination)
    try:
        employees = readFile(destination)
        createAllTables()
        insertEmployeesToDb(employees)
    except Exception as error:
        return make_response(str(error), 400)
    return make_response("Ok", 200)

@app.route('/createTables', methods=['POST'])
@cross_origin()
def createTables():
    print('creating tables',file=sys.stderr)
    createAllTables()
    return make_response("ok", 200)

@app.route('/users', methods=["GET"])
@cross_origin()
def getUsers():
    min = float(request.args.get("minSalary"))
    max = float(request.args.get("maxSalary"))
    order = request.args.get("sort")
    print(min, max, order)
    # if min == None or max == None or order == None:
    #     return make_response("Missing parameters detected.", 400)
    # if order == "+id":
    #     option = 1
    # elif order == "+name":
    #     option = 2
    # elif order == "+login":
    #     option = 3
    # elif order == "+salary":
    #     option = 4
    # elif order == "-id":
    #     option = 5
    # elif order == "-name":
    #     option = 6
    # elif order == "-login":
    #     option = 7
    # elif order == "-salary":
    #     option = 8
    # else:
    #     return make_response("Invalid sort parameters", 400)
    # results = filterMinMax(min, max, option)
    # employees = []
    # for employee in results:
    #     tmp = {}
    #     tmp['id'] = employee.id
    #     tmp['name'] = employee.name
    #     tmp['login'] = employee.login
    #     tmp['salary'] = employee.salary
    #     employees.append(tmp)
    response = {}
    # response['results'] = employees
    return response



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)