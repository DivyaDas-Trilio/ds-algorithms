class Node:
    def __init__(self, data, next=None):
        self.next = next
        self.data = data
        
class CircularLinkedList:
    def __init__(self, data):
        self._head = Node(data=data)
    
    def create_cll(self, node_count):
        head = self._head
        while(node_count):
            node_count -= 1
            temp_head = Node(data=node_count)
            self._head.next = temp_head
            self._head = self._head.next
        return head
            
    
    def insert_at_begin(self, data):
        pass
    
    def insert_at_last(self, data):
        pass
    
    def insert_at_middle(self, data):
        pass
    
    def delete_at_begin(self):
        pass
    
    def delete_at_middle(self):
        pass
    
    def delete_at_end(self):
        pass
    
    def print_cll(self, head):
        while(head.next):
            print(head.data, end=" ")
            head = head.next
    
if __name__ == '__main__':
    cll = CircularLinkedList(10)
    head = cll.create_cll(10)
    cll.print_cll(head)