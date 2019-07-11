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

def plot(fig,num,heading,lat,lon,data):
    ax = fig.add_subplot(str(num))
    #ax.set_title(heading, pad=20)
    # make South pole Stereographic projection
    m = Basemap(projection='spstere', boundinglat=-50, lon_0=180., resolution='h', round=True)
    #m = Basemap()
    # may not be required
    #ax.title(heading)

    # draw parallel longitude lines
    m.drawmeridians(np.arange(-180.,181.,30.), labels=[1,1,1,1])

    # draw parallel latitude lines
    m.drawparallels(np.arange(-90.,-40.,10.), labels=[1,0,0,1])

    # add the observations to the map
    m.fillcontinents(alpha=0.42)

    #data_anomaly = (np.mean(data,axis=0)-np.mean(data))/np.sqrt(np.var(data))

    m.pcolormesh(lon, lat, data, cmap='coolwarm',vmin=-.5,vmax=.5,latlon=True)

    plt.colorbar(orientation='horizontal',ax=ax,shrink=0.7)

data.set_fill_on()

for var in data.variables:
    print(var)
print('\n')

ind = 0

try:
    lat = data.variables["lat"][:]
    lon = data.variables["lon"][:]
except:
    lat = data.variables["latitude"][:]
    lon = data.variables["longitude"][:]
fig = plt.figure()
data_attr = data.variables[sys.argv[2]][:]

print(np.min(data_attr),np.max(data_attr))

plot(fig,121,'sea ice conc',lat,lon,data_attr[0,:,:])
plot(fig,122,'sea ice conc',lat,lon,data_attr[1,:,:])
plt.subplots_adjust(wspace=0.5,hspace=0.5)
plt.show()
