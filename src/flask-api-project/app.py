import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
employees = [
    {'id': 1, 'name': 'Ashley'},
    {'id': 2, 'name': 'Kate'},
    {'id': 3, 'name': 'Joe'}
]

nextEmployeeId = 4

# Helper function to get employee by ID
def get_employee(emp_id):
    return next((e for e in employees if e['id'] == emp_id), None)

# Helper function to validate employee
def employee_is_valid(employee):
    return 'name' in employee

# GET all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

# GET employee by ID
@app.route('/employees/<int:emp_id>', methods=['GET'])
def get_employee_by_id(emp_id):
    employee = get_employee(emp_id)
    if employee is None:
        return jsonify({'error': 'Employee does not exist'}), 404
    return jsonify(employee)

# POST (create employee)
@app.route('/employees', methods=['POST'])
def create_employee():
    global nextEmployeeId

    employee = request.get_json()

    if not employee or not employee_is_valid(employee):
        return jsonify({'error': 'Invalid employee data'}), 400

    employee['id'] = nextEmployeeId
    nextEmployeeId += 1

    employees.append(employee)

    return jsonify(employee), 201

# PUT (update employee)
@app.route('/employees/<int:emp_id>', methods=['PUT'])
def update_employee(emp_id):
    employee = get_employee(emp_id)

    if employee is None:
        return jsonify({'error': 'Employee does not exist'}), 404

    updated_data = request.get_json()

    if not updated_data or not employee_is_valid(updated_data):
        return jsonify({'error': 'Invalid data'}), 400

    employee.update(updated_data)

    return jsonify(employee)

# DELETE employee
@app.route('/employees/<int:emp_id>', methods=['DELETE'])
def delete_employee(emp_id):
    global employees

    employee = get_employee(emp_id)

    if employee is None:
        return jsonify({'error': 'Employee does not exist'}), 404

    employees = [e for e in employees if e['id'] != emp_id]

    return jsonify({'message': 'Employee deleted successfully'})

# Run app
if __name__ == "__main__":
    app.run(port=5000, debug=True)