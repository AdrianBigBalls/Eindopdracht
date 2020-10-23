
mainList = []


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


