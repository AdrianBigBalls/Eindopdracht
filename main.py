# Eindopdracht Adrian
import menus

print("**** Reminder List ****")
userName = input("please enter your username:")

if userName == "":
    print("Username not entered, exiting the program...")

print("Welcome " + userName + ", please make a choice in the menu:")

menus.print_menu()