import menus

mainList = []

def write():
    with open('data.txt', 'w+') as file:
        if file.closed == False:
            for i in menus.myList:
                file.write(i+ '\n')
        else:
            print("cant write in file!!")

def read():
    userList = []
    with open('data.txt', 'r') as file:
        if file.closed == False:
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
