import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do task :")
input_box = sg.InputText(tooltip="Enter a todo ", key="todo")
                                    #key will just put todo in front of the input
add_button = sg.Button("Add")# label
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")


window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button],[list_box, edit_button]],
                   # always edit layout when you change window elements
                   font=('Helvetica', 20))
                                        # we need to connect the elements
                                        # the role of another square bracket is to add rows between elements
while True:
    # we use while to not close the window yet
    event, values = window.read()
# the 2 values from window.read will be
# separated into event and values
    print(1, event)
    print(2, values)
    print(3, values["todos"])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            #we update window here also
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos) #this updates the window after edit

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case "Exit" | sg.WIN_CLOSED:
            break #breaks the loop of while
#print("Hello")
# if we execute with print it will hold
# after window.read until u do an action
# then get the print
window.close()