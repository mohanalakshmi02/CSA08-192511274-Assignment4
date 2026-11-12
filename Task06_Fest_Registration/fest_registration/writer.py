import csv


def write_outputs(master_list, event_participants, errors, output_folder):
    output_folder.mkdir(parents=True, exist_ok=True)

    # Write clean master registration list
    master_file = output_folder / "master_list.csv"

    with open(master_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Register Number",
            "Name",
            "Department",
            "Email",
            "Events"
        ])

        for student in master_list:
            writer.writerow([
                student["register_number"],
                student["name"],
                student["department"],
                student["email"],
                ";".join(student["events"])
            ])

    # Write separate participant files for each event
    for event, participants in event_participants.items():
        safe_event = "".join(
            character.lower() if character.isalnum() else "_"
            for character in event
        )

        event_file = output_folder / f"event_{safe_event}.txt"

        with open(event_file, "w", encoding="utf-8") as file:
            file.write(f"Participants for {event}\n")
            file.write("-------------------------\n")

            for student in participants:
                file.write(
                    f'{student["register_number"]}, '
                    f'{student["name"]}, '
                    f'{student["department"]}, '
                    f'{student["email"]}\n'
                )

    # Write summary report
    summary_file = output_folder / "summary_report.txt"

    with open(summary_file, "w", encoding="utf-8") as file:
        file.write("COLLEGE FEST REGISTRATION SUMMARY\n")
        file.write("---------------------------------\n")
        file.write(f"Total valid registrations: {len(master_list)}\n")
        file.write(f"Total events: {len(event_participants)}\n")
        file.write(f"Total errors: {len(errors)}\n\n")

        file.write("EVENT-WISE PARTICIPANT COUNT\n")

        for event, participants in sorted(event_participants.items()):
            file.write(f"{event}: {len(participants)} participants\n")

    # Write error log
    error_file = output_folder / "error.log"

    with open(error_file, "w", encoding="utf-8") as file:
        if errors:
            for error in errors:
                file.write(error + "\n")
        else:
            file.write("No errors found.\n")