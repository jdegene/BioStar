###MakeTableMaster

"""Ruft den Prozess MakeTable.py mehrfach auf"""

import os, subprocess, time

python_path = "C:/Python26/ArcGIS10.0/Pythonw.exe"
python_script = ".../Python/MakeTableSlave.py"

Month = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

for j in range(2001, 2100, 1):
    for i in range (0, 12, 1):

        iStr = str(i)
        jStr = str(j)

        StartProcTime = time.clock()

        subprocess.call([python_path, python_script, iStr, jStr])

        EndProcTime = time.clock()
        DauerProc = str(int((EndProcTime-StartProcTime)/60))
        print Month[i] + " " + jStr + " Prozessdauer: " + DauerProc + " Minuten"
