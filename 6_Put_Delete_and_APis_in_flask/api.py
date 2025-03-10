from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial data for the to-do list
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

# Home route
@app.route('/')
def home():
    return "Welcome to the sample to-do list app"

# GET: Retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET: Retrieve a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

# POST: Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json or 'description' not in request.json:
        return jsonify({"error": "Invalid input"}), 400

    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item), 201

# PUT: Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404

    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])

    return jsonify(item)

# DELETE: Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": "Item deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)


#=======================================================================================================================

'''
📦 1. Import libraries:

from flask import Flask, jsonify, request
Flask: The core web framework used to create the API.
jsonify: Converts Python dictionaries or lists into JSON responses.
request: Allows you to access incoming HTTP request data (like form data or JSON payloads).

🏠 2. Initialize Flask app:
app = Flask(__name__)
This line initializes the Flask app by creating an instance of the Flask class.
__name__ tells Flask where to look for resources (like templates or static files).
📋 3. Sample data (to-do list items):
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]
A simple in-memory list of dictionaries representing to-do items.
Each item contains:
id: Unique identifier for the item.
name: Name of the to-do task.
description: A short explanation of the task.

🌟 4. Routes:
Home route:
@app.route('/')
def home():
    return "Welcome to the sample to-do list app"
@app.route('/'): Maps the root URL (http://localhost:5000/) to the home() function.
When someone visits this route, the text "Welcome to the sample to-do list app" is displayed in their browser.
Retrieve all items (GET):

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)
URL: /items
Method: GET
Purpose: Returns the full list of to-do items as JSON.
jsonify(items) converts the Python list into JSON format so it can be sent as a response.
Example output:

[
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]
Retrieve a single item by ID (GET):

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)
URL: /items/<item_id>
Method: GET
Purpose: Finds an item by its id and returns it.
<int:item_id>: A variable route that expects an integer, e.g., /items/1.
next(): Iterates through the items list to find the item with the matching id.
If the item doesn’t exist, it returns a 404 error.
Otherwise, it sends the item in JSON format.
Example output:

{"id": 1, "name": "Item 1", "description": "This is item 1"}
Create a new item (POST):

@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json or 'description' not in request.json:
        return jsonify({"error": "Invalid input"}), 400

    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item), 201
URL: /items
Method: POST
Purpose: Adds a new item to the list.
Input:
The request must have JSON data with:

{
  "name": "Item 3",
  "description": "This is item 3"
}
Validation:
If the request is missing name or description, it returns a 400 error.
ID assignment:
The new item’s id is calculated by adding 1 to the last item’s ID (items[-1]["id"] + 1).
Response:
Returns the newly added item with a 201 Created status.
Example output:


{
    "id": 3,
    "name": "Item 3",
    "description": "This is item 3"
}
Update an item (PUT):

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404

    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])

    return jsonify(item)
URL: /items/<item_id>
Method: PUT
Purpose: Updates the name or description of an item by its id.
Input:
You can send partial data:

{
  "name": "Updated Item 1"
}
get(): Safely gets the new values from the request JSON or keeps the old ones.
Response:
Returns the updated item.
Example output:


{
    "id": 1,
    "name": "Updated Item 1",
    "description": "This is item 1"
}
Delete an item (DELETE):

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": "Item deleted"}), 200
URL: /items/<item_id>
Method: DELETE
Purpose: Removes an item from the list by its id.
Global keyword: Needed to modify the items list.
Response:
Returns a confirmation message.
Example output:


{
    "result": "Item deleted"
}

🔥 5. Running the app:

if __name__ == "__main__":
    app.run(debug=True)
app.run(debug=True) starts the Flask development server.
debug=True:
Auto-reloads the server if you change the code.
Shows detailed error messages.

✅ Testing the API:
You can test the endpoints using:

Postman — Great for sending POST, PUT, and DELETE requests.
Curl commands:

# Get all items
curl -X GET http://localhost:5000/items

# Add a new item
curl -X POST -H "Content-Type: application/json" \
-d '{"name": "Item 3", "description": "This is item 3"}' \
http://localhost:5000/items '''