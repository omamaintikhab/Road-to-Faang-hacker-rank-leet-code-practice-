# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0
    for i in range(1,len(prices)):
        if prices[i]> prices[i-1]:
            profit+= (prices[i] - prices[i-1])
    return profit
prices=[7,1,5,3,6,4]

'''
Logic:
if i is greater than i-1, sell it for example
=> 1 is not greater than 7 so we dont sell it.
=> 5 is greater than 1 we sell it and profit = profit + (5-1)
=> we dont sell until value is equal to 6
=> 6 (ie i)> greater than 3 ie (i-1) we sell it and take profitof 3 
'''