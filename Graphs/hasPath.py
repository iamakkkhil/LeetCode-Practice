def hasPathDFSRecursion(graph, source, dest):
    if source == dest:
        return True

    for neighbour in graph[source]:
        if hasPathDFSRecursion(graph, neighbour, dest) == True:
            return True

    return False


def hasPathBFS(graph, source, dest):
    queue = [source]
    while len(queue) > 0:
        current = queue.pop()
        if current == dest:
            return True
        for neighbour in graph[current]:
            queue.insert(0, neighbour)

    return False


if __name__ == "__main__":
    graph = {"f": ["g", "i"], "g": ["h"], "h": [], "i": ["g", "k"], "j": ["i"], "k": []}
    print(hasPathDFSRecursion(graph, "j", "f"))
    print(hasPathBFS(graph, "f", "k"))
