class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ids = []
        n = len(s)
        for i in range(n):
            if s[i] == "(":
                ids.append(i)
            elif s[i] == ")" and ids != []:
                ids.pop()
        # left out indexes
        ans = 0
        st = []
        id_dict = dict()
        for i in ids:id_dict[i] = id_dict.get(i,True)
        cnt = 0
        for i in range(n):
            if s[i] == "(" and not id_dict.get(i,False):
                st.append(s[i])
            elif id_dict.get(i,False):
                ans = max(cnt,ans)
                cnt = 0
            elif s[i] == ")":
                if st == []:
                    ans = max(cnt,ans)
                    cnt = 0
                else:
                    st.pop()
                    cnt +=2
        ans = max(cnt,ans)
        return ans
        