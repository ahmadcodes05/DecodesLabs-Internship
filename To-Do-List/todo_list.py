import json
import os
file_name = "tasks.json"
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        my_task = json.load(file)
else:
    my_task = []
def save_tasks():
    with open(file_name, "w") as file:
        json.dump(my_task, file, indent=4)
while True:
    print("\nWelcome To-Do-List Task")
    print("1 Enter your tasks")
    print("2 View your tasks")
    print("3 Mark task as completed")
    print("4 Delete a task")
    print("5 Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter your tasks: ").strip()

        if task_name:
            my_task.append({
                "task": task_name,
                "completed": False
            })
            save_tasks()
            print("Task has been added!")
        else:
            print("Task cannot be empty!")

    elif choice == "2":
        print("Your tasks:")

        if len(my_task) == 0:
            print("No tasks added!")
        else:
            for i, task in enumerate(my_task, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['task']} - {status}")

    elif choice == "3":
        if len(my_task) == 0:
            print("No tasks added!")
        else:
            print("Your tasks:")

            for i, task in enumerate(my_task, start=1):
                print(f"{i}. {task['task']}")

            try:
                number = int(input("Enter task number to complete: "))

                if 1 <= number <= len(my_task):
                    my_task[number - 1]["completed"] = True
                    save_tasks()
                    print("Task has been completed!")
                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number!")

    elif choice == "4":
        if len(my_task) == 0:
            print("No tasks to delete!")
        else:
            print("Your tasks:")

            for i, task in enumerate(my_task, start=1):
                print(f"{i}. {task['task']}")

            try:
                number = int(input("Enter task number to delete: "))

                if 1 <= number <= len(my_task):
                    deleted_task = my_task.pop(number - 1)
                    save_tasks()
                    print(
                        f"Task '{deleted_task['task']}' has been deleted!"
                    )
                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number!")

    elif choice == "5":
        print("Exit")
        break

    else:
        print("Invalid choice!")

print("Program End")
