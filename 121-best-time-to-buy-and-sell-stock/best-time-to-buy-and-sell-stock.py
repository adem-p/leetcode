class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy = 0
        for day in range(len(prices)):
            if prices[day] < prices[buy]: # We found a cheaper day
                buy = day
            else:
                proposed_profit = prices[day] - prices[buy]
                profit = max(profit, proposed_profit)
        return profit
            
            

    
        