class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        n = len(words)
        ans = ""
        for i in words:
            w = 0
            for j in i:
                w+= weights[ord(j)-ord("a")]
            ans += chr(ord("z")-(w%26))
        return ans
            
                
                
            
            
            
        