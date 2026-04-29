from database import(
    initialize_database,
    add_contact_db,
    get_all_contacts,
    search_contacts_db,
    delete_contact_db,
    update_contact_db,
    get_contact_by_id

)


def test_add_contact_and_get_all_contacts(tmp_path):
    test_db = tmp_path / "test_contacts.db"
    initialize_database(test_db)

    add_contact_db("Alice", "1234567890", "alice@example.com", test_db)

    contacts = get_all_contacts(test_db)

    assert len(contacts) == 1
    assert contacts[0][1] == "Alice"
    assert contacts[0][2] == "1234567890"
    assert contacts[0][3] == "alice@example.com"


def test_search_contacts_db_by_name(tmp_path):
    test_db = tmp_path/ "test_contacts.db"
    initialize_database(test_db)

    add_contact_db("Alice Smith", "1234567890", "alice@example.com", test_db)
    add_contact_db("Bob Johnson", "9876543210", "bob@example.com", test_db)

    results = search_contacts_db("Alice", test_db)

    assert len(results) == 1
    assert results[0][1] == "Alice Smith"
    assert results[0][2] == "1234567890"
    assert results[0][3] == "alice@example.com"


def test_search_contacts_db_by_phone(tmp_path):
    test_db = tmp_path / "test_contacts.db"
    initialize_database(test_db)

    add_contact_db("Alice Smith", "1234567890", "alice@example.com", test_db)
    add_contact_db("Bob Johnson", "9876543210", "bob@xample.com", test_db)

    results = search_contacts_db("1234567890", test_db)

    assert len(results) == 1
    assert results[0][1] == "Alice Smith"
    assert results[0][2] == "1234567890"
    assert results[0][3] == "alice@example.com"


def test_get_contact_by_id(tmp_path):
    test_db = tmp_path / "test_contacts.db"
    initialize_database(test_db)

    add_contact_db("Alice Smith", "1234567890", "alice@example.com", test_db)

    contact = get_contact_by_id(1, test_db)

    assert contact is not None
    assert contact[1] == "Alice Smith"
    assert contact[2] == "1234567890"
    assert contact[3] == "alice@example.com"


def test_delete_contact_db_valid_id(tmp_path):
    test_db = tmp_path / "test_contacts.db"
    initialize_database(test_db)

    add_contact_db("Alice Smith", "1234567890", "alice@example.com", test_db)

    contacts = get_all_contacts(test_db)
    contact_id = contacts[0][0]

    was_deleted = delete_contact_db(contact_id, test_db)
    remaining_contacts = get_all_contacts(test_db)
    assert was_deleted is True
    assert len(remaining_contacts) == 0


def test_delete_contact_db_invalid_id(tmp_path):
    test_db = tmp_path / "test_contacts.db"
    initialize_database(test_db)

    add_contact_db("Alice Smith", "1234567890", "alice@example.com", test_db)


    was_deleted = delete_contact_db(999, test_db)
    contacts = get_all_contacts(test_db)
    assert was_deleted is False
    assert len(contacts) == 1


def test_update_contact_db_valid_id(tmp_path):
    test_db = tmp_path / "test_contacts.db"
    initialize_database(test_db)

    add_contact_db("Alice Smith", "1234567890", "alice@example.com", test_db)
    contacts = get_all_contacts(test_db)
    contact_id = contacts[0][0]
    was_updated = update_contact_db(contact_id, "Alice Johnson", "0987654321", "newemail@gmail.com", test_db)

    updated_contact = get_contact_by_id(contact_id, test_db)
    assert was_updated is True
    assert updated_contact[1] == "Alice Johnson"
    assert updated_contact[2] == "0987654321"
    assert updated_contact[3] == "newemail@gmail.com"


def test_update_contact_db_invalid_id(tmp_path):
    test_db = tmp_path / "test_contacts.db"
    initialize_database(test_db)

    add_contact_db("Alice Smith", "1234567890", "alice@example.com", test_db)

    contacts = get_all_contacts(test_db)
    was_updated = update_contact_db(999, "Alice Johnson", "0987654321", "new@example.com", test_db)
    assert was_updated is False
    assert contacts[0][1] == "Alice Smith"