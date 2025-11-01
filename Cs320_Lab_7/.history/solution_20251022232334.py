from edgegraph import (
    VertexEL,
    EdgeEL,
    GraphEL,
)


def bfs(graph, start):
    eg = EdgeEL()

    if graph is None or start is None:
        raise ValueError("invalid vertex")
    if not start in graph:
        return []

    tuple_list = []
    seen = set()

    seen.add(start)

    while not tuple_list.isEmpty():
        for vertex in eg.vertices():
            for edge in eg.incident(vertex):
                if vertex not in seen:
                    e = eg.add_edge(edge)
                    new_tuple = (eg.get_vertex(), eg.get_edges())
                    tuple_list.add(new_tuple)
                    seen.add(vertex)
                else:
                    e = 0

    return tuple_list

    # Tips
    # This assignment is really just implementing Algorithm 14.4.1 from the textbook with two small
    # wrinkles:
    # •  You need a structure for marking which vertices are explored(see injunction not to mark
    #                                                                 up  the  graph  above)
    # •  Rather  than  creating  multiple  lists  Li you  are  to  structure  them as tuples in a  list  of
    # tuples and return that  list.
    # 2
