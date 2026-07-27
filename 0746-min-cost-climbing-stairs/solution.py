class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost.append(0)
        dp = [float('inf') for _ in range(n+1)]
        prev2 = cost[0]
        prev = cost[1]
        curr = 0
        
        for i in range(2,n+1):
            left = prev+cost[i]
            if i >1:
                right = prev2 + cost[i]
            curr = min(left,right)
            prev2 = prev
            prev = curr
        return curr
