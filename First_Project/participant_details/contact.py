contacts = []  # in-memory storage (list of dicts)

# ******************* CREATE ******************
def create_contact():
    try:
        name = input("Enter name: ").strip()
        if not name or not name.replace(" ", "").isalpha():
            print("Invalid name. Use letters only.")
            return False

        phone = input("Enter phone number (11 digits, start with 0): ").strip()
        if not (phone.isdigit() and len(phone) == 11 and phone.startswith("0")):
            print("Invalid phone number format.")
            return False

        age = input("Enter age: ").strip()
        if not age.isdigit():
            print("Age must be a number.")
            return False
        age = int(age)

        job = input("Enter job title: ").strip()
        if not job:
            print("Job title cannot be empty.")
            return False

        contact = {"name": name, "phone": phone, "age": age, "job": job}
        contacts.append(contact)
        print("Contact added successfully!")
        return True
    except Exception as e:
        print("Error creating contact:", e)
        return False


# ******************* READ ********************
def read_contacts():
    if not contacts:
        print("No contacts available.")
        return
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['age']} | {c['job']}")


# ****************** UPDATE ******************
def update_contact():
    read_contacts()
    if not contacts:
        return

    choice = input("Enter the number of the contact to update: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(contacts)):
        print("Invalid choice.")
        return
    index = int(choice) - 1
    contact = contacts[index]

    print("Leave blank to keep current value.")
    new_name = input(f"New name ({contact['name']}): ").strip()
    new_phone = input(f"New phone ({contact['phone']}): ").strip()
    new_age = input(f"New age ({contact['age']}): ").strip()
    new_job = input(f"New job ({contact['job']}): ").strip()

    if new_name and new_name.replace(" ", "").isalpha():
        contact['name'] = new_name
    if new_phone and new_phone.isdigit() and len(new_phone) == 11 and new_phone.startswith("0"):
        contact['phone'] = new_phone
    if new_age and new_age.isdigit():
        contact['age'] = int(new_age)
    if new_job:
        contact['job'] = new_job

    print("Contact updated!")


# ************************ DELETE ***********************
def delete_contact():
    read_contacts()
    if not contacts:
        return

    choice = input("Enter the number of the contact to delete: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(contacts)):
        print("Invalid choice.")
        return
    index = int(choice) - 1

    confirm = input(f"Are you sure you want to delete {contacts[index]['name']}? (y/n): ").strip().lower()
    if confirm == "y":
        contacts.pop(index)
        print("Contact deleted.")
    else:
        print("Delete cancelled.")


# ********************** SEARCH ********************
def search_contact():
    term = input("Enter name or phone to search: ").strip().lower()
    results = [c for c in contacts if term in c['name'].lower() or term in c['phone']]
    if results:
        for c in results:
            print(f"🔎 {c['name']} | {c['phone']} | {c['age']} | {c['job']}")
    else:
        print("No matching contact found.")