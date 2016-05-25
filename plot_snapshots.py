#!/usr/bin/env python
import field2d_cartesian
import numpy as np


# ## Wavefield Snapshots
# WS=field2d_cartesian.WaveSnapshot(xmin=0, xmax=1000000, Nx=200, zmin=0, zmax=1000000, Nz=200, datadir=
#     '/projects/life9360/code/SEM/specfem2d/EXAMPLES/LFMembrane_SH/OUTPUT_FILES', dn=50, nt=8000);
WS=field2d_cartesian.WaveSnapshot(xmin=0, xmax=1000000, Nx=200, zmin=0, zmax=1000000, Nz=200, datadir=
    '/home/lili/code/specfem2d/EXAMPLES/LFMembrane_SH/OUTPUT_FILES', dn=50, nt=8000);
# WS.ReadGridFile()
# WS.GetElementIndex()
# WS.SaveElementIndex('/projects/life9360/code/SEM/specfem2d/EXAMPLES/LFMembrane_SH/OUTPUT_FILES');
# WS.LoadElementIndex('/projects/life9360/code/SEM/specfem2d/EXAMPLES/LFMembrane_SH/OUTPUT_FILES');
# WS.SaveElementIndex('/home/lili/code/specfem2d/EXAMPLES/LFMembrane_SH/OUTPUT_FILES');
# WS.LoadElementIndex('/home/lili/code/specfem2d/EXAMPLES/LFMembrane_SH/OUTPUT_FILES');
# WS.ReadSnapshots();
# im_ani=WS.PlotSnapshots()
# WS.ReadSingleSnap(1000)
# WS.PlotSingleSnap()/projects/life9360/code/SEM/specfem2d/EXAMPLES/LFMembrane_SH/OUTPUT_FILES
# 
# # # 
# # # WS.LoadDSSnap()
# # # im_ani=WS.PlotDSSnaps()
# # # im_ani=WS.PlotDSSnaps(outfname='/projects/life9360/code/SEM/specfem2d/EXAMPLES/LFMembrane/homo.mp4')
# 