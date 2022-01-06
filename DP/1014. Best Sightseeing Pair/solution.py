def maxScoreSightseeingPair(values) -> int:
    imax = values[0] + 0
    bestscore = -1

    for i in range(1, len(values)):
        bestscore = max(bestscore, imax + values[i] - i)
        imax = max(imax, values[i] + i)

    return bestscore


if __name__ == "__main__":
    print(maxScoreSightseeingPair([8, 1, 5, 2, 6]))
