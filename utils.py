import validator
import json
from datetime import datetime


tasks = []


def print_items(status):
    for idx, item in enumerate(tasks):
        if item['status'] == status:
            print(f"{idx + 1}. {item['description']}")


def add(value: str):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    temp_task = {
        'description': value,
        'status': None,
        'createdAt': now,
        'updatedAt': now
        }
    tasks.append(temp_task)


def update(idx: int, value: str):
    validator.validate_id(idx, tasks)
    idx -= 1
    tasks[idx]['description'] = value


def delete(idx: int):
    validator.validate_id(idx, tasks)
    idx -= 1
    del tasks[idx]


def show_help():
    try:
        with open('help.txt', "r") as f:
            help_text = f.read()
            print(help_text)
    except:
        FileNotFoundError('help.txt not found')


#  Mark


def mark_in_progress(idx: int):
    validator.validate_id(idx, tasks)
    idx -= 1
    tasks[idx]['status'] = 'In Progress'
    return f'{tasks[idx]['description']} was succesfully marked as in progress'


def mark_done(idx: int):
    validator.validate_id(idx, tasks)
    idx -= 1
    tasks[idx]['status'] = 'Done'


#  Display


def all_list():
    print('All tasks:')
    for idx, item in enumerate(tasks):
        print(f'{idx + 1}. {item['description']} | Status: {item['status']}')


def list_done():
    print('Finished tasks:')
    print_items('Done')


def list_todo():
    print('Todo tasks:')
    print_items(None)


def list_in_progress():
    print('In progress tasks:')
    print_items('In Progress')


# Load & Save


def save(filepath):
    filepath = filepath + '.json'
    with open(filepath, "w") as json_file:
        json.dump(tasks, json_file, indent=4)


def load(filepath):
    with open(filepath, "r") as json_file:
        global tasks
        tasks = json.load(json_file)


# Command Handler


def add_command_handler(parts, part):
    try:
        validator.is_2_items(parts, 'Follow the format below: add <description>')

        description = ' '.join(part)        
        add(description)
        print('Task succesfully added')
                    
    except ValueError as e:
        print('Value Error: ', e)


def update_command_handler(parts, part):
    try:
        validator.is_3_items(parts, 'Follow the format below: update <id> <description>')
                    
        idx, description = part
        idx, description = validator.idx_and_desc_converter(idx, description)

        update(idx, description)
        print('Task succesfully updated')

    except ValueError as e:
        print('Value Error: ', e)


def delete_command_handler(parts, part):
    try:
        validator.is_2_items(parts, 'Follow the format below: delete <id>')

        idx = int(part[0])                 

        delete(idx)
        print('Task succesfully deleted')

    except ValueError as e:
        print('Value Error: ', e)


def done_command_handler(parts, idx):
    try:
        idx = validator.idx_converter(idx, 'Follow the format below: mark done <id> << use interger for id')

        mark_done(idx)
        print('Task succesfully set to be done')

    except ValueError as e:
        print('Value Error: ', e)


def in_progress_command_handler(parts, idx):
    try:
        idx = validator.idx_converter(idx, 'Follow the format below: mark in_progress <id> << use interger for id')

        mark_in_progress(idx)
        print('Task succesfully set to be in progress')

    except ValueError as e:
        print('Value Error: ', e)


def save_command_handler(parts, part):
    try:
        validator.is_2_items(parts, 'Follow the format below: save <filepath>')

        filepath = ' '.join(part)
        save(filepath)
        print(f'Succesfully saved as {filepath}.json')
                
    except ValueError as e:
        print('Value Error: ', e)


def load_command_handler(parts, part):
    try:
        validator.is_2_items(parts, 'Follow the format below: load <filepath>')

        filepath = ' '.join(part)
        load(filepath)
        print('File succesfully loaded')

    except ValueError as e:
        print('Value Error: ', e)
