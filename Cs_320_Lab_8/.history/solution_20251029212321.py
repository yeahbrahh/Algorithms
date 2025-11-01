from edgegraph import (
    VertexEL,
    EdgeEL,
    GraphEL
)


def pld_graph(g: GraphEL):
    if g is None:
        raise ValueError("Bad graph")

    seen = set()
    tuple_list = [()]
    new_list = []

    if not tuple_list:
        return []
    else:

        tuple_list.append(tuple(new_list))
    return tuple_list
