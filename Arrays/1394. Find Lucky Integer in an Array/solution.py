def findLucky(arr) -> int:
    count = {}
    for element in arr:
        if element not in count:
            count[element] = 1
        else:
            count[element] += 1

    max_element = -1
    for element in count:
        if count[element] == element and element > max_element:
            max_element = element

    return max_element
