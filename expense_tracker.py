# Expense Tracker

def get_menu_choice():

    print("Main Menu")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Remove Expense")
    print("5. Quit")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 5:
                break
            print("Choice must be between 1 and 5.")
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5.")

    return choice

def add_expense(expenses):

    description = input("What is the expense? ")
    amount = float(input("What is the amount? "))

    expense_dict = {"Description": description, "Amount": amount}
    expenses.append(expense_dict)
    print("Expense added!")

def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    total = 0
    for expense in expenses:
        total += expense["Amount"]
        print(f"{expense['Description']} - ${expense['Amount']:.2f}")

    print(f"Total = ${total:.2f}")

def search_expense(expenses):
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    expense_to_search = input("Which expense? ")

    for expense in expenses:
        if expense["Description"] == expense_to_search:
            print(f"{expense['Description']} - ${expense['Amount']:.2f}")
            return

    print("Expense not found.")


def remove_expense(expenses):
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    expense_to_delete = input("Which expense would you like to remove? ")

    for expense in expenses:
        if expense["Description"] == expense_to_delete:
            expenses.remove(expense)
            print("Expense removed.")
            return
    print("Expense not found.")

def main():
    expenses = []

    while True:
        choice = get_menu_choice()
        if choice == 1:
            add_expense(expenses)
        elif choice == 2:
            view_expenses(expenses)
        elif choice == 3:
            search_expense(expenses)
        elif choice == 4:
            remove_expense(expenses)
        elif choice == 5:
            print("Goodbye!")
            break

main()