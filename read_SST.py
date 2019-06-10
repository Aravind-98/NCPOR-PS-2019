from netCDF4 import Dataset
from pprint import pprint
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt

path = '/home/komalvasudeva/PycharmProjects/PSproject/venv/bin/MODEL.SST.HAD187001-198110.OI198111-201903.nc'
data = Dataset(path, 'r+')

for var in data.variables:
    print(var)
print('\n')
# # gd_m_c = data.variables['goddard_merged_seaice_conc_monthly'][:]
lats = data.variables['lat'][:]
lon = data.variables['lon'][:]
sst = data.variables['SST'][:]
# # print(np.where(gd_m_c.mask == True)[0].shape)
#
# # gd_m_c[0, :, :].mask[np.where(lats >= -50)] = True
#
# # print(gd_m_c[np.where(lats >= -50 and gd_m_c.mask == )])
# # pprint(data.variables['latitude'][:])
"""
for var in lats:
    pprint(var)
"""
# for var in sst:
#     pprint(var)
print(lats.shape)
# pprint("Longitudes are as follows ")

# for var in lon:
#     pprint(var)
print(lon.shape)
print(sst.shape)
for var in sst[360,15,:]:
    pprint(var)

# print(np.where(lats>=-50)[0].shape)
# print(np.where(gd_m_c.mask == True)[0].shape)