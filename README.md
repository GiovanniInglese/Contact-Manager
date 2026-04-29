# Contact Manager / Intake System

A Python-based contact and intake management application built step by step to practice modern software development concepts.

This project started as a command-line contact manager and evolved into a database-backed Flask web application with validation, CRUD functionality, and automated testing.

## Features

- View all contacts
- Add new contacts
- Edit existing contacts
- Delete contacts
- Search contacts
- Input validation for name, phone, and email
- SQLite database persistence
- Flask web interface
- Automated tests with pytest

## Tech Stack

- Python
- Flask
- SQLite
- pytest
- HTML

## Project Progression

This project was built through multiple stages to strengthen software engineering skills:

1. Basic Python CLI contact manager
2. File-based persistence with JSON
3. Refactor into a multi-file modular project
4. Add automated tests
5. Replace JSON storage with SQLite
6. Build a Flask web interface

## Project Structure

```text
contact-manager/
├── app.py
├── database.py
├── contact_services.py
├── validators.py
├── test_database.py
├── test_file_handler.py
├── test_validators.py
├── templates/
│   ├── index.html
│   ├── add_contact.html
│   └── edit_contact.html
├── README.md
└── .gitignore