import unittest

class TestGraphMethods(unittest.TestCase):

    def setUp(self):
        self.graph = Graph(3)
        self.graph.add_edge(0, 1, 10)
        self.graph.add_edge(1, 2, 20)

    def test_add_edge(self):
        self.assertEqual(self.graph.graph[0][1], 10)
        self.assertEqual(self.graph.graph[1][2], 20)

    def test_floyd_warshall(self):
        dist, next_node = self.graph.floyd_warshall()
        self.assertEqual(dist[0][2], 30)  # Distance from 0 to 2 via 1
        self.assertEqual(next_node[0][2], 1)  # Next node from 0 to 2

    def test_get_path(self):
        _, next_node = self.graph.floyd_warshall()
        path = self.graph.get_path(next_node, 0, 2)
        self.assertEqual(path, [0, 1, 2])  # Shortest path from 0 to 2

    def test_calculate_center_of_graph(self):
        center_index = calculate_center_of_graph(self.graph)
        self.assertEqual(center_index, 1)  # Center of the graph is at index 1 (city 1)

if __name__ == '__main__':
    unittest.main()
