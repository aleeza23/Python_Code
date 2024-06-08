class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_p = 0
        right_p = 1
        buy_stock = 0
        max_profit = 0


        while right_p < len(prices):
            if prices[left_p] < prices[right_p]:
                max_profit = max(max_profit , prices[right_p] - prices[left_p])
            else:
                left_p = right_p
            right_p += 1        
         
        return max_profit        


        