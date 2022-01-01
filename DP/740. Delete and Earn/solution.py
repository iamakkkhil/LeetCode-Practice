from typing import Collection

def deleteAndEarn(nums) -> int:
    count = Collection.Counter(nums)
    prev = None
    avoid = using = 0
    for k in sorted(count):
        if k - 1 != prev:
            avoid, using = max(avoid, using), k * count[k] + max(avoid, using)
        else:
            avoid, using = max(avoid, using), k * count[k] + avoid
        prev = k
    return max(avoid, using)


if __name__ == "__main__":
    print(deleteAndEarn([3, 4, 2]))
    print(deleteAndEarn([2, 2, 3, 3, 3, 4]))
    print(deleteAndEarn([3, 7, 4, 5, 6, 1, 2, 8]))