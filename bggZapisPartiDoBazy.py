
import urllib
import re
import bggBazaSQLite as baza

def WstawDoBazy(numer):
 vNAZWA=""
 stronaParti=urllib.urlopen('http://boardgamegeek.com/play/details/'+str(numer)).read()

 plikParti=open('bggwwwParti','w')
 plikParti.write(stronaParti)
 plikParti.close()
 plikParti=open('bggwwwParti')

 imie=0 
 new=0
 position=0
 team=0
 score=0
 win=0
 ranting=0


 for linia in plikParti: 
  

  if ranting==2:
   vRANTING=str(linia.replace("	","").rstrip())
   print vNAZWA,vIMIE,vUSER,vNEW,vPOSITION,vTEAM,vSCORE,vWIN,vRANTING
   baza.WstawDoBazySQLiteJednaPartie(vNAZWA,numer,vIMIE,vUSER,vNEW,vPOSITION,vTEAM,vSCORE,vWIN,vRANTING)
   vPOSITION=""
   vTEAM=""
   vSCORE=""
   vWIN=""
   vRANTING=""
   vUSER=""
   ranting=0
  


  if ranting==1:
   q = re.search('<td align=\'center\'>',linia)
   if q:
    ranting=2


  if win==2:
   if re.search('<img',linia):
    vWIN =1
   else:
    vWIN=0
  
  
   win=0
   ranting=1

  if win==1:
   s = re.search('<td align=\'center\'>',linia)
   if s:
    win=2


  if score==2:
   vSCORE=int(linia.replace("	","").rstrip())
  
  
   score=0
   win=1

  if score==1:
   r = re.search('<td align=\'center\'>',linia)
   if r:
    score=2


  if team==2:
   vTEAM=str(linia.replace("	","").rstrip())
   team=0
   score=1


  if team==1:
   p = re.search('<td align=\'center\'>',linia)
   if p:
    team=2



  if position==2:
   vPOSITION=linia.replace("	","").rstrip()
   
   position=0
   team=1
 
  if position==1:
   o = re.search('<td align=\'center\'>',linia)
   if o:
    position=2
  

  if new==2:
   if re.search('<img',linia):
    vNEW = str(1)
   else:
    vNEW=str(0)
  
   new=0 
   position=1


  if imie==2:
   a = re.search('>[a-zA-z0-9 ]*<',linia)
   if a:
    vUSER = a.group()[1:-1]
   else:
    vUSER = 'N/A'
   new=1
   imie=0



#wyluskanie imienia
  if imie==1:
   vIMIE= str(linia.replace("	","").rstrip())
   imie=2
   
   
  if new==1:
   n = re.search('<td align=\'center\'>',linia)
   if n:
    new=2

 

#imie1
  m = re.search('<td align=\'left\'>',linia)
  x= re.search('<title>[^|]*',linia)
  if m:
     imie=1
  if x:
    vNAZWA=str(x.group(0)[7:])
  

 plikParti.close()
