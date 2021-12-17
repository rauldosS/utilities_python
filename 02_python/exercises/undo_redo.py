'''
    Make a to-do list with the following options:
        add task
        list tasks
        undo option (each time we call, undo the last action)
        redo option (every time we call, redo the last action)

        ['Task 1', 'Task 2']
        ['Task 1'] <- Undo
        ['Task 1', 'Task 2'] <- Redo
        
        input <- New task
'''

def show_op(todo_list):
    print()
    print('Tasks: ')
    print(todo_list)
    print()


def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Nothing to undo')
        return

    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nothing to redo')
        return

    last_redo = redo_list.pop()
    todo_list.append(last_redo)


def do_add(todo, todo_list):
    todo_list.append(todo)


if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Type a task or undo, redo, ls: ')

        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            do_undo(todo_list, redo_list)
            continue
        elif todo == 'redo':
            do_redo(todo_list, redo_list)
            continue

        do_add(todo, todo_list)