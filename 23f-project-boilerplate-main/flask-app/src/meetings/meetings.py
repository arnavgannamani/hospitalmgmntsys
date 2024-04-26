from flask import Blueprint, request, jsonify, make_response
from src import db

Appointment = Blueprint('Appointment', __name__)

# Get all appointment shifts
@Appointment.route('/Appointment', methods=['GET'])
def get_all_Appointments():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Appointment')
    row_headers = [x[0] for x in cursor.description]
    shifts = cursor.fetchall()
    json_data = [dict(zip(row_headers, shift)) for shift in shifts]
    return make_response(jsonify(json_data), 200)

# Get a single appointment shift by id
@Appointment.route('/Appointment/<int:shift_id>', methods=['GET'])
def get_Appointment(shift_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Appointment WHERE id = %s', (shift_id,))
    row_headers = [x[0] for x in cursor.description]
    shift = cursor.fetchone()
    if shift:
        return make_response(jsonify(dict(zip(row_headers, shift))), 200)
    else:
        return make_response(jsonify({"error": "Appointment shift not found"}), 404)

# Create a new appointment shift
@Appointment.route('/Appointment', methods=['POST'])
def create_Appointment():
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO Appointment (start_time, end_time, availability) VALUES (%s, %s, %s)',
                   (data['start_time'], data['end_time'], data['availability']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Appointment shift created successfully"}), 201)

# Update an appointment shift
@Appointment.route('/Appointment/<int:shift_id>', methods=['PUT'])
def update_Appointment(shift_id):
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE Appointment SET start_time = %s, end_time = %s, availability = %s WHERE id = %s',
                   (data['start_time'], data['end_time'], data['availability'], shift_id))
    db.get_db().commit()
    return make_response(jsonify({"message": "Appointment shift updated successfully"}), 200)

# Delete an appointment shift
@Appointment.route('/Appointment/<int:shift_id>', methods=['DELETE'])
def delete_Appointment(shift_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Appointment WHERE id = %s', (shift_id,))
    db.get_db().commit()
    return make_response(jsonify({"message": "Appointment shift deleted successfully"}), 200)
