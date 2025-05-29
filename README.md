


# 📝 Task Tracker CLI

**Project URL:** [https://github.com/NicoGuerrero11/cli-Task-Tracker](https://github.com/NicoGuerrero11/cli-Task-Tracker)

A command-line interface (CLI) application to manage tasks using Python. Tasks are stored locally in a JSON file. This tool supports adding, listing, updating, deleting, and filtering tasks by their status.

## 📁 Project Structure

- `traker.py`: Main CLI script with all logic for managing tasks
- `tasks.json`: Stores the tasks persistently (created automatically)
- `README.md`: Documentation of the project

## 💡 Features

- Add tasks with descriptions
- Update the description of any task
- Update the status of a task (`todo`, `in-progress`, `done`)
- Delete tasks by ID
- List all tasks or filter them by status
- Timestamps for when tasks were created and last updated

## ⚙️ How It Works

### Tasks Structure

Each task in `tasks.json` has the following structure:

```json
{
  "id": 1,
  "description": "Finish homework",
  "status": "in-progress",
  "createdAt": "2025-05-29T15:30:00",
  "updatedAt": "2025-05-29T16:10:00"
}
```

### CLI Commands

Run the program with:

```bash
python traker.py [command] [arguments]
```

#### Commands:

| Command                   | Description                                      |
|--------------------------|--------------------------------------------------|
| `add [description]`      | Adds a new task with the given description       |
| `list`                   | Lists all tasks                                  |
| `list [status]`          | Lists tasks filtered by status (`todo`, `in-progress`, `done`) |
| `update [id] [text]`     | Updates the task description by ID               |
| `mark-done [id]`         | Changes task status to `done`                    |
| `mark-in-progress [id]`  | Changes task status to `in-progress`             |
| `mark-todo [id]`         | Changes task status to `todo`                    |
| `delete [id]`            | Deletes a task by ID                             |

## 🛠 Internals of the Code

- `load_tasks()`: Reads and parses `tasks.json`.
- `save_task(tasks)`: Saves the current task list to the JSON file.
- `new_id(tasks)`: Generates a new unique ID based on existing tasks.
- `add_task(argv)`: Adds a task using command-line input.
- `update_task(argv)`: Updates the task description by its ID.
- `update_status(argv)`: Changes the task's status (used with commands like `mark-done`).
- `delete_task(argv)`: Removes a task from the list using its ID.
- `show_tasks(filter=None)`: Displays tasks, optionally filtering by status.
- `main()`: Handles user commands and routes them to the appropriate function.

## ✅ Valid Statuses

- `todo`
- `in-progress`
- `done`

## 📦 Example Usage

```bash
python traker.py add "Finish reading book"
python traker.py list
python traker.py mark-done 1
python traker.py update 1 "Finish reading the entire book"
python traker.py delete 1
```

## 📄 License

This project is developed for learning and personal use.