
lst = [['Adrian', 'kat', 'hond', 'cavia', 'muis'], ['Noortje', 'pinguins', 'paarden', 'bijen'], ['Jan', 'kut']]

userName = "Noortje"




def find_userlist():
    userFound = False
    print("*** Welcome " + userName + " ****")

    for (i, x) in enumerate(lst):
        print(lst[i][0])
        if lst[i][0] == userName:
            print("user found: " + lst[i][0])
            list = lst[i]
            userFound = True
            print(list)
            break

find_userlist()