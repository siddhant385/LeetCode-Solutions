class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        k = str(num)
        for digit in s:
            if digit != '9':
                for ch in s:
                    if ch == digit:
                        s= s.replace(ch,'9')
                max_num = int(s)
                break
                
        else:
            max_num = num
        for digit in k:
            if digit != '0':
                for ch in k:
                    if digit ==ch:
                        k= k.replace(ch,'0')
                min_num = int(k)        
                break
        else:
            min_num = num
        return max_num - min_num
        