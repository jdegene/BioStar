


import os, re, rpy2, sys
import linecache
import StringIO
import itertools

import rpy2.robjects as robjects
r = robjects.r

#Uebernehmen der Argumente aus Master, rueckwandeln in Listen wo noetig
eesS = sys.argv[1]
ees = eesS.split('~~')[1:]

sxs0S = sys.argv[2]
sxs0 = sxs0S.split('~~')[1:]
sxs1S = sys.argv[3]
sxs1 = sxs1S.split('~~')[1:]
sxs2S = sys.argv[4]
sxs2 = sxs2S.split('~~')[1:]
sxs3S = sys.argv[5]
sxs3 = sxs3S.split('~~')[1:]
sxs4S = sys.argv[6]
sxs4 = sxs4S.split('~~')[1:]
sxs5S = sys.argv[7]
sxs5 = sxs5S.split('~~')[1:]
sxs6S = sys.argv[8]
sxs6 = sxs6S.split('~~')[1:]
sxs7S = sys.argv[9]
sxs7 = sxs7S.split('~~')[1:]
sxs8S = sys.argv[10]
sxs8 = sxs8S.split('~~')[1:]
sxs9S = sys.argv[11]
sxs9 = sxs9S.split('~~')[1:]
co2S = sys.argv[12]
co2 = co2S.split('~~')[1:]

dirOut = sys.argv[13]
dirTxt = sys.argv[14]
dirTxt2 = sys.argv[15]
procNum = sys.argv[16]
plantNo = sys.argv[17]
tmpFol = sys.argv[18]

curFLNR = sys.argv[19]

w = open(dirOut + plantNo + procNum + "p50.txt", "a")


robjects.globalenv["ertragR"] = robjects.FloatVector(ees)

robjects.globalenv["precAutR"] = robjects.FloatVector(sxs0)
robjects.globalenv["precSprR"] = robjects.FloatVector(sxs1)
robjects.globalenv["precSumR"] = robjects.FloatVector(sxs2)
robjects.globalenv["precWinR"] = robjects.FloatVector(sxs3)
robjects.globalenv["precYearR"] = robjects.FloatVector(sxs4)

robjects.globalenv["tempAutR"] = robjects.FloatVector(sxs5)
robjects.globalenv["tempSprR"] = robjects.FloatVector(sxs6)
robjects.globalenv["tempSumR"] = robjects.FloatVector(sxs7)
robjects.globalenv["tempWinR"] = robjects.FloatVector(sxs8)
robjects.globalenv["tempYearR"] = robjects.FloatVector(sxs9)

robjects.globalenv["co2R"] = robjects.FloatVector(co2)

rList = ["precAutR","precSprR","precSumR","precWinR","precYearR","tempAutR","tempSprR","tempSumR","tempWinR","tempYearR","co2R"]

#Variable definieren die nacher den F Wert aufnimmt
fStat = 0.0
pStat = 0.0

#Iterationszaehler
xx = 0


#Alle Kombinationsmoeglicheiten der 11 Unabhaengigen Variablen durchgehen
#Lineare Regression ueber rpy ausfuehren
    
for L in range(1, len(rList)+1):
    for subset in itertools.combinations(rList, L):

        if L == 1:
            rString = "ertragR ~ %s" % subset[0]
            out = r.lm(rString) 
        elif L == 2:
            rString = "ertragR ~ %s + %s" % (subset[0] , subset[1])
            out = r.lm(rString)
        elif L == 3:
            rString = "ertragR ~ %s + %s + %s" % (subset[0] , subset[1], subset[2])
            out = r.lm(rString)
        elif L == 4:
            rString = "ertragR ~ %s + %s + %s + %s" % (subset[0] , subset[1], subset[2], subset[3])
            out = r.lm(rString) 
        elif L == 5:
            rString = "ertragR ~ %s + %s + %s + %s + %s" % (subset[0] , subset[1], subset[2], subset[3], subset[4])
            out = r.lm(rString)
        elif L == 6:
            rString = "ertragR ~ %s + %s + %s + %s + %s + %s" % \
                      (subset[0] , subset[1], subset[2], subset[3], subset[4], subset[5])
            out = r.lm(rString)
        elif L == 7:
            rString = "ertragR ~ %s + %s + %s + %s + %s + %s + %s" \
                  % (subset[0] , subset[1], subset[2], subset[3], subset[4], subset[5], subset[6])
            out = r.lm(rString)
        elif L == 8:
            rString = "ertragR ~ %s + %s + %s + %s + %s + %s + %s + %s" \
                  % (subset[0] , subset[1], subset[2], subset[3], subset[4], subset[5], subset[6], subset[7])
            out = r.lm(rString)
        elif L == 9:
            rString = "ertragR ~ %s + %s + %s + %s + %s + %s + %s + %s + %s" \
                  % (subset[0] , subset[1], subset[2], subset[3], subset[4], subset[5], subset[6], subset[7],
                     subset[8])
            out = r.lm(rString)
        elif L == 10:
            rString = "ertragR ~ %s + %s + %s + %s + %s + %s + %s + %s + %s + %s" \
                  % (subset[0] , subset[1], subset[2], subset[3], subset[4], subset[5], subset[6], subset[7],
                     subset[8], subset[9])
            out = r.lm(rString)
        elif L == 11:
            rString = "ertragR ~ %s + %s + %s + %s + %s + %s + %s + %s + %s + %s + %s" \
                  % (subset[0] , subset[1], subset[2], subset[3], subset[4], subset[5], subset[6], subset[7],
                     subset[8], subset[9], subset[10])
            out = r.lm(rString)



        c = r.summary(out)
        logFile = StringIO.StringIO()
        print >> logFile, c
        logFile.seek(0)
        logList = logFile.readlines()

        for kk in range(len(logList)-30,len(logList)):

            if logList[kk][0:8] == "Multiple":
                ll = logList[kk].split()
                xmRs = ll[2]
                xaRs = ll[5]

            elif logList[kk][0:11] == "F-statistic":
                ll = logList[kk].split()
                fValue = ll[1]
                pValue = ll[-1]


        #Testen ob F-Wert groesser ist als in vorherigen Lauefen
        #Wenn ja wird F-Wert, pWert, runNo, mRs und aRs in Variablen geschrieben
        if float(fValue) > fStat:
            fStat = float(fValue)
            pStat = float(pValue)
            runNo = xx
            mRs = xmRs
            aRs = xaRs

        xx = xx+1
        
        logFile.close()

                

w.write(curFLNR + ";" + str(fStat) + ";" + str(pStat) + ";" + mRs + ";" + aRs + ";" + str(runNo) + "\n")
w.close()








