
from decimal import Decimal, InvalidOperation


def process_mess_bills(filename):
    total = Decimal("0.00")
    report = []
    rejected_lines = []

    try:
        with open(filename, "r", encoding="utf-8") as file:

            for line_number, line in enumerate(file, start=1):
                line = line.strip()

                if not line:
                    continue

                try:
                    parts = line.split(",")

                    if len(parts) != 3:
                        raise ValueError("Expected exactly 3 fields")

                    register_number = parts[0].strip()
                    name = parts[1].strip()
                    amount = Decimal(parts[2].strip())

                    if not register_number or not name:
                        raise ValueError("Missing register number or name")

                    report.append(f"{name} {amount:.2f}")
                    total += amount

                except (ValueError, InvalidOperation) as error:
                    rejected_lines.append(
                        (line_number, line, str(error))
                    )

        print("MESS BILL REPORT")
        print("----------------")

        for record in report:
            print(record)

        print("\nTotal:", f"{total:.2f}")

        print("\nRejected Lines:")
        for item in rejected_lines:
            print(item)

        if not rejected_lines:
            print("No rejected lines")

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except UnicodeDecodeError:
        print("Error: Invalid file encoding.")


process_mess_bills("mess_oct.txt")
