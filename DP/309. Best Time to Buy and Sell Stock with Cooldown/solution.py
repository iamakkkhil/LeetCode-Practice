def maxProfit(prices) -> int:
    sell = 0
    cool = 0
    buy = -10000000
    for price in prices:
        prev_sell = sell
        sell = max(sell, buy + price)
        buy = max(buy, cool - price)
        cool = prev_sell

    return sell


if __name__ == "__main__":
    print(maxProfit([7, 1, 5, 3, 6, 4]))
