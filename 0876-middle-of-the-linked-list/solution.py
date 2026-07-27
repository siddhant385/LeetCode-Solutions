# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        size = 0
        while current:
            current = current.next
            size +=1
        middle = size//2
        current = head
        cnt = 0
        while cnt < middle:
            current = current.next
            cnt+=1
        if current.next:
            return current
        return current

        
        
        