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
        dp = [[-1 for _ in range(n2+1)]for _ in range(n1+1)]
        for i in range(n1,-1,-1):
            for j in range(n2,-1,-1):
                if i == n1 and j == n2:
                    dp[i][j] = 0
                elif i == n1:
                    dp[i][j] = 1 + dp[i][j+1]
                elif j == n2:
                    dp[i][j] = 1 + dp[i+1][j]
                elif str1[i] == str2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    s2 = 1 + dp[i][j+1]
                    s1 = 1 + dp[i+1][j]
                    dp[i][j] = min(s1,s2)
        i,j = 0,0
        ans = ""
        while i < n1 or j < n2:
            if i >=n1 and j >=n2:
                return ans
            if i ==n1:
                ans += str2[j]
                j+=1
            elif j == n2:
                ans += str1[i]
                i +=1
            elif str1[i] == str2[j]:
                    ans += str1[i]
                    i +=1 
                    j +=1
            else:
                s2 = dp[i][j+1]
                s1 = dp[i+1][j]
                if s2 < s1:
                    ans += str2[j]
                    j +=1
                else:
                    ans += str1[i]
                    i+=1
        return ans
        
            


            
                


        