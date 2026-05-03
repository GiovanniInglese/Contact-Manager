import sqlite3
from datetime import datetime

DB_NAME = "contacts.db"


def create_connection(db_name=DB_NAME):
    return sqlite3.connect(db_name)


def initialize_database(db_name=DB_NAME):
    connection = create_connection(db_name)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    cursor.execute("PRAGMA table_info(contacts)")
    columns = [column[1] for column in cursor.fetchall()]

    if "status" not in columns:
        cursor.execute("ALTER TABLE contacts ADD COLUMN status TEXT DEFAULT 'New'")

    if "record_date" not in columns:
        cursor.execute("ALTER TABLE contacts ADD COLUMN record_date TEXT")

    if "notes" not in columns:
        cursor.execute("ALTER TABLE contacts ADD COLUMN notes TEXT DEFAULT ''")

    current_date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
        UPDATE contacts
        SET record_date = ?
        WHERE record_date IS NULL OR record_date = ''
    """, (current_date,))

    connection.commit()
    connection.close()


def add_contact_db(name, phone, email, status="New", notes="", db_name=DB_NAME):
    connection = create_connection(db_name)
    cursor = connection.cursor()

    record_date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
        INSERT INTO contacts (name, phone, email, status, record_date, notes)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, phone, email, status, record_date, notes))

    connection.commit()
    connection.close()

def get_all_contacts(db_name=DB_NAME):
    connection = create_connection(db_name)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, phone, email, status, record_date, notes
        FROM contacts
        ORDER BY id DESC
    """)

    contacts = cursor.fetchall()
    connection.close()
    return contacts


if __name__ == "__main__":
    initialize_database()

    add_contact_db("Alice", "1234567890", "alice@example.com")
    add_contact_db("Bob", "9876543210", "bob@example.com")

    contacts = get_all_contacts()
    print(contacts)    


def search_contacts_db(search_term, db_name=DB_NAME):
    connection = create_connection(db_name)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, phone, email, status, record_date, notes
        FROM contacts
        WHERE LOWER(name) LIKE ?
           OR phone LIKE ?
           OR LOWER(email) LIKE ?
           OR LOWER(status) LIKE ?
           OR LOWER(notes) LIKE ?
        ORDER BY id DESC
    """, (
        f"%{search_term.lower()}%",
        f"%{search_term}%",
        f"%{search_term.lower()}%",
        f"%{search_term.lower()}%",
        f"%{search_term.lower()}%"
    ))

    results = cursor.fetchall()
    connection.close()
    return results

def delete_contact_db(contact_id,db_name=DB_NAME):
    connection = create_connection(db_name)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))

    connection.commit()
    deleted_count = cursor.rowcount
    connection.close()
    return deleted_count > 0


def update_contact_db(contact_id, name, phone, email, status, notes, db_name=DB_NAME):
    connection = create_connection(db_name)
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE contacts
        SET name = ?, phone = ?, email = ?, status = ?, notes = ?
        WHERE id = ?
    """, (name, phone, email, status, notes, contact_id))

    connection.commit()
    updated_count = cursor.rowcount
    connection.close()

    return updated_count > 0


def get_contact_by_id(contact_id, db_name=DB_NAME):
    connection = create_connection(db_name)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, phone, email, status, record_date, notes
        FROM contacts
        WHERE id = ?
    """, (contact_id,))

    contact = cursor.fetchone()
    connection.close()
    return contact
