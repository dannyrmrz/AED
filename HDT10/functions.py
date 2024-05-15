
import numpy as np
import pandas as pd

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[float('inf')] * self.V for _ in range(self.V)]
        for i in range(self.V):
            self.graph[i][i] = 0

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight

    def floyd_warshall(self):
        dist = [row[:] for row in self.graph]
        next_node = [[None if i == j or dist[i][j] == float('inf') else j for j in range(self.V)] for i in range(self.V)]
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_node[i][j] = next_node[i][k]
        return dist, next_node

    def get_path(self, next_node, u, v):
        if next_node[u][v] is None:
            return []
        path = [u]
        while u != v:
            u = next_node[u][v]
            path.append(u)
        return path

def read_graph_from_file(filename):
    df = pd.read_csv(filename, sep=" ", header=0)
    cities = list(set(df["Ciudad1"].tolist() + df["Ciudad2"].tolist()))
    num_cities = len(cities)
    graph = Graph(num_cities)
    for index, row in df.iterrows():
        city1, city2 = row["Ciudad1"], row["Ciudad2"]
        weight = row["tiempoNormal"]
        graph.add_edge(cities.index(city1), cities.index(city2), weight)
    return graph, cities