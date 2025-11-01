from edgegraph import (
    VertexEL,
    EdgeEL,
    GraphEL
)


class Graph:

    def pld_graph(self, g: GraphEL):
        if g is None:
            raise ValueError("Bad graph")
        start = VertexEL(g._vertices)
        self.bfs(g, start)

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
