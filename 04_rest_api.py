"""
04_rest_api.py

A REST API for managing notes, built with Flask.

Features:
- GET    /notes        -> list all notes
- GET    /notes/<id>   -> get a single note
- POST   /notes        -> create a new note
- PUT    /notes/<id>   -> update an existing note
- DELETE /notes/<id>   -> delete a note

Data is currently stored in memory (a Python list), so it resets whenever
the server restarts. The next step for this project is replacing the list
with a SQLite database, following the same approach used in the todo app
in this repo.

Setup:
    pip install flask
    python 04_rest_api.py

The server runs at http://127.0.0.1:5000

Example requests (using Python's requests library, see test_api.py):
    GET    /notes
    POST   /notes        with JSON body {"title": "...", "content": "..."}
    PUT    /notes/<id>   with JSON body {"title": "..."} and/or {"content": "..."}
    DELETE /notes/<id>
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# ---------------------------------------------------------------------------
# In-memory data store: a list of note dictionaries.
# Each note looks like: {"id": 1, "title": "...", "content": "..."}
# ---------------------------------------------------------------------------
notes = [
    {"id": 1, "title": "Welcome", "content": "This is the first note."},
    {"id": 2, "title": "Learning REST", "content": "GET reads, POST creates, PUT updates, DELETE removes."},
]

# Tracks the next id to assign to a new note.
next_id = 3


def find_note(note_id):
    """Return the note with the given id, or None if it doesn't exist."""
    for note in notes:
        if note["id"] == note_id:
            return note
    return None


# ---------------------------------------------------------------------------
# GET /notes - list every note
# ---------------------------------------------------------------------------
@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes), 200


# ---------------------------------------------------------------------------
# GET /notes/<id> - get a single note by id
# ---------------------------------------------------------------------------
@app.route("/notes/<int:note_id>", methods=["GET"])
def get_note(note_id):
    note = find_note(note_id)
    if note is None:
        return jsonify({"error": f"No note found with id {note_id}"}), 404
    return jsonify(note), 200


# ---------------------------------------------------------------------------
# POST /notes - create a new note
# ---------------------------------------------------------------------------
@app.route("/notes", methods=["POST"])
def create_note():
    global next_id

    data = request.get_json(silent=True)
    if not data or "title" not in data:
        return jsonify({"error": "Request must include a 'title' field"}), 400

    new_note = {
        "id": next_id,
        "title": data["title"],
        "content": data.get("content", ""),
    }
    notes.append(new_note)
    next_id += 1

    return jsonify(new_note), 201


# ---------------------------------------------------------------------------
# PUT /notes/<id> - update an existing note
# ---------------------------------------------------------------------------
@app.route("/notes/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    note = find_note(note_id)
    if note is None:
        return jsonify({"error": f"No note found with id {note_id}"}), 404

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request must include JSON data"}), 400

    if "title" in data:
        note["title"] = data["title"]
    if "content" in data:
        note["content"] = data["content"]

    return jsonify(note), 200


# ---------------------------------------------------------------------------
# DELETE /notes/<id> - delete a note
# ---------------------------------------------------------------------------
@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    note = find_note(note_id)
    if note is None:
        return jsonify({"error": f"No note found with id {note_id}"}), 404

    notes.remove(note)
    return jsonify({"message": f"Note {note_id} deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)