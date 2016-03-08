#!/usr/bin/env python
import specfem2dPy
import numpy as np

### Input Checker
InCheck=specfem2dPy.InputChecker(dt=0.05,
        dx=6., dz=6., fc=0.1, lpd=4, vmin=3.5, vmax=3.5);
InCheck.Check();

# SLst=specfem2dPy.StaLst();
# SLst.HomoStaLst(xmin=0, xmax=480000, zmin=0, zmax=480000, dx=5000, dz=5000);
# SLst.WriteStaList('/projects/life9360/code/SEM/specfem2d/EXAMPLES/LFMembrane/DATA/STATIONS');


Vm=specfem2dPy.VelocityModel(xmin=0, xmax=480000, Nx=40, zmin=0, zmax=480000, Nz=40);
# Vm.CircleGradualAnomaly(Xc=120000, Zc=120000, R=60000, Va=3000);
# Vm.plotModel()
# # Vm.ReadModel('/projects/life9360/code/SEM/specfem2d/EXAMPLES/LFMembrane/DATA/proc000000_rho_vp_vs.dat')
# # Vm.BlockHomoAnomaly(Xmin=50000, Xmax=100000, Zmin=120000, Zmax=180000, Va=3000);
# # Vm.CircleHomoAnomaly(Xc=100000, Zc=100000, R=50000, Va=2000.)
# # Vm.BlockHomoAnomaly(Xmin=0, Xmax=100000, Zmin=0, Zmax=180000, Va=3000);
# # Vm.plot()
# # Vm.WriteModel('/projects/life9360/code/SEM/specfem2d/EXAMPLES/LFMembrane/DATA/proc000000_rho_vp_vs.dat_lf')
# # IC=specfem2dPy.InputChecker(dt=0.01, dx=5., dz=5., fc=0.1, lpd=4, vmin=3.0, vmax=3.5)
# 
itest=np.loadtxt('proc000000_rho_vp_vs.dat');
AAA=itest[:,0];
BBB=itest[:,1];

# 
# 
# ### Wavefield Snapshots
# WS=specfem2dPy.WaveSnapshot(datadir=
#     '/projects/life9360/code/SEM/specfem2d/EXAMPLES/LFMembrane/OUTPUT_FILES', nf=4800);
# # WS.ReadSnapshots();
# # WS.ReadGridFile()
# # WS.SaveDSSnap()
# # 
# # WS.LoadDSSnap()
# # im_ani=WS.PlotDSSnaps()
# # im_ani=WS.PlotDSSnaps(outfname='/projects/life9360/code/SEM/specfem2d/EXAMPLES/LFMembrane/homo.mp4')
# # im_ani=WS.PlotSnapshots()