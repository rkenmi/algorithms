import unittest

from graphs.Graph import Digraph, WeightedDirectedEdge, Vertex
from graphs.GraphClient import ShortestPath


class DigraphCreation(unittest.TestCase):
    def build_simple_digraph(self):
        g = Digraph(5)
        a, b, c, d = Vertex(1), Vertex(2), Vertex(3), Vertex(4)
        g.add_edge(WeightedDirectedEdge(a, b, 3.0))
        g.add_edge(WeightedDirectedEdge(b, c, 5.0))
        g.add_edge(WeightedDirectedEdge(c, d, 1.0))
        g.add_edge(WeightedDirectedEdge(b, d, 3.0))
        return g

    def test_values_exist(self):
        g = self.build_simple_digraph()
        self.assertEqual(3.0, g.adj[1][0].weight)
        self.assertEqual(5.0, g.adj[2][0].weight)

    def test_basic_shortest_paths(self):
        g = self.build_simple_digraph()
        v1 = g.adj[1][0].get_from()
        sp = ShortestPath(g, v1)
        self.assertEqual(3.0, sp.dist_to[2])
        self.assertEqual(8.0, sp.dist_to[3])
        self.assertEqual(6.0, sp.dist_to[4])

        v4 = g.adj[3][0].get_to()
        footsteps_from_source = sp.get_path_to(v4)

        self.assertEqual(1, footsteps_from_source[0].id)
        self.assertEqual(2, footsteps_from_source[1].id)
        self.assertEqual(4, footsteps_from_source[2].id)

        self.assertEqual(6.0, sp.get_dist_to(v4))

if __name__ == '__main__':
    unittest.main()
