class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for i in s:
            dic[i] = dic.get(i,0) +1
        res = ""
        for i in sorted(dic.items(),key=lambda x:-x[1]):
            res += i[0] * i[1]
        return res


        