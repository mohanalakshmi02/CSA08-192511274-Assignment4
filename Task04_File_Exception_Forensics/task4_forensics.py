
def save_returns_bad(books):
    log = open("returns.log", "w")

    for book in books:
        log.write(book)

    log.close()


def process_bad(day_file):
    try:
        books = open(day_file).read().split("\n")
        save_returns_bad(books)
    except FileNotFoundError:
        print("missing")


def save_returns(books):
    with open("returns_fixed.log", "a", encoding="utf-8") as log:
        for book in books:
            if book.strip():
                log.write(book.strip() + "\n")


def process(day_file):
    try:
        with open(day_file, "r", encoding="utf-8") as file:
            books = file.read().splitlines()

        save_returns(books)
        print(day_file, "processed successfully.")

    except (FileNotFoundError, PermissionError, UnicodeDecodeError) as error:
        print("Error:", error)

        with open("error.log", "a", encoding="utf-8") as error_file:
            error_file.write(str(error) + "\n")


# Create three daily input files
daily_data = {
    "day1.txt": "Book A\nBook B",
    "day2.txt": "Book C\nBook D",
    "day3.txt": "Book E\nBook F"
}

for filename, data in daily_data.items():
    with open(filename, "w", encoding="utf-8") as file:
        file.write(data)


# Demonstrate the defective program
print("DEFECTIVE PROGRAM OUTPUT")

for day in daily_data:
    process_bad(day)

print("\nDefective Returns Log:")

with open("returns.log", "r", encoding="utf-8") as file:
    print(file.read())


# Run the corrected program
print("\nCORRECTED PROGRAM OUTPUT")

for day in daily_data:
    process(day)


# Test missing-file error handling
process("day4.txt")


# Display corrected returns log
print("\nCorrected Returns Log:")

with open("returns_fixed.log", "r", encoding="utf-8") as file:
    print(file.read())


# Display error log
print("Error Log:")

with open("error.log", "r", encoding="utf-8") as file:
    print(file.read())
