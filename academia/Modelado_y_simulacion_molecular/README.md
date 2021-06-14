<div style='text-align: left;'> <a href="../README.md#Modelado-simulacion">Ir al menú anterior</a> </div>

-----

# Modelado y Simulación Molecular

## Qué es un modelo molecular
- Qué es un modelo molecular.
- Niveles de descripción.
        - Modelos cuántico
                - Modelos híbridos cuántico-clásico
                - Modelos clásico a todos los átomos
                - Modelos coarse-grained.
        - Topología y coordenadas.
        - Las interacciones entre los átomos y los campos de fuerzas.
        - Y si tenemos la topología, las coordenadas y las interacciones, ¿Qué podemos predecir?
                - La termodinámica (mecánica estadística).
                - La cinética (dinámica).
        - Qué es un buen modelo? Todos los ojos en el sistema real.
                - Difracción de rayos X
                - Resonancia Magnético nuclear
                - Espectroscopía
                - Microcalorimetría
                - Microscopía electrónica
        - Algunos números sobre lo que es posible modelar hoy.

## Proteins Models
- From the PDB to the parametrized interactions in a forcefield.
- ForceFields: From Charmm to OpenForcefield.
- Visualization workshop: Primary secondary, ternary and quaternary structure.
- Gaussian Network Models and Normal Modes
- Coarse-grained models.
- Pockets, Cavities and Channels.
- Allosterism.
- Folding-unfolding.
- Pka and protonated states.
- Breaking/forming covalent interactions.
- Polar models.
-

## Proteins Structure Modeling.
- Solving the structure experimentally.
- The ramachandran map and stress or stability as quality test.
- Modeling the structure from homology.
- Ab-initio models.
- Rosetta.
- Foldit (game).
- CASP Challenge.
- AlphaFold: AI folding proteins.
- Improved Sampling Strategies for Protein Model Refinement Based on Molecular Dynamics Simulation
- Protein models to fit cryo density clouds.

## Water Models

- Classical water models.
- How the models behave: "Do not drink".
- Polar water models.
-

## Ions, Cosolutes and Small Molecules Models.

- What's in the popular forcefields and what's not.
- Parametrizing a small molecule.
-

## DNA and RNA models.

- Simple DNA toy models: new interactions to be modeled (stacking).
- Nucleic acids in all popular forcefields.
- Experiments vs simulations with DNA and RNA.
-

## Lipids and Membranes Models
-

## Implicit Solvent Models.
-

## Implicit Membranes Models.
-

## Other physical models of interest.
- Solid state models.
- Adsortion and absortion models.
- Soft-Matter models.
- Fluid models.
- Gases models.
-

## The Potential Energy Landscape.
-

## The Free Energy Landscape.
- Whats a basin of attraction: a metastable conformational state.
- Conformational entropy.
- Whats a barrier.
- Effect of temperature on the free energy landscape.
-

## Molecular Dynamics Simulation.
- ForceFields revisited.
- Periodic boundary Conditions and long range interactions:
  - PME
  - Ewald
- Integrators.
- Termostates and Langevin dynamics.
- Barostates.
- Microcanonical and canonical ensembles.
- Equilibrium simulations: average observables and fluctuations -thermodynamics-.
- When time matters: damping and relaxation -kinetics-.
-

## The problems of working with a multi-multi-dimensional system.
- The thermodynamics from a few degrees of freedom projection.
- The kinetics from a few degrees of freedom projection.
- Dimensionality reduction techniques:
  - Principal Component Analysis
  - Multidimensional Scaling
 - Clustering Techniques:
  - K-means
  -
- Internal Friction

## Equilibrium and out of equilibrium.

- Is the system in equilibrium?
- Is the trajectory representative of equilibrium behaviour?
- Are many short trajectories telling the same than a single long one?
- What does convergence mean? Is the trajectory long enough to say that the observation converged?
- Does the sampling interval matter? What does correlation or decorrelation mean?
- What's markovianity?
-

## Enhanced Sampling Techniques
- 

## Kinetic Networks and Markov State Models
- 

## Folding-Unfolding simulation.
- Is there a single unfolded state? Intermediates.
- Thermal stability simulations: from Go Models to all-atom.
- Folding kinetics.
- Effect of mutations on stability.
- Intrinsically Misfolded or Disordered Peptides and Proteins: Are the popular forcefield usuful here?
- RNA folding models: prediction of stability and structure.
- Atomic force microscopy simulations with proteins or DNA: constant force vs constant velocity curves.
-

## External forces in a molecular dynamics simulation
- The friction as an external virtual force: from langevin to damping distance dependent model.
- Constraints and Restraints.
- Pulling experiments.
- Electric fields in the molecular model.
-

## Allosterism.
-

## Solvation
- Bulk water
- Water phase diagram: crystallization and vaporization simulations.
- Solvation Free Energy
- Behaviour of water around proteins.
- Water on crowded environments.
-

## Molecule-Molecule Interaction (I)
- The double well two particles binding model.
- The two bodies binding model: rigid and flexible.
- The role of water: hydration/dehydration and confined water networks.
- Ions association/dissociation simulations.
- The design paradigm: a fight against entropy.
-

## Molecule-Molecule Interaction (II)
- Protein-Small Molecule interactions.
- Pharmacophores, fingerprints and virtual screening.
- Protein-Small Molecule Docking
- Kd, Ka and the binding free energy.
- The role of water molecules.
- The role of receptor flexibility.
- Binding poses or modes.
- Intermediate metastable states in the route in/out.
- Kon, Koff and dwell time from molecular dynamics simulations.
- SAMPL challenge.
-

## Molecule-Molecule Interaction (III)
- Protein-Protein Interfase
- The role or water molecules: hydration/dehydration of interfases.
- Protein-Protein Docking
- Protein-Protein Binding Energy.
- The CAPRI challenge.
- Protein-DNA Models.
- Peptides polimerization: Amyloids agregation models and simulations.
- Crowded environments.
-

## Membranes simulations.
- How to set up a membrane system.
- Proteins embeded in a lipidic bilayer.
- Small molecules membrane permeation.
- Peptides membrane crossing or pore formation
- Micelles.
- Order/disorder phases, rafts, and the role of lipids in protein interactions.
-

## Molecular Dynamics with Quantum Mechanics/Molecular Mechanics
- A water simulation just with atoms and charges.
- Charge transportation along proteins.
- Interacting with photons: chromophores models and the FMO complex.
-

## Free Energy Methods and Alchemistry
- Free Energy Perturbation Methods.
- Free Energy Integration Methods.
- Aminoacids mutations.
- Alchemistry to drug design and optimization.
-

### Simulación molecular

Mecánica molecular

- Qué es la simulación molecular.
        - Tipos de campos de fuerzas.
        - El cálculo de la interacciones a largo alcance.
        - Integradores.
        - Termostatos.
        - La dinámica de Langevin.
        - Barostatos.
        - El equilibrio y sus técnicas de simulación (termodinámica)
                - Los observables y las distribución de probabilidad en equilibrio.
        - Cuando el tiempo importa (cinética):
                - Difusión.
                - Procesos estocásticos.
                - Relajacióna
                - Las constantes cinéticas en equilibrio.
        - La dinámica molecular.

- Técnicas de exploración de la energía libre potencial.
        - Aproximación a la termodinámica y la cinética en equilibrio desde el PES.
        - Exploración de los mínimos.
        - Exploración de los puntos silla.
        - Disconnectivity graphs.

- Técnicas Monte Carlo.
        - ...

- La dinámica molecular con OpenMM.
        - Motores para la simulación de la dinámica molecular.
        - OpenMM.

## OpenMM

- Qué es OpenMM y cómo se usa
- [Sistemas moleculares con OpenMM][menu:sistemas_openmm]
   - [La partícula libre][unidad:particula_libre]
   - [La partícula en un potencial armónico][unidad:potencial_armonico]
   - [La partícula en un potencial doble pozo][unidad:doble_pozo]
   - [Dos partículas de Lennard-Jones][unidad:dos_particulas_LJ]
   - [El gas de Lennard-Jones 2D][unidad:LJ_2D]
   - [El gas de Lennard-Jones 3D][unidad:LJ_3D]

<br>

-------
<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/uibcdf/Academia">UIBCDF-Academia</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/uibcdf/Academia/graphs/contributors">UIBCDF Lab, autores y colaboradores</a> es material protegido bajo una licencia <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/deed.es?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial-ShareAlike 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>

[menu:sistemas_openmm]: OpenMM/Sistemas/README.md
[unidad:particula_libre]: OpenMM/Sistemas/particula_libre/particula_libre.ipynb
[unidad:potencial_armonico]: OpenMM/Sistemas/potencial_armonico/potencial_armonico.ipynb
[unidad:doble_pozo]: OpenMM/Sistemas/doble_pozo/doble_pozo.ipynb
[unidad:dos_particulas_LJ]: OpenMM/Sistemas/dos_particulas_LJ/dos_particulas_LJ.ipynb
[unidad:LJ_2D]: OpenMM/Sistemas/LJ_2D/LJ_2D.ipynb
[unidad:LJ_3D]: OpenMM/Sistemas/LJ_3D/LJ_3D.ipynb

