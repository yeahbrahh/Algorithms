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

        for next in graph._vertices[start] - seen:
            self.dfs(graph, next, seen)
        return seen
