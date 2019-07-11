from netCDF4 import Dataset
from pprint import pprint
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.basemap import Basemap
import matplotlib.cm as cm
from scipy.stats import linregress
import sys

def make_colormap(seq):
    """Return a LinearSegmentedColormap
    seq: a sequence of floats and RGB-tuples. The floats should be increasing
    and in the interval (0,1).
    """
    seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
        if isinstance(item, float):
            r1, g1, b1 = seq[i - 1]
            r2, g2, b2 = seq[i + 1]
            cdict['red'].append([item, r1, r2])
            cdict['green'].append([item, g1, g2])
            cdict['blue'].append([item, b1, b2])
    return mcolors.LinearSegmentedColormap('CustomMap', cdict)

def plot(fig,num,heading,lat,lon,data):
    #ax = fig.add_subplot(str(num))
    #ax.set_title(heading, pad=20)
    # make South pole Stereographic projection
    m = Basemap(projection='spstere', boundinglat=-30, lon_0=180., resolution='h', round=True)

    # may not be required
    #ax.title(heading)

    # draw parallel longitude lines
    m.drawmeridians(np.arange(-180.,181.,30.), labels=[1,1,1,1])

    # draw parallel latitude lines
    m.drawparallels(np.arange(-90.,-40.,10.), labels=[1,0,0,1])

    # add the observations to the map
    m.pcolormesh(lon, lat, data, cmap='coolwarm',latlon=True,vmin=-1,vmax=1)
    m.fillcontinents(alpha=0.42)
    plt.colorbar(orientation='horizontal')

path = sys.argv[1]
data = Dataset(path,'r+')

for var in data.variables:
    print(var)
print('\n')

try:
    lat = data.variables["latitude"][:]
    lon = data.variables["longitude"][:]
except:
    lat = data.variables["lat"][:]
    lon = data.variables["lon"][:]

base_year = 1979
time_dur = [1979,1999]

x = np.arange(time_dur[0],time_dur[1])
y = data.variables[sys.argv[2]][time_dur[0]-base_year:time_dur[1]-base_year,:,:]
x_t = np.tile(x,(y.shape[1],y.shape[2])).reshape((y.shape[1],y.shape[0],y.shape[2])).reshape(y.shape)
#y[np.where(y.mask==True)] = -1

print(x.shape)
print(y.shape)
print(x_t.shape)
#trends = np.zeros(y[0,:,:].shape)
print(trends.shape)

"""
print('lin reg...')
for i in range(y.shape[1]):
    print(i)
    for j in range(y.shape[2]):
        trends[i,j],_,_,p,_ = linregress(x,y[:,i,j])
        if  p >= 0.05:
            trends[i,j] = 0

"""
print('plotting...')
trends = trends*100
#trends[np.where(trends.mask==True)] = 0
print(np.min(trends),np.max(trends))
ind = np.where(trends!=0)
print(ind[0].shape)
fig = plt.figure()
plot(fig,111,'trends',lat,lon,trends)
plt.show()
