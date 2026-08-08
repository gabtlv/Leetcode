class Solution(object):
    def maxProfit(self, prices):
        # iterate through the whole array and see whats the best day to buy and sell
        
        minPrice = prices[0]
        maxProfit = 0 
        for price in prices:
            if price - minPrice  > maxProfit:
                maxProfit = price - minPrice
                print(maxProfit)
            elif price < minPrice:
                minPrice = price
        return maxProfit
