import config.config as cfg


def update_db():
    name=input("Enter name to update: ")
    new_salary=int(input("Enter new salary: "))

    if cfg.db_type == "mongo":
        result=cfg.get_mongo().update_one(
            {"name": name},
            {"$set": {"salary": new_salary}}
        )

        if result.modified_count > 0:
            print("Employee updated successfully")
        else:
            print("No employee found with that name")
    elif cfg.db_type == "postgre":
        cfg.make_table()
        cur=cfg.get_post_cursor()
        conn=cfg.get_post_conn()

        cur.execute(
            "UPDATE employees SET salary=%s WHERE name=%s",
            (new_salary, name)
        )

        conn.commit()

        if cur.rowcount > 0:
            print("Employee updated successfully")
        else:
            print("No employee found with that name")
    else:
        print("Invalid database type")
