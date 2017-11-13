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


