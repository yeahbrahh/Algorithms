from edgegraph import (
    VertexEL,
    EdgeEL,
    GraphEL
)


class Graph:

    def pld_graph(self, g: GraphEL):
        if g is None:
            raise ValueError("Bad graph")
        start = g.vertices[0]

    def dfs(self, graph: GraphEL, start: VertexEL, seen=None):

        if seen is None:
            seen = set()
        seen.add(start)

        for neighbor in graph._adjacency[start]:
            if neighbor not in seen:
                self.dfs(graph, next, seen)
        return seen
