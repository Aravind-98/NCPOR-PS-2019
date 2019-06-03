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

def add_params(root_grp):
    root_grp.createDimension('time',None)
    root_grp.createDimension('lat',180)
    root_grp.createDimension('lon',360)
    time = root_grp.createVariable('time', 'f8', ('time',))
    lat = root_grp.createVariable('latitude', 'f4', ('lat'))
    lon = root_grp.createVariable('longitude', 'f4', ('lon'))
    sst = root_grp.createVariable('SST', 'f8', ('time','lat','lon'))

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

for var in data.variables:
    print(var)
print('\n')
print(data.variables["SST"])

base_year = 1870
base_month = 1

def get_data(year,month):
    index =  12*(year - base_year) + month - base_month
    return data.variables["SST"][:][index,:,:]

for year in range(1979,2018+1):
    print(year)
    print('djf')
    if year == base_year:
        djf["SST"][year-base_year,:,:] = (get_data(year,1)+get_data(year,2))/2
    else:
        djf["SST"][year-base_year] = (get_data(year-1,12)+get_data(year,1)+get_data(year,2))/3
    print('mam')
    mam["SST"][year-base_year] = (get_data(year,3)+get_data(year,4)+get_data(year,5))/3
    print('jja')
    jja["SST"][year-base_year] = (get_data(year,6)+get_data(year,7)+get_data(year,8))/3
    print('son')
    son["SST"][year-base_year] = (get_data(year,9)+get_data(year,10)+get_data(year,11))/3

djf.close()
mam.close()
jja.close()
son.close()
