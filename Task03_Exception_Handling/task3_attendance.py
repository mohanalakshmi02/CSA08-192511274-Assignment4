import os
import tempfile


class InvalidRecord(Exception):
    """Raised when an attendance record is invalid."""


def parse_line(line):
    parts = line.strip().split(",")

    try:
        if len(parts) != 3:
            raise ValueError(
                f"expected 3 fields, found {len(parts)}"
            )

        register_number, date, status = (
            part.strip() for part in parts
        )

        if status not in ("P", "A"):
            raise ValueError(f"invalid status '{status}'")

        if not register_number or not date:
            raise ValueError("register number or date is missing")

    except ValueError as error:
        raise InvalidRecord(str(error)) from error

    return register_number, date, status


def summarise(path):
    present = 0
    absent = 0
    errors = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if not line.strip():
                    continue

                try:
                    register_number, date, status = parse_line(line)

                    if status == "P":
                        present += 1
                    else:
                        absent += 1

                except InvalidRecord as error:
                    errors.append((line_number, str(error)))

    except FileNotFoundError as error:
        raise FileNotFoundError(
            f"Attendance file not found: {path}"
        ) from error

    except PermissionError as error:
        raise PermissionError(
            f"Permission denied: {path}"
        ) from error

    except UnicodeDecodeError as error:
        raise UnicodeError(
            f"Invalid file encoding: {path}"
        ) from error

    else:
        return present, absent, errors


data = (
    "192311001,2026-10-08,P\n"
    "192311002,2026-10-08,A\n"
    "192311003,2026-10-08\n"
    "192311004,2026-10-08,L\n"
)

with tempfile.NamedTemporaryFile(
    "w", suffix=".csv", delete=False, encoding="utf-8"
) as tmp:
    tmp.write(data)
    filename = tmp.name

try:
    print(summarise(filename))

    try:
        summarise("missing_attendance.csv")
    except FileNotFoundError as error:
        print(error)
    else:
        print("File processed successfully.")
    finally:
        print("Missing-file test completed.")

finally:
    os.remove(filename)