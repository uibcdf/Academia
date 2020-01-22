import numpy as np
import simtk.openmm as mm
import simtk.openmm.app as app
import simtk.unit as unit
import pickle

# Definición del sistema.
n_particles = 1 # número de partículas
mass = 180.15 * unit.amu # masa de la glucosa

# Definición de las condiciones del estado termodinámico.
temperature = 0*unit.kelvin # temperatura a zero para que langevin simule la dinámica clásica

# Condiciones iniciales
initial_positions  = np.zeros([n_particles, 3], np.float32) * unit.nanometers # posiciones iniciales
initial_velocities = np.zeros([n_particles, 3], np.float32) * unit.nanometers/unit.picoseconds # velocidades iniciales

# Parámetros de la simulación.
integration_timestep = 0.1*unit.picoseconds # paso del integrador
saving_timestep = 1*unit.picoseconds # tiempo de guardado
total_time = 1*unit.nanoseconds # tiempo total de simulación

n_steps = int(round(total_time/integration_timestep)) # número total de pasos de integración a simular
steps_per_cicle = int(round(saving_timestep/integration_timestep)) # pasos de integración por ciclo de guardado
n_cicles = int(round(n_steps/steps_per_cicle)) # número total de ciclos de guardado a simular

# Creación del sistema.
system = mm.System()
for ii in range(n_particles):
    system.addParticle(mass)

# Creación del integrador.
friction = 5.0/unit.picosecond # fricción del sistema (0.0/unit.picoseconds si no queremos fricción)
integrator = mm.LangevinIntegrator(temperature, friction, integration_timestep)

# Creación de la plataforma.
platform_name = 'CUDA'
platform = mm.Platform.getPlatformByName(platform_name)

# Creación del contexto.
context = mm.Context(system, integrator, platform)
context.setPositions(initial_positions)
context.setVelocities(initial_velocities)

# Creación de arrays reporteros del tiempo, la posición y la velocidad.
times = np.zeros([n_cicles], np.float32) * unit.picoseconds
positions = np.zeros([n_cicles, n_particles, 3], np.float32) * unit.nanometers
velocities = np.zeros([n_cicles, n_particles, 3], np.float32) * unit.nanometers/unit.picosecond
kinetic_energy = np.zeros([n_cicles], np.float32) * unit.kilocalories_per_mole
potential_energy = np.zeros([n_cicles], np.float32) * unit.kilocalories_per_mole

# Almacenamiento en reporteros de las condiciones iniciales para tiempo 0
state = context.getState(getPositions=True, getVelocities=True, getEnergy=True)
times[0] = state.getTime()
positions[0] = state.getPositions()
velocities[0] = state.getVelocities()
kinetic_energy[0] = state.getKineticEnergy()
potential_energy[0] = state.getPotentialEnergy()

# Ejecuto el bucle sobre el número de ciclos de guardado que vamos a simular
for ii in range(1,n_cicles):
    context.getIntegrator().step(steps_per_cicle)
    state = context.getState(getPositions=True, getVelocities=True)
    times[ii] = state.getTime()
    positions[ii] = state.getPositions()
    velocities[ii] = state.getVelocities()
    kinetic_energy[ii] = state.getKineticEnergy()
    potential_energy[ii] = state.getPotentialEnergy()

# Guardo, si es necesario, en un fichero pickle el resultado de la simulación
filename_traj = 'trajectory.pickle'
file_traj = open(filename_traj,'wb')
pickle.dump( times, file_traj )
pickle.dump( positions, file_traj )
pickle.dump( velocities, file_traj )
pickle.dump( kinetic_energy, file_traj )
pickle.dump( potential_energy, file_traj )
file_traj.close()

