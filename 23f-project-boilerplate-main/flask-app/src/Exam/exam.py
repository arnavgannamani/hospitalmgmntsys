from flask import Blueprint, request, jsonify, make_response
from src import db

Exam = Blueprint('Exam', __name__)

# Get all Exams
@Exam.route('/Exam', methods=['GET'])
def get_all_Exams():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Exam')
    row_headers = [x[0] for x in cursor.description]
    Exams = cursor.fetchall()
    json_data = [dict(zip(row_headers, Exam)) for Exam in Exams]
    return make_response(jsonify(json_data), 200)

# Get a single Exam by id
@Exam.route('/Exam/<int:examID>', methods=['GET'])
def get_Exam(examID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Exam WHERE id = %s', (examID,))
    row_headers = [x[0] for x in cursor.description]
    Exam = cursor.fetchone()
    if Exam:
        return make_response(jsonify(dict(zip(row_headers, Exam))), 200)
    else:
        return make_response(jsonify({"error": "Exam not found"}), 404)

# Create a new Exam
@Exam.route('/Exam', methods=['POST'])
def create_Exam():
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO Exam (name, date) VALUES (%s, %s)',
                   (data['name'], data['date']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Exam created successfully"}), 201)

# Update an Exam
@Exam.route('/Exam/<int:examID>', methods=['PUT'])
def update_Exam(examID):
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE Exam SET name = %s, date = %s WHERE id = %s',
                   (data['name'], data['date'], examID))
    db.get_db().commit()
    return make_response(jsonify({"message": "Exam updated successfully"}), 200)

# Delete an Exam
@Exam.route('/Exam/<int:examID>', methods=['DELETE'])
def delete_Exam(examID):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Exam WHERE id = %s', (examID,))
    db.get_db().commit()
    return make_response(jsonify({"message": "Exam deleted successfully"}), 200)


Exam_result = Blueprint('Exam_result', __name__)

# Get all Exam results
@Exam_result.route('/examResultID', methods=['GET'])
def get_all_Exam_results():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Exam_result')
    row_headers = [x[0] for x in cursor.description]
    results = cursor.fetchall()
    json_data = [dict(zip(row_headers, result)) for result in results]
    return make_response(jsonify(json_data), 200)

# Get a single Exam result by id
@Exam_result.route('/examResultID/<int:result_id>', methods=['GET'])
def get_Exam_result(result_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Exam_result WHERE id = %s', (result_id,))
    row_headers = [x[0] for x in cursor.description]
    result = cursor.fetchone()
    if result:
        return make_response(jsonify(dict(zip(row_headers, result))), 200)
    else:
        return make_response(jsonify({"error": "Exam result not found"}), 404)

# Create a new Exam result
@Exam_result.route('/examResultID', methods=['POST'])
def create_Exam_result():
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO Exam_result (examID, student_id, marks) VALUES (%s, %s, %s)',
                   (data['examID'], data['student_id'], data['marks']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Exam result created successfully"}), 201)

# Update an Exam result
@Exam_result.route('/examResultID/<int:result_id>', methods=['PUT'])
def update_Exam_result(result_id):
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE Exam_result SET examID = %s, student_id = %s, marks = %s WHERE id = %s',
                   (data['examID'], data['student_id'], data['marks'], result_id))
    db.get_db().commit()
    return make_response(jsonify({"message": "Exam result updated successfully"}), 200)