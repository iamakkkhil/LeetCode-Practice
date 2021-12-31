def minCostClimbingStairs(cost) -> int:
    f = [0] * len(cost)
    f[-1], f[-2] = cost[-1], cost[-2]

    for i in range(len(cost) - 3, -1, -1):
        f[i] = cost[i] + min(f[i + 1], f[i + 2])

    return min(f[0], f[1])


if __name__ == "__main__":
    print(minCostClimbingStairs([10, 15, 20]))
    print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
