FILENAME = "todos.txt"


def get_todos(filepath=FILENAME):
    # we assign filepath = todos.txt as default argument
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILENAME):

    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print(__name__)
if __name__ == "__main__":

# we use a variable for the executed file to avoid issues
# when we use a script or run the file standalone
    print("Hello")
    print(get_todos())