
"""Automatisiert die Berechnungen von Biostar
Im Vergleich zu Biostar_2.py wird hier der Saatzeitpunkt fuer die Sommergetreide angepasst und nicht standardmaessig auf
25.4. gelegt
Die Berechnung findet nur statt, wenn der 25.4. (Tag 115) nicht bereits in der Standardmodellierung der Starttermin war
"""


import subprocess
import os
import time

from subprocess import Popen


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


#Saattermin bei 8 Grad Temperatur
seed8Deg = {2001:115, 2002:115, 2003:115, 2004:115, 2005:115, 2006:115, 2007:115, 2008:115, 2009:115, 2010:115,
            2011:115, 2012:115, 2013:115, 2014:115, 2015:115, 2016:115, 2017:115, 2018:115, 2019:115, 2020:115,
            2021:115, 2022:115, 2023:115, 2024:115, 2025:115, 2026:115, 2027:115, 2028:115, 2029:115, 2030:115,
            2031:115, 2032:115, 2033:105, 2034:105, 2035:105, 2036:115, 2037:95, 2038:115, 2039:105, 2040:115,
            2041:95, 2042:105, 2043:105, 2044:105, 2045:115, 2046:115, 2047:105, 2048:115, 2049:105, 2050:95,
            2051:105, 2052:115, 2053:105, 2054:105, 2055:95, 2056:115, 2057:105, 2058:95, 2059:105, 2060:105,
            2061:85, 2062:95, 2063:95, 2064:105, 2065:105, 2066:105, 2067:95, 2068:95, 2069:95, 2070:105,
            2071:95, 2072:95, 2073:75, 2074:85, 2075:85, 2076:65, 2077:65, 2078:95, 2079:85,
            2080:65, 2081:95, 2082:95, 2083:105, 2084:85, 2085:95, 2086:95, 2087:95, 2088:105, 2089:95,
            2090:95, 2091:85, 2092:95, 2093:95, 2094:85, 2095:85, 2096:85, 2097:85, 2098:85, 2099:65}

#Saattermin bei 10 Grad Temperatur
seed10Deg = {2001:115, 2002:125, 2003:115, 2004:125, 2005:125, 2006:125, 2007:125, 2008:125, 2009:125, 2010:115,
            2011:125, 2012:125, 2013:125, 2014:125, 2015:125,2016:125, 2017:125, 2018:125, 2019:125, 2020:125,
             2021:115, 2022:115, 2023:115, 2024:115, 2025:125, 2026:115, 2027:135, 2028:125, 2029:125, 2030:125,
            2031:115, 2032:115, 2033:125, 2034:115, 2035:125, 2036:115, 2037:115, 2038:125, 2039:125, 2040:115,
            2041:105, 2042:125, 2043:115, 2044:105, 2045:115, 2046:115, 2047:115, 2048:115, 2049:115, 2050:115,
            2051:115, 2052:115, 2053:115, 2054:115, 2055:115, 2056:125, 2057:115, 2058:115, 2059:115, 2060:115,
            2061:105, 2062:115, 2063:115, 2064:115, 2065:115, 2066:115, 2067:115, 2068:115, 2069:115, 2070:115,
            2071:105, 2072:95, 2073:115, 2074:95, 2075:115, 2076:105, 2077:115, 2078:115, 2079:115, 2080:115,
            2081:115, 2082:115, 2083:115, 2084:115, 2085:115, 2086:115, 2087:115, 2088:115, 2089:115, 2090:115,
            2091:115, 2092:105, 2093:115, 2094:115, 2095:115, 2096:115, 2097:115, 2098:105, 2099:105}

#Saattermin bei 12 Grad Temperatur
seed12Deg = {2001:135, 2002:135, 2003:145, 2004:135, 2005:125, 2006:145, 2007:125, 2008:135, 2009:125, 2010:135,
            2011:135, 2012:135, 2013:135, 2014:135, 2015:135, 2016:135, 2017:135, 2018:145, 2019:135, 2020:135,
            2021:125, 2022:135, 2023:135, 2024:135, 2025:135, 2026:135, 2027:135, 2028:145, 2029:135, 2030:125,
            2031:125, 2032:135, 2033:135, 2034:125, 2035:125, 2036:125, 2037:135, 2038:125, 2039:125, 2040:125,
            2041:125, 2042:125, 2043:125, 2044:125, 2045:125, 2046:135, 2047:135, 2048:135, 2049:125, 2050:125,
            2051:125, 2052:125, 2053:125, 2054:125, 2055:125, 2056:125, 2057:125, 2058:125, 2059:115, 2060:125,
            2061:115, 2062:125, 2063:125, 2064:125, 2065:125, 2066:125, 2067:125, 2068:125, 2069:125, 2070:125,
            2071:115, 2072:125, 2073:115, 2074:115, 2075:115, 2076:125, 2077:115, 2078:115, 2079:115, 2080:115,
            2081:125, 2082:125, 2083:125, 2084:115, 2085:125, 2086:115, 2087:125, 2088:125, 2089:125, 2090:115,
            2091:125, 2092:115, 2093:125, 2094:125, 2095:125, 2096:115, 2097:115, 2098:125, 2099:115}





#Liste mit den Namen der einzelnen Datenbanken
DBlist = ["2001_2010.accdb", "2011_2020.accdb", "2021_2030.accdb", "2031_2040.accdb", "2041_2050.accdb",
          "2051_2060.accdb", "2061_2070.accdb", "2071_2080.accdb", "2081_2090.accdb", "2091_2099.accdb"]


Java = "C:/Programme/Java/jdk1.7.0_03/bin/Java.exe" # Pfad der Java.exe
jarFile = "Biostar.jar"                             # Name der .jar Datei
os.chdir("D:/Test/Biostar")                         # Pfad der .jar Datei


DBdir = "D:/Test6/"  # Pfad der Datenbanken
Fruit = "S-Wheat"                                     # Zu berechnende Feldfrucht


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


#Liste in der Jahre stehen der Saatpunkt von 115 abweicht
seedList = []
for i in range(2001,2100):
    if seed8Deg[i] is not 115:
        seedList.append(i)


#Start und Endjahr+1 eintragen
#for i in range(2001, 2100, 4):
for j in range(0,len(seedList),4):

    StartProcTime = time.clock()                    # Timestamp pro Schleife

    

    i = seedList[j]
    if seedList[j] < 2099:
        i2 = seedList[j+1]
    if seedList[j] < 2098:
        i3 = seedList[j+2]
    if seedList[j] < 2097:
        i4 = seedList[j+3]
    #i5 = i+4

    iStr = str(i)

    
    
                                     # aktuelle Tabelle in der DB
    CO2 = str(CO2dict[i])           # CO2 Konzentration in ppm aus CO2dict
    CO2_2 = str(CO2dict[i2])
    CO2_3 = str(CO2dict[i3])
    CO2_4 = str(CO2dict[i4])
    #CO2 = "390"
    
    #Saatzeitpunkt waehlen
    date = str(seed8Deg[i])
    date_2 = str(seed8Deg[i2])
    date_3 = str(seed8Deg[i3])
    date_4 = str(seed8Deg[i4])
    
    

    
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
                          + Table + " " + Fruit +  " " + date + " " + "300 2.1 100 0.1 0.1 " + CO2 + " 0 0 0")
    
    if i2 <= 2099:
         p2 = subprocess.Popen(Java + " -jar " + jarFile + " " + DBdir + DBfile2 + " " \
                          + Table2 + " " + Fruit +  " " + date_2 + " " + "300 2.1 100 0.1 0.1 " + CO2_2 + " 0 0 0")
    else:
        continue
    
    if i3 <= 2098:
         p3 = subprocess.Popen(Java + " -jar " + jarFile + " " + DBdir + DBfile3 + " " \
                          + Table3 + " " + Fruit +  " " + date_3 + " " + "300 2.1 100 0.1 0.1 " + CO2_3 + " 0 0 0")
    else:
        continue
    

    if i4 <= 2097:
         p4 = subprocess.Popen(Java + " -jar " + jarFile + " " + DBdir + DBfile4 + " " \
                          + Table4 + " " + Fruit +  " " + date_4 + " " + "300 2.1 100 0.1 0.1 " + CO2_4 + " 0 0 0")
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
    print "Jahre " + Table + ", " + Table2 + ", " + Table3 + ", " + Table4 + " beendet nach " + Dauer + \
          " Minuten." + " Frucht: " + Fruit + " CO2: " + CO2 + ", " + CO2_2 + ", " + CO2_3 + ", " + CO2_4 + \
          " STARTDAY: " + date + ", " + date_2 + ", " + date_3 + ", " + date_4
