from netCDF4 import Dataset
import numpy as np
import sys
from scipy.interpolate import griddata

in_path = sys.argv[1]
out_path = sys.argv[2]
data = Dataset(in_path,'r+')

root_grp = Dataset(out_path,'w')

root_grp.createDimension('time', None)
root_grp.createDimension('xgrid', 161)
root_grp.createDimension('ygrid', 1441)
time = root_grp.createVariable('time', 'f8', ('time',))
x =  root_grp.createVariable('xgrid','f8',('xgrid'))
y =  root_grp.createVariable('ygrid','f8',('ygrid'))
lat = root_grp.createVariable('latitude', 'f4', ('xgrid','ygrid'))
lon = root_grp.createVariable('longitude', 'f4', ('xgrid','ygrid'))
g_m_conc = root_grp.createVariable('sea_ice_conc', 'f4', ('time','xgrid','ygrid'), fill_value=0)
#m_o_day = root_grp.createVariable('melt_onset_day_seaice_conc_monthly_cdr', 'f8', ('time','lat','lon'), fill_value=0)

in_lat = data.variables["latitude"][:].flatten()
in_lon = data.variables["longitude"][:].flatten()
vals = data.variables["goddard_merged_seaice_conc_monthly"][:].flatten()

points = np.column_stack((in_lat,in_lon))

grid_x, grid_y = np.mgrid[-90:-50:161j, -180:180:1441j]

grid  = griddata(points,vals, (grid_x,grid_y), method='nearest')
grid[np.isnan(grid)] = 0

lat[:] = grid_x
lon[:] = grid_y
g_m_conc[0,:] = grid

root_grp.close()
