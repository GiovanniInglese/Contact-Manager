def get_valid_input(prompt, validation_func, error_message):
    while True:
        user_input = input(prompt).strip()
        if validation_func(user_input):
            return user_input
        print(error_message)



def is_valid_name(name):
    return len(name) > 0 and all(char.isalpha() or char.isspace() for char in name) and len(name) <= 50



def is_valid_phone(phone):
    return phone.isdigit()and len(phone) >= 7 and len(phone) <= 10 



def is_valid_email(email):
    email = email.strip()

    if "@" not in email:
        return False

    local_part, domain_part = email.split("@", 1)

    if not local_part or not domain_part:
        return False

    if "." not in domain_part:
        return False

    domain_name, extension = domain_part.rsplit(".", 1)

    if not domain_name or not extension:
        return False

    return True