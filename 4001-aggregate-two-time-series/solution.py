class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        s1 = len(series1)
        s2 = len(series2)
        l,r = 0,0
        ans = []
        while l < s1 and r < s2:
            if series1[l][0] == series2[r][0]:
                ans.append([series1[l][0], series1[l][1] + series2[r][1]])
                l += 1
                r += 1
            elif series1[l][0] < series2[r][0]:
                ans.append([series1[l][0],series1[l][1]+series2[r][1]])
                l+=1
            
            else:
                ans.append([series2[r][0],series1[l][1]+series2[r][1]])
                r+=1
        while l < s1:
            ans.append(series1[l])
            l+=1
            

        while r < s2:
            ans.append(series2[r])
            r+=1
            
        return ans
            
            
            
                
                
                
        