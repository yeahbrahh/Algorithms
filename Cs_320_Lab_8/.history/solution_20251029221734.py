from edgegraph import (
    VertexEL,
    EdgeEL,
    GraphEL
)


def pld_graph(g: GraphEL):
    if g is None:
        raise ValueError("Bad graph")
    start = g.vertices[0]
    paths = dfs(g, start)


def dfs(graph: GraphEL, start: VertexEL, seen=None):

    if seen is None:
        seen = set()
    seen.add(start)

    for neighbor in graph._adjacency[start.name]:
        if neighbor not in seen:
            dfs(graph, neighbor, seen)
    return seen
