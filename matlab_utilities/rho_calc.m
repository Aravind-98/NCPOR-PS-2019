

% addpath('C:\Users\NCAOR7\Desktop\ocean_seasons')
% % ncdisp('C:\Users\NCAOR7\Desktop\BITS\ocean_seasons\so_djf.nc')
% filename='C:\Users\NCAOR7\Desktop\BITS\ocean_seasons\so_djf.nc';
% % time=ncread(filename,'time');
% Lon=ncread(filename,'longitude');
% Lat=ncread(filename,'latitude');
% lev=ncread(filename,'LEV');
% % Lon(1:165)=[];
% lev(19:30)=[];
% lev = -lev;
%  [Lev1,Lon1]=meshgrid(lev,Lon);
% So=ncread(filename,'so');
% % So(1:165,:,:,:)=[];
% So(:,:,19:30,:)=[];
% so=So(:,21,:,:);
% so=squeeze(so);
% so(:,:,38)=[];
%  so(so>10e+10)=nan;
% so_pre=so(:,:,1:21);
% so_post=so(:,:,22:37);

T=temp2;
S=salinity2;
dep=depth;
depth2=depth1;
p = -(1025*9.8*dep);
p = p*1.0e-5;
% p = p';


a0 = 999.842594;
a1 = 6.793953 * 10^-2;
a2 = -9.095290 * 10^-3;
a3 = 1.001685 * 10^-4;
a4 = -1.120083 * 10^-6;
a5 = 6.536332 * 10^-9;

b0 = 8.2449 * 10^-1;
b1 = -4.0899 * 10^-3;
b2 = 7.6438 * 10^-5;
b3 = -8.2467 * 10^-7;
b4 = 5.3875 * 10^-9;

c0 = -5.7246 * 10^-3;
c1 = 1.0227 * 10^-4;
c2 = -1.6546 * 10^-6;
d0 = 4.8314 * 10^-4;

e0 = 19652.210000;
e1 = 148.420600;
e2= -2.327105;
e3 = 1.360477 * 10^-2;
e4= -5.155288 * 10^-5;

f0 = 54.674600;
f1 = -0.603459;
f2 = 1.099870 * 10^-2;
f3 = -6.167000 * 10^-5;

g0 = 7.9440 * 10^-2;
g1 = 1.6483 * 10^-2;
g2 = -5.3009 * 10^-4;

h0 = 3.23990;
h1 = 1.43713 * 10^-3;
h2 = 1.16092 * 10^-4;
h3 = -5.77905 * 10^-7;

i0 = 2.28380 * 10^-3;
i1 = -1.09810 * 10^-5;
i2 = -1.60780 * 10^-6;
j0 = 1.91075 * 10^-4;

k0 = 8.50935 * 10^-5;
k1 = -6.12293 * 10^-6;
k2 = 5.27870 * 10^-8;

m0 = -9.9348 * 10^-7;
m1 = 2.0816 * 10^-8;
m2 = 9.1697 * 10^-10;

B1 = b0 + b1*T + b2*T.^2 + b3*T.^3 + b4*T.^4;

C1 = c0 + c1*T + c2*T.^2;


rho_SMOW = a0 + a1*T + a2*T.^2 + a3*T.^3 + a4*T.^4 + a5*T.^5;

rho_0 = rho_SMOW + B1.*S + C1.*(S.^1.5) + d0*S.^2;



Kw = e0 + e1*T + e2*T.^2 + e3*T.^3 + e4*T.^4;
F1 = f0 + f1*T + f2*T.^2 + f3*T.^3;
G1 = g0 + g1*T + g2*T.^2;

K = Kw + F1.*S + G1.*(S.^1.5);

Bw = k0 + k1*T + k2*T.^2;
B2 = Bw + (m0 + m1*T + m2*T.^2).*S;

Aw = h0 + h1*T + h2*T.^2 + h3*T.^3;
A1 = Aw + (i0 + i1*T + i2*T.^2).*S + j0*(S.^1.5);

K_p = K + A1.*p + B2.*(p.^2);

rho = rho_0./(1-(p./K_p));


e = diff(rho,1,2);
% lev_diff = diff(Lev1,1,2);
lev_diff = diff(depth2,1,2);
e = e./lev_diff;
rho(:,500)=[];
E = -(e./rho);


%C calculation

p = p./1.0e-5;
p = p./1000;



C00=	1402.388;	
A02	=7.166E-5;
C01=	5.03830;
A03	=2.008E-6;
C02=	-5.81090E-2;
A04=	-3.21E-8;
C03=	3.3432E-4;
A10=	9.4742E-5;
C04=	-1.47797E-6;
A11	=-1.2583E-5;
C05	=3.1419E-9;
A12	=-6.4928E-8;
C10	=0.153563;
A13	=1.0515E-8;
C11	=6.8999E-4;
A14	=-2.0142E-10;
C12	=-8.1829E-6;
A20	=-3.9064E-7;
C13	=1.3632E-7;
A21	=9.1061E-9;
C14	=-6.1260E-10;
A22	=-1.6009E-10;
C20	=3.1260E-5;
A23	=7.994E-12;
C21	=-1.7111E-6;
A30	=1.100E-10;
C22	=2.5986E-8;
A31	=6.651E-12;
C23	=-2.5353E-10;
A32	=-3.391E-13;
C24	=1.0415E-12;
B00	=-1.922E-2;
C30	=-9.7729E-9;
B01	=-4.42E-5;
C31	=3.8513E-10;
B10	=7.3637E-5;
C32	=-2.3654E-12;
B11	=1.7950E-7;
A00	=1.389;
D00	=1.727E-3;
A01	=-1.262E-2;
D10	=-7.9836E-6;


 
Cw =	(C00 + C01*T + C02*T.^2 + C03*T.^3 + C04*T.^4 + C05*T.^5) +(C10 + C11.^T + C12*T.^2 + C13*T.^3 + C14*T.^4).*p +(C20 +C21*T +C22*T.^2 + C23*T.^3 + C24*T.^4).*p.^2 +(C30 + C31*T + C32*T.^2).*p.^3;
 
A =  	(A00 + A01*T + A02*T.^2 + A03*T.^3 + A04*T.^4) +(A10 + A11*T + A12*T.^2 + A13*T.^3 + A14*T.^4).*p +(A20 + A21*T + A22*T.^2 + A23*T.^3).*p.^2 +(A30 + A31*T + A32*T.^2).*p.^3;
 
B =	B00 + B01*T + (B10 + B11*T).*p;
 
D =	D00 + D10*p;

c =  	Cw + A.*S + B.*(S.^3/2) + D.*(S.^2);
c(:,500)=[];

E = E - (9.8./(c.^2));
E = E*10e+4;
N = 9.8*E;

% lev(18)=[];
% [Lev1,Lon1]=meshgrid(lev,Lon);
% [tr,P]=trend(N,10);

% [M,c]=contourf(Lon1,Lev1,tr,8,'ShowText','off');
% hold on
% xlabel('longitude');
% ylabel('depth (meters)');
% stipple(Lon1,Lev1,P<0.05,...
%  'density',350,...
%     'color',rgb('black'),...
%     'markersize',6)
% c.LineWidth=0.20;
%   cb=colorbar;
%   caxis([-8 8])
%   colormap(redblue(30))
% title('Stability of ocean water, BV frequency (scaled up by 10E+4)');
% ylabel(cb,'Trends (per decade)')

%  depth(200)=[];
% depth(200:499)=[];
dep(200:end)=[];
N(:,200:end)=[];
[depth3,lon2]=meshgrid(dep,long);

[M,c]=contourf(lon2,depth3,N,'ShowText','on','LevelList',[-10:4:10],'Levelstep',4);
hold on
xlabel('longitude (13-E to 72-E)');
ylabel('depth (meters)');

c.LineWidth=0.5;
  cb=colorbar;
  caxis([-20 20])
  colormap(redblue(20))
title('BV Frequency');
xticks([12:2:72])
%  ylabel(cb,'Temperature in celcius')
hold off







