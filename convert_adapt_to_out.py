from netCDF4 import Dataset
import numpy as np
import sys
from scipy.interpolate import griddata

in_path = sys.argv[1]
out_path = './multi-data.nc'

data = Dataset(in_path, 'r+')

#data_time = data.variables["time"][:]
#data_sst = data.variables["sst"][:]
#data_lat = data.variables["latitude"][:]
#data_lon = data.variables["longitude"][:]

#data.close()

root_grp = Dataset(out_path, 'w')

root_grp.createDimension('time', None)
root_grp.createDimension('ygrid', 1441)
root_grp.createDimension('xgrid', 161)
time = root_grp.createVariable('time', 'f8', ('time',))
x = root_grp.createVariable('x', 'f8', ('xgrid'))
y = root_grp.createVariable('y', 'f8', ('ygrid'))
SST = root_grp.createVariable('SST', 'f8', ('time', 'xgrid', 'ygrid'))
lat = root_grp.createVariable('lat', 'f4', ('xgrid','ygrid'))
lon = root_grp.createVariable('lon', 'f4', ('xgrid','ygrid'))
# g_m_conc = root_grp.createVariable('sea_ice_conc', 'f4', ('time', 'xgrid', 'ygrid'), fill_value=0)
# m_o_day = root_grp.createVariable('melt_onset_day_seaice_conc_monthly_cdr', 'f8', ('time','lat','lon'), fill_value=0)

in_lat = data.variables["latitude"][:].flatten()
in_lon = data.variables["longitude"][:].flatten()
in_lon = np.mod(in_lon+180,360) - 180

temp_x,temp_y = np.meshgrid(in_lat,in_lon)
temp_x = temp_x.T
temp_y = temp_y.T

grid_lat, grid_lon = np.mgrid[-90:-50:161j, -180:180:1441j]
lat[:] = grid_lat
lon[:] = grid_lon

for i in range(data.variables["time"].shape[0]):
    print(i)

    vals = data.variables["sst"][i][:][:].flatten()

    grid_lat, grid_lon = np.mgrid[-90:-50:161j, -180:180:1441j]
    points = np.column_stack((temp_x.flatten(), temp_y.flatten()))

    grid = griddata(points, vals, (grid_lat, grid_lon), method='linear')
    grid[np.isnan(grid)] = 0
    SST[i,:,:] = grid

root_grp.close()
