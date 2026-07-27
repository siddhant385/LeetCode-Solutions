class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:

        def isPrime(n):
            if n <=1: return False
            if n <=3: return True
            if n %2 ==0 or n%3 ==0: return False
            i =5
            while i*i <= n:
                if n %i ==0 or n %(i+2) ==0:
                    return False
                i +=6
            return True
        
        map = {}
        for i in nums:
            map[i] = 1 + map.get(i,0)

        for m in map:
            if isPrime(map[m]):
                return True
        return False
                
        