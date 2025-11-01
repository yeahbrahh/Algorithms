def bfs(graph, start):
    if graph is None or start is None:
        raise ValueError("invalid vertex")
    if not start in graph:
        return []

    tuple_list = []
    seen = set()

    seen.add(start)

    i = 0
    while not tuple_list.isEmpty():
        new_tuple = []
        for vertex in new_tuple:
            e =
            for edge in incident_to_v:

            if vertex not in seen:

                # Tips
                # This assignment is really just implementing Algorithm 14.4.1 from the textbook with two small
                # wrinkles:
                # •  You need a structure for marking which vertices are explored(see injunction not to mark
                #                                                                 up  the  graph  above)
                # •  Rather  than  creating  multiple  lists  Li you  are  to  structure  them as tuples in a  list  of
                # tuples and return that  list.
                # 2
