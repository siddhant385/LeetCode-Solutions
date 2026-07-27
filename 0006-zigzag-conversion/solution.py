class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # if len(s) <= numRows:
        #     return s
        if numRows == 1: return s
        rows = [''] * numRows
        end = numRows - 1
        flag = True
        index = 0
        num = 0
        while not num == len(s):
            if index == 0:
                flag = True
            if index == end:
                flag = False
            if flag:
                rows[index] += s[num]
                num +=1
                index +=1
            else:
                rows[index] += s[num]
                num +=1
                index -=1
        print(rows)
        sol = ""
        for i in rows:
            for j in i:
                sol +=j

        return sol     
