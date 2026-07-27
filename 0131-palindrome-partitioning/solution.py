class Solution:
    def partition(self, si: str) -> List[List[str]]:
        ans = []
        size = len(si)

        def plin(string):
            sze=len(string)
            for i in range(sze):
                if string[i] != string[(sze-1)-i]:
                    return False
            return True

        def helper(lst,ind):
            if ind == size:
                ans.append(lst[:])
                return
            for i in range(ind,size):
                tocheck = si[ind:i+1]

                if plin(tocheck):
                    lst.append(tocheck)

                    helper(lst,i+1)

                    lst.pop()
                
        helper([],0)
        return ans

            
            

        