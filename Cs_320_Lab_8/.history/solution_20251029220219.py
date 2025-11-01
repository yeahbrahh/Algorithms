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

    def dfs(graph: GraphEL, start: VertexEL):

        stack = []
        stack.append(start)

        seen = set()
        seen.add(start)

        #     procedure DFS(G, v) is
        # label v as discovered
        # for all directed edges from v to w that are in G.adjacentEdges(v) do
        # if vertex w is not labeled as discovered then
        # recursively call DFS(G, w)
