# Python CSV Data Checker

A beginner-friendly Python project that checks sample customer records in a CSV file and writes a report of common data-quality issues.

## Features

- Detects missing names
- Detects missing email addresses
- Flags simple email-format problems
- Identifies duplicate name-and-email records
- Exports findings to `report.csv`
- Gives a helpful message if the input file or required columns are missing

## Requirements

- Python 3
- No third-party packages are required

## How to run

1. Keep `main.py` and `customers.csv` in the same folder.
2. Open that folder in VS Code.
3. Open **Terminal → New Terminal**.
4. Run:

   ```bash
   python3 main.py
   ```

5. Open `report.csv` to review the findings.

## Sample data

The included `customers.csv` contains fictional sample records with intentional issues for testing. It does not contain real customer data.

## Expected result

The sample file should produce four records with problems:
- Missing email
- Missing name
- Duplicate record
- Invalid email format

## Limitations

The email check is intentionally basic. It does not verify that an email address exists or implement the full email-address standard. Duplicate detection matches both the name and email. The program reports problems but does not change the source file.

## Skills demonstrated

Python functions, CSV file handling, dictionaries, lists, sets, conditional statements, loops, basic validation, error handling, and generating a report.

## Possible future improvements

- Add automated unit tests
- Let the user choose an input file
- Add more validation rules
- Create a summary of issue types
