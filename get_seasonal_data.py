from netCDF4 import Dataset
from pprint import pprint
import numpy as np
import numpy.ma as ma

def add_params(root_grp):
    root_grp.createDimension('time',None)
    root_grp.createDimension('xgrid',316)
    root_grp.createDimension('ygrid',332)
    time = root_grp.createVariable('time', 'f8', ('time',))
    x = root_grp.createVariable('xgrid', 'f4', ('xgrid',))
    y = root_grp.createVariable('ygrid', 'f4', ('ygrid',))
    lat = root_grp.createVariable('latitude', 'f4', ('ygrid','xgrid'))
    lon = root_grp.createVariable('longitude', 'f4', ('ygrid','xgrid'))
    g_m_conc = root_grp.createVariable('goddard_merged_seaice_conc_monthly', 'i4', ('time','ygrid','xgrid'))
    m_o_day = root_grp.createVariable('melt_onset_day_seaice_conc_monthly_cdr', 'i8', ('time','ygrid','xgrid'))

#prefix_path_out= './final_data/'
prefix_path_out = '/home/aravindan/NCPOR-PS-2019/season/'

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
prefix_path_in='/home/aravindan/NCPOR-PS-2019/data_backup/'
for year in range(1978+1,2017+1):
    print(year)
    # season 1 - djf
    d_in = Dataset(prefix_path_in+f'{year-1}12.nc')
    gm_d = d_in.variables["goddard_merged_seaice_conc_monthly"][0,:,:]
    mo_d = d_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][0,:,:]
    if year != 1988:
        j_in = Dataset(prefix_path_in+f'{year}01.nc')
        gm_j = j_in.variables["goddard_merged_seaice_conc_monthly"][0,:,:]
        mo_j = j_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][0,:,:]
    f_in = Dataset(prefix_path_in+f'{year}02.nc')
    gm_f = f_in.variables["goddard_merged_seaice_conc_monthly"][0,:,:]
    mo_f = f_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][0,:,:]
    gm_d = ma.masked_less_equal(gm_d,0.0)
    gm_j = ma.masked_less_equal(gm_d,0.0)
    gm_f = ma.masked_less_equal(gm_d,0.0)
    if year != 1988:
        djf.variables["goddard_merged_seaice_conc_monthly"][year-base_year,:,:] = (gm_d+gm_j+gm_f)/3
        djf.variables["melt_onset_day_seaice_conc_monthly_cdr"][year-base_year,:,:] = (gm_d+gm_j+gm_f)/3
    else:
        djf.variables["goddard_merged_seaice_conc_monthly"][year-base_year,:,:] = (gm_d+gm_f)/2
        djf.variables["melt_onset_day_seaice_conc_monthly_cdr"][year-base_year,:,:] = (gm_d+gm_f)/2

    # season 2 - mam
    ma_in = Dataset(prefix_path_in+f'{year}03.nc')
    gm_ma = ma_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_ma = ma_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]
    a_in = Dataset(prefix_path_in+f'{year}04.nc')
    gm_a = a_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_a = a_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]
    my_in = Dataset(prefix_path_in+f'{year}05.nc')
    gm_my = my_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_my = my_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]

    mam.variables["goddard_merged_seaice_conc_monthly"][year-base_year,:,:] = (gm_ma+gm_a+gm_my)/3
    mam.variables["melt_onset_day_seaice_conc_monthly_cdr"][year-base_year,:,:] = (mo_ma+mo_a+mo_my)/3

    # season 3 - jja
    jun_in = Dataset(prefix_path_in+f'{year}06.nc')
    gm_jun = jun_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_jun = jun_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]
    jul_in = Dataset(prefix_path_in+f'{year}07.nc')
    gm_jul = jul_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_jul = jul_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]
    aug_in = Dataset(prefix_path_in+f'{year}08.nc')
    gm_aug = aug_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_aug = aug_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]

    jja.variables["goddard_merged_seaice_conc_monthly"][year-base_year,:,:] =(gm_jun+gm_jul+gm_aug)/3
    jja.variables["melt_onset_day_seaice_conc_monthly_cdr"][year-base_year,:,:] =(mo_jun+mo_jul+mo_aug)/3

    # season 4 - son
    s_in = Dataset(prefix_path_in+f'{year}09.nc')
    gm_s = s_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_s = s_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]
    o_in = Dataset(prefix_path_in+f'{year}10.nc')
    gm_o = o_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_o = o_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]
    n_in = Dataset(prefix_path_in+f'{year}11.nc')
    gm_n = n_in.variables["goddard_merged_seaice_conc_monthly"][:]
    mo_n = n_in.variables["melt_onset_day_seaice_conc_monthly_cdr"][:]

    son.variables["goddard_merged_seaice_conc_monthly"][year-base_year,:,:] = (gm_s+gm_o+gm_n)/3
    son.variables["melt_onset_day_seaice_conc_monthly_cdr"][year-base_year,:,:] = (mo_s+mo_o+mo_n)/3

djf.close()
mam.close()
jja.close()
son.close()
