from netCDF4 import Dataset
from pprint import pprint
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.cm as cm
import sys

path =  '/home/komalvasudeva/PycharmProjects/PSproject/venv/bin/model_SST_output.nc'
data = Dataset(path,'r+')

def plot(fig,num,heading,lat,lon,data):
    ax = fig.add_subplot(str(num))
    ax.set_title(heading, pad=20)
    # make South pole Stereographic projection
    m = Basemap(projection='spstere', boundinglat=-30, lon_0=180., resolution='h', round=True)

    # may not be required
    #ax.title(heading)

    # draw parallel longitude lines
    m.drawmeridians(np.arange(-180.,181.,30.), labels=[1,1,1,1])

    # draw parallel latitude lines
    m.drawparallels(np.arange(-90.,-40.,10.), labels=[1,0,0,1])

    # add the observations to the map
    m.fillcontinents(alpha=0.42)
    m.pcolormesh(lon, lat, data[:,:], cmap='RdYlBu',latlon=True)

#    plt.colorbar(cm.ScalarMappable(cmap='RdYlBu'),orientation='horizontal',ax=ax)

data.set_fill_on()

for var in data.variables:
    print(var)
print('\n')

try:
    lat = data.variables["lat"][:]
    lon = data.variables["lon"][:]
except:
    lat = data.variables["latitude"][:]
    lon = data.variables["longitude"][:]
fig = plt.figure()

ind = 24
try:
    g_merged = data.variables["sea_ice_conc"][24,:,:]
except:
    g_merged = data.variables["SST"][24,:,:]

g_merged_masked = g_merged
g_merged_masked = ma.masked_less_equal(g_merged,0.0)
print(g_merged_masked[np.where(g_merged_masked.mask==True)].shape)

plot(fig,111,'sea ice conc',lat,lon,g_merged_masked)

plt.title('South Pole Stereographic Projection for sea ice concentration for 12-2017')
plt.subplots_adjust(wspace=0.5,hspace=0.5)
plt.show()