import menus

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
                #print("* ", item, end='')
                if item.startswith('#'):
                    print("starts with a hashtag")
                    item = item[1:][:-1]
                    userList.append(item)
                    print(userList)
                elif item.startswith('%'):
                    print("found a Percentage sign")
                else:
                    print("Found an item")
        else:
            print("cant read file!!")