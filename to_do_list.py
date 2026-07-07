# A to do list

def get_menu_choice():

    print("Main Menu")
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

def add_task(tasks):

    task = input("Enter a task: ")

    tasks.append(task)

    print("Task added!")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def remove_task(tasks):
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

        while True:
            try:
                task_to_delete = int(input("Enter the number of the task you want to delete: "))
                if 1 <= task_to_delete <= len(tasks):
                    break
                print(f"Please enter a number between 1 and {len(tasks)}.")
            except ValueError:
                print("Error. Please enter a valid number of a task.")

        tasks.pop(task_to_delete - 1)
        print("Task removed!")

def main():
    tasks = []

    while True:
        choice = get_menu_choice()

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            remove_task(tasks)
        elif choice == 4:
            print("Goodbye!")
            break

main()