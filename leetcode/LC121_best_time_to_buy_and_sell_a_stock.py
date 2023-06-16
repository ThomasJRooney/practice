class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if list(reversed(sorted(prices))) == prices: return 0
        buy, sell = 0, 1
        max_profit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]: max_profit =max(prices[sell] - prices[buy], max_profit)
            else: buy = sell
            sell += 1
        return max_profit