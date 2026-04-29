from database import add_contact_db, get_all_contacts , search_contacts_db, delete_contact_db, update_contact_db, get_contact_by_id
from validators import get_valid_input, is_valid_name, is_valid_phone, is_valid_email

# Database functions
def create_contact_db(name, phone, email):
    add_contact_db(name, phone, email)


def display_contacts_list(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContacts:")
        for contact in contacts:
            contact_id, name, phone, email = contact
            print(f"ID: {contact_id}, Name: {name}, Phone: {phone}, Email: {email}")



def view_contacts_db():
    contacts = get_all_contacts()
    if not contacts:
        print("No contacts found.")
        return

    display_contacts_list(contacts)


def add_contact_db_interactive():
    name = get_valid_input("Enter contact name: ", is_valid_name, "Invalid name. Please enter a valid name (only letters and spaces, max 50 characters).")
    phone = get_valid_input("Enter contact phone number: ", is_valid_phone, "Invalid phone number. Please enter a valid phone number (only digits, 7-10 characters).")
    email = get_valid_input("Enter contact email: ", is_valid_email, "Invalid email. Please enter a valid email address.")

    create_contact_db(name, phone, email)
    print(f"Contact '{name}' added successfully to the database!")



def search_contacts_db_interactive():
    search_term = input("Enter name or phone number to search: ").strip().lower()
    results = search_contacts_db(search_term)
    
    if not results:
        print("No contacts found matching the search term.")
    else:
        print(f"\nSearch results for '{search_term}':")
        display_contacts_list(results)



def delete_contact_db_interactive():
    while True:
        contacts = get_all_contacts()

        if not contacts:
            print("No contacts to delete.")
            return
        
        display_contacts_list(contacts)

       

        contact_id = input("Enter the ID of the contact to delete: ").strip()

        if not contact_id.isdigit():
            print("Invalid ID. Please enter a valid number.")
            continue

        was_deleted = delete_contact_db(int(contact_id))

        if was_deleted:
            print("Contact deleted successfully.")
            break
        else:
            print("No contact found with that ID. Please try again.")



def edit_contact_db_interactive():
    while True:
        contacts = get_all_contacts()

        if not contacts:
            print("No contacts to edit.")
            return
        
        display_contacts_list(contacts)

        

        contact_id = input("Enter the ID of the contact to edit: ").strip()

        if not contact_id.isdigit():
            print("Invalid ID. Please enter a valid number.")
            continue

        contact_id = int(contact_id)
        contact = get_contact_by_id(contact_id)

        if not contact:
            print("No contact found with that ID. Please try again.")
            continue

        _, current_name, current_phone, current_email = contact

        print("\nLeave blank to keep the current value.")
        new_name = input(f"Enter new name [{current_name}]: ").strip()
        new_phone = input(f"Enter new phone [{current_phone}]: ").strip()
        new_email = input(f"Enter new email [{current_email}]: ").strip()

        final_name = current_name
        final_phone = current_phone
        final_email = current_email

        if new_name:
            if is_valid_name(new_name):
                final_name = new_name
            else:
                print("Invalid name. Keeping current name.")

        if new_phone:
            if is_valid_phone(new_phone):
                final_phone = new_phone
            else:
                print("Invalid phone number. Keeping current phone.")

        if new_email:
            if is_valid_email(new_email):
                final_email = new_email
            else:
                print("Invalid email. Keeping current email.")

        was_updated = update_contact_db(contact_id, final_name, final_phone, final_email)

        if was_updated:
            print("Contact updated successfully.")
            break
        else:
            print("Update failed. Please try again.")