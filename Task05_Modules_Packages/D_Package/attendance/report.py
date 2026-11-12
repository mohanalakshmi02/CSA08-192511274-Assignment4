
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
