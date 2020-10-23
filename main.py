# Eindopdracht Adrian
import menus
import database

print("**** Reminder List ****")
userName = input("please enter your username:")
if userName == "":
    exit("Username not entered, exiting the program...")

#print("Welcome " + userName + ", please make a choice in the menu:")
currentUserIndex = 0


def find_userlist():
    global currentUserIndex
    userFound = False
    print("*** Welcome " + userName + " ****")
    for (user_index, x) in enumerate(database.mainList):
        print(database.mainList[user_index][0])
        if database.mainList[user_index][0] == userName:
            print("user found: " + database.mainList[user_index][0])
            menus.myList = database.mainList[user_index]
            currentUserIndex = user_index
            userFound = True
            break

    if not userFound:
        menus.myList.append(userName)
        database.mainList.append(menus.myList)
        currentUserIndex = (len(database.mainList) - 1)


def save_list():
    print("Saving the list....")
    database.mainList[currentUserIndex] = menus.myList
    menus.print_menu()


database.read()
find_userlist()
menus.print_menu()
database.write()

#print(database.mainList[0][0])
#menus.print_menu()

