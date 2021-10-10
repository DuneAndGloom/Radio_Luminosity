

"""I want to import from files.py, my data from the bootes field.
I want to take the Total_flux variable, as well as the z_best variable,
 and calculate & plot the radio luminosity of the source, as a function  of redshift z."""

'''This file will only be used to execute tasks:
 e.g. Reading in columns, using functions from other files.
 All "algebra" and definitions will be outlined elsewhere.'''

import os
from methods import Reading
from methods import Calculating
from methods import Plotting
from files import fitsfile

#print(fitsfile)

#hdu_list = fits.open('fitsfile', memmap=True)

coco = Reading() #example of simplifying names
#coco.read_headers(fitsfile)
#print(coco)
#coco.read_RA_and_Dec(fitsfile)
#coco.read_z(fitsfile)
calc = Calculating()
plot = Plotting()

#calc.calc_lum_dist(fitsfile)
#calc.calc_Luminosity(fitsfile)
plot.plot_Luminosity(fitsfile)
