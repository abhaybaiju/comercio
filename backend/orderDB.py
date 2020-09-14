import sqlite3
from sqlite3 import Error

conn = None
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    global conn
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection('omsdb.db')

