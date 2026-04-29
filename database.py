import sqlite3

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



    connection.commit()
    connection.close()


def add_contact_db(name, phone, email, db_name=DB_NAME):
    connection = create_connection(db_name)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO contacts (name, phone, email)
        VALUES (?, ?, ?)
    """, (name, phone, email))

    connection.commit()
    connection.close()



def get_all_contacts(db_name=DB_NAME):
    connection = create_connection(db_name)
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, phone, email FROM contacts")
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
        SELECT id, name, phone, email FROM contacts
        WHERE name LIKE ? OR phone LIKE ?
    """, (f"%{search_term.lower()}%", f"%{search_term}%"))

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


def update_contact_db(contact_id, name, phone, email, db_name=DB_NAME):
    connection = create_connection(db_name)
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE contacts
        SET name = ?, phone = ?, email = ?
        WHERE id = ?
    """, (name, phone, email, contact_id))

    connection.commit()
    updated_count = cursor.rowcount
    connection.close()
    return updated_count > 0


def get_contact_by_id(contact_id, db_name=DB_NAME):
    connection = create_connection(db_name)
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, phone, email FROM contacts WHERE id = ?", (contact_id,))
    contact = cursor.fetchone()
    connection.close()
    return contact
