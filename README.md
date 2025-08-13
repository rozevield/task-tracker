# task-tracker
A simple Python CLI for managing tasks. Add, update, delete, and organize tasks with statuses like "In Progress" and "Done". Supports saving/loading tasks to/from JSON files. Easy-to-use for managing to-do lists directly from the terminal. Perfect for lightweight task management.

## Features
- Add, update, and delete tasks.
- Mark tasks as "In Progress" or "Done".
- List tasks based on their status: All tasks, Todo, In Progress, Done.
- Save and load tasks from a JSON file.
- Help guide on how to use the commands.

## Requirements
- Python 3.x
- External modules: `json`, `datetime`

## Files

- `main.py`: The main script that handles user input and calls functions from `utils.py`.
- `utils.py`: Contains the logic for managing tasks (add, update, delete, etc.) and reading/writing tasks to a file.
- `validator.py`: Contains functions for input validation (e.g., checking valid task IDs).
- `help.txt`: Contains instructions for using the task management CLI (optional).

## Setup
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
Ensure that all dependencies are installed (you might need validator.py for input validation):

pip install -r requirements.txt
Ensure that help.txt exists for the help command, or modify the code to handle missing files.

Usage
Run the program by executing main.py:

python main.py
Once the program is running, you can enter the following commands:

Commands:
Add a Task:

>> add <task_description>

Adds a new task to the list with the given description.

Update a Task:

>> update <task_id> <new_description>

Updates the description of the task with the specified ID.

Delete a Task:

>> delete <task_id>

Deletes the task with the specified ID.

Mark Task as "In Progress":

>> mark in_progress <task_id>

Marks the task as "In Progress".

Mark Task as "Done":

>> mark done <task_id>

Marks the task as "Done".

List All Tasks:

>> list

Lists all tasks with their current status.

List "Done" Tasks:

>> list done

Lists tasks that are marked as "Done".

List "In Progress" Tasks:

>> list in_progress

Lists tasks that are marked as "In Progress".

List "Todo" Tasks:

>> list todo

Lists tasks that have not been started yet.

Save Tasks to File:

>> save <file_path>

Saves the current task list to a .json file.

Load Tasks from File:

>> load <file_path>

Loads tasks from a saved .json file.

Help:

>> help

Displays the help text explaining how to use the program.

Exit:

>> exit

Exits the program.

Example
Add a task:

>> add Finish the report
Task successfully added
List all tasks:

>> list
All tasks:
1. Finish the report | Status: None
Mark a task as done:

>> mark done 1
Task successfully set to be done
Save tasks:

>> save tasks_list
Successfully saved as tasks_list.json
Load tasks:

>> load tasks_list
File successfully loaded
How It Works
Task Management:

Tasks are stored in a list as dictionaries. Each task has the following attributes:

description: A short text describing the task.

status: A string indicating the task's status (None, 'In Progress', or 'Done').

createdAt: The timestamp when the task was created.

updatedAt: The timestamp when the task was last updated.

Input Parsing and Command Handling:

The program continuously asks for user input.

Commands are parsed and matched using Python's match statement to execute the corresponding function in utils.py.

Validation:

Input is validated (e.g., ensuring the task ID is valid, the correct number of arguments is provided for each command).

Contributing
Feel free to fork this repository, submit issues, or create pull requests. Contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.


This `README.md` will guide users in setting up and using your task management system. It covers installat
