import json

# File to store contacts
CONTACT_FILE = "contacts.json"


# Load contacts from JSON file
def load_contacts():
    try:
        with open(CONTACT_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save contacts to JSON file
def save_contacts(contacts):
    with open(CONTACT_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)


# Add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!")


# View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


# Search contact by name
def search_contact():
    name = input("Enter the name to search: ")
    contacts = load_contacts()
    found_contacts = [c for c in contacts if name.lower() in c["name"].lower()]

    if not found_contacts:
        print("No matching contacts found.")
    else:
        print("Search Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


# Delete contact by name
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    contacts = load_contacts()
    updated_contacts = [c for c in contacts if c["name"].lower() != name.lower()]

    if len(contacts) == len(updated_contacts):
        print("No contact found with that name.")
    else:
        save_contacts(updated_contacts)
        print("Contact deleted successfully!")


def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting Contact Management System...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

