import urllib
import re
import bggBazaSQLite as baza
import sys
from xml.dom import minidom
import logging 



logging.basicConfig(fileName="log.log", level=logging.DEBUG)



NAZWA_PLIKU_XML=sys.argv[1]+'.xml'
baza.StworzBazeSQLite(sys.argv[1])

logging.debug("Rozpoczecie sciaganie statystyk dla " + sys.argv[1])

strona=urllib.urlopen('http://boardgamegeek.com/xmlapi2/plays?username='+sys.argv[1]).read()
plik=open(NAZWA_PLIKU_XML,'w')
plik.write(strona)
plik.close()
DOMTree = minidom.parse(NAZWA_PLIKU_XML)
TOTAL = DOMTree.getElementsByTagName("plays")[0].getAttribute("total")
PAGES= int(TOTAL) % 100
logging.debug("Ilosc stron do pobrania " + str(PAGES))
for p in range(PAGES):
 logging.debug("Sciaganie strony nr " + str(p))
 strona=urllib.urlopen('http://boardgamegeek.com/xmlapi2/plays?username='+sys.argv[1]+'&page='+str(p+1)).read()
 plik=open(NAZWA_PLIKU_XML,'w')
 plik.write(strona)
 plik.close()
 DOMTree = minidom.parse(NAZWA_PLIKU_XML)
 cNodes = DOMTree.getElementsByTagName("play")
 for i in cNodes:
  id=i.getAttribute("id")
  location=i.getAttribute("location")
  data=i.getAttribute("date")
  game=i.getElementsByTagName("item")[0].getAttribute("name")
  cNodes2 = i.getElementsByTagName("players")
  if (cNodes2):
   for j in i.getElementsByTagName("player"):
    username=j.getAttribute("username")
    name=j.getAttribute("name")
    startposition= j.getAttribute("startposition")
    color= j.getAttribute("color")
    score= j.getAttribute("score")
    new= j.getAttribute("new")
    rating= j.getAttribute("rating")
    win= j.getAttribute("win")
    baza.WstawDoBazySQLiteJednaPartie(sys.argv[1],game,id,name,username,new,startposition,color,score,win,rating,location,data)







