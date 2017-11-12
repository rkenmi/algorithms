import math


class ShortestPath:
    def __init__(self, G, source):
        self.G = G  # graph
        self.source = source  # source vertex
        self.dist_to = [0] * G.size()  # the distance to the vertex id FROM THE SOURCE
        self.edge_to = [None] * G.size()  # the last edge that connects to vertex id (not necessarily from the source!)

        for i in range(len(self.dist_to)):
            if i != source.id:  # dist to itself is always 0
                self.dist_to[i] = math.inf

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
