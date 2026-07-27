# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
            
        slow = head
        fast = head.next  # <-- तेज वाले को एक कदम आगे से शुरू कर सकते हैं

        while slow != fast:
            # अगर fast लिस्ट के अंत तक पहुँच गया, तो साइकिल नहीं है
            if not fast or not fast.next:
                return False
            
            slow = slow.next
            fast = fast.next.next
            
        return True # अगर लूप टूटा मतलब slow और fast बराबर हो गए