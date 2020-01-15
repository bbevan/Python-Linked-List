import unittest
from Graph import *

class MyGraphTest(unittest.TestCase):

    def setUp(self):
        myGraph = Graph(1,1)

    def test_init(self):
        self.assertIsInstance(self.myGraph, Graph)

    # (!) forgot to add a getPoint() method
    # (2) added the method, doesn't seem to work
    def test_addpoint(self):
        myGraph.addPoint(1,2)
        self.assertEqual(myGraph.getPoint(), [1,2])

    