class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        ans = 10000000000000
        for i in range(n):
            for j in range(m):
                ans = min(max(landStartTime[i]+landDuration[i],waterStartTime[j])+waterDuration[j],ans)
        for j in range(m):
            for i in range(n):
                ans = min(max(waterStartTime[j]+waterDuration[j],landStartTime[i])+landDuration[i],ans)
        return ans


        