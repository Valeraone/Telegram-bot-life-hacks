import sqlite3
import random


def living():

    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        x = random.randint(1, 8)

        if x == 1:
            query = cursor.execute("""SELECT text FROM living WHERE id = 1""")
        elif x == 2:
            query = cursor.execute("""SELECT text FROM living WHERE id = 2""")
        elif x == 3:
            query = cursor.execute("""SELECT text FROM living WHERE id = 3""")
        elif x == 4:
            query = cursor.execute("""SELECT text FROM living WHERE id = 4""")
        elif x == 5:
            query = cursor.execute("""SELECT text FROM living WHERE id = 5""")
        elif x == 6:
            query = cursor.execute("""SELECT text FROM living WHERE id = 6""")
        elif x == 7:
            query = cursor.execute("""SELECT text FROM living WHERE id = 7""")
        elif x == 8:
            query = cursor.execute("""SELECT text FROM living WHERE id = 8""")
        query = cursor.fetchone()
        return query[0]


def kitchen():

    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        x = random.randint(1, 6)

        if x == 1:
            query = cursor.execute("""SELECT text FROM kitchen WHERE id = 1""")
        elif x == 2:
            query = cursor.execute("""SELECT text FROM kitchen WHERE id = 2""")
        elif x == 3:
            query = cursor.execute("""SELECT text FROM kitchen WHERE id = 3""")
        elif x == 4:
            query = cursor.execute("""SELECT text FROM kitchen WHERE id = 4""")
        elif x == 5:
            query = cursor.execute("""SELECT text FROM kitchen WHERE id = 5""")
        elif x == 6:
            query = cursor.execute("""SELECT text FROM kitchen WHERE id = 6""")
        query = cursor.fetchone()
        return query[0]


def travel():
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        x = random.randint(1, 4)

        if x == 1:
            query = cursor.execute("""SELECT text FROM travel WHERE id = 1""")
        elif x == 2:
            query = cursor.execute("""SELECT text FROM travel WHERE id = 2""")
        elif x == 3:
            query = cursor.execute("""SELECT text FROM travel WHERE id = 3""")
        elif x == 4:
            query = cursor.execute("""SELECT text FROM travel WHERE id = 4""")
        query = cursor.fetchone()
        return query[0]


def google():
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        x = random.randint(1, 4)

        if x == 1:
            query = cursor.execute("""SELECT text FROM google WHERE id = 1""")
        elif x == 2:
            query = cursor.execute("""SELECT text FROM google WHERE id = 2""")
        elif x == 3:
            query = cursor.execute("""SELECT text FROM google WHERE id = 3""")
        elif x == 4:
            query = cursor.execute("""SELECT text FROM google WHERE id = 4""")
        query = cursor.fetchone()
        return query[0]
