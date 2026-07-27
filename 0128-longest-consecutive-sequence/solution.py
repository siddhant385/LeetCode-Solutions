class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_streak = 0
        for num in num_set:
            if (num-1) not in num_set:
                streak = 1
                while(num+1) in num_set:
                    streak +=1
                    num +=1
                max_streak = max(streak,max_streak)
        return max_streak

        