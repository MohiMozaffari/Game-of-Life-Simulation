# Game of Life Simulation

This repository contains Python code for simulating Conway's Game of Life with added noise and random initial states.

## Introduction

Conway's Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

In this simulation, we add noise to the traditional Game of Life rules. Cells can randomly revive with a probability determined by the `epsilon` parameter.

## Getting Started

To run the simulation, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Install the required dependencies by running:
```bash
pip install numpy matplotlib seaborn
```
4. Run the script `game_of_life_simulation.py`:

```bash
python game_of_life_simulation.py
```

## Code Structure
The code consists of the following main parts:

initial_state(N): Initializes the lattice with random states.

checkflip(lattice, N, epsilon): Checks if the cell is alive or dead based on the rules of the Game of Life.

step(lattice, N, nstep, epsilon): Simulates the Game of Life for a given number of steps.

animate(i): Animates the simulation using Matplotlib's animation module

## Parameters
N: Number of cells in the lattice.

epsilon: Noise parameter, determines the probability of random cell revival.

nstep: Number of simulation steps.

## Visualization
The simulation is visualized using Matplotlib's animation capabilities. Each frame represents a step in the simulation, displaying the updated state of the lattice.
