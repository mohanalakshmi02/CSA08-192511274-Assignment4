# CSA08 – Python Programming Assignment 4

## Student Details

- **Name:** Mohanalakshmi S
- **Register Number:** 192511274
- **Department:** Computer Science and Engineering
- **Python Version:** 3.14.7

## Project Description

This repository contains the implementation and design solutions for Python Programming Assignment 4 (CO4). The assignment focuses on file handling, exception handling, modular programming, packages and real-world file-processing applications.

## Tasks Completed

### Task 1 – File Processing Design Review
Designed and implemented a mess bill processing program using file handling and exception handling. The program calculates the total bill amount and identifies invalid records.

### Task 2 – From Requirement to File-Processing Design
Designed an attendance processing system using suitable data structures, file operations, pseudocode and complexity analysis.

### Task 3 – Design the Error Handling
Implemented an attendance processing program using custom exceptions, built-in exceptions and structured error handling.

### Task 4 – File and Exception Forensics
Analysed common file-handling errors and implemented a corrected file-processing program using append mode, context managers and exception handling.

### Task 5 – The Same Utility Organised Four Ways
Implemented an attendance processing utility using four different structures:
- Single Python script
- Single Python module
- Multiple Python modules
- Python package

### Task 6 – College Fest Registration Desk
Developed a modular registration processing system that:
- Reads registration details from department files.
- Validates student information and email addresses.
- Identifies and removes duplicate registrations.
- Handles damaged records and missing files.
- Generates a master registration list.
- Creates event-wise participant files.
- Produces a summary report and error log.

## Technologies Used

- Python 3.14.7
- Visual Studio Code
- Git
- GitHub
- Python Standard Library

## Libraries Used

The assignment uses Python's built-in standard library modules, including:

- `csv`
- `pathlib`
- `decimal`
- `tempfile`
- `os`

No external Python packages are required.

## Repository Structure

```text
CSA08-192511274-Assignment4/
│
├── Task01_File_Processing/
│
├── Task03_Exception_Handling/
│
├── Task04_File_Exception_Forensics/
│
├── Task05_Modules_Packages/
│   ├── A_One_Script/
│   ├── B_One_Module/
│   ├── C_Three_Modules/
│   └── D_Package/
│
└── Task06_Fest_Registration/
    ├── input/
    ├── fest_registration/
    ├── output/
    └── main.py
```

Task 2 contains design work and is documented in the assignment report.

## How to Run the Programs

Open the respective task folder in the VS Code terminal.

**Task 1**
```bash
py task1_mess_bills.py
```

**Task 3**
```bash
py task3_attendance.py
```

**Task 4**
```bash
py task4_forensics.py
```

**Task 5**

Run the `main.py` file inside each implementation folder. Keep `attendance.csv` in the location expected by the program.

**Task 6**
```bash
py main.py
```

Run this command from inside the `Task06_Fest_Registration` folder.

## Expected Results

The programs demonstrate:
- Successful processing of valid input records.
- Identification and logging of invalid records.
- Handling of missing files and exceptions.
- Generation of attendance and registration reports.
- Modular organisation and reusable Python code.

## Conclusion

This assignment provides practical experience in Python file processing, exception handling, modular programming and package development. It demonstrates how Python can be used to develop reliable applications that process real-world data and handle errors effectively.
