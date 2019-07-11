addpath('C:\Users\NCAOR7\Desktop\ocean_seasons')
ncdisp('C:\Users\NCAOR7\Desktop\BITS\ocean_seasons\so_djf.nc')
filename='C:\Users\NCAOR7\Desktop\BITS\ocean_seasons\so_son.nc';
% time=ncread(filename,'time');
Lon=ncread(filename,'longitude');
Lat=ncread(filename,'latitude');
lev=ncread(filename,'LEV');
% % Lon(1:165)=[];
% lev(23:30)=[];
% lev = -lev;
%  [Lev1,Lon1]=meshgrid(lev,Lon);
So=ncread(filename,'so');
% So(1:165,:,:,:)=[];
So(:,:,23:30,:)=[];
so=So(:,21,:,:);
so=squeeze(so);
so(:,:,38)=[];
 so(so>10e+10)=nan;
so_pre=so(:,:,1:21);
so_post=so(:,:,22:37);
% 
% 
% 
%  [tr,p]=trend(so_post,10);
%  trsig=tr;
%  trsig(p>=0.05)=nan;
%  
%  [M,c]=contourf(Lon1,Lev1,tr,8,'ShowText','off');
% hold on
% xlabel('longitude');
% ylabel('depth (meters)');
% stipple(Lon1,Lev1,p<0.05,...
%  'density',350,...
%     'color',rgb('black'),...
%     'markersize',4)
% c.LineWidth=0.25;
%   cb=colorbar;
%   caxis([-0.4 0.4])
%   colormap(redblue(30))
% title('Salinity of ocean water trends at 65-S Section');
% ylabel(cb,'Trends (per decade')
% 
%   
