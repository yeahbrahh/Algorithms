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

    return paths


def dfs(graph: GraphEL, start: VertexEL, visited=None):

    if visited is None:
        visited = set()
    visited.add(start)

    for neighbor in graph.adjacent(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited
