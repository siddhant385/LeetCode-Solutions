class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = float('inf')
        max_value = float('-inf')
        profit = 0
        for i in prices:
            if i < min_value:
                min_value = i
                max_value = i
            else:
                max_value = max(max_value,i)
            profit = max(profit,max_value - min_value)
        return profit
        