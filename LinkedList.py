
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

    def printElement(self):
        self.current = self.first
        while (self.current != None):
            print(self.current.node)
            self.moveForward()


if __name__ == "__main__":
    myList = LinkedList(1)
    print("1 added")

    myList.addNode(2)
    print("2 added")

    myList.addNode(3)
    print("3 added")

    print("printing list")
    myList.printElement()