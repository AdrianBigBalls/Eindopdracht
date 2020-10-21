# Eindopdracht Adrian
import menus
import database

print("**** Reminder List ****")
userName = input("please enter your username:")

if userName == "":
    exit("Username not entered, exiting the program...")

#print("Welcome " + userName + ", please make a choice in the menu:")

def find_userlist():
    userFound = False
    print("*** Welcome " + userName + " ****")

    for (i, x) in enumerate(database.mainList):
        print(database.mainList[i][0])
        if database.mainList[i][0] == userName:
            print("user found: " + database.mainList[i][0])
            menus.myList = database.mainList[i]
            userFound = True
            print(menus.myList)
            break

database.read()
print(database.mainList)
find_userlist()
menus.print_menu()

#print(database.mainList[0][0])
#menus.print_menu()
#database.write()
