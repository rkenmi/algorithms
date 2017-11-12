import collections

class Vertex:
    def __init__(self, id, name=None):
        self.id = id
        self.name = name


class WeightedDirectedEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def get_from(self):
        return self.v

    def get_to(self):
        return self.w

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight


class Digraph:
    def __init__(self, size):
        # self.adj_list = collections.defaultdict([])
        self.adj = [None] * size

        # Iteration
        self.counter = 0

    def add_edge(self, edge):
        # self.adj_list[edge.get_from()].append(edge)
        source = edge.get_from()
        if self.adj[source.id] is None:
            self.adj[source.id] = [edge]
        else:
            self.adj[source.id].append(edge)

    def size(self):
        return len(self.adj)

    def __iter__(self):
        return self

    def __next__(self):
        while self.adj[self.counter] is None:
            self.counter += 1

            if self.counter >= len(self.adj):
                self.counter = 0
                raise StopIteration

        vertex = self.adj[self.counter]
        self.counter += 1
        return vertex


