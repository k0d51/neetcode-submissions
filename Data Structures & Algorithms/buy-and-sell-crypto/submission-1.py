class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_sell = 100
        max_profit = 0
        for j in range(len(prices)):
            min_sell = min(min_sell, prices[j])
            buy = prices[j]
            profit = buy - min_sell
            max_profit = max(max_profit, profit)

        return max_profit