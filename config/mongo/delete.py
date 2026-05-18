from database.database import collection

def delete_db():
    name=input("Enter name to delete: ")
    result=collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print("Employee deleted successfully")
    else:
        print("No employee found with that name")
