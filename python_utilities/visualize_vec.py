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

def plot(fig,num,heading,lat,lon,u,v):
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

    skip = 8
    urot,vrot,x,y = m.rotate_vector(u,v,lon,lat,returnxy=True)
    c_m  = np.hypot(x,y)
    c_m_k = np.ones(x[::skip,::skip].shape)
    m.quiver(x, y, urot, vrot, c_m, color='k', scale=80)
    print(x.shape,y.shape,urot.shape,vrot.shape)
    #print(x[::2,::2].shape,y[::2].shape,urot[::2].shape,vrot[::2].shape)
    #m.quiver(x[::skip,::skip], y[::skip,::skip], urot[::skip,::skip], vrot[::skip,::skip], c_m_k, color='k', scale=80)
    #m.quiver(x, y, urot, vrot, c_m, c='scale=20)
    #m.quiver(lon, lat, u, v, latlon=True, scale=10)
    #q2 = m.quiver(x, y, u, v, latlon=True, scale=30, scale_units='inches')
    #m.streamplot(lon,lat,u,v)
    #ax.set_aspect('equal')
    plt.colorbar(orientation='horizontal',ax=ax)

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

ind = -1

u = data.variables['u'][ind,:,:]
v = data.variables['v'][ind,:,:]

plot(fig,111,'sea ice conc',lat,lon,u,v)

#plt.title('South Pole Stereographic Projection for sea ice concentration for 12-2017')
#plt.subplots_adjust(wspace=0.5,hspace=0.5)
plt.show()
