from unicodedata import category


n, m = 3, 4
products_price = [[2, 40, 1, 1], [40, 3, 1, 2], [2, 40, 1, 1]]


def select_product(products_price, n, m):
    min_cost = 0
    # based on index number as in first row therefore -1
    category_blacklisted = -1

    for category in range(n):
        min_price_in_category = max(products_price[category])
        index_product = -1
        # print(min_price_in_category)
        for product in range(m):
            if product != category_blacklisted:
                if products_price[category][product] < min_price_in_category:
                    min_price_in_category = products_price[category][product]
                    index_product = product

        min_cost += min_price_in_category
        category_blacklisted = index_product

    return min_cost


select_product(products_price, n, m)
