from netCDF4 import Dataset
from pprint import pprint
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.cm as cm
import sys

path = sys.argv[1]
data = Dataset(path,'r+')

for var in data.variables:
    print(var)
print('\n')

lat = data.variables["lat"][:]
lon = data.variables["lon"][:]

print(lat)
#print(np.meshgrid(lat,lon))
