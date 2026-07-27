class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Jab tak fast pointer aage jaa sakta hai
        while fast and fast.next:
            slow = slow.next          # Slow 1 kadam chalta hai
            fast = fast.next.next   # Fast 2 kadam chalta hai

        # Jab loop rukta hai, slow pointer hamesha middle mein hota hai
        return slow
