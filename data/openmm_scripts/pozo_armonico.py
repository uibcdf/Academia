# Partícula Libre

import numpy as np
import pickle
from tqdm import tqdm
import simtk.openmm as mm
import simtk.openmm.app as app
import simtk.unit as unit

# Definición del sistema.

n_particles = 1
mass = (12.010*15.999)/(12.010+15.999) * unit.amu # masa reducidad de la molécula diatómica: C-O

# Definición de las condiciones del estado termodinámico y el integrador.

temperature = 300*unit.kelvin
friction = 1.0/unit.picosecond # Damping del Langevin
step_size = 0.01*unit.picoseconds

# Condiciones iniciales

initial_positions  = np.zeros([n_particles, 3], np.float32) * unit.angstroms
initial_velocities = np.zeros([n_particles, 3], np.float32) * unit.angstroms/unit.picoseconds

# Parámetros de la simulación.

simulation_time = 5.0*unit.nanosecond
saving_time = 1.0*unit.picoseconds

n_steps_per_period = int(saving_time/step_size) # número de pasos del periodo de guardado
n_periods = int(simulation_time/saving_time) # número de periodos guardados

# Creación del sistema.

system = mm.System()

for ii in range(n_particles):
    system.addParticle(mass)

# Añadiendo el potencial externo al sistema

K = 10.0 * unit.kilocalorie_per_mole/unit.nanometers**2

force = mm.CustomExternalForce('(K/2.0) * (x^2 + y^2 + z^2)')
force.addGlobalParameter('K', K * unit.kilocalories_per_mole/unit.angstrom**2)

for ii in range(n_particles):
    force.addParticle(ii, [])

_ = system.addForce(force)

# Creación del integrador.

integrator = mm.LangevinIntegrator(temperature, friction, step_size)

# Creación de la plataforma.

platform_name = 'CUDA'
platform = mm.Platform.getPlatformByName(platform_name)

# Creación del contexto.

context = mm.Context(system, integrator, platform)
context.setPositions(initial_positions)
context.setVelocities(initial_velocities)

# Creación de arrays reporteros del tiempo, la posición y la velocidad.

times = np.zeros([n_periods], np.float32) * unit.picoseconds
positions = np.zeros([n_periods, n_particles, 3], np.float32) * unit.angstroms
velocities = np.zeros([n_periods, n_particles, 3], np.float32) * unit.angstroms/unit.picosecond
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


