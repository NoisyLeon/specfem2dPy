import obspy
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats



Dx=200.
infname = '/lustre/janus_scratch/life9360/specfem2d_working_dir/LFMembrane_SH_healing_004/field_data/Amp_10.0.txt'
inArr=np.loadtxt(infname)

XArr=inArr[:,0]
AmpArr=inArr[:,2]

ind=np.argsort(XArr)
XArr=XArr[ind]
AmpArr=AmpArr[ind]

XArr2= XArr
AmpArr2= np.ones(XArr.size) / np.sqrt(np.abs(XArr-Dx))

index=np.where(XArr==500.)
amp=AmpArr[index]
index2=np.where(XArr2==500.)
amp2=AmpArr2[index2]

a0=AmpArr[XArr==3000.]/amp
a2=AmpArr2[XArr2==3000.]/amp2
# index3=np.where(XArr3==1300.)
# amp3=AmpArr3[index3]

fig, ax=plt.subplots()
# ax.plot(XArr-Dx, AmpArr/amp,'go', lw=3, markersize=10, label='circular low velocity anomaly' );
# ax.plot(XArr2-Dx, AmpArr2/amp2,'b--', lw=5, markersize=10, label='homogeneous' );
ax.plot(XArr2-Dx, AmpArr/amp/AmpArr2*amp2,'bo', lw=5, markersize=10);
# ax.plot(XArr, (TArr-TArr2-1.5),'ro', lw=3, markersize=10, label='difference')
# ax.plot(Dx, 1, 'y*', markersize=20)
plt.legend(loc='upper right', fontsize=25, numpoints = 1)
y1=900
y2=1100
ax.fill_betweenx(np.array([0, (AmpArr/amp).max()]), y1, y2, facecolor='red', alpha=0.5)
# y1=2200
# y2=2400
# ax.fill_betweenx(np.array([0.2, 1.1]), y1, y2, facecolor='blue', alpha=0.5)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=20)
plt.ylim([0, 1.05])
plt.xlim([300., 3500.])
plt.xticks(np.arange(300., 3700., 200.))
# plt.ylim([(TArr-TArr2-1.5).min(), (TArr-TArr2).max()])
plt.ylabel('Normalized amplitude', fontsize=30);
# plt.xlabel('X position (km)', fontsize=30);
plt.xlabel('Distance (km)', fontsize=30);
# plt.title('Amplitude measurement with rectangle anomaly', fontsize=30);
# plt.title('Amplitude measurement with circular anomaly', fontsize=30);
plt.show()
