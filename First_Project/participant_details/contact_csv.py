# csv -> File handling

import csv
from pathlib import Path
from participant_details.contact import contacts

FILENAME = Path("contacts.csv")

if not FILENAME.exists():
    with FILENAME.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Age", "Job"])

# **************** SAVE *****************
def save_to_csv():
    try:
        with open(FILENAME, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Phone", "Age", "Job"])
            for c in contacts:
                writer.writerow([c["name"], c["phone"], c["age"], c["job"]])
        print("Contacts saved to CSV.")
    except Exception as e:
        print("Error saving to CSV:", e)


# **************** LOAD ****************
def load_from_csv():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            contacts.clear()
            for row in reader:
                contacts.append({
                    "name": row["Name"],
                    "phone": row["Phone"],
                    "age": int(row["Age"]),
                    "job": row["Job"]
                })
        print("Contacts loaded from CSV.\n")
    except FileNotFoundError:
        print("No CSV file found, starting fresh.")
    # except Exception as e:
    #     print("Error loading from CSV:", e)