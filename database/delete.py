import config.config as cfg


def delete_db():
    name=input("Enter name to delete: ")

    if cfg.db_type == "mongo":
        result=cfg.get_mongo().delete_one({"name": name})

        if result.deleted_count > 0:
            print("Employee deleted successfully")
        else:
            print("No employee found with that name")
    elif cfg.db_type == "postgre":
        cfg.make_table()
        cur=cfg.get_post_cursor()
        conn=cfg.get_post_conn()

        cur.execute(
            "DELETE FROM employees WHERE name=%s",
            (name,)
        )

        conn.commit()

        if cur.rowcount > 0:
            print("Employee deleted successfully")
        else:
            print("No employee found with that name")
    else:
        print("Invalid database type")
