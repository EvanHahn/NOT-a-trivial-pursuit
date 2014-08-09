from bs4 import BeautifulSoup
from requests import get
import os
import parsedatetime
import re
import sexmachine.detector as sexmachine
import sqlite3 as sql


def populate_tables():

    # MAX_GAME_ID = 4596
    # MAX_PLAYER_ID = 9268

    MAX_GAME_ID = 1

    database_path = os.path.abspath('archive.db')

    con = sql.connect(database_path)
    cur = con.cursor()

    gender_detector = sexmachine.Detector()

    for game_id in xrange(1, MAX_GAME_ID + 1):

        print 'Parsing game ' + str(game_id) + '...'

        game_url = ('http://www.j-archive.com/showgame.php?game_id=' +
                    str(game_id))

        r = get(game_url)
        if r.status_code != 200:
            print 'Error in game ' + str(game_id)
            continue

        soup = BeautifulSoup(r.text)

        comments = soup.find(id='game_comments').text
        date = soup.title.text[-10:]

        player_els = soup.find_all('p', class_='contestants')
        for player_el in player_els:
            player_link = player_el.find('a')
            player_name = player_link.text
            player_gender = gender_detector.get_gender(player_name.split()[0])
            player_id = re.sub(r'\D', '', player_link['href'])
            cur.execute('INSERT OR IGNORE INTO Players (Id, Name, Gender) '
                        'VALUES (?, ?, ?)', (
                            player_id,
                            player_name,
                            player_gender
                        ))

    con.commit()
    con.close()
