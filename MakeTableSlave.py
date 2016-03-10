# -*- coding: cp1252 -*-

### MakeTable

"""Erstellt aus Rastern Tabellen die in BioStar eingelesen werden koennen"""

import os, arcpy, sys, time, math, shutil

from arcpy import env
from arcpy.sa import *

arcpy.env.overwriteOutput = True                        # Ueberschreiben fuer ArcGIS aktivieren
arcpy.env.outputCoordinateSystem = ".../MeanMonTemp/2001Apr.tif" # coordinate system blueprint
                                                        # Koordinatensystem uebernehmen
arcpy.env.cellSize = "default"                          # Berechnet die default Cellsize

env.workspace = ".../Workspace"


#Argumente aus dem Master uebernehmen
iStr = sys.argv[1]
jStr = sys.argv[2]

#Konvertieren der uebernommenen Strings in Integer
i = int(iStr)
j = int(jStr)

#Definieren der lokalen Variablen
Month = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
MonthZif = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")

#Arbeitsordner erstellen, da dieser nach jeder Schleife geloescht wird
os.makedirs("D:/Test/Workspace/Tables")

#Laden der Shapes und Raster
ZonesNord = ".../Nordteil_Bük50_FL.shp"
ZonesSouth = ".../Südteil_Bük50_FLed.shp"
ZonesAll = ".../BÜK50_FLNR_ed.shp"

rss = Raster(".../rss_MPEH5C/" + jStr + Month[i] + ".tif")   # Kurzwellige Strahlung J/cm^2/d
rls = Raster(".../rls_MPEH5C/" + jStr + Month[i] + ".tif")   # Langwellige Strahlung J/cm^2/d
                                               

Prec = Raster(".../SumMonPrec/" + jStr + Month[i] + ".tif")          # Niederschlagsraster
Temp = Raster(".../MeanMonTemp/" + jStr + Month[i] + ".tif")         # Temperaturraster
LF = Raster(".../LF/" + jStr + Month[i] + ".tif")                   # Luftfeuchte Raster

Wind = Raster(".../nds_uf_" + MonthZif[i] + ".tif")



arcpy.CheckOutExtension("Spatial")

# Strahlungstabelle auf Grundlage der BÜK50 Flächen erstellen

RJ = rls                                          # Kurzwellige Strahlung berechnen J/cm^2/d

arcpy.env.cellSize = 20                                 # Zellengröße auf 20 festlegen, da sonst ZonalStat nicht alle Flächen berechnet

statRJNorth = ZonalStatisticsAsTable(ZonesNord, "FL_NR", RJ,  # Strahlungs-Tabelle für den Nordteil erstellen
                                  "D.../statRJNorth", "NODATA", "MEAN")
statRJSouth = ZonalStatisticsAsTable(ZonesSouth, "FL_NR", RJ, # Strahlungs-Tabelle für den Südteil erstellen
                                  ".../statRJSouth", "NODATA", "MEAN")

arcpy.Merge_management([statRJNorth, statRJSouth],      #Nord und Südtabelle mergen
                       ".../RadTab")

                                                   
# Niederschlagstabelle auf Grundlage der BÜK50 Flächen erstellen

statRJNorth = ZonalStatisticsAsTable(ZonesNord, "FL_NR", Prec,  # Strahlungs-Tabelle für den Nordteil erstellen
                                  ".../statRJNorth", "NODATA", "MEAN")
statRJSouth = ZonalStatisticsAsTable(ZonesSouth, "FL_NR", Prec, # Strahlungs-Tabelle für den Südteil erstellen
                                  ".../statRJSouth", "NODATA", "MEAN")

arcpy.Merge_management([statRJNorth, statRJSouth],      #Nord und Südtabelle mergen
                       ".../PrecTab")


# Temperaturtabelle auf Grundlage der BÜK50 Flächen erstellen

statRJNorth = ZonalStatisticsAsTable(ZonesNord, "FL_NR", Temp,  # Strahlungs-Tabelle für den Nordteil erstellen
                                  ".../statRJNorth", "NODATA", "MEAN")
statRJSouth = ZonalStatisticsAsTable(ZonesSouth, "FL_NR", Temp, # Strahlungs-Tabelle für den Südteil erstellen
                                  ".../statRJSouth", "NODATA", "MEAN")

arcpy.Merge_management([statRJNorth, statRJSouth],      #Nord und Südtabelle mergen
                       ".../TempTab")


# Luftfeuchtetabelle auf Grundlage der BÜK50 Flächen erstellen


statRJNorth = ZonalStatisticsAsTable(ZonesNord, "FL_NR", LF,  # Strahlungs-Tabelle für den Nordteil erstellen
                                  ".../statRJNorth", "NODATA", "MEAN")
statRJSouth = ZonalStatisticsAsTable(ZonesSouth, "FL_NR", LF, # Strahlungs-Tabelle für den Südteil erstellen
                                  ".../statRJSouth", "NODATA", "MEAN")

arcpy.Merge_management([statRJNorth, statRJSouth],      #Nord und Südtabelle mergen
                       ".../LFtab")



# Windtabelle auf Grundlage der BÜK50 Flächen erstellen

statRJNorth = ZonalStatisticsAsTable(ZonesNord, "FL_NR", Wind,  # Strahlungs-Tabelle für den Nordteil erstellen
                                  ".../statRJNorth", "NODATA", "MEAN")
statRJSouth = ZonalStatisticsAsTable(ZonesSouth, "FL_NR", Wind, # Strahlungs-Tabelle für den Südteil erstellen
                                  ".../statRJSouth", "NODATA", "MEAN")

arcpy.Merge_management([statRJNorth, statRJSouth],      #Nord und Südtabelle mergen
                       ".../WindTab")






# Joined alle Tabellen zu einer

JoinField = "FL_NR"

RadTab = ".../RadTab.dbf"
PrecTab = ".../PrecTab.dbf"
TempTab = ".../TempTab.dbf"
LFtab = ".../LFtab.dbf"
WindTab = ".../WindTab.dbf"

arcpy.JoinField_management(RadTab, JoinField, PrecTab, JoinField, ["MEAN"])
arcpy.JoinField_management(RadTab, JoinField, TempTab, JoinField, ["MEAN"])
arcpy.JoinField_management(RadTab, JoinField, LFtab, JoinField, ["MEAN"])
arcpy.JoinField_management(RadTab, JoinField, WindTab, JoinField, ["MEAN"])


# Verbleibende 0 Werte bei LF sollen mit 0.8 ersetzt werden
codeblock = """def RecTable(mean):
    if mean == 0:
        return 0.8
    else:
        return mean"""

arcpy.CalculateField_management(RadTab, "MEAN_12_13",                 
                                "RecTable(!MEAN_12_13!)", "PYTHON", codeblock)

# Verbleibende 0 Werte bei Wind sollen mit 3 ersetzt werden
codeblock = """def RecTable(mean):
    if mean == 0:
        return 3
    else:
        return mean"""

arcpy.CalculateField_management(RadTab, "MEAN_12_14",                 
                                "RecTable(!MEAN_12_14!)", "PYTHON", codeblock)


# Neue Spalten wg Umbenennung erzeugen (auf 6 Ziffern begrenzt bei Float, Zahl dahinter = Nachkommastellen)

arcpy.AddField_management(RadTab, "MON", "SHORT")
arcpy.AddField_management(RadTab, "RJ", "SHORT")
arcpy.AddField_management(RadTab, "PREC", "FLOAT", 6, 3)
arcpy.AddField_management(RadTab, "TCEL", "FLOAT", 6, 4)
arcpy.AddField_management(RadTab, "HAIRFR", "FLOAT", 6, 6)
arcpy.AddField_management(RadTab, "WIND", "FLOAT", 6, 5)


# Werte aus den alten Spalten hineinkopieren

arcpy.CalculateField_management(RadTab, "MON", i + 1 , "PYTHON")
arcpy.CalculateField_management(RadTab, "RJ", "!MEAN!" , "PYTHON")
arcpy.CalculateField_management(RadTab, "PREC", "!MEAN_1!" , "PYTHON")
arcpy.CalculateField_management(RadTab, "TCEL", "!MEAN_12!" , "PYTHON")
arcpy.CalculateField_management(RadTab, "HAIRFR", "!MEAN_12_13!" , "PYTHON")
arcpy.CalculateField_management(RadTab, "WIND", "!MEAN_12_14!" , "PYTHON")


# Alte Spalten löschen und Table speichern

arcpy.DeleteField_management(RadTab, ["COUNT", "AREA", "MEAN", "MEAN_1", "MEAN_12", "MEAN_12_13", "MEAN_12_14"])
arcpy.TableToDBASE_conversion(RadTab, ".../Output")
arcpy.Rename_management(".../RadTab.dbf", ".../Output/" + jStr + Month[i] + ".dbf")

shutil.rmtree(".../Workspace/Tables")     # löscht den Inhalt des Ordners

arcpy.CheckInExtension("Spatial")

Time = time.clock()
print str(int(Time))
