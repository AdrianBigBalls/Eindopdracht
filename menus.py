import database


myList = []


def print_menu():
    print(" 1 - Print list\n 2 - Add to list\n 3 - Delete from list\n 4 - Quit")
    choice = int(input())
    if choice == 1:
        print_list()
    elif choice == 2:
        add_item()
    elif choice == 3:
        delete_item()
    elif choice == 4:
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
    database.write()
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


