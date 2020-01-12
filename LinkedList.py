
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
        return self.current

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

    def __init__(self,value):
        self.label = 0
        self.list = LinkedList(value)

    def incrementLabel(self):
        self.label += 1

    def addLabeledNode(self,value):
        self.list.addNode(value)
        self.incrementLabel()




labeledlist = LabeledLinkedList("a")
labeledlist.addLabeledNode("b")
print(labeledlist.label)
print(labeledlist.list.first.node)
