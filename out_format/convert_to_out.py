from netCDF4 import Dataset
from pprint import pprint
import numpy as np
import numpy.ma as ma

in_path = '../data/seaice_conc_monthly_sh_f08_198906_v03r01.nc'

root_grp = Dataset('test_out.nc','w')
data = Dataset(in_path,'r+')

root_grp.createDimension('time', None)
root_grp.createDimension('lat', 159)
root_grp.createDimension('lon', 1440)
time = root_grp.createVariable('time', 'f8', ('time',))
lat = root_grp.createVariable('lat', 'f4', ('lat',))
lon = root_grp.createVariable('lon', 'f4', ('lon',))
g_m_conc = root_grp.createVariable('goddard_merged_seaice_conc_monthly', 'f4', ('time','lat','lon'))
m_o_day = root_grp.createVariable('melt_onset_day_seaice_conc_monthly_cdr', 'f8', ('time','lat','lon'))

#in_lat = data.variables["latitude"][:]
#in_lon = data.variables["longitude"][:]
in_lat_fl = data.variables["latitude"][:].flatten()
in_lon_fl = data.variables["longitude"][:].flatten()
in_gm_fl = data.variables["goddard_merged_seaice_conc_monthly"][0,:,:].flatten()
in_mo_fl = data.variables["melt_onset_day_seaice_conc_monthly_cdr"][0,:,:].flatten()

"""
lat[:] = in_lat[ind]
lon[:] = in_lon[ind]

print(in_lat[ind].shape)
#print(in_lat[ind].flatten())
#print(in_lon[ind].flatten())

l = len(ind[0])
for i in ind[0]:
    print(f'{i}/{l}')
    for j in ind[1]:
        g_m_conc[0,in_lat[i,j],in_lon[i,j]] = in_gm[i,j]
        m_o_day[0,in_lat[i,j],in_lon[i,j]] = in_mo[i,j]

root_grp.close()
"""

lat[:] = np.arange(-90,-50.25,0.25)
lon[:] = np.arange(-180,180,0.25)

for i in np.arange(-90,-50.25,0.25):
    print(i)
    for j in np.arange(-180,180,0.25):
        ind = np.argmin(np.square(in_lat_fl-i)+np.square(in_lon_fl-j))
        g_m_conc[0,i,j] = in_gm_fl[ind]
        m_o_day[0,i,j] = in_mo_fl[ind]
