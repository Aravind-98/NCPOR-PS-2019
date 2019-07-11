from netCDF4 import Dataset
import numpy as np
import sys
from scipy.interpolate import griddata

in_path = sys.argv[1]
out_path = sys.argv[2]
print(in_path,out_path)
with Dataset(in_path, 'r+') as data:
	with Dataset(out_path, 'w') as root_grp:

		root_grp.createDimension('time', None)
		root_grp.createDimension('ygrid', 1441)
		root_grp.createDimension('xgrid', 161)
		time = root_grp.createVariable('time', 'f8', ('time',))
		x = root_grp.createVariable('x', 'f8', ('xgrid'))
		y = root_grp.createVariable('y', 'f8', ('ygrid'))
		sic = root_grp.createVariable('sic', 'f8', ('time', 'xgrid', 'ygrid'))
		lat = root_grp.createVariable('lat', 'f4', ('xgrid','ygrid'))
		lon = root_grp.createVariable('lon', 'f4', ('xgrid','ygrid'))
		try:
			in_lat = data.variables["latitude"][:].flatten()
			in_lon = data.variables["longitude"][:].flatten()
		except:
			in_lat = data.variables["lat"][:].flatten()
			in_lon = data.variables["lon"][:].flatten()

		#in_lon = np.mod(in_lon+180,360) - 180

		grid_lat, grid_lon = np.mgrid[-90:-50:161j, -180:180:1441j]
		lat[:] = grid_lat
		lon[:] = grid_lon
		time[:] = data.variables["time"][:]

		points = np.column_stack((in_lat.flatten(),in_lon.flatten()))
		for i in range(data.variables["time"].shape[0]):
		#for i in range(10):
			"""
			with open('log_adapt','a') as f:
				f.write(u(i)+'\n')
			"""
			vals = data.variables["seaice_conc_monthly_cdr"][i][:][:].flatten()
			grid = griddata(points, vals, (grid_lat, grid_lon), method='nearest')
			sic[i,:,:] = grid
