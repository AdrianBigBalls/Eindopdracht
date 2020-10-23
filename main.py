# Eindopdracht Adrian



print("**** Reminder List ****")
userName = input("please enter your username:")
if userName == "":
    exit("Username not entered, exiting the program...")

#print("Welcome " + userName + ", please make a choice in the menu:")
currentUserIndex = 0
mainList = []
myList = []

def write():
    with open('data.txt', 'w+') as file:
        if not file.closed:
            for (userindex, x) in enumerate(mainList):
                for (listindex, y) in enumerate(mainList[userindex]):
                    if listindex == 0:
                        file.write('#' + mainList[userindex][listindex] + '\n')
                    else:
                        file.write(mainList[userindex][listindex] + '\n')
                file.write('%' + '\n')
        else:
            print("cant write in file!!")


def read():
    userList = []
    with open('data.txt', 'r') as file:
        if not file.closed:
            for item in file:
                if item.startswith('#'):
                    item = item[1:][:-1]
                    userList.append(item)

                elif item.startswith('%'):
                    mainList.append(userList.copy())
                    userList.clear()

                else:
                    item = item[:-1]
                    userList.append(item)
        else:
            print("cant read file!!")


def find_userlist():
    global myList
    global currentUserIndex
    userFound = False
    print("*** Welcome " + userName + " ****")
    for (user_index, x) in enumerate(mainList):
        print(mainList[user_index][0])
        if mainList[user_index][0] == userName:
            print("user found: " + mainList[user_index][0])
            myList = mainList[user_index]
            currentUserIndex = user_index
            userFound = True
            break

    if not userFound:
        myList.append(userName)
        mainList.append(myList)
        currentUserIndex = (len(mainList) - 1)


def save_list():
    print("Saving the list....")
    mainList[currentUserIndex] = myList
    print_menu()


def print_menu():
    print(" 1 - Print list\n 2 - Add to list\n 3 - Delete from list\n 4 - Save list\n 5 - Quit")
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
        return
    else:
        print("Not a valid choice, exiting...")
        exit()

def print_list():

    if len(myList) > 0:
        for i in myList:
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
    item = input("Enter an item to add to your list: ")
    myList.append(item)
    print("  You added " + item + " to your list\n")
    print_menu()


def delete_item():
    print("     **** Delete Item ****\nSelect an index number to delete: ")
    if len(myList) > 0:
        for (i, x) in enumerate(myList):
            print(i, x)
        item = int(input())
        myList.pop(item)
        print_menu()
    else:
        print("NO ITEMS TO DELETE! - Returning.")
        print_menu()




read()
find_userlist()
print_menu()
write()

#print(database.mainList[0][0])
#menus.print_menu()