import menus
import database


userName = "Adrian"


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


def write():
    with open('output.txt', 'w+') as file:
        if not file.closed:
            for i in menus.myList:
                file.write(i + '\n')
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
                    database.mainList.append(userList.copy())
                    userList.clear()

                else:
                    item = item[:-1]
                    userList.append(item)
        else:
            print("cant read file!!")


read()
find_userlist()
