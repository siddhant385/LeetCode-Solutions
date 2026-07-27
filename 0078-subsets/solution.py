class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(i,st):
            if i == len(nums):
                ans.append(st[:])
                return
            st.append(nums[i])
            helper(i+1,st)
            st.pop()
            helper(i+1,st)
        helper(0,[])    
        return ans

        