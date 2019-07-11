from netCDF4 import Dataset
import numpy as np
import csv

def add_params(root_grp):
    root_grp.createDimension('time',None)
    time = root_grp.createVariable('time', 'f8', ('time',))
    pres = root_grp.createVariable('sam', 'f8', ('time',))

    root_grp.variables["time"][:] = np.arange(1979,2018+1)
    root_grp.variables["sam"][:] = np.zeros((40,))

prefix_path_out = './final_final_data/index_sam_'

out_path_djf = prefix_path_out+'djf.nc'
djf = Dataset(out_path_djf,'w')
add_params(djf)

out_path_mam = prefix_path_out+'mam.nc'
mam = Dataset(out_path_mam,'w')
add_params(mam)

out_path_jja = prefix_path_out+'jja.nc'
jja = Dataset(out_path_jja,'w')
add_params(jja)

out_path_son = prefix_path_out+'son.nc'
son = Dataset(out_path_son,'w')
add_params(son)

by = 1979
fy = 2018

with open('sam.txt') as f:
    for line in f.readlines():
        data = line.split()
        year = int(data[0])

        if year < by:
            continue

        if year > fy:
            continue

        print(year)

        mam.variables["sam"][year-by] = float(data[2])
        jja.variables["sam"][year-by] = float(data[3])
        son.variables["sam"][year-by] = float(data[4])
        djf.variables["sam"][year-by] = float(data[5])

djf.close()
mam.close()
jja.close()
son.close()
