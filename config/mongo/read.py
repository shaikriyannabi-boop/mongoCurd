from database.database import collection

def read_db():
    employees = collection.find()

    print("\nEmployees:\n")

    for emp in employees:
        print(emp)
    if collection.count_documents({}) == 0:
        print("No employees found.\n")
