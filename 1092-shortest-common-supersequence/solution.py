class Solution:
    def recursion(self,idx1,idx2,str1,str2,n1,n2,dp):
        if idx1>=n1 and idx2>=n2:
            return ""
        if idx1 >= n1  or idx2 >= n2:
            if idx1 >= n1:
                return str2[idx2] + self.recursion(idx1,idx2+1,str1,str2,n1,n2,dp)
            else:
                return str1[idx1] + self.recursion(idx1+1,idx2,str1,str2,n1,n2,dp)
        if dp[idx1][idx2] != -1: return dp[idx1][idx2]
        if str1[idx1] == str2[idx2]:
            return str1[idx1] + self.recursion(idx1+1,idx2+1,str1,str2,n1,n2,dp)
        s2 = str2[idx2] + self.recursion(idx1,idx2+1,str1,str2,n1,n2,dp)
        s1 = str1[idx1] + self.recursion(idx1+1,idx2,str1,str2,n1,n2,dp)
        if len(s1) < len(s2):
            dp[idx1][idx2] = s1
            return dp[idx1][idx2]
        dp[idx1][idx2] = s2
        return dp[idx1][idx2]

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)
        prev = ["" for _ in range(n2+1)]
        for i in range(n1,-1,-1):
            curr = ["" for _ in range(n2+1)]
            for j in range(n2,-1,-1):
                if i == n1 and j == n2:
                    curr[j] = ""
                elif i == n1:
                    curr[j] = str2[j] + curr[j+1]
                elif j == n2:
                    curr[j] += str1[i] + prev[j]
                elif str1[i] == str2[j]:
                    curr[j] = str1[i] + prev[j+1]
                else:
                    s2 = str2[j] + curr[j+1]
                    s1 = str1[i] + prev[j]
                    if len(s1) < len(s2):
                        curr[j] = s1
                    else: curr[j] = s2
            prev = curr
                    

        return prev[0]

        