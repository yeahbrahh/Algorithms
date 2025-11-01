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

    i = 0
    while not tuple_list.isEmpty():
        new_tuple = (eg.get_vertex(), eg.get_edges())
        for vertex in new_tuple:
            incident_to_vertex = eg.incident(vertex)
            for edge in incident_to_vertex:
                e = eg.add_edge(edge)

            if vertex not in seen:

                # Tips
                # This assignment is really just implementing Algorithm 14.4.1 from the textbook with two small
                # wrinkles:
                # •  You need a structure for marking which vertices are explored(see injunction not to mark
                #                                                                 up  the  graph  above)
                # •  Rather  than  creating  multiple  lists  Li you  are  to  structure  them as tuples in a  list  of
                # tuples and return that  list.
                # 2
