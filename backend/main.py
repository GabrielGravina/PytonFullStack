# localhost:5000/create_contact

# Request has a type: GET, POST, PATCH, DELETE...
# We can pass JSON data. For example, we can pass what contact we want to delete.
# Back-End returns a Responde. It has a status.

from flask import request, jsonify
from config import app, db
from models import Contact

@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)