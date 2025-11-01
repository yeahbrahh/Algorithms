from edgegraph import (
    VertexEL,
    EdgeEL,
    GraphEL
)


class Graph:

    def pld_graph(self, g: GraphEL, visited=None):
        if g is None:
            raise ValueError("Bad graph")
        start = g.vertices[0]

    def dfs(graph: GraphEL, start: VertexEL):

        seen = set()
        seen.add(start)

        for next in graph.vertices():
            dfs(graph, next)
