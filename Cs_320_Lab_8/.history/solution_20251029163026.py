from edgegraph import (
    VertexEL,
    EdgeEL,
    GraphEL
)


def pld_graph(g: GraphEL):
    if g is None:
        raise ValueError("Bad graph")

    tuple_list = []

    if not tuple_list:
        return []
