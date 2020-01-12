
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

    def printElement(self):
        self.firstNode()
        while (self.current != None):
            print(self.current.node)
            self.moveForward()


if __name__ == "__main__":
    myList = LinkedList(1)
    myList.addNode(2)
    myList.addNode(3)

    print("printing list")
    myList.printElement()