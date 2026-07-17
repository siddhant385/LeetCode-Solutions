# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = l1, l2
        carry = 0
        node = None
        tmp = None

        while h1 or h2:
            val1 = h1.val if h1 else 0
            val2 = h2.val if h2 else 0

            total = val1 + val2 + carry
            val = total % 10
            carry = total // 10

            if tmp:
                tmp.next = ListNode(val)
                tmp = tmp.next
            else:
                tmp = ListNode(val)
                node = tmp

            h1 = h1.next if h1 else None
            h2 = h2.next if h2 else None

        # 🔴 THIS IS THE "LAST CASE" FIX
        if carry:
            tmp.next = ListNode(carry)

        return node
