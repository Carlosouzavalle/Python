# É uma estrutura de lista onde cada nó aponta para o próximo e para o anterior

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        
    
    
    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
        
        
    def print_backward(self):
        current = self.head
        if not current:
            print("None")
            return
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" <- ")
            current = current.prev
        print("None")
        
        
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)


dll.print_forward()  
dll.print_backward()