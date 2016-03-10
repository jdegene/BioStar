
#Schreibt die Informationen zum Bodentyp in 14 1dm Felder

#Vorbereitung: BUK50 Tabelle in .csv umwandeln
#Schichtgrenze // in + umwandeln, damit ein einzelnes Zeichen vorliegt

#Zuerst werden 7 Faelle und 2 Sonderfaelle ueber Regeln abgehandelt,
#so dass alle Boeden mit max 3 eingetragenen Schichten abgedeckt sind!
#Alle anderen wurden anschliessend manuell eingetragen


import os

dirX = "C:/Test/Boden/"
dirOut = "C:/Test/Boden/Output/"

#Listet alle validen Bodenarten auf
TypeList = ("ff", "hh", "hn", "ss", "ls", "us", "su", "lu", "tu", "sl",
            "ll", "tl", "ut", "lt")


#Generiet bzw. nutzt eine neue Datei als Output
w = open(dirOut + "BodenFini.txt", "a")

#Laed die Datei mit den urspruenglichen Daten
f = open(dirX + "BodenLeer1.csv", "r")
d = f.read().split()


#Erste Zeile der neuen Datei schreiben
w.write("FL_NR, HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7," +
        "HOR8, HOR9, HOR10, HOR11, HOR12, HOR13, HOR14 \n")

#Funktion die jeweilige Abfolge in Datei schreibt
def InTxt(iStr, a,b,c,d,e,f,g,h,j,k,l,m,n,o,p,q):

    w.write(iStr + " , " + a + " , " + b + " , " + c + " , " + d + " , "\
            + e + " , " + f + " , " + g + " , " +
            h + " , " + j + " , " + k + " , " + l + " , " + \
            m + " , " + n + " , " + o + " , " + p + " , " + q + "\n")

#Einzelne Horizonte Schritt fuer Schritt berechnen


k = 0


for i in range(1, 91016, 1):
    iStr = str(i)

    bType = d[i][7:]   # Waehlt den Bodentyp Teil des jeweiligen Wortes aus


    #####################################################################################
    ###Fall 1: Es ist nur EINE Sache eingetragen die EIN valider Bodentyp ist
    #####################################################################################

    if len(bType) == 2 and bType in list(TypeList):

        HOR1= HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = \
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #####################################################################################
    ###Fall 2: Es ist nur EINE Schicht eingetragen, die KEIN valider Bodentyp ist
    #####################################################################################

    elif (len(bType) == 2 and bType not in list(TypeList)) or bType == "xxx":

        HOR1= HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = \
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 = =HOR15 =HOR16 "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #####################################################################################
    ###Fall 3: Es sind ZWEI Schichten eingetragen, die BEIDE valide Bodentypen sind
    #####################################################################################

        #Fuer \  == 10dm
    elif len(bType) == 5 and (bType[0:2] and bType[3:5] in list(TypeList)) \
            and bType[2] == "\\" :

        HOR1 = bType[0:2]
        HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = \
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[3:5]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer / == 30dm
    elif len(bType) == 5 and (bType[0:2] and bType[3:5] in list(TypeList)) \
            and bType[2] == "/" :
        
        HOR1 = HOR2 = HOR3 = bType[0:2]
        HOR4= HOR5= HOR6= HOR7 = \
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[3:5]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer + (eigentlich //) == 60dm
    elif len(bType) == 5 and (bType[0:2] and bType[3:5] in list(TypeList)) \
            and bType[2] == "+" :
        
        HOR1 = HOR2 = HOR3 = HOR4= HOR5= HOR6=  bType[0:2]
        HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[3:5]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer = == 110dm
    elif len(bType) == 5 and (bType[0:2] and bType[3:5] in list(TypeList)) \
            and bType[2] == "=" :

        HOR1 = HOR2 = HOR3 = HOR4= HOR5= HOR6= \
        HOR7 = HOR8= HOR9= HOR10= HOR11 = bType[0:2]
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[3:5]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer _ == 170dm
    elif len(bType) == 5 and (bType[0:2] and bType[3:5] in list(TypeList)) \
            and bType[2] == "_" :

        HOR1= HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = \
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[0:2]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #####################################################################################
    ###Fall 4: Es sind ZWEI Schichten eingetragen, nur die ERSTE ist ein valider Bodentyp
    #####################################################################################

        #Fuer \  == 10dm
    elif len(bType) == 5 and (bType[0:2] and bType[3:5] not in list(TypeList)) \
            and bType[2] == "\\" :

        HOR1 = bType[0:2]
        HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = \
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16  = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer / == 30dm
    elif len(bType) == 5 and (bType[0:2] and bType[3:5] not in list(TypeList)) \
            and bType[2] == "/" :
        
        HOR1 = HOR2 = HOR3 = bType[0:2]
        HOR4= HOR5= HOR6= HOR7 = \
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer + (eigentlich //) == 60dm
    elif len(bType) == 5 and (bType[0:2] and bType[3:5] not in list(TypeList)) \
            and bType[2] == "+" :
        
        HOR1 = HOR2 = HOR3 = HOR4= HOR5= HOR6=  bType[0:2]
        HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer = == 110dm
    elif len(bType) == 5 and (bType[0:2] and bType[3:5] not in list(TypeList)) \
            and bType[2] == "=" :

        HOR1 = HOR2 = HOR3 = HOR4= HOR5= HOR6= \
        HOR7 = HOR8= HOR9= HOR10= HOR11 = bType[0:2]
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer _ == 170dm
    elif len(bType) == 5 and (bType[0:2] and bType[3:5] not in list(TypeList)) \
            and bType[2] == "_" :

        HOR1= HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = \
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[0:2]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)
        



    #####################################################################################
    ###Fall 5: Es sind DREI Schichten eingetragen, alle DREI sind ein valider Bodentyp
    #####################################################################################

        #Fuer \  == 10dm und \ == 10dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] and bType[6:8] in list(TypeList)) \
            and bType[2] == "\\" and bType[5] == "\\" :

        HOR1 = bType[0:2]
        HOR2= bType[3:5]
        HOR3 = HOR4= HOR5= HOR6= HOR7 = \
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[6:8]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer \  == 10dm und / == 30dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] and bType[6:8] in list(TypeList)) \
            and bType[2] == "\\" and bType[5] == "/" :

        HOR1 = bType[0:2]
        HOR2= HOR3= bType[3:5]
        HOR4= HOR5= HOR6= HOR7 = \
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[6:8]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer \  == 10dm und + == 60dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] and bType[6:8] in list(TypeList)) \
            and bType[2] == "\\" and bType[5] == "+" :

        HOR1 = bType[0:2]
        HOR2= HOR3= HOR4= HOR5= HOR6= bType[3:5]
        HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[6:8]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer \  == 10dm und = == 110dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] and bType[6:8] in list(TypeList)) \
            and bType[2] == "\\" and bType[5] == "=" :

        HOR1 = bType[0:2]
        HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= HOR11=bType[3:5]
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[6:8]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer \  == 10dm und _ == 170dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] and bType[6:8] in list(TypeList)) \
            and bType[2] == "\\" and bType[5] == "_" :

        HOR1 = bType[0:2]
        HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= HOR11= \
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[3:5]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #------------------------------------------------------------------------------------#

        #Fuer / == 30dm und / == 30dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] and bType[6:8] in list(TypeList)) \
            and bType[2] == "/" and bType[5] == "/" :

        HOR1 = HOR2= HOR3= bType[0:2]
        HOR4= bType[3:5]
        HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[6:8]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer / == 30dm und + == 60dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] and bType[6:8] in list(TypeList)) \
            and bType[2] == "/" and bType[5] == "+" :

        HOR1 = HOR2= HOR3= bType[0:2]
        HOR4= HOR5= HOR6= bType[3:5]
        HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[6:8]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)
        

        #Fuer / == 30dm und = == 110dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] and bType[6:8] in list(TypeList)) \
            and bType[2] == "/" and bType[5] == "=" :

        HOR1 = HOR2= HOR3= bType[0:2]
        HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= HOR11= bType[3:5]
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[6:8]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer / == 30dm und _ == 170dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] and bType[6:8] in list(TypeList)) \
            and bType[2] == "/" and bType[5] == "_" :

        HOR1 = HOR2= HOR3= bType[0:2]
        HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= HOR11= \
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[3:5]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #------------------------------------------------------------------------------------#
        
        #Fuer + == 60dm und + == 60dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] and bType[6:8] in list(TypeList)) \
            and bType[2] == "+" and bType[5] == "+" :

        HOR1 = HOR2= HOR3= HOR4= HOR5= HOR6= bType[0:2]
        HOR7 = HOR8= bType[3:5]
        HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[6:8]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer + == 60dm und = == 110dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] and bType[6:8] in list(TypeList)) \
            and bType[2] == "+" and bType[5] == "=" :

        HOR1 = HOR2= HOR3= HOR4= HOR5= HOR6= bType[0:2]
        HOR7 = HOR8= HOR9= HOR10= HOR11= bType[3:5]
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[6:8]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer + == 60dm und _ == 170dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] and bType[6:8] in list(TypeList)) \
            and bType[2] == "+" and bType[5] == "_" :

        HOR1 = HOR2= HOR3= HOR4= HOR5= HOR6= bType[0:2]
        HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[3:5]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #------------------------------------------------------------------------------------#

        #Fuer = == 110dm und = == 110dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] and bType[6:8] in list(TypeList)) \
            and bType[2] == "=" and bType[5] == "=" :

        HOR1 = HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= bType[0:2]
        HOR11= HOR12= bType[3:5]
        HOR13= HOR14 =HOR15 =HOR16 = bType[6:8]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)
        
        #Fuer = == 110dm und _ == 170dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] and bType[6:8] in list(TypeList)) \
            and bType[2] == "=" and bType[5] == "_" :

        HOR1 = HOR2= HOR3= HOR4= HOR5= HOR6= \
        HOR7 = HOR8= HOR9= HOR10= HOR11= bType[0:2]
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[3:5]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #------------------------------------------------------------------------------------#

        #Fuer _ == 170dm und _ == 170dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] and bType[6:8] in list(TypeList)) \
            and bType[2] == "_" and bType[5] == "_" :

        HOR1 = HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= \
        HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[0:2]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)
        
        

    #####################################################################################
    ###Fall 6: Es sind DREI Schichten eingetragen, nur die ersten ZWEI valide Bodentypen
    #####################################################################################

        #Fuer \  == 10dm und \ == 10dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] in list(TypeList) and \
        bType[6:8] not in list(TypeList)) and bType[2] == "\\" and bType[5] == "\\" :

        HOR1 = bType[0:2]
        HOR2= bType[3:5]
        HOR3 = HOR4= HOR5= HOR6= HOR7 = \
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer \  == 10dm und / == 30dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] in list(TypeList) and \
        bType[6:8] not in list(TypeList)) and bType[2] == "\\" and bType[5] == "/" :

        HOR1 = bType[0:2]
        HOR2= HOR3= bType[3:5]
        HOR4= HOR5= HOR6= HOR7 = \
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer \  == 10dm und + == 60dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] in list(TypeList) and \
        bType[6:8] not in list(TypeList)) and bType[2] == "\\" and bType[5] == "+" :

        HOR1 = bType[0:2]
        HOR2= HOR3= HOR4= HOR5= HOR6= bType[3:5]
        HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer \  == 10dm und = == 110dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] in list(TypeList) and \
        bType[6:8] not in list(TypeList)) and bType[2] == "\\" and bType[5] == "=" :

        HOR1 = bType[0:2]
        HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= HOR11=bType[3:5]
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer \  == 10dm und _ == 170dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] in list(TypeList) and \
        bType[6:8] not in list(TypeList)) and bType[2] == "\\" and bType[5] == "_" :

        HOR1 = bType[0:2]
        HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= HOR11= \
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #------------------------------------------------------------------------------------#

        #Fuer / == 30dm und / == 30dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] in list(TypeList) and \
        bType[6:8] not in list(TypeList)) and bType[2] == "/" and bType[5] == "/" :

        HOR1 = HOR2= HOR3= bType[0:2]
        HOR4= bType[3:5]
        HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer / == 30dm und + == 60dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] in list(TypeList) and \
        bType[6:8] not in list(TypeList)) and bType[2] == "/" and bType[5] == "+" :

        HOR1 = HOR2= HOR3= bType[0:2]
        HOR4= HOR5= HOR6= bType[3:5]
        HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)
        

        #Fuer / == 30dm und = == 110dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] in list(TypeList) and \
        bType[6:8] not in list(TypeList)) and bType[2] == "/" and bType[5] == "=" :

        HOR1 = HOR2= HOR3= bType[0:2]
        HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= HOR11= bType[3:5]
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer / == 30dm und _ == 170dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] in list(TypeList) and \
        bType[6:8] not in list(TypeList)) and bType[2] == "/" and bType[5] == "_" :

        HOR1 = HOR2= HOR3= bType[0:2]
        HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= HOR11= \
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #------------------------------------------------------------------------------------#

        #Fuer + == 60dm und + == 60dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] in list(TypeList) and \
        bType[6:8] not in list(TypeList)) and bType[2] == "+" and bType[5] == "+" :

        HOR1 = HOR2= HOR3= HOR4= HOR5= HOR6= bType[0:2]
        HOR7 = HOR8= bType[3:5]
        HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer + == 60dm und = == 110dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] in list(TypeList) and \
        bType[6:8] not in list(TypeList)) and bType[2] == "+" and bType[5] == "=" :

        HOR1 = HOR2= HOR3= HOR4= HOR5= HOR6= bType[0:2]
        HOR7 = HOR8= HOR9= HOR10= HOR11= bType[3:5]
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer + == 60dm und _ == 170dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] in list(TypeList) and \
        bType[6:8] not in list(TypeList)) and bType[2] == "+" and bType[5] == "_" :

        HOR1 = HOR2= HOR3= HOR4= HOR5= HOR6= bType[0:2]
        HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #------------------------------------------------------------------------------------#

        #Fuer = == 110dm und = == 110dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] in list(TypeList) and \
        bType[6:8] not in list(TypeList)) and bType[2] == "=" and bType[5] == "=" :

        HOR1 = HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= bType[0:2]
        HOR11= HOR12= bType[3:5]
        HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)
        
        #Fuer = == 110dm und _ == 170dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] in list(TypeList) and \
        bType[6:8] not in list(TypeList)) and bType[2] == "=" and bType[5] == "_" :

        HOR1 = HOR2= HOR3= HOR4= HOR5= HOR6= \
        HOR7 = HOR8= HOR9= HOR10= HOR11= bType[0:2]
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #------------------------------------------------------------------------------------#

        #Fuer = == 170dm und = == 170dm
    elif len(bType) == 8 and (bType[0:2] and bType[3:5] in list(TypeList) and \
        bType[6:8] not in list(TypeList)) and bType[2] == "_" and bType[5] == "_" :

        HOR1 = HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= \
        HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 =  bType[0:2]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)
        

    #####################################################################################
    ###Fall 7: Es sind DREI Schichten eingetragen, nur die ERSTE ist ein valider Bodentyp
    #####################################################################################

        #Fuer \  == 10dm und \ == 10dm
    elif len(bType) == 8 and (bType[0:2] in list(TypeList) and (bType[3:5] and \
        bType[6:8] not in list(TypeList))) and bType[2] == "\\" and bType[5] == "\\" :

        HOR1 = bType[0:2]
        HOR2 = "rock"
        HOR3 = HOR4= HOR5= HOR6= HOR7 = \
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer \  == 10dm und / == 30dm
    elif len(bType) == 8 and (bType[0:2] in list(TypeList) and (bType[3:5] and \
        bType[6:8] not in list(TypeList))) and bType[2] == "\\" and bType[5] == "/" :

        HOR1 = bType[0:2]
        HOR2= HOR3= "rock"
        HOR4= HOR5= HOR6= HOR7 = \
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer \  == 10dm und + == 60dm
    elif len(bType) == 8 and (bType[0:2] in list(TypeList) and (bType[3:5] and \
        bType[6:8] not in list(TypeList))) and bType[2] == "\\" and bType[5] == "+" :

        HOR1 = bType[0:2]
        HOR2= HOR3= HOR4= HOR5= HOR6= "rock"
        HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer \  == 10dm und = == 110dm
    elif len(bType) == 8 and (bType[0:2] in list(TypeList) and (bType[3:5] and \
        bType[6:8] not in list(TypeList))) and bType[2] == "\\" and bType[5] == "=" :

        HOR1 = bType[0:2]
        HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= HOR11= "rock"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer \  == 10dm und _ == 170dm
    elif len(bType) == 8 and (bType[0:2] in list(TypeList) and (bType[3:5] and \
        bType[6:8] not in list(TypeList))) and bType[2] == "\\" and bType[5] == "_" :

        HOR1 = bType[0:2]
        HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= HOR11= \
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #------------------------------------------------------------------------------------#

        #Fuer / == 30dm und / == 30dm
    elif len(bType) == 8 and (bType[0:2] in list(TypeList) and (bType[3:5] and \
        bType[6:8] not in list(TypeList))) and bType[2] == "/" and bType[5] == "/" :

        HOR1 = HOR2= HOR3= bType[0:2]
        HOR4= "rock"
        HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer / == 30dm und + == 60dm
    elif len(bType) == 8 and (bType[0:2] in list(TypeList) and (bType[3:5] and \
        bType[6:8] not in list(TypeList))) and bType[2] == "/" and bType[5] == "+" :

        HOR1 = HOR2= HOR3= bType[0:2]
        HOR4= HOR5= HOR6= "rock"
        HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)
        

        #Fuer / == 30dm und = == 110dm
    elif len(bType) == 8 and (bType[0:2] in list(TypeList) and (bType[3:5] and \
        bType[6:8] not in list(TypeList))) and bType[2] == "/" and bType[5] == "=" :

        HOR1 = HOR2= HOR3= bType[0:2]
        HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= HOR11= "rock"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer / == 30dm und _ == 170dm
    elif len(bType) == 8 and (bType[0:2] in list(TypeList) and (bType[3:5] and \
        bType[6:8] not in list(TypeList))) and bType[2] == "/" and bType[5] == "_" :

        HOR1 = HOR2= HOR3= bType[0:2]
        HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= HOR11= \
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #------------------------------------------------------------------------------------#

        #Fuer + == 60dm und + == 60dm
    elif len(bType) == 8 and (bType[0:2] in list(TypeList) and (bType[3:5] and \
        bType[6:8] not in list(TypeList))) and bType[2] == "+" and bType[5] == "+" :

        HOR1 = HOR2= HOR3= HOR4= HOR5= HOR6= bType[0:2]
        HOR7 = HOR8= "rock"
        HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer + == 60dm und = == 110dm
    elif len(bType) == 8 and (bType[0:2] in list(TypeList) and (bType[3:5] and \
        bType[6:8] not in list(TypeList))) and bType[2] == "+" and bType[5] == "=" :

        HOR1 = HOR2= HOR3= HOR4= HOR5= HOR6= bType[0:2]
        HOR7 = HOR8= HOR9= HOR10= HOR11= "rock"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer + == 60dm und _ == 170dm
    elif len(bType) == 8 and (bType[0:2] in list(TypeList) and (bType[3:5] and \
        bType[6:8] not in list(TypeList))) and bType[2] == "+" and bType[5] == "_" :

        HOR1 = HOR2= HOR3= HOR4= HOR5= HOR6= bType[0:2]
        HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #------------------------------------------------------------------------------------#

        #Fuer = == 110dm und = == 110dm
    elif len(bType) == 8 and (bType[0:2] in list(TypeList) and (bType[3:5] and \
        bType[6:8] not in list(TypeList))) and bType[2] == "=" and bType[5] == "=" :

        HOR1 = HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= bType[0:2]
        HOR11= HOR12= "rock"
        HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)
        
        #Fuer = == 110dm und _ == 170dm
    elif len(bType) == 8 and (bType[0:2] in list(TypeList) and (bType[3:5] and \
        bType[6:8] not in list(TypeList))) and bType[2] == "=" and bType[5] == "_" :

        HOR1 = HOR2= HOR3= HOR4= HOR5= HOR6= \
        HOR7 = HOR8= HOR9= HOR10= HOR11= bType[0:2]
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #------------------------------------------------------------------------------------#

        #Fuer = == 170dm und = == 170dm
    elif len(bType) == 8 and (bType[0:2] in list(TypeList) and (bType[3:5] and \
        bType[6:8] not in list(TypeList))) and bType[2] == "_" and bType[5] == "_" :

        HOR1 = HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= \
        HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[0:2]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)
                              

    #####################################################################################
    ###Sonderfall 1: Der Eintrag ist 4 Buchstaben lang => endet immer auf G
    #####################################################################################

        #Fuer \  == 10dm
    elif len(bType) == 4 and bType[2] == "\\":

        HOR1 = bType[0:2]
        HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = \
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer / == 30dm
    elif len(bType) == 4 and bType[2] == "/":
        
        HOR1 = HOR2 = HOR3 = bType[0:2]
        HOR4= HOR5= HOR6= HOR7 = \
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer + (eigentlich //) == 60dm
    elif len(bType) == 4 and bType[2] == "+":
        
        HOR1 = HOR2 = HOR3 = HOR4= HOR5= HOR6=  bType[0:2]
        HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer = == 110dm
    elif len(bType) == 4 and bType[2] == "=":

        HOR1 = HOR2 = HOR3 = HOR4= HOR5= HOR6= \
        HOR7 = HOR8= HOR9= HOR10= HOR11 = bType[0:2]
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer _ == 170dm
    elif len(bType) == 4 and bType[2] == "_":

        HOR1= HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = \
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[0:2]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)


    #####################################################################################
    ###Sonderfall 2: Der Eintrag ist 7 Buchstaben lang => endet immer auf G
    #####################################################################################

        #Fuer \ == 10dm und \ == 10dm
    elif len(bType) == 7 and bType[2] == "\\" and bType[5] == "\\":

        HOR1 = bType[0:2]
        HOR2= bType[3:5]
        HOR3= HOR4= HOR5= HOR6= HOR7 = \
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer \ == 10dm und / == 30dm
    elif len(bType) == 7 and bType[2] == "\\" and bType[5] == "/":

        HOR1 = bType[0:2]
        HOR2= HOR3= bType[3:5]
        HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)
        
        #Fuer \ == 10dm und + == 60dm
    elif len(bType) == 7 and bType[2] == "\\" and bType[5] == "+":

        HOR1 = bType[0:2]
        HOR2= HOR3= HOR4= HOR5= HOR6= bType[3:5]
        HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer \ == 10dm und + == 110dm
    elif len(bType) == 7 and bType[2] == "\\" and bType[5] == "=":

        HOR1 = bType[0:2]
        HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= HOR11= bType[3:5]
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer \ == 10dm und + == 170dm
    elif len(bType) == 7 and bType[2] == "\\" and bType[5] == "_":

        HOR1 = bType[0:2]
        HOR2= HOR3= HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= HOR11= \
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[3:5]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #------------------------------------------------------------------------------------#

        #Fuer / == 30dm und / == 30dm
    elif len(bType) == 7 and bType[2] == "/" and bType[5] == "/":

        HOR1 = HOR2 = HOR3 = bType[0:2]
        HOR4= bType[3:5]
        HOR5= HOR6= HOR7 = \
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer / == 30dm und + == 60dm
    elif len(bType) == 7 and bType[2] == "/" and bType[5] == "+":

        HOR1 = HOR2 = HOR3 = bType[0:2]
        HOR4= HOR5= HOR6= bType[3:5]
        HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer / == 30dm und = == 110dm
    elif len(bType) == 7 and bType[2] == "/" and bType[5] == "=":

        HOR1 = HOR2 = HOR3 = bType[0:2]
        HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= HOR11= bType[3:5]
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer / == 30dm und _ == 170dm
    elif len(bType) == 7 and bType[2] == "/" and bType[5] == "_":

        HOR1 = HOR2 = HOR3 = bType[0:2]
        HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= HOR11= \
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[3:5]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #------------------------------------------------------------------------------------#

        #Fuer + == 60dm und + == 60dm
    elif len(bType) == 7 and bType[2] == "+" and bType[5] == "+":

        HOR1 = HOR2 = HOR3 = HOR4= HOR5= HOR6= bType[0:2]
        HOR7 = HOR8= bType[3:5]
        HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer + == 60dm und = == 110dm
    elif len(bType) == 7 and bType[2] == "+" and bType[5] == "=":

        HOR1 = HOR2 = HOR3 = HOR4= HOR5= HOR6= bType[0:2]
        HOR7 = HOR8= HOR9= HOR10= HOR11= bType[3:5]
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer + == 60dm und = == 170dm
    elif len(bType) == 7 and bType[2] == "+" and bType[5] == "_":

        HOR1 = HOR2 = HOR3 = HOR4= HOR5= HOR6= bType[0:2]
        HOR7 = HOR8= HOR9= HOR10= HOR11= \
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[3:5]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #------------------------------------------------------------------------------------#     

        #Fuer = == 110dm und = == 110dm
    elif len(bType) == 7 and bType[2] == "=" and bType[5] == "=":

        HOR1 = HOR2 = HOR3 = HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= bType[0:2]
        HOR11= HOR12= bType[3:5]
        HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        #Fuer = == 110dm und _ == 170dm
    elif len(bType) == 7 and bType[2] == "=" and bType[5] == "_":

        HOR1 = HOR2 = HOR3 = HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= bType[0:2]
        HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[3:5]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #------------------------------------------------------------------------------------#

        #Fuer _ == 170dm und _ == 170dm
    elif len(bType) == 7 and bType[2] == "_" and bType[5] == "_":

        HOR1 = HOR2 = HOR3 = HOR4= HOR5= HOR6= HOR7 = HOR8= HOR9= HOR10= \
        HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = bType[0:2]

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #####################################################################################
    ###Rest: Manueller Eintrag aller anderen Faelle
    #####################################################################################

    elif bType == "ss+ls=sl_ss":
        HOR1 = HOR2 = HOR3 = HOR4= HOR5= HOR6= "ss"
        HOR7 = HOR8= HOR9= HOR10= HOR11= "ls"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "sl"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)
    
    elif bType == "ss+ls+sl=ut":
        HOR1 = HOR2 = HOR3 = HOR4= HOR5= "ss"
        HOR6 = "ls"
        HOR7 = HOR8= HOR9= HOR10= HOR11="sl"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "ut"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "ut/lt/hn_ss":
        HOR1 = HOR2 = HOR3 = "ut"
        HOR4 = "ls"
        HOR5 = "sl"
        HOR6 = HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "ss"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "ut+lt+ss=sl":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = "ut"
        HOR6 = "lt"
        HOR7 = HOR8= HOR9= HOR10= HOR11= "ss"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "sl"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "ut\lt+ut=^t":
        HOR1 = "ut"
        HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = "lt"
        HOR7 = HOR8= HOR9= HOR10= HOR11= "ut"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu+tu+lu+ll":
        HOR1 = HOR2 = HOR3 = HOR4 = "lu"
        HOR5 = "tu"
        HOR6 = "lu"
        HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "ll"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu+tu+lu_ll":
        HOR1 = HOR2 = HOR3 = HOR4 = "lu"
        HOR5 = "tu"
        HOR6 = HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "lu"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu=tu_lu_ll":
        HOR1 = HOR2 = HOR3 = HOR4 = HOR5 = HOR6 = HOR7 = HOR8= HOR9= HOR10= HOR11= "lu"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "tu"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "sl/ls+ll=ss":
        HOR1 = HOR2 = HOR3 = "sl"
        HOR4 =  HOR5 = HOR6 = "ls"
        HOR7 = HOR8= HOR9= HOR10= HOR11= "ll"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "ss"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu+ll=tl_^u":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = "lu"
        HOR7 = HOR8= HOR9= HOR10= HOR11= "ll"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "tl"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu+tu=lu_tl":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = "lu"
        HOR7 = HOR8= HOR9= HOR10= HOR11= "tu"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "lu"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "ut/lt+ut=^t":
        HOR1 = HOR2 = HOR3 = "ut"
        HOR4 =  HOR5 = HOR6 = "lt"
        HOR7 = HOR8= HOR9= HOR10= HOR11= "ut"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu/tu+ll_^m":
        HOR1 = HOR2 = HOR3 = "lu"
        HOR4 =  HOR5 = HOR6 = "lt"
        HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "ll"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "ll++Gb":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = HOR7 = "ll"
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu=tl=ll_^t":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = HOR7 = HOR8= HOR9= HOR10= "lu"
        HOR11= HOR12= "tl"
        HOR13= HOR14 =HOR15 =HOR16 = "ll"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "ll=tl=ll_^t":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = HOR7 = HOR8= HOR9= HOR10= "lu"
        HOR11= HOR12= "tl"
        HOR13= HOR14 =HOR15 =HOR16 = "ll"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "ss\X+^s":
        HOR1 = "ss"
        HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = HOR7 = HOR8= HOR9= HOR10= \
        HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "hh+ll=tl_^t":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = "hh"
        HOR7 = HOR8= HOR9= HOR10= HOR11= "ll"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "tl"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu+tu=lu=^k":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = "lu"
        HOR7 = HOR8= HOR9= HOR10= "tu"
        HOR11= HOR12= "lu"
        HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu+tu=ut_^k":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = "lu"
        HOR7 = HOR8= HOR9= HOR10= "tu"
        HOR11= HOR12= HOR13 = HOR14 =HOR15 =HOR16 = "ut"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "ut\X+^k":
        HOR1 = "ut"
        HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = HOR7 = HOR8= HOR9= HOR10= \
        HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu+tu+ll_G":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = "lu"
        HOR7 = HOR8= "tu"
        HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "ll\lt=ut=^t":
        HOR1 = "ll"
        HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = HOR7 = HOR8= HOR9= HOR10= "ut"
        HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "rock"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu+tu=lu=ut":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = "lu"
        HOR7 = HOR8= HOR9= HOR10= "tu"
        HOR11= HOR12= "lu"
        HOR13= HOR14 =HOR15 =HOR16 = "ut"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu+tu=su_ss":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = "lu"
        HOR7 = HOR8= HOR9= HOR10= HOR11 = "tu"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "su"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    #problematisch
    elif bType == "s+u+t":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = "ss"
        HOR6 = "ut"
        HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "lt"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu+tu=lu=sl_G":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = "lu"
        HOR7 = HOR8= HOR9= HOR10= "tu"
        HOR11= HOR12= HOR13= "lu"
        HOR14 =HOR15 =HOR16 = "sl"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu+tu=su_tl":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = "lu"
        HOR7 = HOR8= HOR9= HOR10= HOR11 = "tu"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "su"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu+lt=ut_^t":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = "lu"
        HOR7 = HOR8= HOR9= HOR10= HOR11 = "lt"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "ut"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu/tu+lu_ll":
        HOR1 = HOR2 = HOR3 = "lu"
        HOR4 =  HOR5 = HOR6 = "tu"
        HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "lu"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu+tu=lu_ss":
        HOR1 = HOR2 = HOR3 = "lu"
        HOR4 =  HOR5 = HOR6 = HOR7 = HOR8= HOR9= HOR10= HOR11= "tu"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "lu"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu+tu=lu_lt":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = "lu"
        HOR7 = HOR8= HOR9= HOR10= HOR11 = "tu"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "lu"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "ls/ll+sl_ss":
        HOR1 = HOR2 = HOR3 = "ls"
        HOR4 =  HOR5 = HOR6 = "ll"
        HOR7 = HOR8= HOR9= HOR10= HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "sl"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)
        
    elif bType == "ls\ll+ut=ss":
        HOR1 == "ls"
        HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = "ll"
        HOR7 = HOR8= HOR9= HOR10= HOR11= "ut"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "ss"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu=tu=lu_ll":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = HOR7 = HOR8= HOR9= HOR10= "lu"
        HOR11= HOR12= "tu"
        HOR13= HOR14 =HOR15 =HOR16 = "lu"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu+tu=lu=ll":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = "lu"
        HOR7 = HOR8= HOR9= HOR10= "tu"
        HOR11= HOR12= "lu"
        HOR13 = HOR14 =HOR15 =HOR16 = "lu"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu=tu=lu_sl":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = HOR7 = HOR8= HOR9= HOR10= "lu"
        HOR11= HOR12= "tu"
        HOR13= HOR14 =HOR15 =HOR16 = "lu"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "lu+tu=lu_sl":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = "lu"
        HOR7 = HOR8= HOR9= HOR10= HOR11 = "tu"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "lu"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "ut/hh+hn=ss":
        HOR1 = HOR2 = HOR3 = "ut"
        HOR4 =  HOR5 = HOR6 = "hh"
        HOR7 = HOR8= HOR9= HOR10= "hn"
        HOR11= HOR12= HOR13= HOR14 =HOR15 =HOR16 = "ss"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "hh/ss+sl=ut":
        HOR1 = HOR2 = HOR3 = "hh"
        HOR4 =  HOR5 = HOR6 = "ss"
        HOR7 = HOR8= HOR9= HOR10= HOR11 ="sl"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "ut"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "su+lu=lt_^k":
        HOR1 = HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = "su"
        HOR7 = HOR8= HOR9= HOR10= HOR11 = "lu"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "lt"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

    elif bType == "ut\hh+hn=ss":
        HOR1 = "ut"
        HOR2 = HOR3 = HOR4 =  HOR5 = HOR6 = "hh"
        HOR7 = HOR8= HOR9= HOR10= HOR11 = "hn"
        HOR12= HOR13= HOR14 =HOR15 =HOR16 = "ss"

        InTxt(d[i][0:6], HOR1, HOR2, HOR3, HOR4, HOR5, HOR6, HOR7, HOR8,\
              HOR9, HOR10, HOR11, HOR12, HOR13, HOR14, HOR15, HOR16)

        
    else:
        print "Nr. " + str(k) + " bei " + d[i][7:] + " nicht beachtet! i Nr. " + str(i)
        k = k + 1

















