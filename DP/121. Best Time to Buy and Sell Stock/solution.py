def maxProfit(prices) -> int:
    res = 0
    buy = prices[0]

    for i in range(1, len(prices)):
        sell = prices[i]
        if sell - buy > res:
            res = sell - buy

        if sell < buy:
            buy = sell

    return res


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))
