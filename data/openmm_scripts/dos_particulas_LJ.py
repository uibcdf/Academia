# Partícula Libre

import numpy as np
import pickle
from tqdm import tqdm
import simtk.openmm as mm
import simtk.openmm.app as app
import simtk.unit as unit

# Definición del sistema.

## Primer átomo: Argón
mass_1 = 39.948 * unit.amu
sigma_1 = 3.404 * unit.angstroms
epsilon_1 = 0.238 * unit.kilocalories_per_mole
charge_1 = 0.0 * unit.elementary_charge

## Segundo átomo: Xenón
mass_2 = 131.293 * unit.amu
sigma_2 = 3.961 * unit.angstroms
epsilon_2 = 0.459 * unit.kilocalories_per_mole
charge_2 = 0.0 * unit.elementary_charge



# Creación del sistema.

system = mm.System()

non_bonded_force = mm.NonbondedForce()
non_bonded_force.setNonbondedMethod(mm.NonbondedForce.NoCutoff)

# Átomo 1
system.addParticle(mass_1)
non_bonded_force.addParticle(charge_1, sigma_1, epsilon_1)

# Átomo 2
system.addParticle(mass_2)
non_bonded_force.addParticle(charge_2, sigma_2, epsilon_2)

# Caja periódica

system.setDefaultPeriodicBoxVectors([2.0, 0.0, 0.0]*unit.nanometers, [0.0, 2.0, 0.0]*unit.nanometers, [0.0, 0.0, 2.0]*unit.nanometers)

_ = system.addForce(non_bonded_force)


# Definición del estado termodinámico y el integrador.

step_size = 2*unit.femtoseconds
temperature = 300*unit.kelvin
friction = 1.0/unit.picosecond # Damping para la dinámica de Langevin

integrator = mm.LangevinIntegrator(temperature, friction, step_size)


# Creación de la plataforma.

platform_name = 'CUDA'
platform = mm.Platform.getPlatformByName(platform_name)

# Creación del contexto.

context = mm.Context(system, integrator, platform)

# Condiciones iniciales

initial_positions  = np.zeros([2, 3], np.float32) * unit.angstroms
initial_velocities = np.zeros([2, 3], np.float32) * unit.angstroms/unit.picoseconds

initial_positions[1, 0] = 1.0 * unit.nanometers

context.setPositions(initial_positions)
context.setVelocities(initial_velocities)

# Parámetros de la simulación.

simulation_time = 5.0*unit.nanosecond
saving_time = 1.0*unit.picoseconds

n_steps_per_period = int(saving_time/step_size) # número de pasos del periodo de guardado
n_periods = int(simulation_time/saving_time) # número de periodos guardados

# Creación de arrays reporteros del tiempo, la posición y la velocidad.

times = np.zeros([n_periods], np.float32) * unit.picoseconds
positions = np.zeros([n_periods, 2, 3], np.float32) * unit.angstroms
velocities = np.zeros([n_periods, 2, 3], np.float32) * unit.angstroms/unit.picosecond
potential_energies   = np.zeros([n_periods], np.float32) * unit.kilocalories_per_mole
kinetic_energies     = np.zeros([n_periods], np.float32) * unit.kilocalories_per_mole

# Almacenamiento en reporteros de las condiciones iniciales para tiempo 0

state = context.getState(getPositions=True, getVelocities=True, getEnergy=True)
times[0] = state.getTime()
positions[0] = state.getPositions()
velocities[0] = state.getVelocities()
kinetic_energies[0]=state.getKineticEnergy()
potential_energies[0]=state.getPotentialEnergy()

# Ejecuto el bucle sobre el número de periodos que vamos a simular

for ii in tqdm(range(1,n_periods)):
    context.getIntegrator().step(n_steps_per_period)
    state = context.getState(getPositions=True, getVelocities=True, getEnergy=True)
    times[ii] = state.getTime()
    positions[ii] = state.getPositions()
    velocities[ii] = state.getVelocities()
    kinetic_energies[ii]=state.getKineticEnergy()
    potential_energies[ii]=state.getPotentialEnergy()

file = open('traj.pkl','wb')
pickle.dump(times, file)
pickle.dump(positions, file)
pickle.dump(velocities, file)
pickle.dump(potential_energies, file)
pickle.dump(kinetic_energies, file)
file.close()


