
from pathlib import Path

from attendance import (
    read_attendance,
    calculate_statistics,
    find_three_day_absences,
    write_reports
)


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
