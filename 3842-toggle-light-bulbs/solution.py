class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        power_on = []
        for i in bulbs:
            if i in power_on:
                power_on.remove(i)
            else:
                power_on.append(i)
        power_on.sort()
        return power_on
            
        