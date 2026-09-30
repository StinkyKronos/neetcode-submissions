class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]

        for num in prices:
            max_profit = max(max_profit, num - min_buy)
            min_buy = min(min_buy, num)

        return max_profit