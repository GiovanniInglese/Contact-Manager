from contact_services import add_contact_db_interactive,view_contacts_db,search_contacts_db_interactive,delete_contact_db_interactive, edit_contact_db_interactive
from database import initialize_database



def display_menu():
    print("\nContact Manager Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Delete Contact")
    print("5. Edit Contact")
    print("6. Exit")







def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact_db_interactive()
        elif choice == "2":
            view_contacts_db()
        elif choice == "3":
            search_contacts_db_interactive()
        elif choice == "4":
            delete_contact_db_interactive()
        elif choice == "5":
            edit_contact_db_interactive()
        elif choice == "6":
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

