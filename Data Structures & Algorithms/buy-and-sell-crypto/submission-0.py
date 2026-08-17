class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_smallest = 99999999
        l = len(prices)
        for i in range(l-1):
            buy = prices[i]
            sell = prices[i+1]

            current_smallest = min(current_smallest, buy)
            profit = sell - current_smallest
            max_profit = max(profit, max_profit)

        return max_profit
