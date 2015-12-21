import pprint
from ase.visualize import view
from ase import io
from ase.neb import NEB
from ase.optimize import BFGS
from ase.units import *
from ase.calculators.siesta import Siesta
# Read initial and final states:
from ase.io.trajectory import Trajectory, PickleTrajectory
traj = Trajectory("final7.traj")

#traj = io.read('last_iteration.traj')
#for images in traj:
#    print "hello2"


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
calc.set_fdf('SpinPolarized', 'false')

for images in traj:
#    print "hello"
#    pprint.pprint(images)
    images.set_calculator(calc)
    e = images.get_potential_energy()
    print e


