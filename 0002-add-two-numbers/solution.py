# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sol = []
        l1 = self.nodetolist(l1)
        l2 = self.nodetolist(l2)
        reversel1 = l1[::-1]
        reversel2 = l2[::-1]
        n1 = self.listtonum(reversel1)
        n2 = self.listtonum(reversel2)
        res = n1+n2
        final_lstr = [int(x) for x in str(res)]
        print(final_lstr)
        final_lst = final_lstr[::-1]
        node = self.listtolistnode(final_lst)
        return node
    
    def nodetolist(self,listq):
        query = list()
        while listq is not None:
            query.append(listq.val)
            listq = listq.next
        return query
    
    def listtonum(self,listq):
        s = [str(i) for i in listq]
        # Join list items using join()
        res = int("".join(s))
        return(res)
    
    def listtolistnode(self,listq):
        head = ListNode(listq[0])
        tail = head
        e = 1
        while e < len(listq):
            tail.next = ListNode(listq[e])
            tail = tail.next
            e+=1
        return head


                
                
        