
# System

topology = "Input variable"
positions = "Input variable"

forcefield = app.ForceField("amber99sbildn.xml","tip3p.xml")

system = forcefield_generator.createSystem(topology,
                                           contraints=app.HBonds,
                                           nonbondedMethod=app.PME,
                                           nonbondedCutoff=1.0*_unit.nanometers,
                                           rigidWater=True,
                                           ewaldErrorTolerance=0.0005
                                          )

## Thermodynamic State
kB = _unit.BOLTZMANN_CONSTANT_kB * _unit.AVOGADRO_CONSTANT_NA
temperature = temperature
pressure = pressure

## Barostat
barostat_frequency = 25 # steps
barostat = mm.MonteCarloBarostat(pressure, temperature, barostat_frequency)
system.addForce(barostat)

## Integrator
friction   = 1.0/_unit.picosecond
step_size  = 2.0*_unit.femtoseconds
integrator = LangevinIntegrator(temperature, friction, step_size)
integrator.setConstraintTolerance(0.00001)

## Platform
platform = mm.Platform.getPlatformByName('CUDA')
properties = {'CudaPrecision': 'mixed'}

## Simulation
simulation = app.Simulation(topology, system, integrator, platform, properties)
simulation.context.setPositions(positions)
simulation.context.setVelocitiesToTemperature(temperature)

## Iterations parameters
time_equilibration = time
time_iteration = 0.2 * _unit.picoseconds
number_iterations = int(time_equilibration/time_iteration)
steps_iteration = int(time_iteration/step_size)
steps_equilibration = number_iterations*steps_iteration

## Reporters
net_mass, n_degrees_of_freedom = m3t.get(system, net_mass=True, n_degrees_of_freedom=True)
niters = number_iterations
data = dict()
data['time'] = _unit.Quantity(np.zeros([niters], np.float64), _unit.picoseconds)
data['potential'] = _unit.Quantity(np.zeros([niters], np.float64), _unit.kilocalories_per_mole)
data['kinetic'] = _unit.Quantity(np.zeros([niters], np.float64), _unit.kilocalories_per_mole)
data['volume'] = _unit.Quantity(np.zeros([niters], np.float64), _unit.angstroms**3)
data['density'] = _unit.Quantity(np.zeros([niters], np.float64), _unit.gram / _unit.centimeters**3)
data['kinetic_temperature'] = unit.Quantity(np.zeros([niters], np.float64), _unit.kelvin)

## Running Simulation
for iteration in range(number_iterations):
    integrator.step(steps_iteration)
    state = simulation.context.getState(getEnergy=True)
    time = state.getTime()
    potential_energy = state.getPotentialEnergy()
    kinetic_energy = state.getKineticEnergy()
    volume = state.getPeriodicBoxVolume()
    density = (net_mass / volume).in_units_of(unit.gram / unit.centimeter**3)
    kinetic_temperature = (2.0 * kinetic_energy / kB / n_degrees_of_freedom).in_units_of(unit.kelvin) # (1/2) ndof * kB * T = KE
    data['time'][iteration]=time
    data['potential'] = potential_energy
    data['kinetic'] = kinetic_energy
    data['volume'] = volume
    data['density'] = density
    data['kinetic_temperature'] = kinetic_temperature

final_state = simulation.context.getState(getPositions=True, getVelocities=True)
final_positions = final_state.getPositions()
final_velocities = final_state.getVelocities()


