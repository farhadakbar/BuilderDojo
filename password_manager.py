# A program that stores multiple different passwords

passwords = []

def add_password(passwords):
    website = input("Enter the website: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    entry = {
        "website": website,
        "username": username,
        "password": password
    }
    passwords.append(entry)
    print("Password added successfully!")

def view_passwords(passwords):
    if passwords == []:
        print("No passwords saved.")
        return
    for index, entry in enumerate(passwords, 1):
        print(f"{index}. {entry['website']}")
        print(f"Username: {entry['username']}")
        print(f"Password: {entry['password']}")

def search_password(passwords):
    search = input("What website's password: ").lower()

    for entry in passwords:
        if search == entry["website"].lower():
            print(f"Website: {entry['website']}")
            print(f"Username: {entry['username']}")
            print(f"Password: {entry['password']}")
            return

    print("No password found for that website.")

def delete_password(passwords):
    website = input("Enter website to delete: ").lower()

    for entry in passwords:
        if website == entry["website"].lower():
            passwords.remove(entry)
            print("Password deleted successfully!")
            return

    print("No password found for that website.")

def display_menu():
    print("Password Manager\n")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Delete Password")
    print("5. Quit")

def main():
    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            add_password(passwords)
        elif choice == 2:
            view_passwords(passwords)
        elif choice == 3:
            search_password(passwords)
        elif choice == 4:
            delete_password(passwords)
        elif choice == 5:
            print("Thanks for using Password Manager!")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()