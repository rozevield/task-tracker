# Task Management CLI

A **simple Python CLI** for managing tasks. Add, update, delete, and organize tasks with statuses like **"In Progress"** and **"Done"**. Supports saving/loading tasks to/from **JSON** files. This is an easy-to-use tool for managing to-do lists directly from the terminal.

---

## Features

- **Add**, **update**, and **delete** tasks.
- Mark tasks as **"In Progress"** or **"Done"**.
- List tasks based on their status: 
  - All tasks
  - Todo
  - In Progress
  - Done
- Save and load tasks from a **JSON** file.
- **Help** guide for usage instructions.

---

## Requirements

- **Python 3.x**
- External modules: `json`, `datetime`

---

## Files

- **`main.py`**: The main script that handles user input and calls functions from **`utils.py`**.
- **`utils.py`**: Contains the logic for managing tasks (add, update, delete, etc.) and reading/writing tasks to a file.
- **`validator.py`**: Contains functions for input validation (e.g., checking valid task IDs).
- **`help.txt`**: Contains instructions for using the task management CLI (optional).

---

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install dependencies:
   
   pip install -r requirements.txt
   
Ensure that help.txt exists for the help command, or modify the code to handle missing files.

---

## Usage

Run the program by executing main.py:

```
python main.py
```

Once the program is running, you can enter the following commands:

## Commands:

- **Add a Task:**

                  add <task_description>

Adds a new task to the list with the given description.

- **Update a Task:**

                  update <task_id> <new_description>

  Updates the description of the task with the specified ID.

- **Delete a Task:**

                  delete <task_id>

  Deletes the task with the specified ID.

- **Mark Task as "In Progress":**

                  mark in_progress <task_id>

  Marks the task as "In Progress".

- **Mark Task as "Done":**

                  mark done <task_id>

   Marks the task as "Done".

- **List All Tasks:**

                  list

Lists tasks marked as "Done".

- **List "Todo" Tasks:**

                  list todo

   Lists tasks that have not been started yet.

- **Save Tasks to File:**

                  save <file_path>

  Saves the current task list to a .json file.

- **Load Tasks from File:**

                  load <file_path>

  Loads tasks from a saved .json file.

- **Help:**

                  help

  Displays the help text explaining how to use the program.

- **Exit:**

                  exit


  Exits the program.

  ---

  ## Example:

  - **Add a task:**
 
                   >> add Finish the report
                   Task successfully added

  - **List all tasks:**

                  All tasks:
                  1. Finish the report | Status: None

  - **Mark a task as done:**

                   >> mark done 1
                   Task successfully set to be done

  - **Save tasks:**
   
                  >> save tasks_list
                  Successfully saved as tasks_list.json

  - **Load tasks:**

                  >> load tasks_list
                  File successfully loaded

    ---

    ## How It Works

**Task Management:**
Tasks are stored in a list as dictionaries. Each task has the following attributes:

- **description**: A short text describing the task.
- **status**: A string indicating the task's status (None, 'In Progress', or 'Done').
- **createdAt**: The timestamp when the task was created.
- **updatedAt:**: The timestamp when the task was last updated.

## Input Parsing and Command Handling:
The program continuously asks for user input. Commands are parsed and matched using Python's match statement to execute the corresponding function in utils.py.

## Validation:
Input is validated (e.g., ensuring the task ID is valid, and the correct number of arguments is provided for each command).

  ---

## Contributing

Feel free to fork this repository, submit issues, or create pull requests. Contributions are welcome!

  ---

## License

This project is licensed under the MIT License – see the LICENSE file for details.

                - The **"Instructions"** and **"Project URL"** sections should be included towards the beginning of the `README.md` to ensure they’re easy to find.
                - The **"How to Run the Project"** section will give clear instructions to anyone cloning the repository on how to get the project running on their machine.
                  
                When you create your GitHub repository, you can upload this `README.md` file into the root of your repository. This way, it will be the first thing users see when they visit your project’s page.

  ----

## Project URL

For more information and additional resources, visit the [Task Tracker Roadmap](https://roadmap.sh/projects/task-tracker)

                ### Key Changes:
                1. Added your **project URL** under the **"Project URL"** section.
                2. Filled in **"Contributing"**, **"License"**, and other sections to ensure completeness.
                
                This version includes your requested changes and should be ready for upload to your GitHub repository!
