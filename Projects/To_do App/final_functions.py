FILENAME = "todos.txt"


def get_todos(filepath=FILENAME):

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILENAME):

    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print(__name__)
if __name__ == "__main__":


    print("Hello")
    print(get_todos())