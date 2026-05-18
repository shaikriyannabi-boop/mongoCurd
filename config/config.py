from os import getenv

import psycopg2
from pymongo import MongoClient


db_type = getenv("DB_TYPE")

mongo_url = getenv("MONGO_URI")
mongo_db = getenv("MONGO_DATABASE")
mongo_collection = getenv("MONGO_COLLECTION")

post_host = getenv("POSTGRES_HOST")
post_db = getenv("POSTGRES_DATABASE")
post_user = getenv("POSTGRES_USER")
post_password = getenv("POSTGRES_PASSWORD")
post_port = getenv("POSTGRES_PORT")

mongo_client = None
collection = None
post_conn = None
post_cursor = None


if db_type is None:
    db_type = "mongo"
else:
    db_type = db_type.strip().lower()


def check(value, name):
    if value is None or value == "":
        value=input("Enter " + name + ": ")

    return value


def set_db_type(db):
    global db_type

    db = db.strip().lower()

    if db == "1" or db == "mongo" or db == "mongodb":
        db_type = "mongo"
    elif db == "2" or db == "postgre" or db == "postgres" or db == "postgresql":
        db_type = "postgre"
    else:
        raise ValueError("Invalid database type")

    return db_type


def get_mongo():
    global mongo_client, collection, mongo_url, mongo_db, mongo_collection

    if collection is None:
        mongo_url=check(mongo_url, "MONGO_URI")
        mongo_db=check(mongo_db, "MONGO_DATABASE")
        mongo_collection=check(mongo_collection, "MONGO_COLLECTION")

        mongo_client = MongoClient(mongo_url)
        db = mongo_client[mongo_db]
        collection = db[mongo_collection]

    return collection


def get_post_conn():
    global post_conn, post_host, post_db, post_user, post_password, post_port

    if post_conn is None:
        post_host=check(post_host, "POSTGRES_HOST")
        post_db=check(post_db, "POSTGRES_DATABASE")
        post_user=check(post_user, "POSTGRES_USER")
        post_password=check(post_password, "POSTGRES_PASSWORD")
        post_port=check(post_port, "POSTGRES_PORT")

        post_conn = psycopg2.connect(
            host=post_host,
            database=post_db,
            user=post_user,
            password=post_password,
            port=int(post_port)
        )

    return post_conn


def get_post_cursor():
    global post_cursor

    if post_cursor is None:
        post_cursor = get_post_conn().cursor()

    return post_cursor


def make_table():
    cur = get_post_cursor()
    conn = get_post_conn()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        role VARCHAR(100),
        salary INTEGER
    )
    """)

    conn.commit()
