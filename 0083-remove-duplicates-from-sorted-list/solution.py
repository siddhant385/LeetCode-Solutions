# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        f = head
        s = head
        while f!=None:
            if f.val != s.val:
                s.next = f
                s = s.next
            f = f.next
        s.next = None
        return head





               


        