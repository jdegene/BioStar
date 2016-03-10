# BioStar
BioStar scripts and related Python programs

*Note: these are probably deprecated as they were written for a work-in-progress version of BioStar without an official Version number in 2012.
Comments are mostly in german*

These Python (v2.6 and v2.7) programs are all related to the crop model BioStar, developed at the University of Goettingen
http://www.uni-goettingen.de/de/ag-biostar/431252.html



### BestMVarMASTER.py and BestMVarSLAVE.py

Uses the output (i.e. annual yield) from the BioStar model as the independent variable in
a multivariate regression analysis. 11 dependet climate variables are combined to 2047
different models (combination possibilities if order is neglected).

The script was specifically written to run on a part of 91012 sites where the BioStar yields are known.

For each site, and 10 different crops, the best of the 2047 input variations is determined (best F-Value).
This results in the information, which combination of climate variables can explain yield outcomes
the best (e.g. Spring Temperature & Summer Precipitation).


**BestMVarMASTER.py** extracts the necessary information and initializes 4 sub-processes 
(i.e. **BestMVarSLAVE.py**) for the actual model calculation. *-> Manual parallel processing*


### BUK.py
Takes soil horizon information from the official soil map of Niedersachsen (BUK50) and translates
them into the 16 horizon scheme required by the BioStar model

Horizon changes were originally indicated by characters:
> \\\\  change at 0 to <2dm below ground

> /  change at 2 to <4dm below ground

> // change at 4 to <8dm below ground

> =  change at 8 to <13dm below ground

> _  change at 13 to <20dm below ground

(*Boess, Gehrt et al 2004 - Erläuterungsheft zur digitalen nutzungsdifferenzierten Bodenkundlichen Übersichtskarte 1:50.000 von Niedersachsen*)


### BioStar_3.py
Calls the Java BioStar.jar file, hands over values depending on crop and year and 
starts 4 instances of BioStar for manual parallel execution


### MakeTableMaster.py & MakeTableSlave.py
BioStar uses Access tables as input, original climate data however comes in raster form. This script 
uses shape files as zone data and *arcpy* -> *ZonalStatisticsAsTable* for conversion

The process was devided into *Master* and *Slave*, because looping in one process lead to memory leak and extreme 
script slowdown. 
