import json


FILE_NAME = "contacts.json"

def load_contacts_from_file(file_name=FILE_NAME):
    try:
        with open(file_name, 'r') as file:
            contacts = json.load(file)
            return contacts
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Corrupted contacts file. Starting with an empty contact list.")
        return []




def save_contacts_to_file(contacts, file_name=FILE_NAME):
    with open(file_name, 'w') as file:
        json.dump(contacts, file, indent=4)