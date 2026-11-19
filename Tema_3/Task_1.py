contacts = {
    "Ana": {"phone": "0722000001", "email": "ana@example.com"},
    "Mihai": {"phone": "0722000002", "email": "mihai@example.com"}
}

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. List contacts")
    print("2. Add contact")
    print("3. Search by name")
    print("4. Delete contact")
    print("5. Quit")

    choice = input("Choose an option: ")

    # List contacts
    if choice == "1":
        print("\nName       Phone           Email")
        print("-" * 50)

        for name in sorted(contacts):
            phone = contacts[name]["phone"]
            email = contacts[name]["email"]

            print(f"{name:<11}{phone:<16}{email}")

    # Add contact
    elif choice == "2":
        name = input("Enter name: ").strip()

        if not name:
            print("Name cannot be empty.")
            continue

        existing_name = None

        for contact_name in contacts:
            if contact_name.lower() == name.lower():
                existing_name = contact_name
                break

        if existing_name:
            answer = input("Contact already exists. Overwrite? (yes/no): ")

            if answer.lower() != "yes":
                print("Contact was not changed.")
                continue

            name = existing_name

        phone = input("Enter phone: ").strip()
        email = input("Enter email: ").strip()

        contacts[name] = {
            "phone": phone,
            "email": email
        }

        print("Contact added successfully.")

    # Search contact
    elif choice == "3":
        search_name = input("Enter name to search: ").strip()

        found = False

        for name in contacts:
            if name.lower() == search_name.lower():
                print("\nContact found:")
                print("Name:", name)
                print("Phone:", contacts[name]["phone"])
                print("Email:", contacts[name]["email"])
                found = True
                break

        if not found:
            print("Contact not found.")

    # Delete contact
    elif choice == "4":
        delete_name = input("Enter name to delete: ").strip()

        existing_name = None

        for name in contacts:
            if name.lower() == delete_name.lower():
                existing_name = name
                break

        if existing_name:
            del contacts[existing_name]
            print("Contact deleted successfully.")
        else:
            print("Contact does not exist.")

    # Quit
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")