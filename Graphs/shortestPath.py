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


def shortestPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    visited = []
    queue = [[nodeA, 0]]
    visited.append(nodeA)

    while len(queue) > 0:
        currentNode, currentLength = queue.pop()

        if currentNode == nodeB:
            return currentLength

        for neighbour in graph[currentNode]:
            if neighbour not in visited:
                queue.insert(0, [neighbour, currentLength + 1])
                visited.append(neighbour)

    return -1


if __name__ == "__main__":
    edges = [
        ["w", "x"],
        ["x", "y"],
        ["z", "y"],
        ["z", "v"],
        ["w", "v"],
    ]
    print(shortestPath(edges, "w", "y"))
