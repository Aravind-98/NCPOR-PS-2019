from netCDF4 import Dataset
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.cm as cm
path = './seaice_conc_monthly_sh_f08_198903_v03r01.nc'
data = Dataset(path,'r+')

## plot sea ice fraction in p.i.b. on a given month
def plot_ice(name):
    ## read the data
    fh = Dataset(path, mode='r')
    lon = fh.variables['longitude'][:]
    lat = fh.variables['latitude'][:]
    sic = fh.variables[name][:]
    fh.close()

    ## plot sea ice concentration
    fig = plt.figure(figsize=[8,6])
    m = Basemap(projection='stere',resolution='h',lat_0=-64,lon_0=0,\
                llcrnrlon=-80,urcrnrlon=80,llcrnrlat=-39.36,urcrnrlat=-89.84)
    m.drawmapboundary(fill_color='white')
    m.drawcoastlines()
    m.fillcontinents()
    m.drawparallels(np.arange(-89.,-60.,2.),labels=[1,0,0,0],fontsize=14)
    m.drawmeridians(np.arange(-180.,181.,10.),labels=[0,0,0,1],fontsize=14)
    xi, yi = m(lon, lat)

    frac_levels = np.linspace(0,1,11)
    cs = m.contourf(xi, yi, sic[0, :, :], frac_levels, cmap=cm.PuBu_r)
    cbar = plt.colorbar(cs, fraction=0.046, pad=0.04)
    cbar.ax.tick_params(labelsize=14)
    cbar.ax.set_ylabel('Sea Ice Conc.', fontsize=14)
    plt.title('PIB sea ice conc., Summer', fontsize=14)
    #plt.savefig('./media/ice_img/seaice_conc_.png'.format(date))
    plt.show()
    plt.close();
# pprint(data.variables["seaice_conc_monthly_cdr"])
# pprint(data.variables["seaice_conc_monthly_cdr"][:])
ds_meta = data.variables["longitude"]
ds = ds_meta[:]
#pprint(ds_meta)
#pprint(ds[ds.mask==True])
#pprint(ds.shape)
#pprint(ds)
plot_ice('seaice_conc_monthly_cdr')
