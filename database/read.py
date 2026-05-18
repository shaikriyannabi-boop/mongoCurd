import config.config as cfg


def read_db():
    print("\nEmployees:\n")

    if cfg.db_type == "mongo":
        col=cfg.get_mongo()
        employees=col.find()

        for emp in employees:
            print(emp)

        if col.count_documents({}) == 0:
            print("No employees found.\n")
    elif cfg.db_type == "postgre":
        cfg.make_table()
        cur=cfg.get_post_cursor()

        cur.execute("SELECT * FROM employees")
        rows=cur.fetchall()

        if len(rows) == 0:
            print("No employees found.\n")
            return

        for row in rows:
            print(row)
    else:
        print("Invalid database type")
