def dfs(graph, source):
    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)


def dfsRecursive(graph, source):
    print(source)

    for neighbor in graph[source]:
        dfsRecursive(graph, neighbor)


if __name__ == "__main__":
    graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}
    dfs(graph, "a")
    print("\nRecursion: ")
    dfsRecursive(graph, "a")
