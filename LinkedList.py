
class Node:
    
    def __init__(self, value):
        self.node = value # the node itself
        self.next = LastNode()  # pointer to the next node

    def __str__(self):
        return "" + str(self.node)

class LastNode():

    def __init__(self):
        return
   
class LinkedList:

    def __init__(self,value):
        self.first = Node(value)  # first element of the list is a node
        self.current = self.first # pointer to the current node
        self.last = LastNode()
        

    def addNode(self, value):
        
        self.last = Node(value) # let the pointer become a node
        self.moveForward() 

    def moveForward(self):
        if (not self.Done()):
            self.last = self.current.next # move the pointer forward
            self.last = LastNode()

    def firstNode(self):
        self.current = self.first # go back to the first node

    # (!) problem here
    def getNode(self):
        return self.current.node # get the value of the node

    def Done(self):
        if (type(self.current) == type(self.last)):
            return True
        else:
            return False

    # print the entire linked list
    def printList(self):
        self.firstNode()
        
        while (not self.Done()):
            print(self.current)
            self.moveForward()

    # print the current node
    def printNode(self):
        print(self.current.node)

    def __iter__(self):
        #self.firstNode()
        return self

    def __next__(self):

        if self.Done():
            raise StopIteration
        else:
            self.moveForward()

        #return self.getNode()

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
