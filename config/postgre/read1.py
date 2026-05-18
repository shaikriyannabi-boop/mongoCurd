from database.postgresql import cursor, conn

def read_postgre_db():
    cursor.execute("SELECT * FROM employees")

    rows = cursor.fetchall()

    print("\nEmployees:\n")

    if len(rows) == 0:
        print("No employees found.\n")
        return

    for row in rows:
        print(row)
