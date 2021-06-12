from uibcdf_test_systems import FreeParticle
from uibcdf_test_systems.simulation import langevin_NVT
import numpy as np
from simtk import unit


# Sistema de test con el sistema de OpenMM como atributo
free_particle = FreeParticle(n_particles = 1, mass = 64 * unit.amu)

# Posiciones iniciales
initial_positions =  np.zeros([1, 3], np.float32) * unit.nanometers
initial_velocities = np.zeros([1, 3], np.float32) * unit.nanometers/unit.picoseconds

# Simulación de Langevin
time, position, velocity, kinetic_energy, potential_energy = langevin_NVT (free_particle.system,
                                                                           temperature = 300*unit.kelvin,
                                                                           friction = 0.5/unit.picoseconds,
                                                                           initial_positions = initial_positions,
                                                                           initial_velocities = initial_velocities,
                                                                           integration_timestep = 0.02 * unit.picoseconds,
                                                                           saving_timestep = 0.5 * unit.picoseconds,
                                                                           total_time = 10 * unit.picoseconds)
