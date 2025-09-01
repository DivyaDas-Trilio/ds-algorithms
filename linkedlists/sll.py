class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        

if __name__ == '__main__':
    head = None
    n1 = Node(10)
    print(n1.data)
    print(n1.next)
    head = n1
    
    # second Node
    n2 = Node(20)
    print(n2.data)
    print(n2.next)
    
    # Third Node.
    n3 = Node(30)
    print(n3.data)
    print(n3.next)
    
    # Fourth Node
    n4 = Node(40)
    print(n4.data)
    print(n4.next)
    
    # connect nodes.
    n1.next = n2
    n2.next = n3
    n3.next = n4