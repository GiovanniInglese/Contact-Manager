
from file_handler import load_contacts_from_file, save_contacts_to_file

def test_save_and_load_contacts(tmp_path):
    test_file = tmp_path / "test_contacts.json"

    test_contacts = [
        {"name": "Alice", "phone": "1234567890", "email": "alice@example.com"}
    ]

    # Save contacts to the temporary file
    save_contacts_to_file(test_contacts, test_file)

    # Load contacts from the temporary file
    loaded_contacts = load_contacts_from_file(test_file)

    # Assert that the loaded contacts match the expected contacts
    assert loaded_contacts == test_contacts

def test_load_missing_file_returns_empty_list(tmp_path):
    test_file = tmp_path / "non_existent_file.json"

    # Load contacts from a non-existent file
    loaded_contacts = load_contacts_from_file(test_file)

    # Assert that the loaded contacts is an empty list
    assert loaded_contacts == []


def test_load_invalid_json_returns_empty_list(tmp_path):
    test_file = tmp_path / "invalid_contacts.json"

    # Create a file with invalid JSON content
    with open(test_file, 'w') as file:
        file.write("This is not valid JSON")

    # Load contacts from the file with invalid JSON
    loaded_contacts = load_contacts_from_file(test_file)

    # Assert that the loaded contacts is an empty list
    assert loaded_contacts == []
