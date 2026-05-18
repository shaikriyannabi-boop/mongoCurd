from database.postgresql import cursor, conn

def delete_postgre_db():
    name=input("Enter name to delete: ")

    cursor.execute(
        "DELETE FROM employees WHERE name=%s",
        (name,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Employee deleted successfully")
    else:
        print("No employee found with that name")
