class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res_list = nums1+nums2
        res_list.sort()
        num = len(res_list)
        if (num%2)== 0:
            return self.evenmedian(res_list,num)

        else:
            median = self.oddmedian(res_list,num)
            return median
        # print("length is: ",num)
        # print("Mod is: ", sum(res_list)/num)
        # return sum(res_list)/num
    
    def oddmedian(self,listq,n):
        nthterm = n//2
        return listq[nthterm]
    
    def evenmedian(self,list,n):
        nm1thterm = (n-1)//2
        nthterm = n//2
        median = (list[nm1thterm]+list[nthterm])/2
        return median
        