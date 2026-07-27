class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        ans = 10000000000000
        minLand = [float('inf'),0]
        minWater = [float('inf'),0]
        for i in range(n):
            c = landStartTime[i] + landDuration[i]
            if c < minLand[0]:
                minLand[0] = c
                minLand[1] = i
        for j in range(m):
            c = waterStartTime[j] + waterDuration[j]
            if c < minWater[0]:
                minWater[0] = c
                minWater[1] = j
        minRide = float('inf')
        for i in range(m):
            minRide = min(minRide,max(minLand[0],waterStartTime[i])+waterDuration[i])
        for j in range(n):
            minRide = min(minRide,max(minWater[0],landStartTime[j])+landDuration[j])
        return minRide


        