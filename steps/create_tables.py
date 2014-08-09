import sqlite3 as sql
import os

def create_tables():

    print 'Creating tables...'

    database_path = os.path.abspath('archive.db')

    con = sql.connect(database_path)
    cur = con.cursor()

    cur.execute('CREATE TABLE Players(Id INT PRIMARY KEY, Name TEXT, Gender TEXT)')
    cur.execute('CREATE TABLE Games(Id INT PRIMARY KEY, Date TEXT, Comments TEXT)')
    cur.execute('CREATE TABLE Scores(Game_Id INT, Player_Id INT, Wagered_Score INT, Coryat_Score INT)')

    con.close()

    print 'Tables created.'
