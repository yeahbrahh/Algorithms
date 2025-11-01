from edgegraph import (
    VertexEL,
    EdgeEL,
    GraphEL,
)


def bfs(graph, start):

    if graph is None or start is None:
        raise ValueError("invalid vertex")
    if not start in graph:
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

    # Tips
    # This assignment is really just implementing Algorithm 14.4.1 from the textbook
    # with two small wrinkles:
    # •  You need a structure for marking which vertices are explored
    #       (see injunction not to mark up  the  graph  above)
    # •  Rather  than  creating  multiple  lists  Li you  are  to  structure them as tuples in a  list  of
    #   tuples and return that list.
