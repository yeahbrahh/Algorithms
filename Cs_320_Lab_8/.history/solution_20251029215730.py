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

        while len(stack) < 0 and stack:
            current = stack.pop()
        for edge in graph.adjacent():

            #     procedure DFS(G, v) is
            # label v as discovered
            # for all directed edges from v to w that are in G.adjacentEdges(v) do
            # if vertex w is not labeled as discovered then
            # recursively call DFS(G, w)

    def bfs(graph: GraphEL, start: VertexEL):

        if graph is None or start is None:
            raise ValueError("Invalid graph or vertex")
        if start.name not in graph._vertices:
            return []

        seen = set()

        seen.add(start)

        tuple_list = [(start, )]

        i = 0
        while i < len(tuple_list) and tuple_list[i]:
            new_list = []
            for vertex in tuple_list[i]:
                for edge in graph.incident(vertex):
                    v1, v2 = edge.ends()
                    neighbor = v1 if v2 == vertex else v2
                    if neighbor not in seen:
                        seen.add(neighbor)
                        new_list.append(neighbor)
            if new_list:
                tuple_list.append(tuple(new_list))
            i += 1

        return tuple_list
