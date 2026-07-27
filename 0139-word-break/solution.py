class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wset = set(wordDict)
        cache = {}

        def backtrack(cs):
            if cs in cache:
                return cache[cs]
            if cs == "":
                return True
            for i in range(1,len(s)+1):
                prefix = cs[:i]
                suffix = cs[i:]

                if prefix in wset and backtrack(suffix):
                    cache[cs] = True
                    return True
            cache[cs] = False
            return False
        return backtrack(s)
