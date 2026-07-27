# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dicti = dict()
        curr = headA
        curr2 = headB
        while curr is not None:
            dicti[curr] = dicti.get(curr,0)+1
            curr = curr.next
        while curr2 is not None:
            dicti[curr2] = dicti.get(curr2,0)+1
            curr2 = curr2.next
        for i in dicti.keys():
            if dicti[i] > 1:
                return i
        return None
        