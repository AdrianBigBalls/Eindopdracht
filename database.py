

def write():
    with open('data.txt', 'w+') as file:
        if file.closed == False:
            file.write("1\n2\n3\n4\n5")
        else:
            print("cant write in file!!")

def read():
    with open('data.txt', r) as file:
        if file.closed == False:

        else:
            print("cant read file!!")