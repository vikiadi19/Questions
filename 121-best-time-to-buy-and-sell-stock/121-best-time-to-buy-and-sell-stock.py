class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = -math.inf
        # left, right = 0, 1
        # while left < len(prices)-1:
        #     if right >= len(prices):
        #         left += 1
        #         right = left+1
        #     if prices[right] < prices[left]:
        #         right += 1
        #         left += 1
        #     elif prices[left] < prices[right]:
        #         profit = max(profit, prices[right]-prices[left])
        #         right += 1
        # if profit == -math.inf:
        #     profit = 0
        # return profit
        l, r, maxP = 0, 1, 0
        while r<len(prices):
            if prices[l]>prices[r]:
                l = r
            else:
                profit = prices[r]-prices[l]
                maxP = max(maxP, profit)
            r+=1
            
        return maxP