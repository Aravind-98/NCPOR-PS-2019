from netCDF4 import Dataset
from pprint import pprint
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.cm as cm
import sys

print('reading...')
path = sys.argv[1]
df = Dataset(path,'r+')
data = df.variables["SST"][:]
df.close()
print('done')

def add_params(root_grp):
    root_grp.createDimension('time', None)
    root_grp.createDimension('xgrid', 161)
    root_grp.createDimension('ygrid', 1441)
    time = root_grp.createVariable('time', 'f8', ('time',))
    x =  root_grp.createVariable('xgrid','f8',('xgrid'))
    y =  root_grp.createVariable('ygrid','f8',('ygrid'))
    lat = root_grp.createVariable('latitude', 'f4', ('xgrid','ygrid'))
    lon = root_grp.createVariable('longitude', 'f4', ('xgrid','ygrid'))
    sst = root_grp.createVariable('SST', 'f8', ('time','xgrid','ygrid'), fill_value=0)
    grid_x, grid_y = np.mgrid[-90:-50:161j, -180:180:1441j]
    lat[:] = grid_x
    lon[:] = grid_y

prefix_path_out = '/home/manan/NCPOR/season_SST/'

out_path_djf = prefix_path_out+'djf.nc'
djf = Dataset(out_path_djf,'w')
add_params(djf)

out_path_mam = prefix_path_out+'mam.nc'
mam = Dataset(out_path_mam,'w')
add_params(mam)

out_path_jja = prefix_path_out+'jja.nc'
jja = Dataset(out_path_jja,'w')
add_params(jja)

out_path_son = prefix_path_out+'son.nc'
son = Dataset(out_path_son,'w')

add_params(son)

base_year = 1870
base_month = 1
ind_year = 1979

def get_data(year,month):
    index =  12*(year - base_year) + month - base_month
    return data[index,:,:]

for year in range(1979,2018+1):
    print(year)
    print('djf')
    if year == base_year:
        djf["SST"][year-ind_year,:,:] = (get_data(year,1)+get_data(year,2))/2
    else:
        djf["SST"][year-ind_year,:,:] = (get_data(year-1,12)+get_data(year,1)+get_data(year,2))/3
    print('mam')
    mam["SST"][year-ind_year,:,:] = (get_data(year,3)+get_data(year,4)+get_data(year,5))/3
    print('jja')
    jja["SST"][year-ind_year,:,:] = (get_data(year,6)+get_data(year,7)+get_data(year,8))/3
    print('son')
    son["SST"][year-ind_year,:,:] = (get_data(year,9)+get_data(year,10)+get_data(year,11))/3

djf.close()
mam.close()
jja.close()
son.close()
