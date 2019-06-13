from netCDF4 import Dataset
import numpy as np
import sys
from scipy.interpolate import griddata

in_path = sys.argv[1]
out_path = './final_data_adapt/multi_data_ssr.nc'

data = Dataset(in_path, 'r+')

#data_time = data.variables["time"][:]
#data_sst = data.variables["sst"][:]
#data_lat = data.variables["latitude"][:]
#data_lon = data.variables["longitude"][:]

#data.close()

with Dataset(out_path, 'w') as root_grp:

	root_grp.createDimension('time', None)
	root_grp.createDimension('ygrid', 1441)
	root_grp.createDimension('xgrid', 161)
	time = root_grp.createVariable('time', 'f8', ('time',))
	x = root_grp.createVariable('x', 'f8', ('xgrid'))
	y = root_grp.createVariable('y', 'f8', ('ygrid'))
	ssr = root_grp.createVariable('ssr', 'f8', ('time', 'xgrid', 'ygrid'))
	lat = root_grp.createVariable('lat', 'f4', ('xgrid','ygrid'))
	lon = root_grp.createVariable('lon', 'f4', ('xgrid','ygrid'))

	in_lat = data.variables["latitude"][:].flatten()
	in_lon = data.variables["longitude"][:].flatten()
	in_lon = np.mod(in_lon+180,360) - 180

	temp_x,temp_y = np.meshgrid(in_lat,in_lon)
	temp_x = temp_x.T
	temp_y = temp_y.T

	grid_lat, grid_lon = np.mgrid[-90:-50:161j, -180:180:1441j]
	lat[:] = grid_lat
	lon[:] = grid_lon
	time[:] = data.variables["time"][:]

	for i in range(data.variables["time"].shape[0]):

		with open('log_adapt','a') as f:
			f.write(str(i)+'\n')

		vals = data.variables["ssr"][i][:][:].flatten()
		grid_lat, grid_lon = np.mgrid[-90:-50:161j, -180:180:1441j]
		points = np.column_stack((temp_x.flatten(), temp_y.flatten()))

		grid = griddata(points, vals, (grid_lat, grid_lon), method='linear')
		grid[np.isnan(grid)] = 0
		ssr[i,:,:] = grid
