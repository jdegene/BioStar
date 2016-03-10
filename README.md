# BioStar
BioStar scripts and related Python programs

*Note: these are probably deprecated as they were written for a work-in-progress version of BioStar without an official Version number*

These Python (v2.7) programs are all related to the crop model BioStar, developed at the University of Goettingen
http://www.uni-goettingen.de/de/ag-biostar/431252.html


### BUK.py
Takes soil horizon information from the official soil map of Niedersachsen (BUK50) and translates
them into the 16 horizon scheme required by the BioStar model

Horizon changes were originally indicated by characters:
> \  change at 0 to <2dm below ground
> /  change at 2 to <4dm below ground
> // change at 4 to <8dm below ground
> =  change at 8 to <13dm below ground
> _  change at 13 to <20dm below ground

*Boess, Gehrt et al 2004 - Erläuterungsheft zur digitalen nutzungsdifferenzierten Bodenkundlichen Übersichtskarte 1:50.000 von Niedersachsen*


### BioStar_3.py
Calls the Java BioStar.jar file, hands over values depending on crop and year and 
starts 4 instances of BioStar for manual parallel execution