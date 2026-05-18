from database.database import collection

def create_db():
    name=input("Enter name: ")  
    role=input("Enter role: ")
    salary=int(input("Enter salary: "))

    employee={
        "name": name,
        "role": role,
        "salary": salary
    }

    result=collection.insert_one(employee)

    print("employee inserted in MongoDB")
    print("MongoDB ID:", result.inserted_id)
