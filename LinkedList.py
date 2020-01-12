
class Node:
    
    def __init__(self, value):
        self.node = value
        self.next = None
   
class LinkedList:

    def __init__(self,value):
        self.first = Node(value)
        self.current = self.first
        

    def addNode(self, value):
        self.current.next = Node(value)
        self.moveForward()

    def moveForward(self):
        self.current = self.current.next

    def firstNode(self):
        self.current = self.first

    def getNode(self):
        return [self.label, self.current]

    def getNext(self):
        return self.current.next

    def printList(self):
        self.firstNode()
        while (self.current != None):
            print(self.current.node)
            self.moveForward()

    def printNode(self):
        print(self.current.node)

class LabeledLinkedList(LinkedList):

    def __init__(self, value, label):
        self.label = label
        super().__init__(value)

    

myList = LinkedList("a")
myList.addNode("b")
myList.printList()

myLabeled = LabeledLinkedList(1, 1)
print(myLabeled.first.node)
print(myLabeled.label)