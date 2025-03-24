tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added!')

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(task_number):
    try:
        task_index = task_number - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f'Task "{removed_task}" deleted!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nOptions: add / show / delete / exit")
        command = input("Enter command: ")
        
        if command == "add":
            task = input("Enter task: ")
            add_task(task)
        elif command == "show":
            show_tasks()
        elif command == "delete":
            show_tasks()
            try:
                task_number = int(input("Enter task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()
