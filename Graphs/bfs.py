def bfs(graph, source):
    queue = [source]
    while len(queue) > 0:
        current = queue.pop()
        print(current)
        for neighbours in graph[current]:
            queue.insert(0, neighbours)


if __name__ == "__main__":
    graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}
    bfs(graph, "a")
