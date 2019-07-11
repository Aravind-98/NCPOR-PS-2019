from netCDF4 import Dataset
import sys

with Dataset('./final_final_data/adapt_merged_heat.nc', 'w') as root_grp:
	root_grp.description = '(str + ssr + slhf + sshf) /12*3600'
	root_grp.createDimension('time', None)
	root_grp.createDimension('ygrid', 1441)
	root_grp.createDimension('xgrid', 161)
	time = root_grp.createVariable('time', 'f8', ('time',))
	x = root_grp.createVariable('x', 'f8', ('xgrid'))
	y = root_grp.createVariable('y', 'f8', ('ygrid'))
	q_merged = root_grp.createVariable('q_merged', 'f8', ('time', 'xgrid', 'ygrid'))
	lat = root_grp.createVariable('lat', 'f4', ('xgrid','ygrid'))
	lon = root_grp.createVariable('lon', 'f4', ('xgrid','ygrid'))

	prefix = './final_final_data/multi_data'
	with Dataset(f'{prefix}_slhf.nc') as in_slhf:
		lat[:,:] = in_slhf.variables["lat"][:]
		lon[:,:] = in_slhf.variables["lon"][:]
		slhf = in_slhf.variables["slhf"][:]
	print('slhf')

	with Dataset(f'{prefix}_sshf.nc') as in_sshf:
		sshf = in_sshf.variables["sshf"][:]
	print('sshf')
	with Dataset(f'{prefix}_sst.nc') as in_sst:
		sst = in_sst.variables["SST"][:]
	print('sst')
	with Dataset(f'{prefix}_ssr.nc') as in_ssr:
		ssr = in_ssr.variables["ssr"][:]
	print('ssr')
	q_merged[:,:,:] = (ssr+sst+sshf+slhf) / (12*3600)
