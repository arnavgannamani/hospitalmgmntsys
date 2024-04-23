from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


patient = Blueprint('patient', __name__)

# Get all patient from the DB
@patient.route('/patient', methods=['GET'])
def get_patient():
    cursor = db.get_db().cursor()
    cursor.execute('select company, last_name,\
        first_name, job_title, business_phone from patient')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# get one patient
@patient.route('/patient/<patientID>', methods=['GET'])
def get_customer(patientID):
    cursor = db.get_db().cursor()
    cursor.execute('select * from customers where id = {0}'.format(patientID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@patient.route('/product', methods=['POST'])
def add_new_product():
    
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    firstName = the_data['firstName']
    lastName = the_data['lastName']
    gender = the_data['']
    tel_number= the_data['product_category']
    email = the_data['email']
    insurance = the_data['insurance']
    emmergencyContact = the_data['emergencyContact']
    

    # Constructing the query
    query = 'insert into products (firstName, lastName, gender, tel_number, email, insurance) values ("'
    query += firstName + '", "'
    query += lastName+ '", "'
    query += gender + '", '
    query += tel_number + '", '
    query += email+ '", '
    query += insurance+ '", '
    query += str(emmergencyContact) + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'
@patient.route('/patient/patientID>', methods=['PUT'])
def update_patient(patientID):
    # Collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    # Extracting variables
    firstName = the_data.get('firstName')
    lastName = the_data.get('lastName')
    gender = the_data.get('gender')
    tel_number = the_data.get('tel_number')
    email = the_data.get('email')
    insurance = the_data.get('insurance')
    emergencyContact = the_data.get('emergencyContact')

    # Constructing the query
    query = 'UPDATE patient SET '
    query += 'firstName = "{}", '.format(firstName) if firstName else ''
    query += 'lastName = "{}", '.format(lastName) if lastName else ''
    query += 'gender = "{}", '.format(gender) if gender else ''
    query += 'tel_number = "{}", '.format(tel_number) if tel_number else ''
    query += 'email = "{}", '.format(email) if email else ''
    query += 'insurance = "{}", '.format(insurance) if insurance else ''
    query += 'emergencyContact = "{}", '.format(emergencyContact) if emergencyContact else ''
    
    # Remove the trailing comma and space
    query = query.rstrip(', ')
    
    # Adding the WHERE clause
    query += ' WHERE id = {}'.format(patientID)

    current_app.logger.info(query)

    # Executing and committing the update statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Success!'

person = Blueprint('person', __name__)

# Get all persons
@person.route('/person', methods=['GET'])
def get_all_persons():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM person')
    row_headers = [x[0] for x in cursor.description]
    persons = cursor.fetchall()
    json_data = [dict(zip(row_headers, person)) for person in persons]
    return make_response(jsonify(json_data), 200)

# Get a single person by id
@person.route('/person/<int:person_id>', methods=['GET'])
def get_person(person_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM person WHERE id = %s', (person_id,))
    row_headers = [x[0] for x in cursor.description]
    person = cursor.fetchone()
    if person:
        return make_response(jsonify(dict(zip(row_headers, person))), 200)
    else:
        return make_response(jsonify({"error": "Person not found"}), 404)

# Create a new person
@person.route('/person', methods=['POST'])
def create_person():
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO person (first_name, last_name, age) VALUES (%s, %s, %s)',
                   (data['first_name'], data['last_name'], data['age']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Person created successfully"}), 201)

# Update a person
@person.route('/person/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE person SET first_name = %s, last_name = %s, age = %s WHERE id = %s',
                   (data['first_name'], data['last_name'], data['age'], person_id))
    db.get_db().commit()
    return make_response(jsonify({"message": "Person updated successfully"}), 200)

# Delete a person
@person.route('/person/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM person WHERE id = %s', (person_id,))
    db.get_db().commit()
    return make_response(jsonify({"message": "Person deleted successfully"}), 200)