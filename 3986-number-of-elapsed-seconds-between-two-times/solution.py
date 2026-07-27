class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        start = startTime.split(":")
        end = endTime.split(":")
        seconds = 3600
        start = [int(i) for i in start]
        end = [int(i) for i in end]
        Startsec = 0
        endSec = 0
        for i in range(3):
            Startsec += start[i] * seconds
            endSec += end[i] * seconds
            seconds /=60
        return int(abs(endSec-Startsec))
        