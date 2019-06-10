from netCDF4 import Dataset
import numpy as np
import sys
from scipy.interpolate import griddata

in_path = '/home/komalvasudeva/PycharmProjects/PSproject/venv/bin/MODEL.SST.HAD187001-198110.OI198111-201903.nc'
out_path = '/home/komalvasudeva/PycharmProjects/PSproject/venv/bin/model_SST_output1.nc'
data = Dataset(in_path, 'r+')

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

# in_lat = data.variables["lat"][:].flatten()
# in_lon = data.variables["lon"][:].flatten()
grid_lat, grid_lon = np.mgrid[-90:-50:161j, -180:180:1441j]
lat[:] = grid_lat
lon[:] = grid_lon
"""
for i in lat:
    print(i)
for i in lon:
    print(i)
"""
for i in range(data.variables["time"].shape[0]):
    vals = data.variables["SST"][i][:][:].flatten()
# print(np.max(vals))
# print(np.min(vals))
# print(vals[np.where(vals>=11.755)].shape)
#
    temp_x, temp_y = np.mgrid[-89.5:89.5:180j, -179.5:179.5:360j]
    grid_lat, grid_lon = np.mgrid[-90:-50:161j, -180:180:1441j]
    points = np.column_stack((temp_x.flatten(), temp_y.flatten()))
#    print('--->')
    # print(points.shape)
    # print(vals.shape)
    grid = griddata(points, vals, (grid_lat, grid_lon), method='linear')
    grid[np.isnan(grid)] = 0

    # print(np.min(grid))
    # print(np.max(grid))

     # print(grid)

    SST[i,:,:] = grid
    if i%10==0:
        print(i+1)

root_grp.close()


















