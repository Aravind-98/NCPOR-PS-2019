from netCDF4 import Dataset
from pprint import pprint
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.cm as cm
path = './out_format/198903.nc'
data = Dataset(path,'r+')

data.set_fill_on()

for var in data.variables:
    print(var)
print('\n')

lat = data.variables["lat"]
lon = data.variables["lon"]
sic = data.variables["goddard_merged_seaice_conc_monthly"]
print(sic)

colors = { (0,0.25):'green', (0.25,0.5): 'yellow', (0.5,0.75): 'orange', (0.75,1): 'red' }

plt.xlim([-180,180])
plt.ylim([-90,-50])
for i in np.arange(-90,-50+1,1):
    print(i,sic[0,i,0])
    for j in np.arange(-180,180+1,1):
        if sic[0,i,j] >= 0.05:
            for r,c in colors.items():
                if r[0] <= sic[0,i,j] <= r[1]:
                    plt.scatter(j,i,color=c)
                    break
plt.show()
