# IsingModel
An old project from Fall 2016 which I refactored for legibility. The Ising Model is a simple model of how magnetism arises in a lattice.  The spins of the unpaired valence electrons couple as the temperature decreases spontaneously creating magnetism. This script simulates the formulation of magnetism in a 2 dimensional lattice.

## Ising Model
In physical materials, the spins of electrons are free to point in any direction. In the Ising Model, spins are constrained to point in only 2 directions, up or down. 

## Magnetization
Magnetization is an indicator of how magnetized a material is. It's proportional to the number of spins aligned minus the number antialigned. In the case of

M = sum

Magnetization occurs spontaneously below a certain temperature in metals due to its decrease in entropy or randomness. As temperature increases, energy is more freely available so spins have less incentive to align and magnetism vanishes.

## Susceptibility
Spins typically align in the direction of a magnetic field. Susceptibility is an indicator of how strongly spins are pulled into that direction. Of course, in the case of diamegnetism, the spins try to anti-align with the magnetic field which is indicated by a negative susceptibility.

## Monte Carlo Simulation

A monte carlo process is a process that uses probability to determine the outcome. In the simulation, spins are selected randomly for the direction of spin to change. If the switch is energetically favorable, the spin is flipped. Otherwise a probability dependent on the energy cost of flipping and temperature is computed to determine whether or not the spin should be flipped. As the temperature increases the spins are more likely to change, decreasing the time required to converge on a magnetized state.

## Results

![susceptibility_with_temperature](https://cloud.githubusercontent.com/assets/23300144/24078261/4eca3ba4-0c26-11e7-9d7b-a2b54fc3b899.png)
