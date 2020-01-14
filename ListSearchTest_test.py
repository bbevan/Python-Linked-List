import unittest
from LinkedList import LinkedList, Node

class searchTest(unittest.TestCase):
  
    def setUp(self):
        self.myList = LinkedList(1)

        for i in range(10):
            self.myList.addNode(i)
    
    def test_searchMethodTest(self):
        result = Node(5)
        self.assertEqual(self.myList.searchList(5).node, result.node)

    def test_searchNextTest(self):
        result = Node(5)
        self.assertEqual(self.myList.searchNext(4).node, result.node)

    def test_deleteNode(self):
        key = 4

        self.myList.deleteNode(key)

        for all in self.myList:
            if all.node == key:
                print("Found key " + str(key))
                return False
            else:
                return True

        