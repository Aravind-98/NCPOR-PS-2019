from netCDF4 import Dataset
from pprint import pprint
import numpy as np
import numpy.ma as ma

#function to identify leap_year
def is_leap_year(year):
        if year%400==0:
            return True
        elif year%100==0:
            return False
        if year%4==0:
            return True
        else:
            return False
index={
"jan":(0,31-1),
"feb":(31,31+28-1),
"mar":(59,59+31-1),
"apr":(90,90+30-1),
"may":(120,120+31-1),
"jun":(151,151+30-1),
"jul":(181,181+31-1),
"aug":(212,212+31-1),
"sep":(243,243+31-1),
"oct":(274,274+30-1),
"nov":(304,304+31-1),
"dec":(335,335+30-1),
}
index_leap={
"jan":(0,31-1),
"feb":(31,31+29-1),
"mar":(60,60+31-1),
"apr":(91,91+30-1),
"may":(121,121+31-1),
"jun":(152,152+30-1),
"jul":(182,182+31-1),
"aug":(213,213+31-1),
"sep":(244,244+31-1),
"oct":(275,275+30-1),
"nov":(305,305+31-1),
"dec":(336,336+30-1),
}

def add_params(root_grp):
    root_grp.createDimension('time',None)
    root_grp.createDimension('x',321)
    root_grp.createDimension('y',321)
    time = root_grp.createVariable('time', 'f8', ('time',))
    x = root_grp.createVariable('x', 'f4', ('x',))
    y = root_grp.createVariable('y', 'f4', ('y',))
    lat = root_grp.createVariable('latitude', 'f4', ('y','x'))
    lon = root_grp.createVariable('longitude', 'f4', ('y','x'))
    u = root_grp.createVariable('u','f8',('time','y','x'))
    v = root_grp.createVariable('v','f8',('time','y','x'))

get_avg = lambda a,b,c: (np.sum(a,axis=0)+np.sum(b,axis=0)+np.sum(c,axis=0))/(np.shape(a)[0]+np.shape(b)[0]+np.shape(c)[0])

#prefix_path_out= './final_data/'
prefix_path_out = '/home/aravindan/NCPOR-PS-2019/season_ice/'

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

base_year = 1979
prefix_path_in='/home/aravindan/NCPOR-PS-2019/ice_data/'
for year in range(1978+1,2018+1):
    print(year)
    # season 1 - djf
    in_file_prev = Dataset(prefix_path_in+f'{year-1}.nc')
    in_file = Dataset(prefix_path_in+f'{year}.nc')

    u_prev = in_file_prev.variables["u"][:]
    v_prev = in_file_prev.variables["v"][:]
    u_prev = ma.masked_less_equal(u_prev,0.0)
    v_prev = ma.masked_less_equal(v_prev,0.0)

    u = in_file.variables["u"][:]
    v = in_file.variables["v"][:]
    u = ma.masked_less_equal(u,0.0)
    v = ma.masked_less_equal(v,0.0)

    if is_leap_year(year):
        dec_u = u_prev[index_leap["dec"][0]:index_leap["dec"][1],:,:]
        jan_u = u[index_leap["jan"][0]:index_leap["jan"][1],:,:]
        feb_u = u[index_leap["feb"][0]:index_leap["feb"][1],:,:]
        mar_u = u[index_leap["mar"][0]:index_leap["mar"][1],:,:]
        apr_u = u[index_leap["apr"][0]:index_leap["apr"][1],:,:]
        may_u = u[index_leap["may"][0]:index_leap["may"][1],:,:]
        jun_u = u[index_leap["jun"][0]:index_leap["jun"][1],:,:]
        jul_u = u[index_leap["jul"][0]:index_leap["jul"][1],:,:]
        aug_u = u[index_leap["aug"][0]:index_leap["aug"][1],:,:]
        sep_u = u[index_leap["sep"][0]:index_leap["sep"][1],:,:]
        oct_u = u[index_leap["oct"][0]:index_leap["oct"][1],:,:]
        nov_u = u[index_leap["nov"][0]:index_leap["nov"][1],:,:]

        djf.variables["u"][year-base_year,:,:] = get_avg(dec_u,jan_u,feb_u)
        mam.variables["u"][year-base_year,:,:] = get_avg(mar_u,apr_u,may_u)
        jja.variables["u"][year-base_year,:,:] = get_avg(jun_u,jul_u,aug_u)
        son.variables["u"][year-base_year,:,:] = get_avg(sep_u,oct_u,nov_u)

        dec_v = v_prev[index_leap["dec"][0]:index_leap["dec"][1],:,:]
        jan_v = v[index_leap["jan"][0]:index_leap["jan"][1],:,:]
        feb_v = v[index_leap["feb"][0]:index_leap["feb"][1],:,:]
        mar_v = v[index_leap["mar"][0]:index_leap["mar"][1],:,:]
        apr_v = v[index_leap["apr"][0]:index_leap["apr"][1],:,:]
        may_v = v[index_leap["may"][0]:index_leap["may"][1],:,:]
        jun_v = v[index_leap["jun"][0]:index_leap["jun"][1],:,:]
        jul_v = v[index_leap["jul"][0]:index_leap["jul"][1],:,:]
        aug_v = v[index_leap["aug"][0]:index_leap["aug"][1],:,:]
        sep_v = v[index_leap["sep"][0]:index_leap["sep"][1],:,:]
        oct_v = v[index_leap["oct"][0]:index_leap["oct"][1],:,:]
        nov_v = v[index_leap["nov"][0]:index_leap["nov"][1],:,:]

        djf.variables["v"][year-base_year,:,:] = get_avg(dec_v,jan_v,feb_v)
        mam.variables["v"][year-base_year,:,:] = get_avg(mar_v,apr_v,may_v)
        jja.variables["v"][year-base_year,:,:] = get_avg(jun_v,jul_v,aug_u)
        son.variables["v"][year-base_year,:,:] = get_avg(sep_v,oct_v,nov_v)

    else:
        dec_u = u_prev[index["dec"][0]:index["dec"][1],:,:]
        jan_u = u[index["jan"][0]:index["jan"][1],:,:]
        feb_u = u[index["feb"][0]:index["feb"][1],:,:]
        mar_u = u[index["mar"][0]:index["mar"][1],:,:]
        apr_u = u[index["apr"][0]:index["apr"][1],:,:]
        may_u = u[index["may"][0]:index["may"][1],:,:]
        jun_u = u[index["jun"][0]:index["jun"][1],:,:]
        jul_u = u[index["jul"][0]:index["jul"][1],:,:]
        aug_u = u[index["aug"][0]:index["aug"][1],:,:]
        sep_u = u[index["sep"][0]:index["sep"][1],:,:]
        oct_u = u[index["oct"][0]:index["oct"][1],:,:]
        nov_u = u[index["nov"][0]:index["nov"][1],:,:]

        djf.variables["u"][year-base_year,:,:] = get_avg(dec_u,jan_u,feb_u)
        mam.variables["u"][year-base_year,:,:] = get_avg(mar_u,apr_u,may_u)
        jja.variables["u"][year-base_year,:,:] = get_avg(jun_u,jul_u,aug_u)
        son.variables["u"][year-base_year,:,:] = get_avg(sep_u,oct_u,nov_u)

        dec_v = v_prev[index["dec"][0]:index["dec"][1],:,:]
        jan_v = v[index["jan"][0]:index["jan"][1],:,:]
        feb_v = v[index["feb"][0]:index["feb"][1],:,:]
        mar_v = v[index["mar"][0]:index["mar"][1],:,:]
        apr_v = v[index["apr"][0]:index["apr"][1],:,:]
        may_v = v[index["may"][0]:index["may"][1],:,:]
        jun_v = v[index["jun"][0]:index["jun"][1],:,:]
        jul_v = v[index["jul"][0]:index["jul"][1],:,:]
        aug_v = v[index["aug"][0]:index["aug"][1],:,:]
        sep_v = v[index["sep"][0]:index["sep"][1],:,:]
        oct_v = v[index["oct"][0]:index["oct"][1],:,:]
        nov_v = v[index["nov"][0]:index["nov"][1],:,:]

        djf.variables["v"][year-base_year,:,:] = get_avg(dec_v,jan_v,feb_v)
        mam.variables["v"][year-base_year,:,:] = get_avg(mar_v,apr_v,may_v)
        jja.variables["v"][year-base_year,:,:] = get_avg(jun_v,jul_v,aug_u)
        son.variables["v"][year-base_year,:,:] = get_avg(sep_v,oct_v,nov_v)

djf.close()
mam.close()
jja.close()
son.close()
