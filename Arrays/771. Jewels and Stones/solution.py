def numJewelsInStones(jewels: str, stones: str) -> int:
    total_jewels = 0
    for jewel in jewels:
        total_jewels += stones.count(jewel)

    return total_jewels


if __name__ == "__main__":
    jewels = "aA"
    stones = "aAAbbbb"
    print(numJewelsInStones(jewels, stones))
