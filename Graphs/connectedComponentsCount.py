def ghumo(graph, src, visited):
    if src in visited:
        return False

    visited.append(src)

    for neighbour in graph[src]:
        ghumo(graph, neighbour, visited)

    return True


def connectedComponentsCount(graph):
    visited = []
    count = 0
    for node in graph:
        if ghumo(graph, node, visited) == True:
            count += 1

    return count


if __name__ == "__main__":
    graph = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2],
    }
    print(connectedComponentsCount(graph))
