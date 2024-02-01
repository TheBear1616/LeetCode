class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        buy = int(1e9)

        for i in range(len(prices)):
            if prices[i] < buy: buy = prices[i]
            if i + 1 < len(prices) and prices[i] > prices[i + 1]:
                result += abs(prices[i] - buy)
                buy = prices[i + 1]
        
        result += abs(prices[-1] - buy) if buy < prices[-1] else 0

        return result
