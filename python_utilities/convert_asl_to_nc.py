from netCDF4 import Dataset
import numpy as np

def add_params(root_grp):
    root_grp.createDimension('time',None)
    time = root_grp.createVariable('time', 'f8', ('time',))
    lon = root_grp.createVariable('longitude', 'f8', ('time',))
    pres = root_grp.createVariable('asl', 'f8', ('time',))

    root_grp.variables["time"][:] = np.arange(1980,2017+1)
    root_grp.variables["longitude"][:] = np.zeros((38,))
    root_grp.variables["asl"][:] = np.zeros((38,))

prefix_path_out = './final_final_data/index_asl_'

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

count_djf = 0
count_mam = 0
count_jja = 0
count_son = 0

by = 1980
fy = 2017

with open('asl.txt') as f:
    for line in f.readlines():
        data = line.split()
        year = int(data[0])
        season = data[1].lower()
        index_asl = float(data[3])
        in_lon = float(data[4])
        if season == 'djf':
            year += 1

        if year < by:
            continue

        if year > fy:
            continue

        print(year)

        if season == 'djf':
            djf.variables["longitude"][year-by] = in_lon
            djf.variables["asl"][year-by] = index_asl

        if season == 'mam':
            mam.variables["longitude"][year-by] = in_lon
            mam.variables["asl"][year-by] = index_asl

        if season == 'jja':
            jja.variables["longitude"][year-by] = in_lon
            jja.variables["asl"][year-by] = index_asl

        if season == 'son':
            son.variables["longitude"][year-by] = in_lon
            son.variables["asl"][year-by] = index_asl

djf.close()
mam.close()
jja.close()
son.close()
