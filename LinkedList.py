
class Node:
    
    def __init__(self, value, label):
        self.node = value
        self.next = None
        self.label = label
   
class LabeledLinkedList:

    def __init__(self,value, label):
        self.first = Node(value, label)
        self.current = self.first
        

    def addNode(self, value, label):
        self.current.next = Node(value, label)
        self.moveForward()

    def moveForward(self):
        self.current = self.current.next

    def firstNode(self):
        self.current = self.first
        self.label = 0

    def getNode(self):
        return [self.label, self.current]

    def getNext(self):
        return self.current.next

    def printList(self):
        self.firstNode()
        while (self.current != None):
            print(self.current.label)
            print(self.current.node)
            self.moveForward()

    def printNode(self):
        print(self.current.node)

myList = LabeledLinkedList("a", 1)
myList.addNode("b", 2)
myList.printList()