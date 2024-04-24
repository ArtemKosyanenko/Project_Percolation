import numpy as np
import matplotlib.pyplot as plt

def create_cluster(size, p):
    return np.random.choice([0, 1], size=(size, size), p=[1-p, p])

def percolate_boundaries(cluster):
    size = cluster.shape[0]
    visited = np.zeros((size, size))
    top, bottom, left, right = False, False, False, False
    percolation_cells = []

    for j in range(size):
        if cluster[0, j] == 1:
            stack = [(0, j)]
            while len(stack) > 0:
                i, j = stack.pop()
                if visited[i, j] == 1:
                    continue
                visited[i, j] = 1
                percolation_cells.append((i, j))
                if i == size - 1:
                    top = True
                if i == 0:
                    bottom = True
                if j == 0:
                    left = True
                if j == size - 1:
                    right = True
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < size and 0 <= nj < size and cluster[ni, nj] == 1 and visited[ni, nj] == 0:
                        stack.append((ni, nj))

    return top, bottom, left, right, percolation_cells

size = 100
p = 0.8
cluster = create_cluster(size, p)
top_percolates, bottom_percolates, left_percolates, right_percolates, percolation_cells = percolate_boundaries(cluster)

# Highlight percolation cells in the cluster
for cell in percolation_cells:
    cluster[cell[0], cell[1]] = 2

plt.imshow(cluster, cmap='binary', interpolation='nearest')
plt.title(f"Percolates - Bottom: {top_percolates}, Top: {bottom_percolates}, Left: {left_percolates}, Right: {right_percolates}")
plt.show()
