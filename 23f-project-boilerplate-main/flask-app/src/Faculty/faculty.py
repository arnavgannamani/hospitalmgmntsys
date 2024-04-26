from flask import Blueprint, request, jsonify, make_response
from src import db

faculty = Blueprint('faculty', __name__)

# Get all faculties
@faculty.route('/faculty', methods=['GET'])
def get_all_faculties():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM faculty')
    row_headers = [x[0] for x in cursor.description]
    faculties = cursor.fetchall()
    json_data = [dict(zip(row_headers, faculty)) for faculty in faculties]
    return make_response(jsonify(json_data), 200)

# Get a single faculty by id
@faculty.route('/faculty/<int:employeeID>', methods=['GET'])
def get_faculty(employeeID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM faculty WHERE id = %s', (employeeID,))
    row_headers = [x[0] for x in cursor.description]
    faculty = cursor.fetchone()
    if faculty:
        return make_response(jsonify(dict(zip(row_headers, faculty))), 200)
    else:
        return make_response(jsonify({"error": "Faculty not found"}), 404)

# Create a new faculty
@faculty.route('/faculty', methods=['POST'])
def create_faculty():
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO faculty (name, department) VALUES (%s, %s)',
                   (data['name'], data['department']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Faculty created successfully"}), 201)

# Update a faculty
@faculty.route('/faculty/<int:employeeID>', methods=['PUT'])
def update_faculty(employeeID):
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE faculty SET name = %s, department = %s WHERE id = %s',
                   (data['name'], data['department'], employeeID))
    db.get_db().commit()
    return make_response(jsonify({"message": "Faculty updated successfully"}), 200)

# Delete a faculty
@faculty.route('/faculty/<int:employeeID>', methods=['DELETE'])
def delete_faculty(employeeID):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM faculty WHERE id = %s', (employeeID,))
    db.get_db().commit()
    return make_response(jsonify({"message": "Faculty deleted successfully"}), 200)


doctor = Blueprint('doctor', __name__)

# Get all doctors
@doctor.route('/doctor', methods=['GET'])
def get_all_doctors():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM doctor')
    row_headers = [x[0] for x in cursor.description]
    doctors = cursor.fetchall()
    json_data = [dict(zip(row_headers, doctor)) for doctor in doctors]
    return make_response(jsonify(json_data), 200)

# Get a single doctor by id
@doctor.route('/doctor/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM doctor WHERE id = %s', (doctor_id,))
    row_headers = [x[0] for x in cursor.description]
    doctor = cursor.fetchone()
    if doctor:
        return make_response(jsonify(dict(zip(row_headers, doctor))), 200)
    else:
        return make_response(jsonify({"error": "Doctor not found"}), 404)

# Create a new doctor
@doctor.route('/doctor', methods=['POST'])
def create_doctor():
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO doctor (name, specialty) VALUES (%s, %s)',
                   (data['name'], data['specialty']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Doctor created successfully"}), 201)

# Update a doctor
@doctor.route('/doctor/<int:doctor_id>', methods=['PUT'])
def update_doctor(doctor_id):
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE doctor SET name = %s, specialty = %s WHERE id = %s',
                   (data['name'], data['specialty'], doctor_id))
    db.get_db().commit()
    return make_response(jsonify({"message": "Doctor updated successfully"}), 200)

# Delete a doctor
@doctor.route('/doctor/<int:doctor_id>', methods=['DELETE'])
def delete_doctor(doctor_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM doctor WHERE id = %s', (doctor_id,))
    db.get_db().commit()
    return make_response(jsonify({"message": "Doctor deleted successfully"}), 200)