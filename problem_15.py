import math 

def lattice_paths(grid_size):
    # Compute the binomial coefficient C(2n, n)
    return math.comb(2 * grid_size, grid_size)

if __name__ == '__main__':
    print(lattice_paths(20))