import warnings
warnings.filterwarnings("ignore")

import os
import sys
from time import time as realtime
from time import asctime, localtime, strftime, gmtime
from pytools_uibcdf.Time import formatting_elapsed_time
import numpy as np
import pickle as pickle
import molmodmt as m3t
import simtk.openmm as mm
import simtk.openmm.app as app
import simtk.unit as unit
from openmmtools.integrators import LangevinIntegrator
from molmodmt.utils.openmm.forces import HarmonicRestraintPositions

start_realtime = realtime()
print("")
print("Start:",asctime(localtime()))
print("")

#### Loading PDB

pdb = m3t.convert('system_minimized.pdb', 'openmm.PDBFile')

#### System

topology = m3t.convert(pdb, 'openmm.Topology')
forcefield = app.ForceField('amber99sbildn.xml','tip3p.xml')
system = forcefield.createSystem(topology,
                                 nonbondedMethod=app.PME,
                                 nonbondedCutoff=1.2*unit.nanometers,
                                 constraints=app.HBonds,
                                 rigidWater=True,
                                 ewaldErrorTolerance=0.0005)

#### Custom Forces

#atoms_restrained = m3t.select(topology, 'type C N O P S and not water')
#harmonic_constant = 1.0*unit.kilocalories_per_mole/unit.angstrom**2
#pinned_positions = m3t.get(pdb, selection=atoms_restrained, coordinates=True)
#force = HarmonicRestraintPositions(atoms_restrained, harmonic_constant, pinned_positions)
#system.addForce(force)

#### Thermodynamic State

kB = unit.BOLTZMANN_CONSTANT_kB * unit.AVOGADRO_CONSTANT_NA
temperature = 300.0*unit.kelvin
pressure    = None

#### Integrator

friction   = 1.0/unit.picosecond
step_size  = 2.0*unit.femtoseconds
integrator = LangevinIntegrator(temperature, friction, step_size)
integrator.setConstraintTolerance(0.00001)

#### Platform

platform = mm.Platform.getPlatformByName('CUDA')
properties = {'CudaPrecision': 'mixed'}

#### Simulation

simulation = app.Simulation(topology, system, integrator, platform, properties)

#### Initial Conditions

positions = m3t.get(pdb, coordinates=True)
simulation.context.setPositions(positions)
simulation.context.setVelocitiesToTemperature(temperature)

#### Iterations Parameters

time_simulation = 100.0 * unit.picoseconds
time_saving = 1.0 * unit.picoseconds
time_verbose = 10.0 * unit.picoseconds
time_checkpoint = 10.0 * unit.picoseconds

number_iterations = int(time_simulation/time_saving)
elapsed_iterations_verbose = int(time_verbose/time_saving)
elapsed_iterations_checkpoint = int(time_checkpoint/time_saving)
steps_per_iteration = int(time_saving/step_size)
total_simulation_steps = number_iterations*steps_per_iteration

#### Reporters

# Observables Stored

net_mass, n_degrees_of_freedom = m3t.get(system, net_mass=True, n_degrees_of_freedom=True)
number_states_saved = number_iterations+1
data = dict()
data['time'] = unit.Quantity(np.zeros([number_states_saved], np.float64), unit.picoseconds)
data['potential'] = unit.Quantity(np.zeros([number_states_saved], np.float64), unit.kilocalories_per_mole)
data['kinetic'] = unit.Quantity(np.zeros([number_states_saved], np.float64), unit.kilocalories_per_mole)
data['volume'] = unit.Quantity(np.zeros([number_states_saved], np.float64), unit.nanometers**3)
data['density'] = unit.Quantity(np.zeros([number_states_saved], np.float64), unit.gram / unit.centimeters**3)
data['kinetic_temperature'] = unit.Quantity(np.zeros([number_states_saved], np.float64), unit.kelvin)

# Simulation Status

def printout_status(iteration, number_iterations, time, kinetic_temperature, volume):

    progression = 100.0*(iteration/number_iterations)
    msg="Progress: {:6.2f}%, Time: {:.2f} ps, Kinetic Temperature: {:.3f} K, Volume: {:.3f} nm^3"
    print(msg.format(progression, time.value_in_unit(unit.picoseconds),
                     kinetic_temperature.value_in_unit(unit.kelvin), volume.value_in_unit(unit.nanometers**3)))

#### CheckPoint and Finnal State

def dump_state(simulation, filename):

    state = simulation.context.getState(getPositions=True, getVelocities=True)
    time = state.getTime() / unit.picoseconds
    positions = state.getPositions() / unit.nanometers
    velocities = state.getVelocities() / unit.nanometers*unit.picoseconds
    box_vectors = state.getPeriodicBoxVectors() / unit.nanometers

    with open(os.path.join(filename), 'wb') as f:
        pickle.dump((time, positions, velocities, box_vectors), f)

def save_checkpoint_state(simulation):
    return dump_state(simulation, "checkpoint.pkl")

def save_finnal_state(simulation):
    return dump_state(simulation, "restart.pkl")

#### Reporting Initial State

state = simulation.context.getState(getEnergy=True)
time = state.getTime()
potential_energy = state.getPotentialEnergy()
kinetic_energy = state.getKineticEnergy()
volume = state.getPeriodicBoxVolume()
density = (net_mass / volume).in_units_of(unit.gram / unit.centimeter**3)
kinetic_temperature = (2.0 * kinetic_energy / kB / n_degrees_of_freedom).in_units_of(unit.kelvin)
data['time'][0] = time
data['potential'][0] = potential_energy
data['kinetic'][0] = kinetic_energy
data['volume'][0] = volume
data['density'][0] = density
data['kinetic_temperature'][0] = kinetic_temperature

printout_status(0, number_iterations, time, kinetic_temperature, volume)

#### Running Simulation

start_simulation_realtime = realtime()

for iteration in range(1, number_iterations+1):
    integrator.step(steps_per_iteration)
    state = simulation.context.getState(getEnergy=True)
    time = state.getTime()
    potential_energy = state.getPotentialEnergy()
    kinetic_energy = state.getKineticEnergy()
    volume = state.getPeriodicBoxVolume()
    density = (net_mass / volume).in_units_of(unit.gram / unit.centimeter**3)
    kinetic_temperature = (2.0 * kinetic_energy / kB / n_degrees_of_freedom).in_units_of(unit.kelvin)
    data['time'][iteration]=time
    data['potential'] = potential_energy
    data['kinetic'] = kinetic_energy
    data['volume'] = volume
    data['density'] = density
    data['kinetic_temperature'] = kinetic_temperature
    if (iteration%elapsed_iterations_verbose)==0:
        printout_status(iteration, number_iterations, time, kinetic_temperature, volume)
    if (iteration%elapsed_iterations_checkpoint)==0:
        save_checkpoint_state(simulation)

end_simulation_realtime = realtime()

#### Savind Data

with open(os.path.join('data.pkl'), 'wb') as f:
    pickle.dump(data, f)

#### Saving Finnal State

save_finnal_state(simulation)
m3t.convert(simulation,'system_equilibrated_nvt.pdb')

#### Summary


end_realtime = realtime()
preparation_elapsed_realtime = (start_simulation_realtime - start_realtime)*unit.seconds
simulation_elapsed_realtime = (end_simulation_realtime - start_simulation_realtime)*unit.seconds
total_elapsed_realtime = (end_realtime - start_realtime)*unit.seconds

performance = (time_simulation/unit.nanoseconds) / (simulation_elapsed_realtime/unit.hours)

print("")
print("End:",asctime(localtime()))
print("")
print("************************")
print("")
print("Total time: "+formatting_elapsed_time(total_elapsed_realtime/unit.seconds))
print("Preparation time: "+formatting_elapsed_time(preparation_elapsed_realtime/unit.seconds))
print("Simulation time: "+formatting_elapsed_time(simulation_elapsed_realtime/unit.seconds))
print("")
print("Simulation Performance: {:.3f} ns/h".format(performance))
print("")

