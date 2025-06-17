import sqlite3
from colorama import init, Fore, Style
import tabulate
import time
import sys

init()

def addStudent():
    student = input(Fore.GREEN + Style.BRIGHT + "Student Name: ")
    subject = input(Fore.GREEN + Style.BRIGHT + "Class Subject: ")
    grade = input(Fore.GREEN + Style.BRIGHT + "Student's grade in the class: ")

    cur.execute("INSERT INTO students (name, subject, grade) VALUES (?, ?, ?)", (student, subject, grade))
    conn.commit()
    conn.close()
    print()
    time.sleep(1)
    print(Fore.GREEN + Style.BRIGHT + "Added " + student + " to the class.")
    print()
    time.sleep(1)
    main()

def viewAll():
    headers = ["Id", "Name", "Subject", "Grade"]
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    print()
    print(tabulate.tabulate(data, headers=headers))
    print()

def main():
    print(Fore.GREEN + Style.BRIGHT + "----- Welcome to the school's class management system -----")
    print()
    print("To get started please tell us the name of the class")
    print()
    
    global base
    base = input("Name: " + Style.RESET_ALL)
    if base == "/end":
        sys.exit()
    global database
    database = base + ".db"
    global conn

    try:
        conn = sqlite3.connect(database)
    except sqlite3.OperationalError:
        print(Fore.RED + Style.BRIGHT + "Invalid Database File Name" + Style.RESET_ALL)

    global cur
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            subject TEXT,
            grade REAL
        );
    """)
    time.sleep(1)
    ch = input(Fore.GREEN + Style.BRIGHT + "Would you like to add a new student or look for student records?: " + Style.RESET_ALL)
        
    if "add" in ch:
        addStudent()
    
    if "look" in ch or "record" in ch:
        ch2 = input(Fore.GREEN + Style.BRIGHT + "Would you like to view all records or search for a student?: " + Style.RESET_ALL)
        
        if "all" in ch2:
            viewAll()
        
        if "search" in ch2:
            pass

        if "all" in ch2 and "search" in ch2:
            print(Fore.RED + Style.BRIGHT + "Program couldn't understand please try again" + Style.RESET_ALL)
            main()
        
        else:
            print(Fore.RED + Style.BRIGHT + "Program couldn't understand please try again" + Style.RESET_ALL)
            main()

    else:
        pass


main()