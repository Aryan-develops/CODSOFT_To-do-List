"""Aryan's TaskBook: Classes for tasks and the main list """

class Task:
    def __init__(self, title, description="", due_date="", priority="Medium", completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.title} ({self.priority}) | Due: {self.due_date} | {self.description}"

class TaskBook:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def list(self, show_all=True):
        if not self.tasks:
            print("No tasks in your list yet. Time to get productive!")
            return
        print("\n--- Your Tasks ---")
        for i, task in enumerate(self.tasks, 1):
            if show_all or not task.completed:
                print(f"{i}. {task}")

    def delete(self, idx):
        if 0 <= idx < len(self.tasks):
            print(f"Deleted: {self.tasks[idx].title}")
            del self.tasks[idx]
        else:
            print("Task number not found.")

    def complete(self, idx):
        if 0 <= idx < len(self.tasks):
            self.tasks[idx].completed = True
            print(f"Congrats! Marked '{self.tasks[idx].title}' as done.")
        else:
            print("Task number not found.")

    def edit(self, idx, title=None, description=None, due_date=None, priority=None):
        if 0 <= idx < len(self.tasks):
            task = self.tasks[idx]
            if title: task.title = title
            if description: task.description = description
            if due_date: task.due_date = due_date
            if priority: task.priority = priority
            print(f"Updated: {task.title}")
        else:
            print("Task number not found.")

    def filter_by_priority(self, priority):
        print(f"\n--- Tasks with priority: {priority} ---")
        found = False
        for i, task in enumerate(self.tasks, 1):
            if task.priority.lower() == priority.lower():
                print(f"{i}. {task}")
                found = True
        if not found:
            print("No tasks with that priority found.")