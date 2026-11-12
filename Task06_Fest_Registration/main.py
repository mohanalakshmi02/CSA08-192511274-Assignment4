from pathlib import Path

from fest_registration.processor import process_department_files
from fest_registration.writer import write_outputs


def main():
    base_folder = Path(__file__).parent

    input_folder = base_folder / "input"
    output_folder = base_folder / "output"

    department_files = [
        input_folder / "cse.txt",
        input_folder / "ece.txt",
        input_folder / "eee.txt",
        input_folder / "mech.txt",
        input_folder / "civil.txt"
    ]

    master_list, event_participants, errors = (
        process_department_files(department_files)
    )

    write_outputs(
        master_list,
        event_participants,
        errors,
        output_folder
    )

    print("COLLEGE FEST REGISTRATION PROCESSING")
    print("------------------------------------")
    print("Valid registrations:", len(master_list))
    print("Events processed:", len(event_participants))
    print("Errors recorded:", len(errors))
    print("\nOutput files created successfully.")
    print("Check the output folder for the reports.")


if __name__ == "__main__":
    main()