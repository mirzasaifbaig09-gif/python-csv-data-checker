import csv
from pathlib import Path

INPUT_FILE = Path("customers.csv")
OUTPUT_FILE = Path("report.csv")


def check_data():
    """Check customer records for common data-quality problems."""
    problems = []
    seen_records = set()

    if not INPUT_FILE.exists():
        print(f"Error: Could not find {INPUT_FILE}. Put it in this folder and try again.")
        return

    try:
        with INPUT_FILE.open("r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames or not {"name", "email"}.issubset(reader.fieldnames):
                print("Error: customers.csv must have these column headings: name,email")
                return

            for row_number, row in enumerate(reader, start=2):
                name = (row.get("name") or "").strip()
                email = (row.get("email") or "").strip()
                issues = []

                if not name:
                    issues.append("Missing name")

                if not email:
                    issues.append("Missing email")
                elif "@" not in email or "." not in email.split("@")[-1]:
                    issues.append("Invalid email format")

                record = (name.casefold(), email.casefold())
                if name and email and record in seen_records:
                    issues.append("Duplicate record")
                if name and email:
                    seen_records.add(record)

                if issues:
                    problems.append({
                        "row_number": row_number,
                        "name": name,
                        "email": email,
                        "issue": "; ".join(issues),
                    })

        with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
            columns = ["row_number", "name", "email", "issue"]
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            writer.writerows(problems)

        print("Data check completed!")
        print(f"Records checked: {max(0, row_number - 1) if 'row_number' in locals() else 0}")
        print(f"Records with problems: {len(problems)}")
        print(f"Report saved to: {OUTPUT_FILE.resolve()}")

    except (OSError, csv.Error) as error:
        print(f"Could not process the CSV file: {error}")


if __name__ == "__main__":
    check_data()
