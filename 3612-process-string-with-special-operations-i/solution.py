class Solution:
    def processStr(self, s: str) -> str:
        ans = []
        for char in s:
            if char == "#":
                ans += ans
            elif char == "*":
                if ans != []:
                    ans.pop()
            elif char == "%":
                ans = ans[-1::-1]
            else:
                ans.append(char)
        return "".join(ans)
        