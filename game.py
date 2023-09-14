import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def init_grid(rows, cols, density):
    return (np.random.rand(rows, cols) < density).astype(int)

def get_count(grid):
    # Define the convolution kernel for the Moore neighborhood
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])

    # Use convolution to calculate the number of neighbors for each cell
    neighbor_count = np.zeros_like(grid, dtype=int)

    for i in range(-1, 2):
        for j in range(-1, 2):
            neighbor_count += np.roll(grid, (i, j), axis=(0, 1))

    # Exclude the center cell from the count
    neighbor_count -= grid

    # Apply Conway's rules to calculate the next state of each cell
    next_state = (grid == 1) & ((neighbor_count == 2) | (neighbor_count == 3)) | (grid == 0) & (neighbor_count == 3)

    return next_state.astype(int)

def update_grid(generations):
    global grid  # Access the global grid variable
    new_grid = grid.copy()
    
    # Calculate the next state of the board
    grid = get_count(new_grid)

    # Update the plot data
    img.set_data(grid)
    
    return img,

grid = None

if __name__ == "__main__":
    rows = 100
    cols = 100
    density = 0.5

    grid = init_grid(rows, cols, density)

    fig, ax = plt.subplots()
    img = ax.imshow(grid, cmap='binary')

    ani = animation.FuncAnimation(fig, update_grid, frames=100, interval=100)

    plt.show()
