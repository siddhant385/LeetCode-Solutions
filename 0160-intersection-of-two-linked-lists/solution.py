# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a1,a2 = headA, headB

        while a1 != a2:
            a1 = a1.next if a1 else headB
            a2 = a2.next if a2 else headA
        return a1
            
        
        