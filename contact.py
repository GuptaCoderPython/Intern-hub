contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added successfully.")

def display_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

def search_contact():
    name = input("Enter the name to search: ")
    if name in contacts:
        details = contacts[name]
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Management System Internhub")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            display_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
