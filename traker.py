import sys
import json
from datetime import datetime

# Constants
JSON_FILE = "tasks.json"
VALID_STATUSES = ["todo", "in-progress", "done"]

# Load tasks from the JSON file
def load_tasks():
    try:
        with open(JSON_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# Show tasks (optionally filtered by status)
def show_tasks(filter = None):
    tasks = load_tasks()

    if not tasks:
        print("No tasks...")
        return
    
    # Filter tasks by status if a valid filter is provided
    if filter and filter in VALID_STATUSES:
        tasks = [t for t in tasks if t["status"] == filter]
    
    for task in tasks:
        print(f"\n🆔 ID: {task['id']}")
        print(f"📄 Description: {task['description']}")
        print(f"⏳ Status: {task['status']}")
        print(f"📅 Created: {task['createdAt']}")
        print(f"🔄 Updated: {task['updatedAt']}")
        print("-" * 40)

    
# Save tasks to the JSON file
def save_task(tasks):
    with open(JSON_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Generate new ID
def new_id(tasks):
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1

# Add a new task
def add_task(argv):
    description = " ".join(argv[2:])
    if not description:
        print("No description provided.")
        return
    tasks = load_tasks()
    id = new_id(tasks)
    now = datetime.now().isoformat()

    new_task = {
        "id": id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    tasks.append(new_task)
    save_task(tasks)
    print(f"\nnew task added ID: {id}")


# Update task description by ID
def update_task(argv):
    if len(argv) < 3:
        print("You must add an ID")
        return
    try:
        id = int(argv[2])
    except ValueError:
        print("Invalid ID format")

    description = " ".join(argv[3:])
    if not description:
        print("No description provided.")
        return

    tasks = load_tasks()
    found = False

    for task in tasks:
        if task["id"] == id:
            task["description"] = description
            task["updatedAt"] = datetime.now().isoformat()
            found = True
            break
        
    if found:
        save_task(tasks)
        print(f"Task with ID {id} updated.")
    else:
        print("ID not found")

            
# Delete task by ID
def delete_task(argv):
    if len(argv) < 3:
        print("You must add an ID")
        return
    try:
        id = int(argv[2])
    except ValueError:
        print("Invalid ID format")
    
    tasks = load_tasks()
    original_len = len(tasks)

    #Filter all tasks except the one with the ID we want to delete
    tasks = [task for task in tasks if task["id"] != id]

    if len(tasks) < original_len:
        save_task(tasks)
        print(f"🗑️ Tarea con ID {id} eliminada.")
    else:
        print("No se encontró ninguna tarea con ese ID.")

# Update task status by ID
def update_status(argv):
    if len(argv) < 3:
        print("You must add an ID")
        return
    try:
        id = int(argv[2])
    except ValueError:
        print("Invalid ID format")
    
    tasks = load_tasks()
    found = False
    if argv[1] not in VALID_STATUSES:
        print("Invalid status")
        return

    for task in tasks:
        if task["id"] == id:
            task["status"] = argv[1]
            task["updatedAt"] = datetime.now().isoformat()
            found = True
            break
        
    if found:
        save_task(tasks)
        print(f"Status of task ID {id} updated.")
    else:
        print("ID not found")


def main():
    argv = sys.argv

    if len(argv) < 2:
        print("You have to add a command")
        return
    
    command = argv[1]

    if command == "add":
        add_task(argv)
    elif command == "list":
        filter = argv[2] if len(argv) > 2 else None
        show_tasks(filter)
    elif command == "update":
        update_task(argv)
    elif command.startswith("mark-"):
        status = command.split("mark-")[1]
        # replaces the original command with the clean status
        argv[1] = status  
        update_status(argv)
    elif command == "delete":
        delete_task(argv)
    else:
        print(f"{command} command not found")

if __name__ == "__main__":
    main()
