def ghumo(grid, source, visited):
    row, col = source
    if not row >= 0 or not row < len(grid):
        return False
    if not col >= 0 or not col < len(grid[0]):
        return False

    if [row, col] in visited:
        return False

    if grid[row][col] == "W":
        return False

    visited.append([row, col])
    size = 1

    size += ghumo(grid, [row - 1, col], visited)
    size += ghumo(grid, [row + 1, col], visited)
    size += ghumo(grid, [row, col - 1], visited)
    size += ghumo(grid, [row, col + 1], visited)

    return size


def minIsland(grid):
    visited = []
    minIslandSize = len(grid[0]) * len(grid)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "L" and [row, col] not in visited:
                islandSize = ghumo(grid, [row, col], visited)
                if islandSize < minIslandSize:
                    minIslandSize = islandSize

    return minIslandSize


if __name__ == "__main__":
    grid = [
        ["W", "L", "W", "W", "W"],
        ["W", "L", "W", "W", "W"],
        ["W", "W", "W", "L", "W"],
        ["W", "W", "L", "L", "W"],
        ["L", "W", "W", "L", "L"],
        ["L", "L", "W", "W", "W"],
    ]

    print(minIsland(grid))
