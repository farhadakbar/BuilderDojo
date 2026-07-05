# A to do list
def get_menu_choice():

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 4:
                break
            print("Choice must be between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    return choice

get_menu_choice()