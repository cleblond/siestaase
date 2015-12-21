from ase.visualize import view
from ase import io
from ase.neb import NEB
from ase.optimize import BFGS, MDMin
from ase.units import *
from ase.calculators.siesta import Siesta
from ase.io.trajectory import Trajectory
# Read initial and final states:
#initial = io.read('initial.extxyz')
#final = io.read('final.extxyz')
traj = Trajectory("final7.traj")

imagesfinal=[]
for images in traj:
#for image in images:
    imagesfinal += [images] 

neb = NEB(imagesfinal, k=0.5)
# Interpolate linearly the potisions of the three middle images:
#neb.interpolate()

#view(images)

calc = Siesta(label='pes_neb',
              xc='RPBE',
              meshcutoff=200 * Ry,
              basis='dzp',
              mix=0.1,
              pulay=12,
              kpts=[6, 6, 1])

calc.set_fdf('xc.functional', 'GGA')
calc.set_fdf('PAO.EnergyShift', 0.01 * Ry)
calc.set_fdf('DM.KickMixingWeight', 0.008)
calc.set_fdf('DM.UseSaveDM', 'true')
calc.set_fdf('SpinPolarized', 'true')
#calc.set_fdf('ElectronicTemperature', 500 * C)


# Set calculators:
#for images in traj:
for image in imagesfinal:
    image.set_calculator(calc)
# Optimize:
optimizer = BFGS(neb, trajectory='final.traj')
optimizer.run(fmax=0.02)
