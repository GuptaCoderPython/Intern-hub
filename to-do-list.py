
store={}

def display_tasks():
    if not store:
        print("No tasks in the to-do list.")
    else:
        print("\nTo-Do List:")
        for task_id, task in store.items():
            print(f"{task_id}: {task}")

def add_task():
    task = input("Enter the task description: ")
    task_id = len(store) + 1
    store[task_id] = task
    print(f"Task added with ID {task_id}.")

def update_task():
    display_tasks()
    try:
        task_id = int(input("Enter the task ID to update: "))
        if task_id in store:
            new_task = input("Enter the updated task description: ")
            store[task_id] = new_task
            print("Task updated successfully.")
        else:
            print("Invalid task ID.")
    except ValueError:
        print("Please enter a valid task ID.")

def delete_task():
    display_tasks()
    try:
        task_id = int(input("Enter the task ID to delete: "))
        if task_id in store:
            del store[task_id]
            print("Task deleted successfully.")
        else:
            print("Invalid task ID.")
    except ValueError:
        print("Please enter a valid task ID.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the application. Goodbye!,internhub!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
