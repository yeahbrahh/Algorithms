from edgegraph import (
    VertexEL,
    GraphEL,
)


def bfs(graph: GraphEL, start: VertexEL):

    if graph is None or start is None:
        raise ValueError("invalid vertex")
    if start.name not in graph._vertices:
        return []

    seen = set()

    seen.add(start)

    tuple_list = [(start, )]

    i = 0
    while tuple_list[i]:
        new_list = []
        for vertex in tuple_list[i]:
            for neighbor in graph.incident(vertex):
                if neighbor not in seen:
                    seen.add(neighbor)
                    new_list.append(neighbor)
        if new_list:
            tuple_list.append(tuple(new_list))
        i += 1

    return tuple_list
