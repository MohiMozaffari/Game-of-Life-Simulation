import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import animation




def initial_state(N):
    """initial state

    Args:
        N (int): number of lattice

    Returns:
        array: initial state
    """
    lattice = np.random.choice([0,1],(N,N))
    return lattice



def checkflip(lattice, N, epsilon):
    """Check if the cell is alive or dead

    Args:
        lattice (2d_array): lattice
        N (int): number of lattice
        epsilon (float): if a random number is lower than an epsilon, dead cells revive
    """
    def bc(i):
        """periodic boundry condition"""
        if i > N-1:
            return 0
        if i < 0:
            return N-1
        else:
            return i
    new_lattice = np.zeros((N,N))
    for r,c in np.ndindex(lattice.shape):

        total = (lattice[r][bc(c+1)] + lattice[r][bc(c-1)] + lattice[bc(r+1)][c] + lattice[bc(r-1)][c] 
                + lattice[bc(r+1)][bc(c+1)] + lattice[bc(r-1)][bc(c+1)] + lattice[bc(r+1)][bc(c-1)]
                + lattice[bc(r-1)][bc(c-1)])
    
        if lattice[r][c] == 1:
            if (total < 2) or (total > 3):
                new_lattice[r][c] = 0
            else:
                new_lattice[r][c] = 1
        else:
            if total == 3:
                new_lattice[r][c] = 1                
            else:
                if np.random.rand() < epsilon:
                    new_lattice[r][c] = 1
                else:
                    new_lattice[r][c] = 0


    return new_lattice


def step(lattice, N, nstep, epsilon):
    """simluate game of life

    Args:
        lattice (2d_array): lattice
        N (int): number of lattice
        nstep (int): number of simlulation steps
        epsilon (float): if a random number is lower than an epsilon, dead cells revive

    Returns:
        2d_array: lattice after eqSteps 
    """
    for _ in range(nstep):
        lattice = checkflip(lattice, N, epsilon)
        
    return lattice



if __name__ == "__main__":



    N = 10  ##number of lattice

    epsilon = 0 #noise

    lattice = initial_state(N)  #random initial satate


    

    fig = plt.figure(figsize=(7,7))
    ax = plt.axes()
    cmap= "viridis"
    
    sns.heatmap(lattice, cmap=cmap, cbar=False, yticklabels=False, xticklabels=False, vmin = 0, vmax = 1)
    #plt.savefig("initial_state_game_of_life_with_noise_and_random_state")

    def animate(i):
        sns.heatmap(step(lattice, N , i, epsilon), cmap=cmap, cbar=False, yticklabels=False, xticklabels=False, vmin = 0, vmax = 1)
        # if i in [50,100,150]:
        #     plt.savefig(f"{i}frame_of_game_of_life_with_noise_and_random_state")
           
    anim = animation.FuncAnimation(fig, animate, frames=200, repeat=False)
    plt.show()


    # f = r"/home/mohaddeseh/Documents/Programing/Stochastic/game_of_life_with_noise_and_random_state.mp4" 
    # writervideo = animation.FFMpegWriter(fps=10) 
    # anim.save(f, writer=writervideo)
    # plt.savefig("last_state_game_of_life_with_noise_and_random_state")