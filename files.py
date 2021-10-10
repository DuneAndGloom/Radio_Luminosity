"""This will be the file which contains all of the
data files and directory paths, which tell the main.py
where to find all of the FITS files and other stuff"""

from astropy.io import fits


rootdir = "//Users//lewis//PycharmProjects//pythonProject1//abcd"
fitsfile = fits.open(rootdir + "//bootes_final_cross_match_catalogue-v1.0.fits")
#os.chdir(rootdir) #changes the directory to the specified rootdir
