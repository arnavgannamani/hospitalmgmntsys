from flask import Blueprint, request, jsonify, make_response
from src import db

# Blueprint for managing Items
Item = Blueprint('Item', __name__)

# Get all Items
@Item.route('/items', methods=['GET'])
def get_all_items():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Item')
    row_headers = [x[0] for x in cursor.description]
    items = cursor.fetchall()
    json_data = [dict(zip(row_headers, item)) for item in items]
    return make_response(jsonify(json_data), 200)

# Get a single Item by id
@Item.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Item WHERE id = %s', (item_id,))
    row_headers = [x[0] for x in cursor.description]
    item = cursor.fetchone()
    if item:
        return make_response(jsonify(dict(zip(row_headers, item))), 200)
    else:
        return make_response(jsonify({"error": "Item not found"}), 404)

# Create a new Item
@Item.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO Item (name, price) VALUES (%s, %s)',
                   (data['name'], data['price']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Item created successfully"}), 201)

# Update an Item
@Item.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE Item SET name = %s, price = %s WHERE id = %s',
                   (data['name'], data['price'], item_id))
    db.get_db().commit()
    return make_response(jsonify({"message": "Item updated successfully"}), 200)

# Delete an Item
@Item.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Item WHERE id = %s', (item_id,))
    db.get_db().commit()
    return make_response(jsonify({"message": "Item deleted successfully"}), 200)


# Blueprint for managing Department Items
Department_Item = Blueprint('Department_Item', __name__)

# Get all Department Items
@Department_Item.route('/department_items', methods=['GET'])
def get_all_department_items():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM department_item')
    row_headers = [x[0] for x in cursor.description]
    department_items = cursor.fetchall()
    json_data = [dict(zip(row_headers, department_item)) for department_item in department_items]
    return make_response(jsonify(json_data), 200)

# Get a single Department Item by id
@Department_Item.route('/department_items/<int:department_item_id>', methods=['GET'])
def get_department_item(department_item_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM department_item WHERE id = %s', (department_item_id,))
    row_headers = [x[0] for x in cursor.description]
    department_item = cursor.fetchone()
    if department_item:
        return make_response(jsonify(dict(zip(row_headers, department_item))), 200)
    else:
        return make_response(jsonify({"error": "Department Item not found"}), 404)

# Create a new Department Item
@Department_Item.route('/department_items', methods=['POST'])
def create_department_item():
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO department_item (name, quantity) VALUES (%s, %s)',
                   (data['name'], data['quantity']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Department Item created successfully"}), 201)

# Update a Department Item
@Department_Item.route('/department_items/<int:department_item_id>', methods=['PUT'])
def update_department_item(department_item_id):
    data = request.get_json()
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE department_item SET name = %s, quantity = %s WHERE id = %s',
                   (data['name'], data['quantity'], department_item_id))
    db.get_db().commit()
    return make_response(jsonify({"message": "Department Item updated successfully"}), 200)

# Delete a Department Item
@Department_Item.route('/department_items/<int:department_item_id>', methods=['DELETE'])
def delete_department_item(department_item_id):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM department_item WHERE id = %s', (department_item_id,))
    db.get_db().commit()
    return make_response(jsonify({"message": "Department Item deleted successfully"}), 200)