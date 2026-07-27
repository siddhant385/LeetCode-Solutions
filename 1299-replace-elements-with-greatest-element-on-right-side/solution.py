class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_ele = -1
        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = max_ele
            max_ele = max(temp,max_ele)
        return arr
            
            