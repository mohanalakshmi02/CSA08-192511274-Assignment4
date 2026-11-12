
import csv
from datetime import date


def read_attendance(filename):
    records = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            register = row["register"].strip()
            attendance_date = date.fromisoformat(row["date"].strip())
            status = row["status"].strip().upper()

            records.append((register, attendance_date, status))

    return records
