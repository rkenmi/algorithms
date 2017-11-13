import math

from graphs.Graph import WeightedDirectedEdge


class ShortestPath:
    def __init__(self, G, source):
        self.G = G  # graph
        self.source = source  # source vertex
        self.dist_to = [math.inf] * G.size()  # the distance to the vertex id FROM THE SOURCE
        self.edge_to = [None] * G.size()  # the last edge that connects to vertex id (not necessarily from the source!)

        self.dist_to[source.id] = 0
        queue = [G.adj[source.id]]

        while queue:
            edges = queue.pop(0)
            for edge in edges:
                self._relax(edge)
                to_node = G.adj[edge.get_to().id]
                if to_node:
                    queue.append(to_node)

    def _relax(self, edge):
        v = edge.get_from().id
        w = edge.get_to().id

        if self.dist_to[w] > self.dist_to[v] + edge.get_weight():
            self.dist_to[w] = self.dist_to[v] + edge.get_weight()
            self.edge_to[w] = edge

    def get_path_to(self, v):
        #  Follow the path backwards using edge_to. Reverse stack to flip path at the end.
        stack, reverse_stack = [v], []
        while v:
            edge = self.edge_to[v.id]
            if edge:
                v = edge.get_from()
                stack.append(v)
            else:
                break

        while stack:
            reverse_stack.append(stack.pop())

        return reverse_stack

    def get_dist_to(self, v):
        return self.dist_to[v.id]


import heapq
class DjikstraSP(ShortestPath):
    """
        Restriction: No negative weights
        Performance: Good; O(E logV).
    """
    def __init__(self, G, source):
        self.dist_to = [math.inf] * G.size()
        self.edge_to = [None] * G.size()

        self.dist_to[source.id] = 0

        self.heap = [( 0 , source )]

        while self.heap:
            tup = heapq.heappop(self.heap)
            adj = G.adj[tup[1].id]
            if adj is None:
                continue

            for edge in adj:
                self._relax(edge)
                self._update_heap(edge.get_to())

    def _update_heap(self, w):
        """
            Update the heap with the newest distance for w, the node to move to.
        :param w:
        :return:
        """
        exists = False
        for i, pair in enumerate(self.heap):
            if w.id == pair[1].id:
                self.heap[i] = (self.dist_to[w.id], w)
                exists = True
        if not exists:
            heapq.heappush(self.heap, (self.dist_to[w.id], w))


class BellmanFordSP(ShortestPath):
    """
        Restriction: No negative cycles
        Performance: Pretty slow; O(E * V). Can be improved significantly with a queue.
    """
    def __init__(self, G, source):
        self.G = G  # graph
        self.source = source  # source vertex
        self.dist_to = [math.inf] * G.size()  # the distance to the vertex id FROM THE SOURCE
        self.edge_to = [None] * G.size()  # the last edge that connects to vertex id (not necessarily from the source!)
        self.dist_to[source.id] = 0

        for i in range(G.size()):
            for edges in G:
                for edge in edges:
                    self._relax(edge)


class TopologicalSP(ShortestPath):
    """
        Restriction: No directed cycles. Can handle negative weights, unlike Djikstra's.
        Performance: Linear O(V + E), but you need O(V) space to track visited vertices.
    """
    def __init__(self, G, source):
        self.G = G  # graph
        self.source = source  # source vertex
        self.dist_to = [math.inf] * G.size()  # the distance to the vertex id FROM THE SOURCE
        self.edge_to = [None] * G.size()  # the last edge that connects to vertex id (not necessarily from the source!)
        self.dist_to[source.id] = 0

        order = self._get_topological_order()
        for vertex in order:
            edges = G.adj[vertex.id]
            if edges:
                for edge in edges:
                    self._relax(edge)

    def _get_topological_order(self):
        visited = [False] * self.G.size()
        stack = [self.source]
        order = []
        while stack:
            node = stack.pop()
            edges = self.G.adj[node.id]
            if edges:
                for edge in edges:
                    if not visited[edge.get_to().id]:
                        stack.append(edge.get_to())

            if not visited[node.id]:
                order.append(node)
                visited[node.id] = True
        return order


