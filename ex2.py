import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

np.random.seed(1)

def percolation_point_ratio(size, p_start, p_end, p_step, trials):
    p_values = np.arange(p_start, p_end, p_step)
    ratios = []

    for p in p_values:
        percolation_points = []
        total_points = []
        for _ in range(trials):
            cluster = np.random.choice([0, 1], size=(size, size), p=[1-p, p])
            graph = nx.grid_2d_graph(size, size)

            for i in range(size):
                for j in range(size):
                    if cluster[i, j] == 0:
                        graph.remove_node((i, j))
                
            connected_components = list(nx.connected_components(graph))
            percolation_cluster = max(connected_components, key=len)
            percolation_points.append(len(percolation_cluster))
            total_points.append(sum(len(component) for component in connected_components))

        ratios.append((np.mean(percolation_points) / np.mean(total_points)))

    plt.plot(p_values, ratios, 'bo-')
    plt.xlabel('Вероятность заполнения')
    plt.ylabel('Отношение точек в перколяционном кластере к общему числу точек')
    plt.title('Зависимость отношения числа точек в перколяционном кластере к общему числу точек от вероятности заполнения')
    plt.show()

    threshold = p_values[np.argmax(np.array(ratios) > 0.5)]
    print(f'Порог перколяции: {threshold}')

size = 50
p_start, p_end, p_step = 0.1, 0.9, 0.01
trials = 10
percolation_point_ratio(size, p_start, p_end, p_step, trials)
