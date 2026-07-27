class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        strs = sorted(strs)
       
        first = strs[0]
        last = strs[-1]
        print(first,last)
        for i in range(min(len(first),len(last))):
            if first[i]!=last[i]:
                print(first[i],last[i])
                return ans
            ans+=first[i]
        return ans




           
            

            

        