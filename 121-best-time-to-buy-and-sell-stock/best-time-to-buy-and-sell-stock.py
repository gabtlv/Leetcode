class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            if price - minPrice > maxProfit:
                maxProfit = price - minPrice
            elif price < minPrice:
                minPrice = price
        return maxProfit