
def generateMaxwellBoltzmannVelocities(system, temperature):
    """ Generate velocities from a Maxwell-Boltzmann distribution. """
    # Get number of atoms
    natoms = system.getNumParticles()
    # Create storage for velocities.
    velocities = Quantity(np.zeros([natoms, 3], np.float32), nanometer / picosecond) # velocities[i,k] is the kth component of the velocity of atom i
    # Compute thermal energy and inverse temperature from specified temperature.
    kB = BOLTZMANN_CONSTANT_kB * AVOGADRO_CONSTANT_NA
    kT = kB * temperature # thermal energy
    beta = 1.0 / kT # inverse temperature
    # Assign velocities from the Maxwell-Boltzmann distribution.
    for atom_index in range(natoms):
        mass = system.getParticleMass(atom_index) # atomic mass
        sigma = sqrt(kT / mass) # standard deviation of velocity distribution for each coordinate for this atom
        for k in range(3):
            velocities[atom_index,k] = sigma * np.random.normal()
    return velocities

