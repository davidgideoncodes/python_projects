"""
test_api.py

Tests the REST API defined in 04_rest_api.py by exercising every endpoint:
GET, POST, GET by id, PUT, and DELETE.

Usage:
    1. Run the API first, in its own terminal:
       python 04_rest_api.py
    2. In a second terminal, run this script:
       pip install requests
       python test_api.py
"""

import requests

BASE_URL = "http://127.0.0.1:5000"


def show(label, response):
    print(f"\n--- {label} ---")
    print(f"Status code: {response.status_code}")
    print("Response body:")
    print(response.json())


# 1. GET all notes
response = requests.get(f"{BASE_URL}/notes")
show("GET all notes", response)

# 2. POST a new note
new_note = {
    "title": "My first API note",
    "content": "Built with Flask"
}
response = requests.post(f"{BASE_URL}/notes", json=new_note)
show("POST new note", response)

created_id = response.json()["id"]

# 3. GET that note back
response = requests.get(f"{BASE_URL}/notes/{created_id}")
show(f"GET note {created_id}", response)

# 4. PUT - update the note's title
update_data = {"title": "Updated title"}
response = requests.put(f"{BASE_URL}/notes/{created_id}", json=update_data)
show(f"PUT update note {created_id}", response)

# 5. DELETE the note
response = requests.delete(f"{BASE_URL}/notes/{created_id}")
show(f"DELETE note {created_id}", response)

# 6. GET all notes again to confirm the delete worked
response = requests.get(f"{BASE_URL}/notes")
show("GET all notes (after delete)", response)