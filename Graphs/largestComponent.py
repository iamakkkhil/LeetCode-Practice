def ghumo(graph, src, visited):
    if src in visited:
        return 0

    visited.append(src)
    size = 1

    for neighbour in graph[src]:
        size += ghumo(graph, neighbour, visited)

    return size


def largestComponent(graph):
    largest_component_size = 0
    visited = []

    for node in graph:
        component_count = ghumo(graph, node, visited)

        if largest_component_size < component_count:
            largest_component_size = component_count

    return largest_component_size


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
    print(largestComponent(graph))
