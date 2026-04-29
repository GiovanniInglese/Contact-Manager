from flask import Flask, render_template, request, redirect, url_for
from database import initialize_database, get_all_contacts, add_contact_db, search_contacts_db, delete_contact_db, update_contact_db
from validators import is_valid_name, is_valid_phone, is_valid_email
from contact_services import get_contact_by_id
app = Flask(__name__)


@app.route("/")
def index():
    contacts = get_all_contacts()
    return render_template("index.html", contacts=contacts)


@app.route("/add", methods=["GET", "POST"])
def add_contact():
    error = None
    name = ""
    phone = ""
    email = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        email = request.form.get("email", "").strip()

        if not is_valid_name(name):
            error = "Invalid name. Please use only letters and spaces."
        elif not is_valid_phone(phone):
            error = "Invalid phone number. Please enter 7 to 10 digits."
        elif not is_valid_email(email):
            error = "Invalid email address."
        else:
            add_contact_db(name, phone, email)
            return redirect(url_for("index"))

    return render_template(
        "add_contact.html",
        error=error,
        name=name,
        phone=phone,
        email=email
    )

@app.route("/delete/<int:contact_id>", methods=["POST"])
def delete_contact(contact_id):
    delete_contact_db(contact_id)
    return redirect(url_for("index"))

@app.route("/edit/<int:contact_id>", methods=["GET", "POST"])
def edit_contact(contact_id):
    contact = get_contact_by_id(contact_id)

    if not contact:
        return redirect(url_for("index"))

    _, current_name, current_phone, current_email = contact
    error = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        email = request.form.get("email", "").strip()

        if not is_valid_name(name):
            error = "Invalid name. Please use only letters and spaces."
        elif not is_valid_phone(phone):
            error = "Invalid phone number. Please enter 7 to 10 digits."
        elif not is_valid_email(email):
            error = "Invalid email address."
        else:
            update_contact_db(contact_id, name, phone, email)
            return redirect(url_for("index"))

        return render_template(
            "edit_contact.html",
            contact_id=contact_id,
            name=name,
            phone=phone,
            email=email,
            error=error
        )

    return render_template(
        "edit_contact.html",
        contact_id=contact_id,
        name=current_name,
        phone=current_phone,
        email=current_email,
        error=error
    )





if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)

