class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    
    def find(self,node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self,i,j):
        abs_i = self.find(i)
        abs_j = self.find(j)
        if abs_i != abs_j:
            if self.rank[abs_i] < self.rank[abs_j]:
                self.parent[abs_i] = abs_j
            elif self.rank[abs_i] > self.rank[abs_j]:
                self.parent[abs_j] = abs_i
            else:
                self.parent[abs_j] = abs_i
                self.rank[abs_i] +=1
            return True
        return False

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # it should be in the format of mail:index
        n = len(accounts)
        dx = DSU(n)
        mail_dict = dict()
        for i in range(n):
            for j in range(1,len(accounts[i])):
                mail_idx = mail_dict.get(accounts[i][j],None)
                if mail_idx == None:
                    # here we will give index to our mail
                    mail_dict[accounts[i][j]] = i
                else:
                    dx.union(mail_idx,i)
        
        # now we will create a list 
        mail_list = defaultdict(list)
        for mail in mail_dict:
            idx = mail_dict[mail]
            abs_parent = dx.find(idx)
            mail_list[abs_parent].append(mail)
        
        # now we will append accounts to our list and return final list with sorting
        ans = []
        for idx in mail_list:
            new_list = [accounts[idx][0]]
            new_list = new_list+sorted(mail_list[idx])
            ans.append(new_list)
        return ans
        





