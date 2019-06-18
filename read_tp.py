import csv

with Dataset(out_path, 'w') as root_grp:

	root_grp.createDimension('time', None)
	root_grp.createDimension('ind', None)
    time = root_grp.createVariable('time','f8',('time',))
    ind = root_grp.createVariable('ind','f8',('ind',))
    lat = root_grp.createVariable('lat','f8',('ind',))
    lon = root_grp.createVariable('lon','f8',('ind',))
    tp = root_grp.createVariable('tp','f8',('time','ind',))

    base_year = 1979

    in_ind = 0
    tp_ind = 0
    for year in range(1979,2018):

        fyear = str(year)[-2:]
        fname = f'cmap_mon_v1906_{fyear}.txt'

        with open(fname) as f:
            data = f.readline().split()
            in_year = int(data[0])
            in_month = int(data[1])
            in_lat = float(data[2])
            in_lon = float(data[3])
            in_tp = float(data[4])

            if year == base_year:
                lat[ind] = in_lat
                lon[ind] = in_lon
                ind += 1

            tp[12*in_year+in_month,tp_ind] = in_tp
            tp_ind += 1
