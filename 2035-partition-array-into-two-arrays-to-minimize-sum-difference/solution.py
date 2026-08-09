class Solution:

    def dfs(self,idx,size,total_sum,nums,n,array):
        if idx >= n:
            return array[size].append(total_sum)
        pick = self.dfs(idx+1,size+1,total_sum+nums[idx],nums,n,array)
        notPick = self.dfs(idx+1,size,total_sum,nums,n,array)
    def minimumDifference(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        left = nums[:n//2]
        right = nums[n//2:]
        leftSums = defaultdict(list)
        rightSums = defaultdict(list)
        self.dfs(0,0,0,left,n//2,leftSums)
        self.dfs(0,0,0,right,n//2,rightSums)
        for keys in rightSums:
            rightSums[keys].sort()
        
        mindiff = float('inf')
        for k in leftSums:
            for S_L in leftSums[k]:
                target = (total // 2) - S_L
                right_list = rightSums[n//2 - k]
                idx = bisect.bisect_left(right_list, target)
                if idx < len(right_list):
                    S_R = right_list[idx]
                    current_sum = S_L + S_R
                    mindiff = min(mindiff, abs(total - 2 * current_sum))
                    
                # Case 2: idx 0 se bada hai (target se chhota element bhi try karo)
                if idx > 0:
                    S_R = right_list[idx - 1]
                    current_sum = S_L + S_R
                    mindiff = min(mindiff, abs(total - 2 * current_sum))

        return mindiff



             