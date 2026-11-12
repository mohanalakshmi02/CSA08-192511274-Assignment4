from .reader import read_department_file
from .validator import parse_registration, InvalidRegistration


def process_department_files(file_paths):
    master_list = []
    event_participants = {}
    errors = []
    seen_registers = set()

    for file_path in file_paths:
        lines, file_error = read_department_file(file_path)

        if file_error:
            errors.append(file_error)
            continue

        for line_number, line in lines:
            if not line:
                continue

            try:
                student = parse_registration(line)

                register_number = student["register_number"]

                if register_number in seen_registers:
                    errors.append(
                        f"{file_path.name}, line {line_number}: "
                        f"Duplicate registration {register_number}"
                    )
                    continue

                seen_registers.add(register_number)
                master_list.append(student)

                for event in student["events"]:
                    event_participants.setdefault(event, []).append(student)

            except InvalidRegistration as error:
                errors.append(
                    f"{file_path.name}, line {line_number}: {error}"
                )

    return master_list, event_participants, errors