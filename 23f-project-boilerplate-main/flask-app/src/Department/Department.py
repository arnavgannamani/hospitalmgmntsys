from flask import Blueprint, request, jsonify, make_response
from src import db

# Blueprint for managing Departments
Department = Blueprint('Department', __name__)

# Get all Departments
@Department.route('/departments', methods=['GET'])
def get_all_departments():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM department')
    row_headers = [x[0] for x in cursor.description]
    departments = cursor.fetchall()
    json_data = [dict(zip(row_headers, department)) for department in departments]
    return make_response(jsonify(json_data), 200)

# Get a single Department by id
@Department.route('/departments/<int:department_id>', methods=['GET'])
def get_department(department_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM department WHERE id = %s', (department_id,))
    row_headers = [x[0] for x in cursor.description]
    department = cursor.fetchone()
    if department:
        return make_response(jsonify(dict(zip(row_headers, department))), 200)
    else:
        return make_response(jsonify({"error": "Department not found"}), 404)

# Create a new Department
@Department.route('/departments', methods=['POST'])
def create_department():
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO department (name, location) VALUES (%s, %s)',
                   (data['name'], data['location']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Department created successfully"}), 201)

# Update a Department
@Department.route('/departments/<int:department_id>', methods=['PUT'])
def update_department(department_id):
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE department SET name = %s, location = %s WHERE id = %s',
                   (data['name'], data['location'], department_id))
    db.get_db().commit()
    return make_response(jsonify({"message": "Department updated successfully"}), 200)

# Delete a Department
@Department.route('/departments/<int:department_id>', methods=['DELETE'])
def delete_department(department_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM department WHERE id = %s', (department_id,))
    db.get_db().commit()
    return make_response(jsonify({"message": "Department deleted successfully"}), 200)


# Blueprint for managing DepartmentFinancial
DepartmentFinancial = Blueprint('DepartmentFinancial', __name__)

# Get all DepartmentFinancial
@DepartmentFinancial.route('/department_financials', methods=['GET'])
def get_all_department_financials():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM department_financial')
    row_headers = [x[0] for x in cursor.description]
    department_financials = cursor.fetchall()
    json_data = [dict(zip(row_headers, department_financial)) for department_financial in department_financials]
    return make_response(jsonify(json_data), 200)

# Get a single DepartmentFinancial by id
@DepartmentFinancial.route('/department_financials/<int:department_financial_id>', methods=['GET'])
def get_department_financial(department_financial_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM department_financial WHERE id = %s', (department_financial_id,))
    row_headers = [x[0] for x in cursor.description]
    department_financial = cursor.fetchone()
    if department_financial:
        return make_response(jsonify(dict(zip(row_headers, department_financial))), 200)
    else:
        return make_response(jsonify({"error": "Department Financial not found"}), 404)

# Create a new DepartmentFinancial
@DepartmentFinancial.route('/department_financials', methods=['POST'])
def create_department_financial():
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO department_financial (department_id, budget) VALUES (%s, %s)',
                   (data['department_id'], data['budget']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Department Financial created successfully"}), 201)

# Update a DepartmentFinancial
@DepartmentFinancial.route('/department_financials/<int:department_financial_id>', methods=['PUT'])
def update_department_financial(department_financial_id):
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE department_financial SET department_id = %s, budget = %s WHERE id = %s',
                   (data['department_id'], data['budget'], department_financial_id))
    db.get_db().commit()
    return make_response(jsonify({"message": "Department Financial updated successfully"}), 200)

# Delete a DepartmentFinancial
@DepartmentFinancial.route('/department_financials/<int:department_financial_id>', methods=['DELETE'])
def delete_department_financial(department_financial_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM department_financial WHERE id = %s', (department_financial_id,))
    db.get_db().commit()
    return make_response(jsonify({"message": "Department Financial deleted successfully"}), 200)
