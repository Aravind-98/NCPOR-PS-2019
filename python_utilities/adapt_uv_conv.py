from netCDF4 import Dataset
from pprint import pprint
import numpy as np
import numpy.ma as ma
import sys
pathin = sys.argv[1]
prefix_path_out='./'
base_year = 1979
base_month = 1
data = Dataset(pathin,'r')
data_lat = data.variables["latitude"][:]
data_lon = data.variables["longitude"][:]
#data_u = data.variablles['u'][:]
#data_v = data.variablles['v'][:]
postfix = '_uv'
data.close()

def get_data_u(year,month):
    index =  12*(year - base_year) + (month - base_month)
    return data_u[index,:,:]

def get_data_v(year,month):
    index =  12*(year - base_year) + (month - base_month)
    return data_v[index,:,:]

def add_params(root_grp):
    root_grp.createDimension('time',None)
    root_grp.createDimension('lat',None)
    root_grp.createDimension('lon',None)
    time = root_grp.createVariable('time', 'f8', ('time',))
    lat = root_grp.createVariable('lat', 'f4', ('lat',))
    lon = root_grp.createVariable('lon', 'f4', ('lon',))
    u = root_grp.createVariable('u', 'f8', ('time','lat','lon'))
    v = root_grp.createVariable('v', 'f8', ('time','lat','lon'))
    lat[:] = data_lat
    lon[:] = data_lon

out_path_djf = prefix_path_out+'djf'+postfix+'.nc'
djf = Dataset(out_path_djf,'w')
add_params(djf)

out_path_mam = prefix_path_out+'mam'+postfix+'.nc'
mam = Dataset(out_path_mam,'w')
add_params(mam)

out_path_jja = prefix_path_out+'jja'+postfix+'.nc'
jja = Dataset(out_path_jja,'w')
add_params(jja)

out_path_son = prefix_path_out+'son'+postfix+'.nc'
son = Dataset(out_path_son,'w')
add_params(son)


for year in range(1979,2016):
    print(year)
    print('djf')
    if year == base_year:
        djf["u"][year-base_year,:,:] = (get_data_u(year,1)+get_data_u(year,2))/2
        djf["v"][year-base_year,:,:] = (get_data_v(year,1)+get_data_v(year,2))/2
    else:
        djf["v"][year-base_year,:,:] = (get_data_u(year-1,12)+get_data_u(year,1)+get_data_u(year,2))/3
        djf["v"][year-base_year,:,:] = (get_data_v(year-1,12)+get_data_v(year,1)+get_data_v(year,2))/3
    print('mam')
    mam["u"][year-base_year,:,:] = (get_data_u(year,3)+get_data_u(year,4)+get_data_u(year,5))/3
    mam["v"][year-base_year,:,:] = (get_data_v(year,3)+get_data_v(year,4)+get_data_v(year,5))/3
    print('jja')
    jja["u"][year-base_year,:,:] = (get_data_u(year,6)+get_data_u(year,7)+get_data_u(year,8))/3
    jja["v"][year-base_year,:,:] = (get_data_v(year,6)+get_data_v(year,7)+get_data_v(year,8))/3
    print('son')
    son["u"][year-base_year,:,:] = (get_data_u(year,9)+get_data_u(year,10)+get_data_u(year,11))/3
    son["v"][year-base_year,:,:] = (get_data_v(year,9)+get_data_v(year,10)+get_data_v(year,11))/3

djf.close()
mam.close()
jja.close()
son.close()
