import csv
import numpy as np
from netCDF4 import Dataset

prefix_path_out = './final_final_data/index_soi.nc'

with Dataset(prefix_path_out,'w') as root_grp:
    root_grp.createDimension('time',None)
    time = root_grp.createVariable('time', 'f8', ('time',))
    soi = root_grp.createVariable('soi', 'f8', ('time',))

    root_grp.variables["time"][:] = np.zeros((40*12,))
    root_grp.variables["soi"][:] = np.zeros((40*12,))

    by = 1979
    fy = 2018
    bm = 1

    with open('soi.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            year = int(row[0][:4])
            month = int(row[0][-2:])
            val = float(row[1])

            if year < by or year > fy:
                continue

            print(year,month,val)
            print(year-by + month-bm)
            time[12*(year-by) + (month-bm)] = 12*(year-by) + (month-bm)
            soi[12*(year-by) + (month-bm)] =  val
