# A simple contact book

def get_menu_choice():

    print("Main Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Quit")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 5:
                break
            print("Choice must be between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

    return choice

def add_contact(contacts):
    name = input("What is the contact's name: ")
    if name in contacts:
        print("Contact already exists.")
    else:
        phone_number = input(f"Enter {name}'s phone number: ")
        contacts[name] = phone_number
        print("Contact added!")

def view_contacts(contacts):
    if len(contacts) == 0:
        print("No contacts yet.")
    else:
        for name, phone_number in contacts.items():
            print(f"Name: {name} | Number: {phone_number}")

def search_contact(contacts):
    contact_to_search = input("What is the contact's name? ")
    if contact_to_search in contacts:
        print(f"Name: {contact_to_search} | Number: {contacts[contact_to_search]}")
    else:
        print("Contact not found.")

def remove_contact(contacts):
    contact_to_delete = input("What is the contact's name? ")
    if contact_to_delete in contacts:
        del contacts[contact_to_delete]
        print("Contact removed.")
    else:
        print("Contact not found.")

def main():
    contacts = {}

    while True:
        choice = get_menu_choice()
        if choice == 1:
            add_contact(contacts)
        elif choice == 2:
            view_contacts(contacts)
        elif choice == 3:
            search_contact(contacts)
        elif choice == 4:
            remove_contact(contacts)
        elif choice == 5:
            print("Goodbye!")
            break

main()