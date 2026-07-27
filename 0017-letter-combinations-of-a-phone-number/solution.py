class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            "1":"",
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        ans = []
        sz = len(digits)
        def helper(idx,s):
            az = len(s)
            # agar index size ke barabar ho jaye
            if sz==0:
                return []
            if az ==sz:
                ans.append(s[:])
                return
            if idx>sz-1:
                return
            # digits[idx] hoga humara 23
            # map[digits hoga humara] [a,b,c]

            for i in range(len(m[digits[idx]])):
                s = s+m[digits[idx]][i]
                helper(idx+1,s)
                s = s[0:az:]
               
        helper(0,"")
        return ans
            

        