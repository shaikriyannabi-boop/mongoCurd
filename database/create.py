import config.config as cfg


def create_db():
    name=input("Enter name: ")
    role=input("Enter role: ")
    salary=int(input("Enter salary: "))

    if cfg.db_type == "mongo":
        data={
            "name": name,
            "role": role,
            "salary": salary
        }

        result=cfg.get_mongo().insert_one(data)

        print("employee inserted in MongoDB")
        print("MongoDB ID:", result.inserted_id)
    elif cfg.db_type == "postgre":
        cfg.make_table()
        cur=cfg.get_post_cursor()
        conn=cfg.get_post_conn()

        cur.execute(
            "INSERT INTO employees (name, role, salary) VALUES (%s, %s, %s)",
            (name, role, salary)
        )

        conn.commit()
        print("employee inserted in PostgreSQL")
    else:
        print("Invalid database type")
