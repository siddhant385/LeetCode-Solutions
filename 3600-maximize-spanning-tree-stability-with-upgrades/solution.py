from typing import List

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:

        def can(x):
            parent = list(range(n))
            rank = [0]*n

            def find(a):
                while parent[a]!=a:
                    parent[a]=parent[parent[a]]
                    a=parent[a]
                return a

            def union(a,b):
                pa,pb=find(a),find(b)
                if pa==pb:
                    return False
                if rank[pa]<rank[pb]:
                    pa,pb=pb,pa
                parent[pb]=pa
                if rank[pa]==rank[pb]:
                    rank[pa]+=1
                return True

            used=0
            upgrades=0

            optional=[]

            # mandatory edges
            for u,v,s,m in edges:
                if m==1:
                    if s<x:
                        return False
                    if not union(u,v):   # cycle check
                        return False
                    used+=1
                else:
                    optional.append((u,v,s))

            normal=[]
            upgrade=[]

            for u,v,s in optional:
                if s>=x:
                    normal.append((u,v))
                elif s*2>=x:
                    upgrade.append((u,v))

            for u,v in normal:
                if union(u,v):
                    used+=1

            for u,v in upgrade:
                if upgrades==k:
                    break
                if union(u,v):
                    upgrades+=1
                    used+=1

            return used==n-1

        lo,hi=1,2*10**5
        ans=-1

        while lo<=hi:
            mid=(lo+hi)//2
            if can(mid):
                ans=mid
                lo=mid+1
            else:
                hi=mid-1

        return ans