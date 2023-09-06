# print("Enter a todo:")  # we introduce an argument at print

""""
# EX 1
user_prompt = "Enter a todo:"
text = input(user_prompt)  # user_text is an assigned variable
print(text)
"""
import time

""""
# EX 2
user_prompt = "Enter a todo:"
todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)
# we now use [] to make a list
# todos = [todo1, todo2, todo3]
todos = [todo1, todo2, todo3, "Hi friend !"]
print(todos)

print(type(user_prompt))  #type shows the type of data
print(type(todos))

"""

# Ex 4
"""
user_prompt = "Enter a todo:"
while 2 > 1:
    todo = input(user_prompt)
    print(todo)
    print("Next:")
"""

# Ex 5
"""
user_prompt = "Enter a todo:"
while True:    # we will use true instead of 2>1
    todo = input(user_prompt)
    todos = [todo] 
#not good because the 2nd value entered in the list will overwrite the first value entered
    print(todos)
"""

# Ex 6
"""
user_prompt = "Enter a todo:"
todos = []
while True:
    todo = input(user_prompt)
    print(todo.capitalize())
# capitalize will Cap the string above
    todos.append(todo)
# append is a method for data types, an object in this case
    print(todos)
 """

# Joaca

"""
while True:
#Infinite loop 
    print("Hello")
"""

# Joaca

"""
todos = []
while True:
    user_prompt = "Enter a todo:"
# NOT RECOM to have variable declaration inside a loop
    todo = input(user_prompt)
    print(todo.title())
    #title will capitalize each word
    todos.append(todo)
"""

# Ex 7
"""
password = input("Enter password: ")

while password != "pass123":
    password = input("Enter password: ")

print("Password correct!")
"""

# Ex 8
"""
x = 1
while x <= 6:
    print(x)
    x = x + 1
"""

# Ex 9
"""
todos = []
while True:
    user_action = input("Type add,show or exit:")

    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break

print("Thanks,bye !")
"""

"""
# Ex 10 Improving

todos = []
while True:
    user_action = input("Type add,show or exit:")
    user_action = user_action.strip()
    # strip is used to remove spaces to avoid errors at inputs

    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item.capitalize())
        case 'exit':
            break

print("Thanks,bye !")
"""
"""
# Ex 11 Improving

todos = []
while True:
    user_action = input("Type add,show or exit:")
    user_action = user_action.strip()
    # strip is used to remove spaces to avoid errors at inputs

    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item.capitalize())
        case 'exit':
            break
        case _:
# _ here is to match random input but u can match with everything instead of _ like whatever but _ is the convention in code
            print("Unknown command")

print("Thanks,bye !")
"""
"""
# Ex 12 Improving

todos = []
while True:
    user_action = input("Type add,show or exit:")
    user_action = user_action.strip()
    # strip is used to remove spaces to avoid errors at inputs

    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show' | 'display':
# | means 'or'
            for item in todos:
                print(item.capitalize())
        case 'exit':
            break


print("Thanks,bye !")
"""
"""
# Ex 13 Improving

todos = []
while True:
    user_action = input("Type add,show or exit:")
    user_action = user_action.strip()
    # strip is used to remove spaces to avoid errors at inputs

    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show':
# | means 'or'
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break

print("Thanks,bye !")
"""
"""

# Ex 14

meals = ['pasta','cake','pie']

for meal in meals:
# in background the for does something like meal='pizza'
    print(meal.capitalize())
for meal in 'meals':
    print(meal.capitalize())
print('bye')
"""
"""
# Ex 15 Improving

todos = []
while True:
    user_action = input("Type add, show, edit or exit:")
    user_action = user_action.strip()
    # strip is used to remove spaces to avoid errors at inputs

    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show' | 'display':
# | means 'or'   
            for item in todos:
                item = item.title()
                print(item)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'exit':
            break

print("Thanks,bye !")

# FLOAT is to convert into a DECIMAL NR
# float("10")=10.0
# x=10  str(x)='10' (converted into string)

"""
"""
# Ex 16

filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace('.','-',1)
    print(filename)
# for real life scenario use file.rename(filename) (the actual disk files will be renamed with it)
"""
"""
# Ex 17

todos = []
while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show' | 'display':
            for index, item in enumerate(todos):
                item = item.title()
                row = f"{index+1}.{item}"
                print(row)
               # we used before print(index+1,'.',item) but not ideal due to spaces
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
print("Thanks,bye !")
"""

"""
# Experiment

todos = []
while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show' | 'display':
            for index, item in enumerate(todos):
                item = item.title()
                row = f"{index+1}.{item}"
                print(row)
            #print(f"Length is {index + 1}") is the nr of todo
            #print("Length is", (len(todo))) is the 2nd method of what i did above with length
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
print("Thanks,bye !")
"""

# Experiment
# run in console
# for i,j in enumerate("Hello"):
# print(i,j)

# Experiment
# run in console
# a = enumerate(["a","b","c"])
# list(a) because above is not a list but an object

"""
# Ex 18

waiting_list = ["sen","ham","iafet"]
#waiting_list=waiting_list.sort()
# No need to do this ! because the method DOESNT return a string
waiting_list.sort(reverse=True)
#  .sort(reverse=True) is for descending order
#   Change True to False if u want ascending
#     .sort() is set to do ascending

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.title()}"
    print(row)
"""

"""
# Ex 19
kg = float(input("How heavy?"))
lbs =  kg * 2.2
print(lbs)
"""
"""
# Ex 20 Adding to Txt what we done

todos = []
while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo:") + "\n"
# we use a break line to separate words in our txt, "\n" is a special symbol that converts into a break line
            todos.append(todo)
            file = open('todos.txt','w')
            file.writelines(todos)
# writelines is a method that will write the list todos into the txt file
#  "w" above means "write" and "r" would mean "read"
        case 'show' | 'display':
            for index, item in enumerate(todos):
                item = item.title()
                row = f"{index+1}.{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
print("Thanks,bye !")
"""

"""
# Ex 21  Now we make a list that wont overwrite itself


while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo:") + "\n"
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
# It's GOOD practice to close the file each time u did an operation in it, to avoid mistakes etc
# Also the cursor in the txt file might stay behind after the last item and when u want to read u will get nothing because cursor is at the end, reason why u need to close file after each operation
# we use a break line to separate words in our txt, "\n" is a special symbol that converts into a break line
            todos.append(todo)
            file = open('todos.txt','w')
            file.writelines(todos)
            file.close()
# writelines is a method that will write the list todos into the txt file
#  "w" above means "write" and "r" would mean "read"
        case 'show' | 'display':
            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
            # the for loop adds by itself break line
                item = item.title()
                row = f"{index+1}.{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
print("Thanks,bye !")


# If u take the txt file and drop it in a different folder it will refactor the new directory in the code
# This above is done by PyCharm
"""

# Experiment

# Run in console
# How to open txt file in python :
# file = open(r"C:\Users\Robert\Desktop\SQL\Final query cu 2 subiecte.txt",'r')
# enter above then enter this : file.read() to read it
# 'r' is placed in front of the path to recognise it as a string

"""
# Ex 22 This code will create the 3txts when run

contents = ["Outside rains.","the grass is green!","I'm delighted :)"]

filenames = ["doc.txt",
             "report.txt",
             "presentation.txt"]

for content, filename in zip(contents,filenames):
#zip will take the data i give and create and return a new object, but i need list() to read it
    file = open(f"Rob's directory for test/{filename}",'w')
#the open function will create the files and also overwrite if the files already exist
# u can use open(f"../files/{filename}",'w') with 2 dots after f" to go up one level in upper directory, that's what the 2 dots do
#we use a "f" string because we need to open the filepath and also mention the variable "filename"
    file.write(content)
"""
"""
# Ex 22 This code will replace strings in filenames

filenames = ["1.doc","1.report","1.present"]

filenames = [filename.replace('.','-') + '.txt' for filename in filenames]

print(filenames)
"""

"""
# Ex 23  Improvements

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo:") + "\n"
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)
            file = open('todos.txt','w')
            file.writelines(todos)
            file.close()

        case 'show' | 'display':
            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()
            

            Method 1
            new_todos = []
            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)
                
                
            #Method 2
            new_todos = [item.strip('\n') for item in todos]
#This will create a new list without the break slashes
# u can see how they looked before with breaks using print(todos)

            for index, item in enumerate(new_todos):
# the for loop adds by itself break line
                item = item.title()
                row = f"{index+1}.{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
print("Thanks,bye !")
                """
"""
# Ex 24  Improvements

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo:") + "\n"
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)
            file = open('todos.txt','w')
            file.writelines(todos)
            file.close()

        case 'show' | 'display':
            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
# the for loop adds by itself break line
                item = item.strip('\n')
                item = item.title()
                row = f"{index+1}.{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
print("Thanks,bye !")
"""
"""
# Ex 25  Improvements

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo:") + "\n"
# With is favorable because you wont have file opened in case the program stops,
            # a better way than to open a file then close it
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

        case 'show' | 'display':

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
# the for loop adds by itself break line
                item = item.strip('\n')
                item = item.title()
                row = f"{index+1}.{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todo to complete: "))
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
                index = number -1
                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        case 'exit':
            break
print("Thanks,bye !")
"""
"""
# Experiment

with open("Rob's directory for test/doc.txt") as file:
    # the mode in open is set to "r" by default
    # that's why above the open runs without "r"
    print(file.read())
"""
"""
# Ex 26

date = input("Enter today's date: ")
mood = input("Rate your mood of today from 1 to 10 ")
thoughts = input("Let your thoughts flow:\n")

with open(f"Journal/{date}.txt","w") as file:
    mood1 = mood + 2 * "\n"
    file.write(f"Mood is rated : {mood1}")
    file.write(thoughts)
"""
"""
# Ex 25  Improvements

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()
    # we selected the whole statements with if then shift tab to indent them outside in the while block
    if 'add' in user_action or 'new' in user_action:
        todo = user_action[4:]
        # the 4 colon gives us the part after 'add'
        # its called list slicing
        # example user_action[4:9] will give characters between 4 and 9
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            todos = file.writelines(todos)

# Using else statement speeds up the program

    elif 'show' in user_action:

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f"{index+1}.{item}"
            print(row)
    elif 'edit' in user_action:
        number = int(user_action[5:])
        #number used is for position 5
        print(number)
        number = number - 1
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        message = f"Todo {todo_to_remove} was removed from the list."
        print(message)
    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid !")
print("Thanks,bye !")

# We learned today add, or, not in operators

"""
"""
# Ex 26 program that checks the strength of a password

password = input("New Password: ")
result = {}

if len(password) >= 8:
# We won't use elif because it needs to check multiple criteria to be applied (more ifs)
    result["length"] = True
else:
    result["length"] = False

digit = False
#we set it as false to change it if condition is true
for i in password:
    if i.isdigit():
    #isdigit checks if input is a digit
        digit = True

result["digits"] = digit

#the logic is that We asume something is false
# then we try to prove it to be true

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["Upper-case"] = uppercase

print(result)
print(result.values())

#we use .values() to check all values inside
if all(result.values()):
#we change all(result) == True: with all(result):
# because it is implied to be true
    print ("Strong password !")
else:
    print ("Weak password !")
# all converts all boolean data types into one,
# if one is False then all are False
# Reminder or,and,not in are boolean operators

#New info: a = [14,20] is a list,
# but b = {"height":14, "width":20} is a dictionary
# dictionaries are important to know what each data is
# a[1] gives 14 but b["width"] gives 20
# for dictionaries we dont use append when we add we use
# example : result["length"] to add values in it

"""
"""
# Ex 27  Improvements

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
# we now use the function .startswith to avoid errors
# if key words are inside the input

        todo = user_action[4:]
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            todos = file.writelines(todos)

# Using else statement speeds up the program

    elif user_action.startswith("show"):

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}.{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            # we change the error message
            print("Your command is not valid.")
            continue #used to start the program from begining
            # instead of continuing it

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
                index = number -1
                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except (IndexError, ValueError):
            print("Item not found.")
        continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid !")
print("Thanks,bye !")
"""
"""
#Experiment

try:
        width = float(input("Width: "))
        length = float(input("Length: "))

        if width == length:
            print("That looks bad")
            exit("That looks bad")
# string inside exit() will show error msg in red

        area = width * length
        print(area)
except ValueError:
    print("Enter a number.")
"""

"""
# Ex 27  Custom functions

def get_todos():
    with open('todos.txt','r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# not recommended to use same variable local inside function
# so we renamed it to todos_local
# same thing with file inside get_todos


while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            todos = file.writelines(todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}.{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:

            print("Your command is not valid.")
            continue


    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except (IndexError, ValueError):
            print("Item not found.")
        continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid !")
print("Thanks,bye !")
"""
"""
# Code experiment

def greet():
    message = "hello"
    new_message = message.capitalize()
    print("Hey")
    return new_message

greeting = greet()
print(len(greeting))
"""
"""
# Ex 28 Argument example

def greet(message):
    new_message = message.capitalize()
    print("Hey hey")
    return new_message

user_entry = input("Type stuff:")
greeting = greet(user_entry)
print(greeting)
"""

"""
# Ex 29  Function arguments


def get_todos(filepath):
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
# this function behaves as a procedure, that's why it has no return


while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos('todos.txt')

        todos.append(todo + '\n')

        write_todos("todos.txt", todos)

    elif user_action.startswith("show"):

        todos = get_todos('todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}.{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = get_todos('todos.txt')

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos("todos.txt", todos)
        except ValueError:

            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos('todos.txt')
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos("todos.txt", todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except (IndexError, ValueError):
            print("Item not found.")
        continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid !")
print("Thanks,bye !")
"""
"""
# Ex 30 Bonus exercise

feet_inches = input("Enter feet and inches: ")


def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    meters = feet * 0.3048 + inches * 0.0254
#    return f"{feet} feet and {inches} inches is equal to {meters} meters"
# The concept of decupling means
# that we need to take out only 1 value from this big string above
    return meters


result = convert(feet_inches)

if result < 1:
    print(f"{int(result)} meters Kid is too small.")
else:
    print(f"{int(result)} meters Kid can use the slide.")

# i added to the print message to print also
# the value and made it in f string,
# instead of just the print msg :)
# now i will add int to remove decimals :)
"""

"""
# Ex 31  Default arguments

# Whenever u do a process just put it in a function !


def get_todos(filepath="todos.txt"):
    # we assign filepath = todos.txt as default argument
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

# print(help(get_todos()))


# we add here also todos.txt

def write_todos(todos_arg, filepath="todos.txt"):
    # because now filepath = todos.txt is default parameter and todos_arg non default parameter,
    # we need to put it before filepath,
    # but now we need to change list before filepath in all code with the new order
    # Or you need to write (filepath = todos.txt, todos_arg=todos) in all
    # which is too much to write and not recommended
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# this function behaves as a procedure, that's why it has no return


while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()
        # now we remove todos.txt
        # because we added it inside the function def as a default argument

        todos.append(todo + '\n')

        # Now we write write_todos(todos, "todos.txt") as below :
        write_todos(todos)
        # because the file is predefined so just mention the list

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:

            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except (IndexError, ValueError):
            print("Item not found.")
        continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid !")
print("Thanks,bye !")
"""

"""
# Code experiment

text = """
# I am happy     #i added # because they arent turned off by """ outside the code
# Yes i am

# 1993
"""

print(text)

#triple quotes auto insert breaklines for each line
# as if i would type "I am happy \n" for each line
"""

"""
# Ex 32 Bonus exercise

feet_inches = input("Enter feet and inches: ")


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}
    # we used a dictionary above


def convert(feet, inches):
# we now change with values inside convert

    meters = feet * 0.3048 + inches * 0.0254
#    return f"{feet} feet and {inches} inches is equal to {meters} meters"
# The concept of decupling means
# that we need to take out only 1 value from this big string above
    return meters

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])


print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters")

if result < 1:
    print(f"{int(result)} meters Kid is too small.")
else:
    print(f"{int(result)} meters Kid can use the slide.")
"""

# Ex 33 Module

import functions
import time
# method recommended when u have few functions

# if we use "import functions"
# we will need to put functions.get_todos() and functions.write_todos() in all our code
# just like we would use methods
# Second method is good only if we have a lot of functions
# and that might be a hassle for first method

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()
        # now we remove todos.txt
        # because we added it inside the function def as a default argument

        todos.append(todo + '\n')

        # Now we write write_todos(todos, "todos.txt") as below :
        functions.write_todos(todos)
        # because the file is predefined so just mention the list

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:

            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except (IndexError, ValueError):
            print("Item not found.")
        continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid !")
print("Thanks,bye !")

# Setting the app
#we can install packages with terminal command


