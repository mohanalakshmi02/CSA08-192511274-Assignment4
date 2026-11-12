class InvalidRegistration(Exception):
    pass


def validate_email(email):
    if email.count("@") != 1:
        return False

    if any(character.isspace() for character in email):
        return False

    username, domain = email.split("@")

    if not username or not domain:
        return False

    if "." not in domain:
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    return True


def parse_registration(line):
    parts = line.split(",")

    if len(parts) != 5:
        raise InvalidRegistration("Expected exactly 5 fields")

    register_number, name, department, email, events = (
        part.strip() for part in parts
    )

    if not all([register_number, name, department, email, events]):
        raise InvalidRegistration("One or more fields are empty")

    if not validate_email(email):
        raise InvalidRegistration("Invalid email address")

    event_list = [event.strip() for event in events.split(";")]

    if not all(event_list):
        raise InvalidRegistration("Invalid or empty event name")

    event_list = list(dict.fromkeys(event_list))

    return {
        "register_number": register_number,
        "name": name,
        "department": department,
        "email": email,
        "events": event_list
    }