# Task List with Save and Load

FILENAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Main program
tasks = load_tasks()

while True:
    print("\nTask List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Save and Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "3":
        save_tasks(tasks)
        print("Tasks saved. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")