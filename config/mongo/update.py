from database.database import collection

def update_db():
    name=input("Enter name to update: ")
    new_salary=int(input("Enter new salary: "))
    result=collection.update_one({"name": name}, {"$set": {"salary": new_salary}})
    if result.modified_count > 0:
        print("Employee updated successfully")
    else:
        print("No employee found with that name")
