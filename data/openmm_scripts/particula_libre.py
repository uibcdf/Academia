# Partícula Libre

import numpy as np
import pickle
from tqdm import tqdm
import simtk.openmm as mm
import simtk.openmm.app as app
import simtk.unit as unit

# Definición del sistema.

num_particles = 1
mass = 180.15 * unit.amu # masa de la glucosa

# Definición de las condiciones del estado termodinámico.

temperature = 300*unit.kelvin
friction = 10.0/unit.picosecond # Damping del Langevin

# Condiciones iniciales

initial_positions  = np.zeros([num_particles, 3], np.float32) * unit.angstroms
initial_velocities = np.zeros([num_particles, 3], np.float32) * unit.angstroms/unit.picoseconds

# Parámetros de la simulación.

step_size = 0.1*unit.picoseconds
steps_per_period = 100
num_periods = 50000
trajectory_file =  'traj.pkl' # Podía ser nombrado como'1_free_particle_300K_10Fric.pkl'

# Creación del sistema.

system = mm.System()

for ii in range(num_particles):
    system.addParticle(mass)

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

times = np.zeros([num_periods], np.float32) * unit.picoseconds
positions = np.zeros([num_periods, num_particles, 3], np.float32) * unit.angstroms
velocities = np.zeros([num_periods, num_particles, 3], np.float32) * unit.angstroms/unit.picosecond

# Almacenamiento en reporteros de las condiciones iniciales para tiempo 0

state = context.getState(getPositions=True, getVelocities=True)
times[0] = state.getTime()
positions[0] = state.getPositions()
velocities[0] = state.getVelocities()

# Ejecuto el bucle sobre el número de periodos que vamos a simular

for ii in tqdm(range(1,num_periods)):
    context.getIntegrator().step(steps_per_period)
    state = context.getState(getPositions=True, getVelocities=True)
    times[ii] = state.getTime()
    positions[ii] = state.getPositions()
    velocities[ii] = state.getVelocities()

file = open(trajectory_file,'wb')
pickle.dump(times, file)
pickle.dump(positions, file)
pickle.dump(velocities, file)
file.close()


