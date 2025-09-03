import random

class Node:
    def __init__(self, prev=None, data=0, next=None):
        self.prev = prev
        self.data = data
        self.next= next
        
class DLL():
    def __init__(self):
        pass
        
    def create_dll(self, count):
        node = Node(data=0)
        ret_head = node
        head = node
        node_count = 0

        while(not head.next):
            node_count += 1
            if(node_count == count):
                break
            each = random.randint(10,90)
            temp_head = Node(data=each)
            head.data = each
            head.next = temp_head
            temp_head.prev = head
            head = head.next

        return ret_head
                
    def print_dll(self, head): 
        while(head.next):
            print(head.data, end=" ")
            head = head.next
        print("\n")
            
    def insert_at_begin(self, head):
        each = random.randint(10,90)
        temp_head = Node(data=each)
        
        temp_head.next = head
        head.prev = temp_head
        head = temp_head
        

if __name__ == '__main__':
    dll = DLL() 
    ret_head = dll.create_dll(10) 
    head = ret_head 
    
    dll.print_dll(ret_head)
    
    dll.insert_at_begin(ret_head)
    
    dll.print_dll(head)