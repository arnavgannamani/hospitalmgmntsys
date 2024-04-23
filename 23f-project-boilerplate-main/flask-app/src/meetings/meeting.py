from flask import Blueprint, request, jsonify, make_response
from src import db

appointment_shift = Blueprint('appointment_shift', __name__)

# Get all appointment shifts
@appointment_shift.route('/appointment-shift', methods=['GET'])
def get_all_appointment_shifts():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM appointment_shift')
    row_headers = [x[0] for x in cursor.description]
    shifts = cursor.fetchall()
    json_data = [dict(zip(row_headers, shift)) for shift in shifts]
    return make_response(jsonify(json_data), 200)

# Get a single appointment shift by id
@appointment_shift.route('/appointment-shift/<int:shift_id>', methods=['GET'])
def get_appointment_shift(shift_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM appointment_shift WHERE id = %s', (shift_id,))
    row_headers = [x[0] for x in cursor.description]
    shift = cursor.fetchone()
    if shift:
        return make_response(jsonify(dict(zip(row_headers, shift))), 200)
    else:
        return make_response(jsonify({"error": "Appointment shift not found"}), 404)

# Create a new appointment shift
@appointment_shift.route('/appointment-shift', methods=['POST'])
def create_appointment_shift():
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO appointment_shift (start_time, end_time, availability) VALUES (%s, %s, %s)',
                   (data['start_time'], data['end_time'], data['availability']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Appointment shift created successfully"}), 201)

# Update an appointment shift
@appointment_shift.route('/appointment-shift/<int:shift_id>', methods=['PUT'])
def update_appointment_shift(shift_id):
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE appointment_shift SET start_time = %s, end_time = %s, availability = %s WHERE id = %s',
                   (data['start_time'], data['end_time'], data['availability'], shift_id))
    db.get_db().commit()
    return make_response(jsonify({"message": "Appointment shift updated successfully"}), 200)

# Delete an appointment shift
@appointment_shift.route('/appointment-shift/<int:shift_id>', methods=['DELETE'])
def delete_appointment_shift(shift_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM appointment_shift WHERE id = %s', (shift_id,))
    db.get_db().commit()
    return make_response(jsonify({"message": "Appointment shift deleted successfully"}), 200)
