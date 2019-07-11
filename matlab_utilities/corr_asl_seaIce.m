%Reaanlysis data 
addpath('C:\Users\NCAOR7\Desktop\BITS\final_data')

addpath('C:\Users\NCAOR7\Desktop\BITS\Reanalysis_data\final_final_data\index_files\seasonal')
% ncdisp('C:\Users\NCAOR7\Desktop\BITS\Reanalysis_data\final_final_data\index_files\seasonal\SOI\djf_soi.nc')
filename='C:\Users\NCAOR7\Desktop\BITS\final_data\conv_djf.nc';
filename1='C:\Users\NCAOR7\Desktop\BITS\Reanalysis_data\final_final_data\index_files\seasonal\ASL\index_asl_son.nc';
filename2='C:\Users\NCAOR7\Desktop\BITS\Reanalysis_data\final_final_data\index_files\seasonal\PDO\son_pdo.nc';
filename3='C:\Users\NCAOR7\Desktop\BITS\Reanalysis_data\final_final_data\index_files\seasonal\SAM\index_sam_djf.nc';
filename4='C:\Users\NCAOR7\Desktop\BITS\Reanalysis_data\final_final_data\index_files\seasonal\SOI\son_soi.nc';

ice=ncread(filename,'sea_ice_conc');
asl=ncread(filename1,'asl');
pdo=ncread(filename2,'pdo');
sam=ncread(filename3,'sam');
soi=ncread(filename4,'soi');

% lon=ncread(filename,'longitude');
% lat=ncread(filename,'latitude');

ice(isnan(ice))=0.00;
ice(:,:,39)=[];
ice(:,:,38)=[];
ice_pre=ice(:,:,1:21);
ice_post=ice(:,:,22:37);
asl(38)=[];
asl_pre=asl(1:21);
asl_post=asl(22:37);
pdo(38:40)=[];
pdo_pre = pdo(1:21);
pdo_post=pdo(22:37);
sam(38:40)=[];
sam_pre=sam(1:21);
sam_post=sam(22:37);
soi(38:40)=[];
soi_pre=soi(1:21);
soi_post=soi(22:37);


[R,P]=corr3(ice_post,sam_post);
globepcolor(lat,lon,R*100);
hold on

globestipple(lat,lon,P<0.05,...
 'density',250,...
    'color',rgb('black'),...
    'markersize',8)
cb = colorbar;
caxis([-100 100])
colormap(redblue(30))
% title('Correlation of Sea Ice-DJF and SAM-DJF');
ylabel(cb,'Correlation scale(%)')
globeborders('color',rgb('black'),'Linewidth',1)
view(-180,-80)
zoom(2)
