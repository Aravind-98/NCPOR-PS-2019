from netCDF4 import Dataset
from pprint import pprint
import numpy as np
import numpy.ma as ma

def add_params(rootgrp):
    time = root_grp.createVariable('time', 'f8', ('time',))
    x = root_grp.createVariable('xgrid', 'f4', ('xgrid',))
    y = root_grp.createVariable('ygrid', 'f4', ('ygrid',))
    lat = root_grp.createVariable('latitude', 'f4', ('ygrid','xgrid'))
    lon = root_grp.createVariable('longitude', 'f4', ('ygrid','xgrid'))
    g_m_conc = root_grp.createVariable('goddard_merged_seaice_conc_monthly', 'i4', ('time','ygrid','xgrid'))
    m_o_day = root_grp.createVariable('melt_onset_day_seaice_conc_monthly_cdr', 'i8', ('time','ygrid','xgrid'))

out_path_son = './temp.nc'
son = Dataset(out_path_son,'w')
add_params(son)

out_path_mam = './temp.nc'
mam = Dataset(out_path_mam,'w')
add_params(mam)

out_path_jja = './temp.nc'
jja = Dataset(out_path_jja,'w')
add_params(jja)

out_path_son = './temp.nc'
son = Dataset(path_son,'w')
add_params(son)

base_year = 1979

for year in range(1978+1,2017+1):
    # season 1 - son
    s_in = Dataset(f'{year-1}-12.nc')
    gm_s = s_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_s = s_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]
    o_in = Dataset(f'{year}-01.nc')
    gm_o = o_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_o = o_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]
    n_in = Dataset(f'{year}-02.nc')
    gm_n = n_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_n = n_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]

    son.variables["goddard_merged_seaice_conc_monthly"][year-base_year,:,:] = np.mean(gm_s,gm_o,gm_n)
    son.variables["melt_onset_day_seaice_conc_monthly_cdr"][year-base_year,:,:] = np.mean(mo_s,mo_o,mo_n)

    # season 2 - mam
    ma_in = Dataset(f'{year}-03.nc')
    gm_ma = ma_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_ma = ma_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]
    a_in = Dataset(f'{year}-04.nc')
    gm_a = a_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_a = a_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]
    my_in = Dataset(f'{year}-05.nc')
    gm_my = my_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_my = my_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]

    mam.variables["goddard_merged_seaice_conc_monthly"][year-base_year,:,:] = np.mean(gm_ma,gm_a,gm_my)
    mam.variables["melt_onset_day_seaice_conc_monthly_cdr"][year-base_year,:,:] = np.mean(mo_ma,mo_a,mo_my)

    # season 3 - jja
    jun_in = Dataset(f'{year}-06.nc')
    gm_jun = jun_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_jun = jun_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]
    jul_in = Dataset(f'{year}-07.nc')
    gm_jul = jul_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_jul = jul_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]
    aug_in = Dataset(f'{year}-08.nc')
    gm_aug = aug_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_aug = aug_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]

    jja.variables["goddard_merged_seaice_conc_monthly"][year-base_year,:,:] = np.mean(gm_jun,gm_jul,gm_aug)
    jja.variables["melt_onset_day_seaice_conc_monthly_cdr"][year-base_year,:,:] = np.mean(mo_,jun_jul,mo_aug)

    # season 4 - son
    s_in = Dataset(f'{year}-09.nc')
    gm_s = s_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_s = s_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]
    o_in = Dataset(f'{year}-10.nc')
    gm_o = o_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_o = o_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]
    n_in = Dataset(f'{year}-11.nc')
    gm_n = n_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_n = n_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]

    son.variables["goddard_merged_seaice_conc_monthly"][year-base_year,:,:] = np.mean(gm_s,gm_o,gm_n)
    son.variables["melt_onset_day_seaice_conc_monthly_cdr"][year-base_year,:,:] = np.mean(mo_s,mo_o,mo_n)
