import sqlite3
from colorama import init, Fore, Style

init()

def main():
    print(Fore.GREEN + Style.BRIGHT + "----- welcome to the school's grading system -----")
    print()
    print("To get started please tell us if you are trying to connect to a exisiting class or make a new one?")
    choice = input("Answer (Connect or New): ")

    if choice == "connect" or "Connect" or "Conn" or "conn":
        print()
    
    if choice == "new" or "New":
        base = input("What would you like to call the new database?: " + Style.RESET_ALL)
        database = base + ".db"
        conn = sqlite3.connect(database)
        cursor = conn.cursor()


main()