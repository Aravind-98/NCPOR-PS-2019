import csv
import numpy as np
from netCDF4 import Dataset

prefix_path_out = './final_final_data/index_pdo.nc'

with Dataset(prefix_path_out,'w') as root_grp:
    root_grp.createDimension('time',None)
    time = root_grp.createVariable('time', 'f8', ('time',))
    pdo = root_grp.createVariable('pdo', 'f8', ('time',))

    root_grp.variables["time"][:] = np.zeros((40*12,))
    root_grp.variables["pdo"][:] = np.zeros((40*12,))

    by = 1979
    fy = 2018
    bm = 1

    with open('pdo.csv') as f:
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
            pdo[12*(year-by) + (month-bm)] =  val
