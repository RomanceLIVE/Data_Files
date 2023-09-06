import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo ")
add_button = sg.Button("Add")# label

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
                                        # we need to connect the elements
                                        # the role of another square bracket is to add rows between elements

window.read()
#print("Hello")
# if we execute with print it will hold
# after window.read until u do an action
# then get the print
window.close()