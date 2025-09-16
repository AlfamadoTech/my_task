# Running the app

from participant_details import contact, contact_csv, display

def main():
    contact_csv.load_from_csv()

    while True:
        display.show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            contact.create_contact()
        elif choice == "2":
            contact.update_contact()
        elif choice == "3":
            contact.delete_contact()
        elif choice == "4":
            contact.read_contacts()
        elif choice == "5":
            contact.search_contact()
        elif choice == "6":
            contact_csv.save_to_csv()
        elif choice == "7":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1–7.")

if __name__ == "__main__":
    main()