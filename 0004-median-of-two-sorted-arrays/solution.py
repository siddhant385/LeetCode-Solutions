class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        total = len(A) + len(B)
        half = total //2
        if len(A)>len(B):
            A,B = B,A
        l,r = 0,len(A)-1

        while True:
            mid1 = l + (r-l)//2 #Aleft
            mid2 = (half - mid1) -2 #Bleft

            Aleft = A[mid1] if mid1>=0 else float('-infinity')
            Bleft = B[mid2] if mid2>=0 else float('-infinity')
            Aright = A[mid1+1] if mid1+1<len(A) else float("infinity")
            Bright = B[mid2+1] if mid2+1<len(B) else float("infinity")
            if Aleft<=Bright and Bleft<=Aright:
                if total%2 !=0:
                    return min(Aright,Bright)
                return (max(Aleft,Bleft) + min(Aright,Bright))/ 2
            elif Aleft > Bright:
                r = mid1-1
            else:
                l = mid1+1





