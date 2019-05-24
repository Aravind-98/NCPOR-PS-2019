from netCDF4 import Dataset
import numpy as np
import numpy.ma as ma

path = './seaice_conc_monthly_sh_f08_198903_v03r01.nc'
data = Dataset(path,'r+')

root_grp = Dataset('1989-07-test.nc', 'w', format='NETCDF4')
root_grp.description = 'Example simulation data'

root_grp.createDimension('time', None)
root_grp.createDimension('xgrid', 316)
root_grp.createDimension('ygrid', 332)

time = root_grp.createVariable('time', 'f8', ('time',))
x = root_grp.createVariable('xgrid', 'f4', ('xgrid',))
y = root_grp.createVariable('ygrid', 'f4', ('ygrid',))
lat = root_grp.createVariable('latitude', 'f4', ('ygrid','xgrid'))
lon = root_grp.createVariable('longitude', 'f4', ('ygrid','xgrid'))
g_m_conc = root_grp.createVariable('goddard_merged_seaice_conc_monthly', 'i4', ('time','ygrid','xgrid'))
m_o_day = root_grp.createVariable('melt_onset_day_seaice_conc_monthly_cdr', 'i8', ('time','ygrid','xgrid'))

in_gm_conc = data.variables["goddard_merged_seaice_conc_monthly"][:]
g_m_conc[:] = in_gm_conc
# g_m_conc[np.where(in_gm_conc.mask==True)] = ma.masked
in_m_o_day = data.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]
m_o_day[:] = in_m_o_day
# m_o_day[np.where(in_m_o_day.mask==True)] = ma.masked
root_grp.close
