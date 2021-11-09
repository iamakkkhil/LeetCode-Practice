class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        visited = [0] * n
        connections = {}
        for i in edges:
            if i[0] not in connections.keys():
                connections[i[0]] = [i[1]]
            else:
                connections[i[0]].append(i[1])
            if i[1] not in connections.keys():
                connections[i[1]] = [i[0]]
            else:
                connections[i[1]].append(i[0])

        q = []
        q.append(start)
        visited[start] = 1

        while len(q) > 0:
            front = q[0]
            q.pop(0)

            if front == end:
                return True

            for i in connections[front]:
                if visited[i] == 0:
                    q.append(i)
                    visited[i] = 1

        return False
