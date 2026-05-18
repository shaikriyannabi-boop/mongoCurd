from database.postgresql import cursor, conn

def create_db():
    name=input("Enter name: ")
    role=input("Enter role: ")
    salary=int(input("Enter salary: "))

    create_postgre_db(name, role, salary)
    print("employee inserted in PostgreSQL")

def create_postgre_db(name, role, salary):
    cursor.execute(
        "INSERT INTO employees (name, role, salary) VALUES (%s, %s, %s)",
        (name, role, salary)
    )

    conn.commit()
