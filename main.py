from config.mongo.create import create_db as create_mongo_db
from config.mongo.read import read_db as read_mongo_db
from config.mongo.update import update_db as update_mongo_db
from config.mongo.delete import delete_db as delete_mongo_db
from config.postgre.create1 import create_db as create_postgre_db
from config.postgre.read1 import read_postgre_db
from config.postgre.update1 import update_postgre_db
from config.postgre.delete1 import delete_postgre_db

from database.postgresql import cursor, conn

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    role VARCHAR(100),
    salary INTEGER
)
""")

conn.commit()

def select_database():
    while True:
        print("\nSelect Database")
        print("1. MongoDB")
        print("2. PostgreSQL")

        db_choice=input("Enter database choice: ").strip().lower()

        if db_choice == "1" or db_choice == "mongo" or db_choice == "mongodb":
            return "mongo"
        elif db_choice == "2" or db_choice == "postgre" or db_choice == "postgres" or db_choice == "postgresql":
            return "postgre"
        else:
            print("Invalid choice, please try again.")

selected_db=select_database()

while True:

    print("\nCurrent Database:", selected_db)
    print("1. Create Employee")
    print("2. Read Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Switch Database")
    print("6. Exit")

    choice=input("Enter your choice: ")

    if choice == "1":
        if selected_db == "mongo":
            create_mongo_db()
        else:
            create_postgre_db()
    elif choice == "2":
        if selected_db == "mongo":
            read_mongo_db()
        else:
            read_postgre_db()
    elif choice == "3":
        if selected_db == "mongo":
            update_mongo_db()
        else:
            update_postgre_db()
    elif choice == "4":
        if selected_db == "mongo":
            delete_mongo_db()
        else:
            delete_postgre_db()
    elif choice == "5":
        selected_db=select_database()
    elif choice == "6":
        break
    else:
        print("Invalid choice, please try again.")
