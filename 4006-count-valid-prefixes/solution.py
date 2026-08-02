class Solution:
    def countValidPrefixes(self, s: str) -> int:
        n = len(s)
        
        
        string = ""
        ans = 0
        for i in s:
            string += i
            count0 = 0
            count1 = 0
            for st in string:
                if st == "0":
                    count0+=1
                else:
                    count1+=1
            length = count0+count1
            if length %2 == 0:
                if count0 == count1:
                    ans +=1
            else:
                if abs(count0-count1) == 1:
                    ans +=1
        return ans
                
                