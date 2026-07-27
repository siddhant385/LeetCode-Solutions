class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        current = self.head 
        cnt = 0
        while current != None:
            if cnt == index:
                return current.val
            cnt +=1
            current = current.next
        return -1
        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            return 
        last_node = self.head
        while last_node.next !=None:
            last_node = last_node.next
        last_node.next = Node(val)
            
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index ==0:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
            return 
        current_node = self.head
        cnt = 0
        while current_node and cnt < index-1:
            current_node = current_node.next
            cnt +=1
        if current_node:
            new_node = Node(val)
            new_node.next = current_node.next
            current_node.next = new_node



        

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return 
        if index == 0:
            self.head = self.head.next
            return
        
        current_node = self.head
        cnt = 0
        while current_node and cnt < index-1:
            current_node = current_node.next
            cnt +=1
        if current_node and current_node.next:
            current_node.next = current_node.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)