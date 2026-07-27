# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        l = 0
        r = len(lst)-1
        ans = 0
        while l<r:
            ans = max(ans,lst[l] + lst[r])
            l+=1
            r-=1
        return ans

        