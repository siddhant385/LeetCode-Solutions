class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        ans = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            if self.mainf(mid, weights, days):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def mainf(self, mid, weights, days):
        required_days = 1
        current_load = 0
        for weight in weights:
            if current_load + weight > mid:
                required_days += 1
                current_load = 0
            current_load += weight
        return required_days <= days
