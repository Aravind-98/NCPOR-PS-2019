from netCDF4 import Dataset
import sys
import numpy as np

ind = 'goddard_merged_seaice_conc_monthly'
ind1 = 'seaice_conc_monthly_cdr'
base_year = 1979
sic_data = 999*np.ones((32,332,316))

for year in range(1979,2010+1):
    with Dataset(f'{year}.nc') as data:
        sic_data[year-base_year,:,:] = data[ind][:][0,:,:]

with Dataset('2018_2019-avg_1979_2010.nc','w') as root_grp:
    root_grp.createDimension('time', None)
    root_grp.createDimension('ygrid', 332)
    root_grp.createDimension('xgrid', 316)
    time = root_grp.createVariable('time','f8',('time',))
    ygrid = root_grp.createVariable('ygrid','f8',('ygrid',))
    xgrid = root_grp.createVariable('xgrid','f8',('xgrid',))
    lat = root_grp.createVariable('latitude','f8',('ygrid', 'xgrid'))
    lon = root_grp.createVariable('longitude','f8',('ygrid', 'xgrid'))
    sic = root_grp.createVariable('sic','f8',('time', 'ygrid', 'xgrid',))
    time = np.array([2018,2019])
    avg_data = np.mean(sic_data,axis=0)
    with Dataset('2018.nc') as f2018:
        lat[:,:] = f2018['latitude'][:]
        lon[:,:] = f2018['longitude'][:]
        sic[0,:,:] = f2018[ind1][:][0,:,:] - avg_data

    with Dataset('2019.nc') as f2019:
        sic[1,:,:] = f2019[ind1][:][0,:,:] - avg_data
