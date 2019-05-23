from netCDF4 import Dataset
from pprint import pprint
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.cm as cm
path = './seaice_conc_monthly_sh_f17_201712_v03r01.nc'
data = Dataset(path,'r+')

for var in data.variables:
    print(var)
print('\n')

def plot(lat,lon,data):
    # make South pole Stereographic projection
    m = Basemap(projection='spstere', boundinglat=-30, lon_0=180., resolution='l', round=True)
    # may not be required
    m.drawcountries(linewidth=0.25)
    m.fillcontinents(alpha=0.42)

    # draw parallel longitude lines
    m.drawmeridians(np.arange(-180.,181.,30.), labels=[1,1,1,1])

    # draw parallel latitude lines
    m.drawparallels(np.arange(-90.,-40.,10.), labels=[1,1,1,1])

    # plot the results
    m.pcolormesh(lon, lat, data[0,:,:], cmap='RdYlBu',latlon=True)
    plt.title('South Pole Stereographic Projection for sea ice concentration')
    plt.colorbar(orientation='horizontal', ticks=np.arange(0,1,10), )
    plt.show()

lat = data.variables["latitude"][:]
lon = data.variables["longitude"][:]

sic = data.variables["seaice_conc_monthly_cdr"][:]
sic_masked = ma.masked_less_equal(sic,0.0)
plot(lat,lon,sic_masked)
