
from pathlib import Path
from attendance_utils import process_attendance


def main():
    folder = Path(__file__).resolve().parent
    input_file = folder.parent / "attendance.csv"

    process_attendance(input_file, folder)


if __name__ == "__main__":
    main()
