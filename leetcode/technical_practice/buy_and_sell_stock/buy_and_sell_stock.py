def maxProfit(self, prices: List[int]) -> int:
    # Earliest you can sell is day 2
    profit = 0

    maximum = max(prices) 
    minimum = min(prices)

    if prices.index(maximum) > prices.index(minimum):
        return maximum - minimum

    # buy low, sell high
    buy = 0
    sell = 1

    while sell < len(prices):
        current = prices[sell] - prices[buy]

        if prices[sell] > prices[buy]:
            profit = current if current > profit else profit

        else:
            buy = sell

        sell += 1

    return profit
