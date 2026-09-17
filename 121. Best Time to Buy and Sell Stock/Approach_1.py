class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        result=0
        buy=float("inf")
        for i in range(len(prices)):
            buy=min(buy,prices[i])
            result=max(result,prices[i]-buy)
        return result