import json

def load_habits():
    try:
        with open("habits.json", "r") as file:
            habits = json.load(file)
    except FileNotFoundError:
        habits = []

    return habits

def save_habits(habits):
    with open("habits.json", "w") as file:
        json.dump(habits, file)

def add_habit(habits):
    habit = input("Enter a habit:")
    new_habit = {"habit": habit, "completed": False}
    habits.append(new_habit)
    save_habits(habits)
    print("Habit added successfully")

def view_habits(habits):
    if habits == []:
        print("No habits found.")
        return

    for index, habit in enumerate(habits, 1):
        if habit["completed"] == True:
            status = "Complete"
        else:
            status = "Incomplete"

        print(f"{index}. {habit['habit']} - {status}")

def mark_habit_complete(habits):
    view_habits(habits)

    if habits == []:
        return

    while True:
        try:
            choice = int(input("Enter habit number: "))

            if 1 <= choice <= len(habits):
                if habits[choice - 1]["completed"] == True:
                    print("Habit already completed!")
                    break
                else:
                    habits[choice - 1]["completed"] = True
                    save_habits(habits)
                    print("Habit marked completed!")
                    break
            else:
                print(f"Enter a number between 1 and {len(habits)}")

        except ValueError:
            print("Please enter a number.")
            continue

def display_menu():
    print("\nHabit Tracker\n")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Mark Habit Complete")
    print("4. Quit")

def main():
    habits = load_habits()

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            add_habit(habits)
        elif choice == 2:
            view_habits(habits)
        elif choice == 3:
            mark_habit_complete(habits)
        elif choice == 4:
            break
        else:
            print("Enter a number between 1 and 4.")

main()