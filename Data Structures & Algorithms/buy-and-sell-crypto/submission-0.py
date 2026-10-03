class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cheap_price = prices[0]
        for i in range(1,len(prices)):
            profit = prices[i]-cheap_price
            max_profit=max(max_profit,profit)
            cheap_price = min(cheap_price,prices[i])
        return max_profit