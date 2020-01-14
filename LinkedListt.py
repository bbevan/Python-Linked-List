class Node:
    
    def __init__(self, value):
        self.node = value # the node itself
        self.next = None  # pointer to the next node

    def __str__(self):
        return "" + str(self.node)

class Tail():
    pass


class LinkedList:

    def __init__(self, value):
        self.first = Node(value)
        self.current = self.first
        self.i = None

    def addNode(self, value):
        self.current.next = Node(value)
        self.current = self.current.next

    def __iter__(self):
        self.i = self.first
        return self

    def __next__(self):
        x = self.i
        if self.i:
            self.i = self.i.next
            return x
        else:
            self.i = self.first
            raise StopIteration
        
        
            
        
