
"""Automatisiert die Berechnungen von Biostar"""


import subprocess
import os
import time

from subprocess import Popen
#from PIL import ImageGrab #gebraucht um Screenshot zu machen



StartTime = time.clock() # allerster timestamp

#CO2 Konzentrationen fuer jedes Jahr als dictionary abspeichern. Keys sind int 
CO2dict = {2000:370, 2001:373, 2002:375, 2003:377, 2004:379, 2005:381, 2006:383, 2007:384, 2008:386, 2009:388, 2010:390,
           2011:393, 2012:395, 2013:398, 2014:400, 2015:403, 2016:405, 2017:408, 2018:410, 2019:413, 2020:415,
           2021:419, 2022:422, 2023:426, 2024:429, 2025:433, 2026:436, 2027:440, 2028:443, 2029:447, 2030:450,
           2031:455, 2032:459, 2033:464, 2034:468, 2035:473, 2036:477, 2037:482, 2038:486, 2039:491, 2040:495,
           2041:500, 2042:504, 2043:509, 2044:513, 2045:518, 2046:522, 2047:527, 2048:531, 2049:536, 2050:540,
           2051:544, 2052:547, 2053:551, 2054:554, 2055:558, 2056:561, 2057:565, 2058:568, 2059:572, 2060:575,
           2061:579, 2062:582, 2063:586, 2064:589, 2065:593, 2066:596, 2067:600, 2068:603, 2069:607, 2070:610,
           2071:614, 2072:618, 2073:622, 2074:626, 2075:630, 2076:634, 2077:638, 2078:642, 2079:646, 2080:650,
           2081:653, 2082:656, 2083:659, 2084:662, 2085:665, 2086:668, 2087:671, 2088:674, 2089:677, 2090:680,
           2091:683, 2092:686, 2093:689, 2094:692, 2095:695, 2096:698, 2097:701, 2098:704, 2099:707}


#Liste mit den Namen der einzelnen Datenbanken
DBlist = ["2001_2010.accdb", "2011_2020.accdb", "2021_2030.accdb", "2031_2040.accdb", "2041_2050.accdb",
          "2051_2060.accdb", "2061_2070.accdb", "2071_2080.accdb", "2081_2090.accdb", "2091_2099.accdb"]


Java = "C:/Programme/Java/jdk1.7.0_03/bin/Java.exe" # Pfad der Java.exe
jarFile = "Biostar.jar"                             # Name der .jar Datei
os.chdir("D:/Test/Biostar")                         # Pfad der .jar Datei
DBdir = "D:/Test4/"  # Pfad der Datenbanken
Fruit = "Maize_f"                                     # Zu berechnende Feldfrucht


def defDB(a):
    if a in range(2001, 2011):
        return DBlist[0]
    elif a in range(2011, 2021):
        return DBlist[1]
    elif a in range(2021, 2031):
        return DBlist[2]
    elif a in range(2031, 2041):
        return DBlist[3]
    elif a in range(2041, 2051):
        return DBlist[4]
    elif a in range(2051, 2061):
        return DBlist[5]
    elif a in range(2061, 2071):
        return DBlist[6]
    elif a in range(2071, 2081):
        return DBlist[7]
    elif a in range(2081, 2091):
        return DBlist[8]
    else:
        return DBlist[9]

#Start und Endjahr+1 eintragen
for i in range(2001, 2100, 4):

    StartProcTime = time.clock()                    # Timestamp pro Schleife

    iStr = str(i)

    i2 = i+1
    i3 = i+2
    i4 = i+3
    #i5 = i+4
    
                                     # aktuelle Tabelle in der DB
    #CO2 = str(CO2dict[i])                           # CO2 Konzentration in ppm aus CO2dict
    CO2 = "390"
    
    
    #CO2_5 = str(CO2dict[i+4])

    
    DBfile = defDB(i)
    DBfile2 = defDB(i2)
    DBfile3 = defDB(i3)
    DBfile4 = defDB(i4)
    #DBfile5 = defDB(i5)
    
    
    Table = str(i)
    Table2 = str(i2)
    Table3 = str(i3)
    Table4 = str(i4)
    #Table5 = str(i5)
    
    
    #Aufrufen des Java Prozesses und uebergeben der Argumente
    p1 = subprocess.Popen(Java + " -jar " + jarFile + " " + DBdir + DBfile + " " \
                          + Table + " " + Fruit + " 115 300 2.1 100 0.1 0.1 " + CO2 + " 0 0 0")
    
    if i < 2099:
         CO2_2 = str(CO2dict[i+1])
         p2 = subprocess.Popen(Java + " -jar " + jarFile + " " + DBdir + DBfile2 + " " \
                          + Table2 + " " + Fruit + " 115 300 2.1 100 0.1 0.1 " + CO2 + " 0 0 0")
    else:
        continue

    if i < 2098:
         CO2_3 = str(CO2dict[i+2])
         p3 = subprocess.Popen(Java + " -jar " + jarFile + " " + DBdir + DBfile3 + " " \
                          + Table3 + " " + Fruit + " 115 300 2.1 100 0.1 0.1 " + CO2 + " 0 0 0")
    else:
        continue

    if i < 2097:
         CO2_4 = str(CO2dict[i+3])
         p4 = subprocess.Popen(Java + " -jar " + jarFile + " " + DBdir + DBfile4 + " " \
                          + Table4 + " " + Fruit + " 115 300 2.1 100 0.1 0.1 " + CO2 + " 0 0 0")
    else:
        continue

    #if i < 2096:
    #     p5 = subprocess.Popen(Java + " -jar " + jarFile + " " + DBdir + DBfile5 + " " \
    #                      + Table5 + " " + Fruit + " 115 300 2.1 100 0.1 0.1 " + CO2_5 + " 0 0 0")
    #else:
    #    continue


    Popen.wait(p1)              #Wartet bis p1 beendet ist
    Popen.wait(p2)              #Wartet bis p2 beendet ist
    Popen.wait(p3)              #Wartet bis p3 beendet ist
    Popen.wait(p4)              #Wartet bis p4 beendet ist


    EndTime = time.clock()
    Dauer = str(int((EndTime-StartProcTime)/60))
    print "Jahre " + Table + "-" + Table4 + " beendet nach " + Dauer + " Minuten." + " Frucht: " + Fruit + " CO2: " + CO2






DBdir = "D:/Test3/"  # Pfad der Datenbanken
Fruit = "Sflower" 
    

for i in range(2001, 2100, 4):

    StartProcTime = time.clock()                    # Timestamp pro Schleife

    iStr = str(i)

    i2 = i+1
    i3 = i+2
    i4 = i+3
    #i5 = i+4
    
                                     # aktuelle Tabelle in der DB
    #CO2 = str(CO2dict[i])                           # CO2 Konzentration in ppm aus CO2dict
    CO2 = "390"
    
    
    #CO2_5 = str(CO2dict[i+4])

    
    DBfile = defDB(i)
    DBfile2 = defDB(i2)
    DBfile3 = defDB(i3)
    DBfile4 = defDB(i4)
    #DBfile5 = defDB(i5)
    
    
    Table = str(i)
    Table2 = str(i2)
    Table3 = str(i3)
    Table4 = str(i4)
    #Table5 = str(i5)
    
    
    #Aufrufen des Java Prozesses und uebergeben der Argumente
    p1 = subprocess.Popen(Java + " -jar " + jarFile + " " + DBdir + DBfile + " " \
                          + Table + " " + Fruit + " 115 300 2.1 100 0.1 0.1 " + CO2 + " 0 0 0")
    
    if i < 2099:
         CO2_2 = str(CO2dict[i+1])
         p2 = subprocess.Popen(Java + " -jar " + jarFile + " " + DBdir + DBfile2 + " " \
                          + Table2 + " " + Fruit + " 115 300 2.1 100 0.1 0.1 " + CO2 + " 0 0 0")
    else:
        continue

    if i < 2098:
         CO2_3 = str(CO2dict[i+2])
         p3 = subprocess.Popen(Java + " -jar " + jarFile + " " + DBdir + DBfile3 + " " \
                          + Table3 + " " + Fruit + " 115 300 2.1 100 0.1 0.1 " + CO2 + " 0 0 0")
    else:
        continue

    if i < 2097:
         CO2_4 = str(CO2dict[i+3])
         p4 = subprocess.Popen(Java + " -jar " + jarFile + " " + DBdir + DBfile4 + " " \
                          + Table4 + " " + Fruit + " 115 300 2.1 100 0.1 0.1 " + CO2 + " 0 0 0")
    else:
        continue

    #if i < 2096:
    #     p5 = subprocess.Popen(Java + " -jar " + jarFile + " " + DBdir + DBfile5 + " " \
    #                      + Table5 + " " + Fruit + " 115 300 2.1 100 0.1 0.1 " + CO2_5 + " 0 0 0")
    #else:
    #    continue


    Popen.wait(p1)              #Wartet bis p1 beendet ist
    Popen.wait(p2)              #Wartet bis p2 beendet ist
    Popen.wait(p3)              #Wartet bis p3 beendet ist
    Popen.wait(p4)              #Wartet bis p4 beendet ist


    EndTime = time.clock()
    Dauer = str(int((EndTime-StartProcTime)/60))
    print "Jahre " + Table + "-" + Table4 + " beendet nach " + Dauer + " Minuten." + " Frucht: " + Fruit + " CO2: " + CO2
 

