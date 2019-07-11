addpath('C:\Users\NCAOR7\Desktop\BITS\Data')
projectdir = 'C:\Users\NCAOR7\Desktop\BITS\SeaIceData';
dinfo = dir( fullfile(projectdir, '*.nc') );
num_files = length(dinfo);
ncdisp('C:\Users\NCAOR7\Desktop\BITS\SeaIceData\198801.nc')
filenames = fullfile( projectdir, {dinfo.name} );
for K = 1 : num_files
  this_file = filenames{K};
  %lats{K} = ncread(this_file, ncvars{1});
  %lons{K} = ncread(this_file, ncvars{2});
  %precips{K} = ncread(this_file, ncvars{3});
  %times{K} = ncread(this_file, ncvars{4});
  ice_con(:,:,K)= ncread(this_file, 'goddard_merged_seaice_conc_monthly');
end
ice_con(:,:,110)=((ice_con(:,:,109)+ice_con(:,:,111))/2);

lat=ncread(this_file,'latitude');
lon=ncread(this_file,'longitude');
ice_concDJF(1:316,1:332,1:39)=0;
for k = 21 : 37
     
    ice_concDJF(:,:,k)=ice_con(:,:,10+((k-1)*12))+ice_con(:,:,11+((k-1)*12))+ice_con(:,:,12+((k-1)*12));
end
ice_concDJF=ice_concDJF/3;
ice_concDJF(isnan(ice_concDJF))=0.00;
[tr,p]=trend(100*ice_concDJF,1);

globepcolor(lat,lon,17*tr);
hold on
%globestipple(Lat,Lon,p<0.05,...
   %'density',250,...
   %'color',rgb('dark green'),...
   %'markersize',8)
cb = colorbar;
caxis([-100 100])
load coast
colormap(redblue(10))
ylabel(cb,'Sea ice conc.')
globeborders('color',rgb('black'),'Linewidth',1)
view(-180,-80)
zoom(2)