
from datetime import timedelta


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
        for current_date in sorted(daily_status):
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
