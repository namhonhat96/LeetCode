class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        mina = prices[0]
        maxa = 0
        for i in range(1, len(prices)):
            mina = min(mina, prices[i])
            if prices[i]>prices[i-1]:
                maxa = max(maxa, prices[i]-mina)
        return maxa
            