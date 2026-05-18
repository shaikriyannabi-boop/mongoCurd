from database.postgresql import cursor, conn

def update_postgre_db():
    name=input("Enter name to update: ")
    new_salary=int(input("Enter new salary: "))

    cursor.execute(
        "UPDATE employees SET salary=%s WHERE name=%s",
        (new_salary, name)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Employee updated successfully")
    else:
        print("No employee found with that name")
