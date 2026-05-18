import config.config as cfg
from database.create import create_db
from database.delete import delete_db
from database.read import read_db
from database.update import update_db


def choose_db():
    while True:
        print("\nSelect Database")
        print("1. MongoDB")
        print("2. PostgreSQL")

        db=input("Enter database choice: ")

        try:
            return cfg.set_db_type(db)
        except ValueError:
            print("Invalid choice, please try again.")


def start():
    choose_db()

    while True:
        print("\nCurrent Database:", cfg.db_type)
        print("1. Create Employee")
        print("2. Read Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Switch Database")
        print("6. Exit")

        choice=input("Enter your choice: ")

        if choice == "1":
            create_db()
        elif choice == "2":
            read_db()
        elif choice == "3":
            update_db()
        elif choice == "4":
            delete_db()
        elif choice == "5":
            choose_db()
        elif choice == "6":
            break
        else:
            print("Invalid choice, please try again.")


start()
