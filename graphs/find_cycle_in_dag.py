def find_cycle_in_dag(vertex):
    visited = []

    def _dfs(node):
        if node is vertex and vertex in visited:
            return True

        visited.append(node)

        return any([_dfs(p) for p in node.processes])

    has_cycle = _dfs(vertex)
    return has_cycle


