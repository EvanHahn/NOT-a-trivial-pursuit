import sqlite3 as sql
import os


def _url_for_id(id):
    return 'http://www.j-archive.com/showplayer.php?player_id=' + str(id)


def the_gender_binary():

    print 'Manually classifying genders...'

    database_path = os.path.abspath('../archive.db')

    con = sql.connect(database_path)
    cur = con.cursor()

    cur.execute('SELECT * FROM Players WHERE Gender = "andy" or (Gender <> "female" and Gender <> "male")')

    unknown_genders = cur.fetchall()

    for player in unknown_genders:

        id, name, classification = player

        check = classification.split('_')
        if check[0] == 'mostly':
            classification = check[1]

        while ((classification != 'male') and
               (classification != 'female') and
               (classification != 'skip')):
            print name,
            print 'was classified as',
            print classification
            print _url_for_id(id)
            classification = raw_input('What gender? ')

        if classification != 'skip':
            cur.execute('UPDATE Players SET Gender=? WHERE Id=?',
                        (classification, id))
            con.commit()

    con.close()

    print 'Genders classified.'

if __name__ == '__main__':
    the_gender_binary()
