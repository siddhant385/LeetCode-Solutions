class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)-1
        i = 1
        digit = 0
        while n>=0:
            digit += digits[n]*i
            i *=10
            n-=1
        digit +=1
        arr = []
        while digit>0:
            num = digit % 10
            arr.append(num)
            digit //=10
        arr.reverse()
        return arr
            

            
        