from netCDF4 import Dataset
from pprint import pprint
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
import sys

in_path = sys.argv[1]
out_path = sys.argv[2]
root_grp = Dataset(out_path,'w')
data = Dataset(in_path,'r+')

root_grp.createDimension('time', None)
root_grp.createDimension('lat', 159)
root_grp.createDimension('lon', 1440)
time = root_grp.createVariable('time', 'f8', ('time',))
lat = root_grp.createVariable('lat', 'f4', ('lat',))
lon = root_grp.createVariable('lon', 'f4', ('lon',))
g_m_conc = root_grp.createVariable('goddard_merged_seaice_conc_monthly', 'f4', ('time','lat','lon'), fill_value=0)
m_o_day = root_grp.createVariable('melt_onset_day_seaice_conc_monthly_cdr', 'f8', ('time','lat','lon'), fill_value=0)

#in_lat = data.variables["latitude"][:]
#in_lon = data.variables["longitude"][:]
in_lat_fl = np.around(data.variables["latitude"][:].flatten(),3)
in_lon_fl = np.around(data.variables["longitude"][:].flatten(),3)

in_gm_fl = data.variables["goddard_merged_seaice_conc_monthly"][0,:,:].flatten()
in_mo_fl = data.variables["melt_onset_day_seaice_conc_monthly_cdr"][0,:,:].flatten()

lat[:] = np.arange(-90,-50.25,0.25)
lon[:] = np.arange(-180,180,0.25)
"""
for i in range(-90,-50+1):
    j = 50
    ind = np.argmin(np.square(in_lat_fl-i)+np.square(in_lon_fl-j))
    print(i,in_gm_fl[ind],in_gm_fl[ind].mask)
"""
#sic = np.zeros((159,1440))
#counti = 0
#countj = 0
a = []
for i in np.arange(-90,-50.25,0.25):
    if i%10 == 0:
        print(f'{out_path} | {i}')
    for j in np.arange(-180,180,0.25):
        ind = np.argmin(np.square(in_lat_fl-i)+np.square(in_lon_fl-j))
        g_m_conc[0,i,j] = in_gm_fl[ind]
        m_o_day[0,i,j] = in_mo_fl[ind]

root_grp.close
