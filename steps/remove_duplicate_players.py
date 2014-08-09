import sqlite3 as sql
import os


def remove_duplicate_players():

    print 'Removing duplicate players...'

    database_path = os.path.abspath('../archive.db')

    con = sql.connect(database_path)
    cur = con.cursor()

    cur.execute('CREATE TABLE Temp AS SELECT * FROM Players GROUP BY Name')
    con.commit()

    cur.execute('DROP TABLE Players')
    con.commit()

    cur.execute('ALTER TABLE Temp RENAME TO Players')
    con.commit()

    print 'Duplicates removed.'

if __name__ == '__main__':
    remove_duplicate_players()
