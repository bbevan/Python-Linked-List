from LinkedList import Node, LinkedList

class GraphNode:

    def __init__(self, node, connection):
        self.node = Node(node)
        self.connection = connection
        self.Pair = [self.node, self.connection]

    def __str__(self):
        return "" + str(self.node) + ", " + str(self.connection)


class Graph:

    def __init__(self, initialNode, initialConnection):
        self.graph = LinkedList(GraphNode(initialNode, initialConnection))

    def addPoint(self, node, connection):
        self.graph.addNode(GraphNode(node, connection))

    def printGraph(self):
        self.graph.printList()

    def getPoint(self):
        return self.graph.getNode().node

myGraph = Graph(0,1)
myGraph.addPoint(1,1)
myGraph.printGraph()