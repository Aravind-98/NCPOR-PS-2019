from netCDF4 import Dataset
import sys
import pyproj
import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

data = Dataset(sys.argv[1],'r')

for var in data.variables:
    print(var)

#print(data.variables["projection"])

x = data.variables["xgrid"][:]
y = data.variables["ygrid"][:]

lat = data.variables["latitude"][:].flatten()
lon = data.variables["longitude"][:].flatten()
vals = data.variables["goddard_merged_seaice_conc_monthly"][:].flatten()

#vals[np.where(vals.mask==True)] = 0
#vals.mask[:] = False
#print(vals.mask)

points = np.column_stack((lat,lon))

grid_x, grid_y = np.mgrid[-90:-50:161j, -180:180-0.25:1440j]

print(points.shape)
print(grid_x.shape)
print(grid_y.shape)
grid  = griddata(points,vals, (grid_x,grid_y), method='nearest')
grid[np.isnan(grid)] = 0
print(grid.shape)

print(np.min(grid),np.max(grid))
print(grid_x)
#print(grid)
"""
plt.subplot(211)
for lt in range(grid.shape[0]):
    print(lt)
    for ln in range(grid.shape[1]):
        if 0.2 <= grid[lt,ln] <= 0.4:
            plt.plot(grid_y[lt,ln],grid_x[lt,ln],'b.',ms=1)
        if 0.4 <= grid[lt,ln] <= 0.6:
            plt.plot(grid_y[lt,ln],grid_x[lt,ln],'g.',ms=1)
        if 0.6 <= grid[lt,ln] <= 0.8:
            plt.plot(grid_y[lt,ln],grid_x[lt,ln],'y.',ms=1)
        if 0.8 <= grid[lt,ln] <= 1:
            plt.plot(grid_y[lt,ln],grid_x[lt,ln],'r.',ms=1)

plt.subplot(212)
for i in range(lat.shape[0]):
    print(i)
    if 0.2 <= vals[i] <= 0.4:
        plt.plot(lon[i], lat[i],'b.',ms=1)
    if 0.4 <= vals[i] <= 0.6:
        plt.plot(lon[i],lat[i],'g.',ms=1)
    if 0.6 <= vals[i] <= 0.8:
        plt.plot(lon[i],lat[i],'y.',ms=1)
    if 0.8 <= vals[i] <= 1:
        plt.plot(lon[i],lat[i],'r.',ms=1)
plt.show()
"""
