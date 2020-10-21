# Eindopdracht Adrian
import menus
import database

print("**** Reminder List ****")
userName = input("please enter your username:")

if userName == "":
    exit("Username not entered, exiting the program...")

print("Welcome " + userName + ", please make a choice in the menu:")

database.read()
menus.print_menu()
#database.write()

