def buildGraph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


def hasPath(graph, src, dest, visited):
    if src in visited:
        return False

    if src == dest:
        return True

    visited[src] = True

    for neighbour in graph[src]:
        if hasPath(graph, neighbour, dest, visited) == True:
            return True
    return False


def unidirectedPath(edges, src, dest):
    graph = buildGraph(edges)
    return hasPath(graph, src, dest, {})


if __name__ == "__main__":
    edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]
    print(unidirectedPath(edges, "i", "o"))
