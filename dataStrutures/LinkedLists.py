"""
    Linked Lists (listas ligadas) são estruturas de dados compostas por nós, onde cada nó contém um valor 
    e uma referência (ou ponteiro) para o próximo nó na sequência. Elas são úteis quando você precisa de 
    inserções e remoções frequentes sem a sobrecarga de realocar a memória, como 
    acontece com listas comuns (list) em Python.
    
    Tipos de Linked List:
    
    Singly Linked List (Lista Ligada Simples) – cada nó aponta apenas para o próximo.

    Doubly Linked List (Lista Duplamente Ligada) – cada nó aponta para o próximo e o anterior.
    
    Circular Linked List – o último nó aponta de volta para o primeiro, formando um ciclo.


"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # aponta para o proximo nó
        
class LinkedList:
    def __init__(self):
        self.head = None # inicio da lista
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
            print('None')
            
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()