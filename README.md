# IsingModel
An old project from Fall 2015 which I refactored for legibility. The [Ising Model](https://en.wikipedia.org/wiki/Ising_model#Basic_properties_and_history) is a simple model of how magnetism arises in a lattice.  The spins of the unpaired valence electrons couple as the temperature decreases spontaneously creating magnetism. This script simulates the formulation of magnetism in a 2 dimensional lattice.

## Ising Model
In physical materials, the spins of electrons are free to point in any direction. In the Ising Model, spins are constrained to point in only 2 directions, up or down. 

## Magnetization
[Magnetization](https://en.wikipedia.org/wiki/Magnetization) is an indicator of how magnetized a material is. It's proportional to the number of spins aligned minus the number antialigned. In the case of

M = sum

Magnetization occurs spontaneously below a certain temperature in metals due to its decrease in entropy or randomness. As temperature increases, energy is more freely available so spins have less incentive to align and magnetism vanishes.

## Susceptibility
Spins typically align in the direction of a magnetic field. [Susceptibility](https://en.wikipedia.org/wiki/Magnetic_susceptibility) is an indicator of how strongly spins are pulled into that direction. Of course, in the case of diamegnetism, the spins try to anti-align with the magnetic field which is indicated by a negative susceptibility.

## Monte Carlo Simulation

A [monte carlo](https://en.wikipedia.org/wiki/Ising_model#Monte_Carlo_methods_for_numerical_simulation) process is a process that uses probability to determine the outcome. In the simulation, spins are selected randomly for the direction of spin to change. If the switch is energetically favorable, the spin is flipped. Otherwise a probability dependent on the energy cost of flipping and temperature is computed to determine whether or not the spin should be flipped. As the temperature increases the spins are more likely to change, decreasing the time required to converge on a magnetized state.

## Results
Magnetization | Expected Results
:----:|:----:
![magnetic_moment_with_temperature](https://cloud.githubusercontent.com/assets/23300144/24078277/a08c49a0-0c26-11e7-8fe6-ca1420f3c4dd.png) | ![](https://cloud.githubusercontent.com/assets/23300144/24081531/f448dd78-0c72-11e7-8331-1e4742f06a7e.png)

Flippidy Flap

Susceptibility| Expected Results
:----:|:----:
![susceptibility_with_temperature](https://cloud.githubusercontent.com/assets/23300144/24078261/4eca3ba4-0c26-11e7-9d7b-a2b54fc3b899.png) | ![Susceptibility](https://cloud.githubusercontent.com/assets/23300144/24081555/545d88a8-0c73-11e7-9181-0f118f9ca0b7.png)

The chaotic behavior at lower temperatures is due to the simulation being unable to settle onto the expected state. The low temperatures causes change to be slow and the simulation wasn't run for enough time steps for the simulation to converge.
