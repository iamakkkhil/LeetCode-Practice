def findRestaurant(list1, list2):
    common = []
    sum_ = float("inf")
    rank = {restuarant: i for i, restuarant in enumerate(list1)}

    for j, res in enumerate(list2):
        if res in rank:
            if rank[res] + j < sum_:
                common = [res]
                sum_ = rank[res] + j
            elif rank[res] + j == sum_:
                common.append(res)
    return common


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Burger King", "Tapioca Express", "Shogun"]
print(findRestaurant(list1, list2))
