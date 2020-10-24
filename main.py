# Adrian Overdijk - ID1G4a.
# With this program you will be able to store a list and save it to a file.
# The lists are stored and loaded per individual user.
# It also has a simple calculator functionality
import datetime
from operator import pow, truediv, mul, add, sub

# Start of program, username is required.
print("**** Reminder List ****")
user_name = input("please enter your username:")
if user_name == "":
    exit("Username not entered, exiting the program...")

current_user_index = 0
main_list = []
my_list = []


# Reads data.txt into user_list until % is seen. Then user_list is read into main_list as a nested list.
# This results in a nested list per user in main_list.
def read():
    user_list = []
    with open('data.txt', 'r') as file:
        if not file.closed:
            for item in file:
                if item.startswith('#'):
                    item = item[1:][:-1]
                    user_list.append(item)
                elif item.startswith('%'):
                    main_list.append(user_list.copy())
                    user_list.clear()
                else:
                    item = item[:-1]
                    user_list.append(item)
        else:
            print("cant read file!!")


# This function displays a welcome message with the current time and date.
# It also loops through main_list and compares user_name with the first element of each nested list.
# When it finds an existing user, it reads corresponding nested list from main_list to my_list.
# If it doesn't find a registered user_name it will create a new user in my_list.
def find_userlist():
    global my_list
    global current_user_index
    user_found = False
    now = datetime.datetime.now()
    print("\n\n  **** Welcome " + user_name + " ****")
    print("The current time and date is: ")
    print(now.strftime("    %Y-%m-%d %H:%M:%S"))
    for (user_index, x) in enumerate(main_list):
        if main_list[user_index][0] == user_name:
            my_list = main_list[user_index]
            current_user_index = user_index
            user_found = True
            break

    if not user_found:
        my_list.append(user_name)
        main_list.append(my_list)
        current_user_index = (len(main_list) - 1)


def write():
    with open('data.txt', 'w+') as file:
        if not file.closed:
            for (userindex, x) in enumerate(main_list):
                for (listindex, y) in enumerate(main_list[userindex]):
                    if listindex == 0:
                        file.write('#' + main_list[userindex][listindex] + '\n')
                    else:
                        file.write(main_list[userindex][listindex] + '\n')
                file.write('%' + '\n')
        else:
            print("cant write in file!!")


def print_menu():
    print("\n      **** Main menu ****\nChoose one of the following options:\n")
    print("  1 - Print list\n  2 - Add to list\n  3 - Delete from list")
    print("  4 - Save list\n  5 - Calculator\n  6 - Exit program")
    choice = int(input())
    if choice == 1:
        print_list()
    elif choice == 2:
        add_item()
    elif choice == 3:
        delete_item()
    elif choice == 4:
        save_list()
    elif choice == 5:
        calculator()
    elif choice == 6:
        return
    else:
        print("Not a valid choice, exiting...")
        exit()


def print_list():
    if len(my_list) > 0:
        for i in sorted(my_list):
            print("* ", i)
    else:
        print("Your list is empty. Returning\n\n")
        print_menu()
    choice = input("Press M to go back the menu")
    if choice == "m" or choice == "M":
        print_menu()
    else:
        exit("Invalid choice, quitting....")


def add_item():
    print("      **** Add Item ****")
    item = input("Enter an item to add to your list.\nStart with the date YYYY-MM-DD followed by a whitespace: ")
    my_list.append(item)
    print("  You added " + item + " to your list\n")
    print_menu()


def delete_item():
    print("     **** Delete Item ****\nSelect an index number to delete: ")
    if len(my_list) > 0:
        for (i, x) in enumerate(my_list):
            print(i, x)
        item = int(input())
        my_list.pop(item)
        print_menu()
    else:
        print("NO ITEMS TO DELETE! - Returning.")
        print_menu()


def save_list():
    print("Saving the list....")
    main_list[current_user_index] = my_list
    print_menu()


######################################
operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
    '^': pow
}


def calculate(s):
    if s.isdigit():
        return float(s)
    for c in operators.keys():
        left, operator, right = s.partition(c)
        if operator in operators:
            return operators[operator](calculate(left), calculate(right))


def calculator():
    calc = input("**** CALCULATOR ****\nType calculation:\n")
    print("Answer: " + str(calculate(calc)))
    print_menu()


##################################

read()
find_userlist()
print_menu()
write()
