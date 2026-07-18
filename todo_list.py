# Simple To-Do List

tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            number = int(input("Enter task number to remove: "))

            if number >= 1 and number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(removed, "removed successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice! Please try again.")
