class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # पहला हिस्सा: मीटिंग पॉइंट ढूंढना
        meeting_point = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                meeting_point = slow  # मीटिंग पॉइंट मिला
                break                 # लूप से बाहर आ जाओ

        # अगर लूप खत्म हो गया और मीटिंग पॉइंट नहीं मिला, मतलब साइकिल नहीं है
        if meeting_point is None:
            return None

        # दूसरा हिस्सा: साइकिल का स्टार्टिंग नोड ढूंढना
        p1 = head
        p2 = meeting_point
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        # जहाँ दोनों मिलेंगे, वही स्टार्ट है
        return p1
