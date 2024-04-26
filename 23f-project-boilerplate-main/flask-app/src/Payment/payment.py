from flask import Blueprint, request, jsonify, make_response
from src import db

# Blueprint for managing Bills
Bill = Blueprint('Bill', __name__)

# Get all Bills
@Bill.route('/bills', methods=['GET'])
def get_all_bills():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM bills')
    row_headers = [x[0] for x in cursor.description]
    bills = cursor.fetchall()
    json_data = [dict(zip(row_headers, bill)) for bill in bills]
    return make_response(jsonify(json_data), 200)

# Get a single Bill by id
@Bill.route('/bills/<int:bill_id>', methods=['GET'])
def get_bill(bill_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM bills WHERE id = %s', (bill_id,))
    row_headers = [x[0] for x in cursor.description]
    bill = cursor.fetchone()
    if bill:
        return make_response(jsonify(dict(zip(row_headers, bill))), 200)
    else:
        return make_response(jsonify({"error": "Bill not found"}), 404)

# Create a new Bill
@Bill.route('/bills', methods=['POST'])
def create_bill():
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO bills (amount, due_date) VALUES (%s, %s)',
                   (data['amount'], data['due_date']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Bill created successfully"}), 201)

# Update a Bill
@Bill.route('/bills/<int:bill_id>', methods=['PUT'])
def update_bill(bill_id):
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE bills SET amount = %s, due_date = %s WHERE id = %s',
                   (data['amount'], data['due_date'], bill_id))
    db.get_db().commit()
    return make_response(jsonify({"message": "Bill updated successfully"}), 200)

# Delete a Bill
@Bill.route('/bills/<int:bill_id>', methods=['DELETE'])
def delete_bill(bill_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM bills WHERE id = %s', (bill_id,))
    db.get_db().commit()
    return make_response(jsonify({"message": "Bill deleted successfully"}), 200)


# Blueprint for managing Insurance
Insurance = Blueprint('Insurance', __name__)

# Get all Insurances
@Insurance.route('/insurances', methods=['GET'])
def get_all_insurances():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM insurance')
    row_headers = [x[0] for x in cursor.description]
    insurances = cursor.fetchall()
    json_data = [dict(zip(row_headers, insurance)) for insurance in insurances]
    return make_response(jsonify(json_data), 200)

# Get a single Insurance by id
@Insurance.route('/insurances/<int:insurance_id>', methods=['GET'])
def get_insurance(insurance_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM insurance WHERE id = %s', (insurance_id,))
    row_headers = [x[0] for x in cursor.description]
    insurance = cursor.fetchone()
    if insurance:
        return make_response(jsonify(dict(zip(row_headers, insurance))), 200)
    else:
        return make_response(jsonify({"error": "Insurance not found"}), 404)

# Create a new Insurance
@Insurance.route('/insurances', methods=['POST'])
def create_insurance():
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO insurance (provider, premium) VALUES (%s, %s)',
                   (data['provider'], data['premium']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Insurance created successfully"}), 201)

# Update an Insurance
@Insurance.route('/insurances/<int:insurance_id>', methods=['PUT'])
def update_insurance(insurance_id):
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE insurance SET provider = %s, premium = %s WHERE id = %s',
                   (data['provider'], data['premium'], insurance_id))
    db.get_db().commit()
    return make_response(jsonify({"message": "Insurance updated successfully"}), 200)

# Delete an Insurance
@Insurance.route('/insurances/<int:insurance_id>', methods=['DELETE'])
def delete_insurance(insurance_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM insurance WHERE id = %s', (insurance_id,))
    db.get_db().commit()
    return make_response(jsonify({"message": "Insurance deleted successfully"}), 200)