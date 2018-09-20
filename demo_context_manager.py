import contextlib
import sqlite3
#
# connect = sqlite3.connect('/tmp/database.sqlite')
# try:
#     try:
#         cursor = connect.cursor()
#         cursor.execute("""
#             CREATE TABLE  IF NOT EXISTS person
#             (id INTEGER PRIMARY KEY AUTOINCREMENT,
#             firstname varchar,
#             lastname varchar
#             )""")
#
#         connect.commit()
#     except Exception:
#         connect.rollback()
#     try:
#         cursor = connect.cursor()
#         cursor.execute('INSERT INTO person(firstname, lastname) VALUES(?,?)',('Stephane', 'Wirtel'))
#         connect.commit()
#     except Exception:
#         connect.rollback()
#
# finally:
#     connect.close()
#
# with sqlite3.connect('/tmp/database.sqlite') as conn:
#     with conn.cursor() as cur:
#         cursor.execute("""
#                     CREATE TABLE  IF NOT EXISTS person
#                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     firstname varchar,
#                     lastname varchar
#                     )""")
#         connect.commit()
#
#     with conn.cursor() as cur:
#         cursor.execute('INSERT INTO person(firstname, lastname) VALUES(?,?)',('Stephane', 'Wirtel'))
#         connect.commit()



@contextlib.contextmanager
def transaction(conn):
    try:
        print("J'ouvre un curseur")
        cursor = conn.cursor()
        yield cursor
        print("Je commit ma transaction")
        conn.commit()
    except Exception:
        print("Je rollback ma transaction")
        conn.rollback()


with sqlite3.connect('/tmp/database.sqlite') as conn:
    with transaction(conn) as cur:
        cur.execute("""
                    CREATE TABLE  IF NOT EXISTS person 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    firstname varchar, 
                    lastname varchar
                    )""")
        cur.execute('INSERT INTO person(firstname, lastname) VALUES(?,?)',('Stephane', 'Wirtel'))


@contextlib.contextmanager
def raises(ExceptionType):
    """ Equivalent au with raises de pytest on veut verif qu'on raise un exception donnee!"""
    try:
        # ici on appelle la partie de code a tester
        yield
        # pas d'exception
        raise Exception('On attendait une exception')
    # le code a genere l'exception attendue
    except ExceptionType:
        pass