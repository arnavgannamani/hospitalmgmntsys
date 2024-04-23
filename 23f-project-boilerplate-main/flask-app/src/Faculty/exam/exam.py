from flask import Blueprint, request, jsonify, make_response
from src import db

exam = Blueprint('exam', __name__)

# Get all exams
@exam.route('/exam', methods=['GET'])
def get_all_exams():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM exam')
    row_headers = [x[0] for x in cursor.description]
    exams = cursor.fetchall()
    json_data = [dict(zip(row_headers, exam)) for exam in exams]
    return make_response(jsonify(json_data), 200)

# Get a single exam by id
@exam.route('/exam/<int:exam_id>', methods=['GET'])
def get_exam(exam_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM exam WHERE id = %s', (exam_id,))
    row_headers = [x[0] for x in cursor.description]
    exam = cursor.fetchone()
    if exam:
        return make_response(jsonify(dict(zip(row_headers, exam))), 200)
    else:
        return make_response(jsonify({"error": "Exam not found"}), 404)

# Create a new exam
@exam.route('/exam', methods=['POST'])
def create_exam():
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO exam (name, date) VALUES (%s, %s)',
                   (data['name'], data['date']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Exam created successfully"}), 201)

# Update an exam
@exam.route('/exam/<int:exam_id>', methods=['PUT'])
def update_exam(exam_id):
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE exam SET name = %s, date = %s WHERE id = %s',
                   (data['name'], data['date'], exam_id))
    db.get_db().commit()
    return make_response(jsonify({"message": "Exam updated successfully"}), 200)

# Delete an exam
@exam.route('/exam/<int:exam_id>', methods=['DELETE'])
def delete_exam(exam_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM exam WHERE id = %s', (exam_id,))
    db.get_db().commit()
    return make_response(jsonify({"message": "Exam deleted successfully"}), 200)


exam_result = Blueprint('exam_result', __name__)

# Get all exam results
@exam_result.route('/exam-result', methods=['GET'])
def get_all_exam_results():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM exam_result')
    row_headers = [x[0] for x in cursor.description]
    results = cursor.fetchall()
    json_data = [dict(zip(row_headers, result)) for result in results]
    return make_response(jsonify(json_data), 200)

# Get a single exam result by id
@exam_result.route('/exam-result/<int:result_id>', methods=['GET'])
def get_exam_result(result_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM exam_result WHERE id = %s', (result_id,))
    row_headers = [x[0] for x in cursor.description]
    result = cursor.fetchone()
    if result:
        return make_response(jsonify(dict(zip(row_headers, result))), 200)
    else:
        return make_response(jsonify({"error": "Exam result not found"}), 404)

# Create a new exam result
@exam_result.route('/exam-result', methods=['POST'])
def create_exam_result():
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO exam_result (exam_id, student_id, marks) VALUES (%s, %s, %s)',
                   (data['exam_id'], data['student_id'], data['marks']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Exam result created successfully"}), 201)

# Update an exam result
@exam_result.route('/exam-result/<int:result_id>', methods=['PUT'])
def update_exam_result(result_id):
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE exam_result SET exam_id = %s, student_id = %s, marks = %s WHERE id = %s',
                   (data['exam_id'], data['student_id'], data['marks'], result_id))
    db.get_db().commit()
    return make_response(jsonify({"message": "Exam result updated successfully"}), 200)