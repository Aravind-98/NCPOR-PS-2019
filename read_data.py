from netCDF4 import Dataset
from pprint import pprint
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.cm as cm
#path = './data/seaice_conc_monthly_sh_f08_198906_v03r01.nc'
path = './out_format/test_out.nc'
data = Dataset(path,'r+')

for var in data.variables:
    print(var)
print('\n')
#print(data.variables["goddard_merged_seaice_conc_monthly"])
#melt_onset_meta = data.variables["melt_onset_day_seaice_conc_monthly_cdr"]
#melt_onset = data.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]
print(data.variables["lat"][:])
print('')
print(data.variables["lon"][:])
print('')
#print(data.variables["goddard_merged_seaice_conc_monthly"][:])
#print('')
#print(data.variables["melt_onset_day_seaice_conc_monthly_cdr"][:])
#print(data.variables["goddard_merged_seaice_conc_monthly"][:])
#print(melt_onset[np.where(melt_onset.mask==False)])
"""
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
    m.pcolormesh(lon, lat, data[0,:,:], cmap='RdYlBu',latlon=True)
    m.fillcontinents(alpha=0.42)

    #fig.colorbar(cm.ScalarMappable(cmap='RdYlBu'),orientation='horizontal',ax=ax)
lat = data.variables["latitude"][:]
lon = data.variables["longitude"][:]
fig = plt.figure()
g_merged = data.variables["goddard_merged_seaice_conc_monthly"][:]
g_merged_masked = ma.masked_less_equal(g_merged,0.0)
plot(fig,111,'goddard merged conc',lat,lon,g_merged_masked)
plt.title('South Pole Stereographic Projection for sea ice concentration for 12-2017')
plt.subplots_adjust(wspace=0.5,hspace=0.5)
plt.show()
"""
