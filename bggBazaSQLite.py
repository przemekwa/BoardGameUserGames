import sqlite3 as sql


def StworzBazeSQLite(NAZWA_PLIKU_BAZY):
 con= sql.connect(NAZWA_PLIKU_BAZY+'.db')
 cur=con.cursor()
 cur.execute('CREATE TABLE IF NOT EXISTS PARTIE(LINK)')
 cur.execute('CREATE TABLE IF NOT EXISTS PARTIA(NAZWA TEXT,IDPARTI INT,PLAYER TEXT,USER TEXT,NEW INT,POSITION INT,TEAM,SCORE INT,WIN INT,RATING INT,LOCATION TEXT,DATA)')




def WstawDoBazySQLitePartie(NAZWA_PLIKU_BAZY,element):
 con= sql.connect(NAZWA_PLIKU_BAZY+'.db')
 cur=con.cursor()
 cur.execute('insert into PARTIE (LINK) values ("'+element+'")')
 con.commit()

def WstawDoBazySQLiteJednaPartie(NAZWA_PLIKU_BAZY,NAZWA,IDPARTI,PLAYER,USER,NEW,POSITION,TEAM,SCORE,WIN,RATING,LOCATION,DATA):
 con= sql.connect(NAZWA_PLIKU_BAZY+'.db')
 cur=con.cursor()
 cur.execute('insert into PARTIA (NAZWA,IDPARTI,PLAYER,USER,NEW,POSITION,TEAM,SCORE,WIN,RATING,LOCATION) values ("'+NAZWA+'","'+IDPARTI+'","'+PLAYER+'","'+USER+'","'+NEW+'","'+POSITION+'","'+TEAM+'","'+SCORE+'","'+WIN+'","'+RATING+'","'+LOCATION+'","'+DATA+'"   )')
 con.commit()
