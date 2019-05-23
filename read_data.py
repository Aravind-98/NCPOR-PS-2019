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

def plot(fig,num,heading,lat,lon,data):
    ax = fig.add_subplot(f'23{num}')
    ax.set_title(heading, pad=20)
    # make South pole Stereographic projection
    m = Basemap(projection='spstere', boundinglat=-30, lon_0=180., resolution='h', round=True)

    # may not be required
    m.fillcontinents(alpha=0.42)
    #ax.title(heading)

    # draw parallel longitude lines
    m.drawmeridians(np.arange(-180.,181.,30.), labels=[1,1,1,1])

    # draw parallel latitude lines
    m.drawparallels(np.arange(-90.,-40.,10.), labels=[1,1,1,1])

    # add the observations to the map
    m.pcolormesh(lon, lat, data[0,:,:], cmap='RdYlBu',latlon=True)

    #fig.colorbar(cm.ScalarMappable(cmap='RdYlBu'),orientation='horizontal',ax=ax)

lat = data.variables["latitude"][:]
lon = data.variables["longitude"][:]
fig = plt.figure()


sic = data.variables["seaice_conc_monthly_cdr"][:]
sic_masked = ma.masked_less_equal(sic,0.0)
plot(fig,1,'Concentration',lat,lon,sic_masked)

std_sic = data.variables["stdev_of_seaice_conc_monthly_cdr"][:]
std_sic_masked = ma.masked_less_equal(sic,0.0)
plot(fig,2,'std_dev',lat,lon,std_sic_masked)

"""
melt = data.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]
melt_masked = ma.masked_less_equal(melt,0.0)
plot(fig,3,'melt onset',lat,lon,melt_masked)
"""
"""
qa = data.variables["qa_of_seaice_conc_monthly_cdr"][:]
qa_masked = ma.masked_less_equal(qa,0.0)
plot(fig,4,'qa',lat,lon,qa_masked)
"""

g_merged = data.variables["goddard_merged_seaice_conc_monthly"][:]
g_merged_masked = ma.masked_less_equal(g_merged,0.0)
plot(fig,3,'goddard merged conc',lat,lon,g_merged_masked)

g_nt = data.variables["goddard_nt_seaice_conc_monthly"][:]
g_nt_masked = ma.masked_less_equal(g_nt,0.0)
plot(fig,4,'goddard nt conc',lat,lon,g_nt_masked)

g_bt = data.variables["goddard_bt_seaice_conc_monthly"][:]
g_bt_masked = ma.masked_less_equal(g_bt,0.0)
plot(fig,5,'goddard bt conc',lat,lon,g_bt_masked)

#plt.title('South Pole Stereographic Projection for sea ice concentration for 12-2017')
plt.subplots_adjust(wspace=0.5,hspace=0.5)
plt.show()
