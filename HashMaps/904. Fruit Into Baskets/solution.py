def totalFruit(fruits):
    start, end = 0, 0
    max_fruits_collected = 0
    d = {}

    while end < len(fruits):
        d[fruits[end]] = end

        if len(d) > 2:
            fruit_with_min_index_value = min(d.values())

            del d[fruits[fruit_with_min_index_value]]
            start = fruit_with_min_index_value + 1

        max_fruits_collected = max(max_fruits_collected, end - start + 1)
        end += 1

    return max_fruits_collected
