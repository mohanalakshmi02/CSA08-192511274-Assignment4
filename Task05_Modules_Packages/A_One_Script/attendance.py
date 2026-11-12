
import csv
from pathlib import Path
from datetime import date, timedelta


# 1. READING FILES
def read_attendance(filename):
    records = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            records.append((
                row["register"].strip(),
                date.fromisoformat(row["date"].strip()),
                row["status"].strip().upper()
            ))

    return records


# 2. COMPUTING STATISTICS
def calculate_statistics(records):
    attendance = {}

    for register, attendance_date, status in records:
        if register not in attendance:
            attendance[register] = {"present": 0, "total": 0}

        attendance[register]["total"] += 1

        if status == "P":
            attendance[register]["present"] += 1

    percentages = {}

    for register, counts in attendance.items():
        percentages[register] = (
            counts["present"] / counts["total"]
        ) * 100

    return percentages


def find_three_day_absences(records):
    student_dates = {}

    for register, attendance_date, status in records:
        if register not in student_dates:
            student_dates[register] = {}

        student_dates[register][attendance_date] = status

    absent_students = []

    for register, daily_status in student_dates.items():
        dates = sorted(daily_status)

        for current_date in dates:
            next_date = current_date + timedelta(days=1)
            third_date = current_date + timedelta(days=2)

            if (
                daily_status.get(current_date) == "A"
                and daily_status.get(next_date) == "A"
                and daily_status.get(third_date) == "A"
            ):
                absent_students.append(register)
                break

    return absent_students


# 3. WRITING REPORTS
def write_reports(percentages, absent_students, folder):
    report_file = folder / "attendance_report.txt"
    absence_file = folder / "three_day_absences.txt"

    with open(report_file, "w", encoding="utf-8") as file:
        file.write("ATTENDANCE PERCENTAGE REPORT\n")
        file.write("----------------------------\n")

        for register, percentage in percentages.items():
            file.write(f"{register}: {percentage:.2f}%\n")

    with open(absence_file, "w", encoding="utf-8") as file:
        file.write("STUDENTS ABSENT FOR THREE CONSECUTIVE DAYS\n")
        file.write("------------------------------------------\n")

        if absent_students:
            for register in absent_students:
                file.write(register + "\n")
        else:
            file.write("No students found.\n")


# MAIN PROGRAM
def main():
    folder = Path(__file__).resolve().parent
    input_file = folder.parent / "attendance.csv"

    records = read_attendance(input_file)

    percentages = calculate_statistics(records)
    absent_students = find_three_day_absences(records)

    write_reports(percentages, absent_students, folder)

    print("Attendance reports generated successfully.")
    print("\nAttendance Percentages:")

    for register, percentage in percentages.items():
        print(f"{register}: {percentage:.2f}%")

    print("\nAbsent for three consecutive days:")
    print(absent_students)


if __name__ == "__main__":
    main()
