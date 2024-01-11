def maxProfit(self, prices: List[int]) -> int:
    profit = 0

    # buy low, sell high
    buy = 0
    sell = 1

    while sell < len(prices):
        current = prices[sell] - prices[buy]

        if prices[sell] > prices[buy]:
            profit += current
            buy = sell

        else:
            buy = sell

        sell += 1

    return profit
