from file_handler import save_contacts_to_file

from validators import get_valid_input, is_valid_name, is_valid_phone, is_valid_email



def create_contact(contacts, name, phone, email):
    contact ={
        "name": name, 
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    save_contacts_to_file(contacts)
    return contact



def add_contact(contacts):


    name = get_valid_input("Enter contact name: ", is_valid_name, "Invalid name. Please enter a valid name (only letters and spaces, max 50 characters).")
    phone = get_valid_input("Enter contact phone number: ", is_valid_phone, "Invalid phone number. Please enter a valid phone number (only digits, 7-10 characters).")
    email = get_valid_input("Enter contact email: ", is_valid_email, "Invalid email. Please enter a valid email address.")

    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contact = create_contact(contacts, name, phone, email)
    print(f"Contact '{name}' added successfully!")




def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContacts:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")  



def remove_contact_by_index(contacts, index):
    if index < 0 or index >= len(contacts):
        return None

    deleted_contact = contacts.pop(index)
    save_contacts_to_file(contacts)
    return deleted_contact



def delete_contact(contacts):
    if not contacts:
        print("No contacts to delete.")
        return

    view_contacts(contacts)
    index = get_valid_input("Enter the number of the contact to delete: ", lambda x: x.isdigit() and 1 <= int(x) <= len(contacts), "Invalid input. Please enter a valid contact number.")
    index = int(index) - 1
    deleted_contact = remove_contact_by_index(contacts, index)
    print(f"Contact '{deleted_contact['name']}' deleted successfully!")



def update_contact(contact, new_name=None, new_phone=None, new_email=None):
    if new_name and is_valid_name(new_name):
        contact['name'] = new_name
    if new_phone and is_valid_phone(new_phone):
        contact['phone'] = new_phone
    if new_email and is_valid_email(new_email):
        contact['email'] = new_email
    return contact



def edit_contact(contacts):
    if not contacts:
        print("No contacts to edit.")
        return

    view_contacts(contacts)
    index = get_valid_input("Enter the number of the contact to edit: ", lambda x: x.isdigit() and 1 <= int(x) <= len(contacts), "Invalid input. Please enter a valid contact number.")
    index = int(index) - 1
    contact = contacts[index]

    print(f"Editing contact '{contact['name']}' (leave blank to keep current value):")
    new_name = input("Enter new name: ").strip()
    new_phone = input("Enter new phone number: ").strip()
    new_email = input("Enter new email: ").strip()

    if new_name:
        if is_valid_name(new_name):
            contact['name'] = new_name
        else:
            print("Invalid name. Keeping current name.")
    
    if new_phone:
        if is_valid_phone(new_phone):
            contact['phone'] = new_phone
        else:
            print("Invalid phone number. Keeping current phone number.")
    
    if new_email:
        if is_valid_email(new_email):
            contact['email'] = new_email
        else:
            print("Invalid email. Keeping current email.")

    update_contact(contact, new_name=new_name, new_phone=new_phone, new_email=new_email)
    save_contacts_to_file(contacts)
    print(f"Contact '{contact['name']}' updated successfully!")



def find_contacts(contacts, search_term):
    search_term = search_term.strip().lower()
    return [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]

def search_contacts(contacts):
    if not contacts:
        print("No contacts to search.")
        return

    search_term = input("Enter name or phone number to search: ").strip().lower()
    found_contacts = find_contacts(contacts, search_term)


    if not found_contacts:
        print("No contacts found matching the search term.")
    else:
        print("\nSearch Results:")
        for idx, contact in enumerate(found_contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")