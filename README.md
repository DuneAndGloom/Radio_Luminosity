# Radio_Luminosity
Calculations of Radio (1.4GHz) luminosity of many AGN in the Bootes field of the LoTSS survey, as a function of redshift z.

main.py is the site of all code executions: plotting graphs, calculating luminosity distance, reading file columns, etc.
files.py is the location of the root directory path and the FITS file itself (on my computer, the file is ~30MB and so cannot be uploaded).
methods.py is the largest piece of code: it contains three classes (with logical names) that contain all calculations, functions and operations that the main.py will then execute.
