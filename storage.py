
"""Aryan's TaskBook: Save and load tasks to a JSON file."""
import json
from taskbook import Task

def save_tasks(taskbook, filename="aryan_tasks.json"):
    data = []
    for task in taskbook.tasks:
        data.append({
            "title": task.title,
            "description": task.description,
            "due_date": task.due_date,
            "priority": task.priority,
            "completed": task.completed
        })
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"\nAll tasks saved to {filename}!")

def load_tasks(taskbook, filename="aryan_tasks.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            for item in data:
                task = Task(
                    title=item["title"],
                    description=item.get("description", ""),
                    due_date=item.get("due_date", ""),
                    priority=item.get("priority", "Medium"),
                    completed=item.get("completed", False)
                )
                taskbook.add(task)
        print(f"Loaded {len(taskbook.tasks)} tasks from {filename}.")
    except FileNotFoundError:
        print("No saved tasks found, starting fresh!")