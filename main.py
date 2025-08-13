import utils

if __name__ == '__main__':
    
    while True:
        command = str(input('>> '))

        parts = command.strip().lower().split(' ', 2)


        match parts:
            case ['list']:
                utils.all_list()


            case ['list', 'done']:
                utils.list_done()


            case ['list', 'todo']:
                utils.list_todo()


            case ['list', 'in_progress']:
                utils.list_in_progress()


            case ['add', *part]:
                utils.add_command_handler(parts, part)


            case ['update', *part]:
                utils.update_command_handler(parts, part)


            case ['delete', *part]:
                utils.delete_command_handler(parts, part)


            case ['mark', 'done', idx]:
                utils.done_command_handler(parts, idx)


            case ['mark', 'in_progress', idx]:
                utils.in_progress_command_handler(parts, idx)


            case ['help']:
                utils.show_help()


            case ['save', *part]:
                utils.save_command_handler(parts, part)


            case ['load', *part]:
                utils.load_command_handler(parts, part)


            case ['exit']:
                break


            case _:
                print('Try using help for more information how to use this simple program\n(>>help)')









