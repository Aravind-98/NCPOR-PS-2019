addpath('C:\Users\NCAOR7\Desktop\ocean_seasons')
ncdisp('C:\Users\NCAOR7\Desktop\BITS\ocean_seasons\vel_djf.nc')
filename='C:\Users\NCAOR7\Desktop\BITS\ocean_seasons\vel_son.nc';
% time=ncread(filename,'time');
Lon=ncread(filename,'longitude');
Lat=ncread(filename,'latitude');
lev=ncread(filename,'LEV');
 lev=-lev;
 lev(23:30)=[];
  [Lev1,Lon1]=meshgrid(lev,Lon);
Uo=ncread(filename,'uo');
Uo(:,:,23:30,:)=[];
uo=Uo(:,25,:,:);
uo=squeeze(uo);
uo(:,:,38)=[];
 uo(uo>10e+10)=nan;
uo_pre=uo(:,:,1:21);
uo_post=uo(:,:,22:37);

Vo=ncread(filename,'vo');
Vo(:,:,23:30,:)=[];
vo=Vo(:,25,:,:);
vo=squeeze(vo);
vo(:,:,38)=[];
 vo(vo>10e+10)=nan;
vo_pre=vo(:,:,1:21);
vo_post=vo(:,:,22:37);

[tr_u,p_u]=trend(uo_post,10);
[tr_v,p_v]=trend(vo_post,10);
%  trsig=tr;
%  trsig(p>=0.05)=nan;
% 
figure(2)
[M,c]=contourf(Lon1,Lev1,tr_v,'ShowText','off');
xlabel('longitude');
ylabel('depth (meters)');
 hold on
 plotEveryThisMany = 3;
tr_u1 = tr_u(1:plotEveryThisMany:end,:);
tr_v1 = tr_v(1:plotEveryThisMany:end,:);
Lon2 = Lon1(1:plotEveryThisMany:end,:);
Lev2 = Lev1(1:plotEveryThisMany:end,:) ;
quiver(Lon2,Lev2,tr_u1,tr_v1,'LineWidth',0.5,'MaxHeadSize',.05,'AutoScaleFactor',1.50,'Color',[0.00 0.00 0.00]);
stipple(Lon1,Lev1,p_v<0.05,...
 'density',350,...
    'color',rgb('green'),...
    'markersize',7)
c.LineWidth=0.25;
  cb=colorbar;
  caxis([-0.05 0.05])
  colormap(redblue(30))
title('Salinity of ocean water trends');
ylabel(cb,'Trends (per decade)')

hold off
%   
