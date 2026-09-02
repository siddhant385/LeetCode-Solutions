class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        isOdd ,isEven = True,True
        # for i in nums1:
        #     if i % 2 !=0:
        #         isEven = False
        #     else:
        #         isOdd = False
        # if isOdd or isEven:
        #     return True
        n1 = len(nums1)
        # for odd
        for i in range(n1):
            for j in range(n1):
                if nums1[i] % 2 == 0:
                    if i != j:
                        if nums1[i] - nums1[j] % 2 == 0:
                            isOdd = False
        
        for i in range(n1):
            for j in range(n1):
                if nums1[i] % 2 != 0:
                    if i != j:
                        if nums1[i] - nums1[j] % 2 != 0:
                            isEven = False
        
        if isOdd or isEven:
            return True
        return False



        


        