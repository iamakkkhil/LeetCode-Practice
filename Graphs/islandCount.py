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

    ghumo(grid, [row - 1, col], visited)
    ghumo(grid, [row + 1, col], visited)
    ghumo(grid, [row, col - 1], visited)
    ghumo(grid, [row, col + 1], visited)

    return True


def islandCount(grid):
    visited = []
    islandCount = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "L" and [row, col] not in visited:
                ghumo(grid, [row, col], visited)
                islandCount += 1

    return islandCount


if __name__ == "__main__":
    grid = [
        ["W", "L", "W", "W", "W"],
        ["W", "L", "W", "W", "W"],
        ["W", "W", "W", "L", "W"],
        ["W", "W", "L", "L", "W"],
        ["L", "W", "W", "L", "L"],
        ["L", "L", "W", "W", "W"],
    ]

    print(islandCount(grid))
