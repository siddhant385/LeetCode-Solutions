class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n <= 1:
            return 1
        p = 1
        candies = [1] * n
        while p < n:
            if ratings[p-1] < ratings[p]:
                candies[p] = candies[p-1]+1
            p+=1
        p = n-2
        while p >-1:
            if ratings[p] > ratings[p+1]:
                candies[p] = max(candies[p],candies[p+1]+1)
            p-=1
        return sum(candies)



        
            
                    
            
                
