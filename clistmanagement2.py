import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):  # If file doesn't exist, create an empty contact list
        return []
    try:
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f).get("contacts", [])
    except json.JSONDecodeError:  # If the file is corrupted
        return []

def save_contacts(people):
    with open(CONTACTS_FILE, "w") as f:
        json.dump({"contacts": people}, f, indent=4)  # `indent=4` makes it more readable

def add_people(people):
    name = input("Name: ").strip()
    age = input("Age: ").strip()
    email = input("Email: ").strip()

    if not name or not age.isdigit() or "@" not in email:
        print("Invalid input. Please enter valid name, age (number), and email.")
        return

    person = {"name": name, "age": age, "email": email}
    people.append(person)
    print(f"Added: {name}")

def display_people(people):
    if not people:
        print("No contacts available.")
        return
    print("\nContact List:")
    print("-" * 30)
    for i, person in enumerate(people, start=1):
        print(f"{i}. {person['name']} | {person['age']} | {person['email']}")
    print("-" * 30)

def delete_contact(people):
    display_people(people)
    if not people:
        return
    
    while True:
        try:
            number = int(input("Enter number of the contact to delete: "))
            if 1 <= number <= len(people):
                removed = people.pop(number - 1)
                print(f"Deleted: {removed['name']}")
                return
            else:
                print("Invalid number. Please enter a valid contact number.")
        except ValueError:
            print("Please enter a valid number.")

# Search for a contact
def search(people):
    search_name = input("Search Name: ").strip().lower()
    results = [person for person in people if search_name in person["name"].lower()]

    if results:
        display_people(results)
    else:
        print("No contacts found.")

# Main program
people = load_contacts()

while True:
    print("\n--- CTI Contact Management ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Quit")

    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        add_people(people)
    elif choice == "2":
        display_people(people)
    elif choice == "3":
        delete_contact(people)
    elif choice == "4":
        search(people)
    elif choice == "5":
        save_contacts(people)
        print("Contacts saved. Goodbye!")
        break
    else:
        print("Invalid choice. Please select from the menu.")

