from flask import request, jsonify
from config import app, db
from models import Notes


@app.route("/", methods=["GET"])
def get_notes():
    notes = Notes.query.all()
    json_notes = list(map(lambda x: x.to_json(), notes))
    return jsonify({"notes": json_notes})

@app.route("/<int:id>", methods=["GET"])
def get_note_detail(id):
    note = Notes.query.get(id)
    json_note = note.to_json
    return jsonify({"note": json_note})

@app.route("/create", methods=["POST"])
def create_notes():
    title = request.json.get("title")
    details = request.json.get("details")
    category = request.json.get("category")
    
    if not title or not details:
        return(
            jsonify({"message": "You must include a title and an email"}), 400,
        )
    
    new_note = Notes(title = title, details = details, category = category)

    try:
        db.session.add(new_note)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "Note created!"}), 201
    

@app.route("/update/<int:id>", methods=["PUT"])
def update(id):
    note = Notes.query.get(id)

    if not note:
        return jsonify({"message": "Note not found"}), 404
    
    data = request.json
    note.title = data.get("title", note.title)
    note.details = data.get("details", note.details)
    note.category = data.get("category", note.category)

    db.session.commit()

    return jsonify({"message": "Note updated"})

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    note = Notes.query.get(id)

    if not note:
        return jsonify({"message": "Note not found"}), 404
    
    db.session.delete(note)
    db.session.commit()

    return jsonify({"message": "Note deleted!"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)