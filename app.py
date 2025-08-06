from taskbook import Task, TaskBook
from storage import save_tasks, load_tasks

def welcome():
    print("""
    **************************************
       Welcome to Aryan's TaskBook! 📝
    **************************************
    """)

def menu():
    print("\nWhat would you like to do?")
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Edit a task")
    print("4. Mark task as complete")
    print("5. Delete a task")
    print("6. Show tasks by priority")
    print("7. Save & Exit")

def get_priority():
    print("Select priority: [High/Medium/Low]")
    pr = input("Priority: ").capitalize()
    if pr not in ["High", "Medium", "Low"]:
        print("Defaulting to Medium.")
        return "Medium"
    return pr

def main():
    taskbook = TaskBook()
    welcome()
    load_tasks(taskbook)

    while True:
        menu()
        choice = input("Enter your choice (1-7): ").strip()
        if choice == "1":
            taskbook.list()
        elif choice == "2":
            title = input("Task title: ")
            desc = input("Description: ")
            due = input("Due date: ")
            pr = get_priority()
            taskbook.add(Task(title, desc, due, pr))
            print("Task added!")
        elif choice == "3":
            taskbook.list()
            try:
                idx = int(input("Task number to edit: ")) - 1
                print("Leave blank to keep current value.")
                title = input("New title: ")
                desc = input("New description: ")
                due = input("New due date: ")
                pr = input("New priority (High/Medium/Low): ").capitalize()
                pr = pr if pr in ["High", "Medium", "Low"] else None
                taskbook.edit(idx, title or None, desc or None, due or None, pr)
            except ValueError:
                print("Please use a number.")
        elif choice == "4":
            taskbook.list()
            try:
                idx = int(input("Task number to mark complete: ")) - 1
                taskbook.complete(idx)
            except ValueError:
                print("Please use a number.")
        elif choice == "5":
            taskbook.list()
            try:
                idx = int(input("Task number to delete: ")) - 1
                taskbook.delete(idx)
            except ValueError:
                print("Please use a number.")
        elif choice == "6":
            pr = input("Enter priority to filter (High/Medium/Low): ").capitalize()
            taskbook.filter_by_priority(pr)
        elif choice == "7":
            save_tasks(taskbook)
            print("Goodbye! Stay productive, Aryan! 🚀")
            break
        else:
            print("Invalid choice. Please pick a number from the menu.")

if __name__ == "__main__":
    main()