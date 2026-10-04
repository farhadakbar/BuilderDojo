# A banking simulator that keeps track of balance and transactions

account = {
    "name": "Farhad",
    "balance": 1000.00,
    "transactions": []
}

def check_balance(account):
    print(f"Current balance: ${account['balance']:.2f}")

def deposit_money(account):
    try:
        amount = float(input("Enter deposit amount: $"))
    except ValueError:
        print("Please enter a valid amount.")
        return

    if amount > 0:
        account["balance"] += amount
        print("Deposit successful!")
        account["transactions"].append(f"Deposit: ${amount:.2f}")
    else:
        print("Deposit amount must be greater than $0.")

def withdraw_money(account):
    try:
        amount = float(input("Enter withdrawal amount: $"))
    except ValueError:
        print("Please enter a valid amount.")
        return

    if amount <= 0:
        print("Invalid withdrawal amount.")
    elif amount > account["balance"]:
        print("Insufficient funds.")
    else:
        account["balance"] -= amount
        print("Withdrawal successful!")
        account["transactions"].append(f"Withdrawal: ${amount:.2f}")

def view_transactions(account):
    if account["transactions"] == []:
        print("No transactions found.")
        return
    print("Transaction History:")
    for index, transaction in enumerate(account["transactions"], 1):
        print(f"{index}. {transaction}")

def display_menu():
    print("Banking Simulator\n")

    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transactions")
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
            check_balance(account)
        elif choice == 2:
            deposit_money(account)
        elif choice == 3:
            withdraw_money(account)
        elif choice == 4:
            view_transactions(account)
        elif choice == 5:
            print("Thanks for banking with us!")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()