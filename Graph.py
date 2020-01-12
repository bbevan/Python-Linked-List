from LinkedList import Node, LinkedList

class GraphNode:

    def __init__(self, node, connection):
        self.Pair = [Node(node), connection]

class Graph:

    def __init__(self, initialNode, initialConnection):
        self.graph = LinkedList(GraphNode(initialNode, initialConnection))

    def addPoint(self, node, connection):
        self.graph.addNode(GraphNode(node, connection))

    def printGraph(self):
        self.graph.printList()

myGraph = Graph(0,1)
myGraph.addPoint(1,1)
myGraph.printGraph()