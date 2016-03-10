
#MASTER
#Ruft MVarSlave auf, laesst hiervon 4 Instanzen auf einmal rechnen
#Das Programm rechnet fuer jede Flaeche alle moeglichen Kombinationen (ohne reihenfolge zu beachten)
#von 11 unabhaengigen Eingangsvariablen die Koeffizienten einer linearen multivariaten Regression
#Fuer das beste Modell gibt das Prog die FL_NR, den F-Wert, den p-Wert, mRs, aRs und die
#RunNo aus. Die RunNo beschreibt bei welchem der moeglichen Durchlaeufe der hoechste F-Wert erreicht
#wurde (max 2047)


import os, re, rpy2
import linecache
import StringIO
import itertools
import subprocess
import time

from subprocess import Popen


import rpy2.robjects as robjects
r = robjects.r



#Ordner definieren
dirTxt = ".../TextPlants/"      # Yield value folder
dirTxt2 = "D:/Test/TextClim/"   # Climate value folder
dirOut = "D:/Test/OutputM/"

#Windows Temp Folder im Users Verzeichnis
tmpFol = ".../appdata/local/temp/"


#Ordner fuer Subprocess definieren
python_path = "C:/Python27/ArcGIS10.1/Python.exe"
python_script = ".../BestMVarSLAVE.py"


#Input .txt Dateien benennen
xbarley = dirTxt + "barley.csv"
xmaize_f = dirTxt + "maize_f.csv"
xmaize_m = dirTxt + "maize_m.csv"
xmaize_s = dirTxt + "maize_s.csv"
xrye = dirTxt + "rye.csv"
xsflower = dirTxt +  "sflower.csv"
xsorghum = dirTxt + "sorghum.csv"
xswheat = dirTxt + "swheat.csv"
xtriti = dirTxt + "triti.csv"
xwheat = dirTxt + "wheat.csv"

xprecAut = dirTxt2 + "PrecAutumn.csv"
xprecSpr = dirTxt2 + "PrecSpring.csv"
xprecSum = dirTxt2 + "PrecSummer.csv"
xprecWin = dirTxt2 + "PrecWinter.csv"
xprecYear = dirTxt2 + "PrecYear.csv"
xtempAut = dirTxt2 + "TempAutumn.csv"
xtempSpr = dirTxt2 + "TempSpring.csv"
xtempSum = dirTxt2 + "TempSummer.csv"
xtempWin = dirTxt2 + "TempWinter.csv"
xtempYear = dirTxt2 + "TempYear.csv"


#Listen definieren
plants = ("barley","maize_f","maize_m", "maize_s", "rye", "sflower", "sorghum", "swheat",
          "triti", "wheat")


xplants = (xbarley, xmaize_f, xmaize_m, xmaize_s, xrye, xsflower, xsorghum, xswheat,
          xtriti, xwheat)
xinClimList = [xprecAut, xprecSpr, xprecSum, xprecWin, xprecYear, xtempAut, xtempSpr,
               xtempSum, xtempWin, xtempYear]

co2 = [370,373,375,376.875,378.75,380.625,382.5,384.375,386.25,388.125,390,392.5,395,397.5,
       400,402.5,405,407.5,410,412.5,415,418.5,422,425.5,429,432.5,436,439.5,443,446.5,450,
       454.5,459,463.5,468,472.5,477,481.5,486,490.5,495,499.5,504,508.5,513,517.5,522,526.5,
       531,535.5,540,543.5,547,550.5,554,557.5,561,564.5,568,571.5,575,578.5,582,585.5,589,
       592.5,596,599.5,603,606.5,610,614,618,622,626,630,634,638,642,646,650,653,656,659,662,
       665,668,671,674,677,680,683,686,689,692,695,698,701,704]

# Create output files for each of the 4 runs (with only 1 file writing errors may occur)
for plantNo in plants:
    
    w1 = open(dirOut + plantNo + "1p50.txt", "a")
    w1.write("FL_NR;Fstat;pValue;Rs;aRs;Run\n")

    w2 = open(dirOut + plantNo + "2p50.txt", "a")
    w2.write("FL_NR;Fstat;pValue;Rs;aRs;Run\n")

    w3 = open(dirOut + plantNo + "3p50.txt", "a")
    w3.write("FL_NR;Fstat;pValue;Rs;aRs;Run\n")

    w4 = open(dirOut + plantNo + "4p50.txt", "a")
    w4.write("FL_NR;Fstat;pValue;Rs;aRs;Run\n")

    w1.close()
    w2.close()
    w3.close()
    w4.close()



    p = dirTxt + plantNo + ".csv"

    sx0, sx1, sx2, sx3, sx4, sx5, sx6, sx7, sx8, sx9, ee =  ([] for i in range(11))

    #Alle Klimadaten in den Cache laden
    for i in range(2,90214):
           
        sx0.append(linecache.getline(xinClimList[0], i))
        sx1.append(linecache.getline(xinClimList[1], i))
        sx2.append(linecache.getline(xinClimList[2], i))
        sx3.append(linecache.getline(xinClimList[3], i))
        sx4.append(linecache.getline(xinClimList[4], i))
        sx5.append(linecache.getline(xinClimList[5], i))
        sx6.append(linecache.getline(xinClimList[6], i))
        sx7.append(linecache.getline(xinClimList[7], i))
        sx8.append(linecache.getline(xinClimList[8], i))
        sx9.append(linecache.getline(xinClimList[9], i))

    for i in range(2,91014):
        ee.append(linecache.getline(p, i))


    # For computation times reduction, only a part of all roughly 90000 areas are calculated
    for i in range(179,82373,176):


        von = 1
        bis = 51


        #tmp_____ Files aus dem tmp Ordner loeschen
        try:
            for files in os.listdir(tmpFol):
                if files[:3] == "tmp":
                    os.remove(tmpFol + files)
                else:
                    continue
        except:
            pass
        


        #####################PROZESS 1#############################
        
        #Aktuelle Flaechennummer FL_NR 
        curFLNRp1 =  sx0[i][0:6]

        #Da Klima .csv und Pflanzen .csv unterschiedlich viele Eintraege haben, wird erst der
        #Pfkanzeneintrag gewaehlt. Danach hier die Klimawerte nach der aktuellen FL_NR durchsucht
        for k in range(91012):
            if ee[k][0:6] == curFLNRp1:
                eekp1 = ee[k]
            else:
                continue

        sxs0p1 = re.split(';|\n', sx0[i])
        sxs1p1 = re.split(';|\n', sx1[i])
        sxs2p1 = re.split(';|\n', sx2[i])
        sxs3p1 = re.split(';|\n', sx3[i])
        sxs4p1 = re.split(';|\n', sx4[i])

        for k in range(90212):
            if sx5[k][0:6] == curFLNRp1:
                
                sxs5p1 = re.split(';|\n', sx5[k])
                sxs6p1 = re.split(';|\n', sx6[k])
                sxs7p1 = re.split(';|\n', sx7[k])
                sxs8p1 = re.split(';|\n', sx8[k])
                sxs9p1 = re.split(';|\n', sx9[k])
            else:
                continue

        eesp1 = re.split(';|\n', eekp1)


        #####################PROZESS 2#############################
        
        #Aktuelle Flaechennummer FL_NR 
        curFLNRp2 =  sx0[i-44][0:6]

        #Da Klima .csv und Pflanzen .csv unterschiedlich viele Eintraege haben, wird erst der
        #Pfkanzeneintrag gewaehlt. Danach hier die Klimawerte nach der aktuellen FL_NR durchsucht
        for k in range(91012):
            if ee[k][0:6] == curFLNRp2:
                eekp2 = ee[k]
            else:
                continue

        sxs0p2 = re.split(';|\n', sx0[i-44])
        sxs1p2 = re.split(';|\n', sx1[i-44])
        sxs2p2 = re.split(';|\n', sx2[i-44])
        sxs3p2 = re.split(';|\n', sx3[i-44])
        sxs4p2 = re.split(';|\n', sx4[i-44])

        for k in range(90212):
            if sx5[k][0:6] == curFLNRp2:
                
                sxs5p2 = re.split(';|\n', sx5[k])
                sxs6p2 = re.split(';|\n', sx6[k])
                sxs7p2 = re.split(';|\n', sx7[k])
                sxs8p2 = re.split(';|\n', sx8[k])
                sxs9p2 = re.split(';|\n', sx9[k])
            else:
                continue

        eesp2 = re.split(';|\n', eekp2)


        #####################PROZESS 3#############################
        
        #Aktuelle Flaechennummer FL_NR 
        curFLNRp3 =  sx0[i-88][0:6]

        #Da Klima .csv und Pflanzen .csv unterschiedlich viele Eintraege haben, wird erst der
        #Pfkanzeneintrag gewaehlt. Danach hier die Klimawerte nach der aktuellen FL_NR durchsucht
        for k in range(91012):
            if ee[k][0:6] == curFLNRp3:
                eekp3 = ee[k]
            else:
                continue

        sxs0p3 = re.split(';|\n', sx0[i-88])
        sxs1p3 = re.split(';|\n', sx1[i-88])
        sxs2p3 = re.split(';|\n', sx2[i-88])
        sxs3p3 = re.split(';|\n', sx3[i-88])
        sxs4p3 = re.split(';|\n', sx4[i-88])

        for k in range(90212):
            if sx5[k][0:6] == curFLNRp3:
                
                sxs5p3 = re.split(';|\n', sx5[k])
                sxs6p3 = re.split(';|\n', sx6[k])
                sxs7p3 = re.split(';|\n', sx7[k])
                sxs8p3 = re.split(';|\n', sx8[k])
                sxs9p3 = re.split(';|\n', sx9[k])
            else:
                continue

        eesp3 = re.split(';|\n', eekp3)


        #####################PROZESS 4#############################
        
        #Aktuelle Flaechennummer FL_NR 
        curFLNRp4 =  sx0[i-132][0:6]

        #Da Klima .csv und Pflanzen .csv unterschiedlich viele Eintraege haben, wird erst der
        #Pfkanzeneintrag gewaehlt. Danach hier die Klimawerte nach der aktuellen FL_NR durchsucht
        for k in range(91012):
            if ee[k][0:6] == curFLNRp4:
                eekp4 = ee[k]
            else:
                continue

        sxs0p4 = re.split(';|\n', sx0[i-132])
        sxs1p4 = re.split(';|\n', sx1[i-132])
        sxs2p4 = re.split(';|\n', sx2[i-132])
        sxs3p4 = re.split(';|\n', sx3[i-132])
        sxs4p4 = re.split(';|\n', sx4[i-132])

        for k in range(90212):
            if sx5[k][0:6] == curFLNRp4:
                
                sxs5p4 = re.split(';|\n', sx5[k])
                sxs6p4 = re.split(';|\n', sx6[k])
                sxs7p4 = re.split(';|\n', sx7[k])
                sxs8p4 = re.split(';|\n', sx8[k])
                sxs9p4 = re.split(';|\n', sx9[k])
            else:
                continue

        eesp4 = re.split(';|\n', eekp4)



        #Umwandeln aller Listen in String, da nur String uebergeben werden koennen

        co2S = ''
        for kk in co2[von-1:bis-1]:
            co2S += '~~' + str(kk)

        eesp1S = ''
        for kk in eesp1[von:bis]:
            eesp1S += '~~' + kk
        sxs0p1S = ''
        for kk in sxs0p1[von:bis]:
            sxs0p1S += '~~' + kk
        sxs1p1S = ''
        for kk in sxs1p1[von:bis]:
            sxs1p1S += '~~' + kk
        sxs2p1S = ''
        for kk in sxs2p1[von:bis]:
            sxs2p1S += '~~' + kk
        sxs3p1S = ''
        for kk in sxs3p1[von:bis]:
            sxs3p1S += '~~' + kk
        sxs4p1S = ''
        for kk in sxs4p1[von:bis]:
            sxs4p1S += '~~' + kk
        sxs5p1S = ''
        for kk in sxs5p1[von:bis]:
            sxs5p1S += '~~' + kk
        sxs6p1S = ''
        for kk in sxs6p1[von:bis]:
            sxs6p1S += '~~' + kk
        sxs7p1S = ''
        for kk in sxs7p1[von:bis]:
            sxs7p1S += '~~' + kk
        sxs8p1S = ''
        for kk in sxs8p1[von:bis]:
            sxs8p1S += '~~' + kk
        sxs9p1S = ''
        for kk in sxs9p1[von:bis]:
            sxs9p1S += '~~' + kk
        

        eesp2S = ''
        for kk in eesp2[von:bis]:
            eesp2S += '~~' + kk
        sxs0p2S = ''
        for kk in sxs0p2[von:bis]:
            sxs0p2S += '~~' + kk
        sxs1p2S = ''
        for kk in sxs1p2[von:bis]:
            sxs1p2S += '~~' + kk
        sxs2p2S = ''
        for kk in sxs2p2[von:bis]:
            sxs2p2S += '~~' + kk
        sxs3p2S = ''
        for kk in sxs3p2[von:bis]:
            sxs3p2S += '~~' + kk
        sxs4p2S = ''
        for kk in sxs4p2[von:bis]:
            sxs4p2S += '~~' + kk
        sxs5p2S = ''
        for kk in sxs5p2[von:bis]:
            sxs5p2S += '~~' + kk
        sxs6p2S = ''
        for kk in sxs6p2[von:bis]:
            sxs6p2S += '~~' + kk
        sxs7p2S = ''
        for kk in sxs7p2[von:bis]:
            sxs7p2S += '~~' + kk
        sxs8p2S = ''
        for kk in sxs8p2[von:bis]:
            sxs8p2S += '~~' + kk
        sxs9p2S = ''
        for kk in sxs9p2[von:bis]:
            sxs9p2S += '~~' + kk
        
        eesp3S = ''
        for kk in eesp3[von:bis]:
            eesp3S += '~~' + kk
        sxs0p3S = ''
        for kk in sxs0p3[von:bis]:
            sxs0p3S += '~~' + kk
        sxs1p3S = ''
        for kk in sxs1p3[von:bis]:
            sxs1p3S += '~~' + kk
        sxs2p3S = ''
        for kk in sxs2p3[von:bis]:
            sxs2p3S += '~~' + kk
        sxs3p3S = ''
        for kk in sxs3p3[von:bis]:
            sxs3p3S += '~~' + kk
        sxs4p3S = ''
        for kk in sxs4p3[von:bis]:
            sxs4p3S += '~~' + kk
        sxs5p3S = ''
        for kk in sxs5p3[von:bis]:
            sxs5p3S += '~~' + kk
        sxs6p3S = ''
        for kk in sxs6p3[von:bis]:
            sxs6p3S += '~~' + kk
        sxs7p3S = ''
        for kk in sxs7p3[von:bis]:
            sxs7p3S += '~~' + kk
        sxs8p3S = ''
        for kk in sxs8p3[von:bis]:
            sxs8p3S += '~~' + kk
        sxs9p3S = ''
        for kk in sxs9p3[von:bis]:
            sxs9p3S += '~~' + kk

        eesp4S = ''
        for kk in eesp4[von:bis]:
            eesp4S += '~~' + kk
        sxs0p4S = ''
        for kk in sxs0p4[von:bis]:
            sxs0p4S += '~~' + kk
        sxs1p4S = ''
        for kk in sxs1p4[von:bis]:
            sxs1p4S += '~~' + kk
        sxs2p4S = ''
        for kk in sxs2p4[von:bis]:
            sxs2p4S += '~~' + kk
        sxs3p4S = ''
        for kk in sxs3p4[von:bis]:
            sxs3p4S += '~~' + kk
        sxs4p4S = ''
        for kk in sxs4p4[von:bis]:
            sxs4p4S += '~~' + kk
        sxs5p4S = ''
        for kk in sxs5p4[von:bis]:
            sxs5p4S += '~~' + kk
        sxs6p4S = ''
        for kk in sxs6p4[von:bis]:
            sxs6p4S += '~~' + kk
        sxs7p4S = ''
        for kk in sxs7p4[von:bis]:
            sxs7p4S += '~~' + kk
        sxs8p4S = ''
        for kk in sxs8p4[von:bis]:
            sxs8p4S += '~~' + kk
        sxs9p4S = ''
        for kk in sxs9p4[von:bis]:
            sxs9p4S += '~~' + kk
            




        p1 = subprocess.Popen([python_path, python_script, eesp1S, sxs0p1S, sxs1p1S,
                               sxs2p1S, sxs3p1S, sxs4p1S, sxs5p1S, sxs6p1S,
                               sxs7p1S, sxs8p1S, sxs9p1S, co2S, dirOut, dirTxt,
                               dirTxt2, "1", plantNo, tmpFol, curFLNRp1]) 

        p2 = subprocess.Popen([python_path, python_script, eesp2S, sxs0p2S, sxs1p2S,
                               sxs2p2S, sxs3p2S, sxs4p2S, sxs5p2S, sxs6p2S,
                               sxs7p2S, sxs8p2S, sxs9p2S, co2S, dirOut, dirTxt,
                               dirTxt2, "2", plantNo, tmpFol, curFLNRp2]) 

        p3 = subprocess.Popen([python_path, python_script, eesp3S, sxs0p3S, sxs1p3S,
                               sxs2p3S, sxs3p3S, sxs4p3S, sxs5p3S, sxs6p3S,
                               sxs7p3S, sxs8p3S, sxs9p3S, co2S, dirOut, dirTxt,
                               dirTxt2, "3", plantNo, tmpFol, curFLNRp3]) 

        p4 = subprocess.Popen([python_path, python_script, eesp4S, sxs0p4S, sxs1p4S,
                               sxs2p4S, sxs3p4S, sxs4p4S, sxs5p4S, sxs6p4S,
                               sxs7p4S, sxs8p4S, sxs9p4S, co2S, dirOut, dirTxt,
                               dirTxt2, "4", plantNo, tmpFol, curFLNRp4]) 



        print "Done " + curFLNRp1 + " " + curFLNRp2 + " " + curFLNRp3 + " " + curFLNRp4 + " at ", time.asctime()[11:19]

        Popen.wait(p1)              #Wartet bis p1 beendet ist
        Popen.wait(p2)              #Wartet bis p2 beendet ist
        Popen.wait(p3)              #Wartet bis p3 beendet ist
        Popen.wait(p4)              #Wartet bis p4 beendet ist


               

                

                
                    

        



    linecache.clearcache()    
              
                


                
            




















