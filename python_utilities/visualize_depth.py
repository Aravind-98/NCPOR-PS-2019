from netCDF4 import Dataset
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
import sys


path = sys.argv[1]
data = Dataset(path,'r+')

for var in data.variables:
    print(var)
print('\n')

try:
    lat = data.variables["lat"][:]
    lon = data.variables["lon"][:]
except:
    lat = data.variables["latitude"][:]
    lon = data.variables["longitude"][:]

depth = data.variables['LEV'][:]
data_attr = data.variables[sys.argv[2]][:]

lat_pos = float(sys.argv[3])
ind = np.argmin(np.abs(lat_pos-lat))

print(f'showing for latitude {lat[ind]}')

X,Y = np.meshgrid(lon,depth)
Z = data_attr[0,:,ind,:]
print(depth)
cp = plt.contour(lon, depth, Z)
plt.gca().invert_yaxis()
plt.title(f'Contour Plot at latitude {lat[ind]}')
#cp.ylabel = (-50,50)
plt.show()
