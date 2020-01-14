import unittest
from LinkedList import LinkedList, Node

class searchTest(unittest.TestCase):
  
    def setUp(self):
        self.myList = LinkedList(1)

        for i in range(2,10):
            self.myList.addNode(i)
    
    def test_searchMethodTest(self):
        result = Node(5)
        self.assertEqual(self.myList.searchList(5).node, result.node)

    def test_searchNextTest(self):
        result = Node(2)
        self.assertEqual(self.myList.searchNext(1).node, result.node)

    def test_searchPreviousTest(self):
        result = Node(3)
        self.assertEqual(self.myList.searchPrevious(4).node, result.node)
    
    def test_deleteNode(self):
        key = 3

        self.myList.deleteNode(key)

        for x in self.myList:
            print(x)
            self.assertNotEqual(x.node, key)

        