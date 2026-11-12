def read_department_file(file_path):
    records = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                records.append((line_number, line.strip()))

        return records, None

    except (OSError, UnicodeDecodeError) as error:
        return [], f"{file_path.name}: {error}"