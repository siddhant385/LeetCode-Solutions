class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        cb = 0
        fb = 0
        for i in range(len(nums)-1):
            fb = max(fb, i+nums[i])
            if i >= cb:
                jump +=1
                cb = fb
        return jump
