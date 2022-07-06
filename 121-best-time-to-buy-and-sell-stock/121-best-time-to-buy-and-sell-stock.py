class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        maxP = 0
        while r<len(prices):
            p = prices[r]-prices[l]
            if p<0:
                l = r
                r+=1
            elif p>=0:
                maxP = max(maxP, p)
                r+=1
        
        return maxP
        # buy, l = math.inf,  0
        # sell, r = -math.inf, 1
        # while r<len(prices):
        #     if l<r:
        #         buy = min(buy, prices[l])
        #         sell = max(sell, prices[r])
        #     l+=1
        #     r+=1
        # maxP = sell-buy
        # if maxP>0:
        #     return maxP
        # return 0