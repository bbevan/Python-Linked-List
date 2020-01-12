
class Node:
    
    def __init__(self, value):
        self.node = value # the node itself
        self.next = None  # pointer to the next node
   
class LinkedList:

    def __init__(self,value):
        self.first = Node(value)  # first element of the list is a node
        self.current = self.first # pointer to the current node
        

    def addNode(self, value):
        self.current.next = Node(value) # let the pointer become a node
        self.moveForward() 

    def moveForward(self):
        self.current = self.current.next # move the pointer forward

    def firstNode(self):
        self.current = self.first # go back to the first node

    def getNode(self):
        return self.current.node # get the value of the node

    def getNext(self):
        return self.current.next # get pointer to the next node
                                 # `current` is always a pointer!

    def isDone(self):
        if (self.current != None):
            pass
        else:
            return True

    # print the entire linked list
    def printList(self):
        self.firstNode()
        
        while (not self.isDone()):
            print(self.getNode())
            self.moveForward()

    # print the current node
    def printNode(self):
        print(self.current.node)


class LabeledLinkedList(LinkedList):

    # Extends LinkedList nodes with labels
    
    def __init__(self, value, label):
        self.firstlabel = label
        self.currentlabel = self.firstlabel
        super().__init__(value)

    def addNode(self,value,label):
        self.current.nextlabel = label
        self.moveForward()
        super().addNode(value)

    def moveForward(self):
        self.currentlabel = self.current.nextlabel
