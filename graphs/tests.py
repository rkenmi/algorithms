import unittest

from graphs.Graph import Digraph, WeightedDirectedEdge, Vertex
from graphs.GraphClient import ShortestPath, DjikstraSP, BellmanFordSP, TopologicalSP


class DigraphCreation(unittest.TestCase):
    def build_simple_digraph(self):
        g = Digraph(5)
        a, b, c, d, e = Vertex(0), Vertex(1), Vertex(2), Vertex(3), Vertex(4)
        g.add_edge(WeightedDirectedEdge(a, b, 3.0))
        g.add_edge(WeightedDirectedEdge(b, c, 5.0))
        g.add_edge(WeightedDirectedEdge(c, d, 1.0))
        g.add_edge(WeightedDirectedEdge(b, d, 3.0))
        g.add_edge(WeightedDirectedEdge(a, e, 2.0))
        return g

    def test_values_exist(self):
        g = self.build_simple_digraph()
        self.assertEqual(3.0, g.adj[1][0].weight)
        self.assertEqual(5.0, g.adj[2][0].weight)

    def _graph_tester(self, G, instance):
        self.assertEqual(3.0, instance.dist_to[1])
        self.assertEqual(8.0, instance.dist_to[2])
        self.assertEqual(6.0, instance.dist_to[3])
        self.assertEqual(2.0, instance.dist_to[4])

        v4 = G.adj[2][0].get_to()
        footsteps_from_source = instance.get_path_to(v4)

        self.assertEqual(0, footsteps_from_source[0].id)
        self.assertEqual(1, footsteps_from_source[1].id)
        self.assertEqual(3, footsteps_from_source[2].id)

        self.assertEqual(6.0, instance.get_dist_to(v4))


    def test_basic_shortest_paths(self):
        g = self.build_simple_digraph()
        v1 = g.adj[0][0].get_from()
        sp = ShortestPath(g, v1)
        self._graph_tester(g, sp)

    def test_djikstra_shortest_paths(self):
        g = self.build_simple_digraph()
        v1 = g.adj[0][0].get_from()
        sp = DjikstraSP(g, v1)
        self._graph_tester(g, sp)

    def test_bellman_ford_shortest_paths(self):
        g = self.build_simple_digraph()
        v1 = g.adj[0][0].get_from()
        sp = BellmanFordSP(g, v1)
        self._graph_tester(g, sp)

    def test_topological_sort_shortest_paths(self):
        g = self.build_simple_digraph()
        v1 = g.adj[0][0].get_from()
        sp = TopologicalSP(g, v1)
        self._graph_tester(g, sp)


if __name__ == '__main__':
    unittest.main()
