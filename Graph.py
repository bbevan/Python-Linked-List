class Node:
    
    def __init__(self, value, label):
        self.node = value
        self.next = None
        self.label = label

class Pair:

    def __init__(self, Node1 = [], Node2 = []):
        self.connection = [Node(Node1[0], [1]), Node(Node2[0], Node2[1])]

        if (Node1[1] != Node2[1]):
            raise Exception("Labels are not the same. The pair is not connected.")

class Graph:

    def __init__(self, *Pairs):
        self.graph = Pairs

        for p in Pairs:
            if (type(p) != "<class 'Pair'>"):
                raise Exception("Some input is not a pair. Try again.")

myGraph = Graph( Pair( [[0,1], [1,1]] ) )
#myGraph = Graph([[1]])
#myGraph = Graph([[0,1], [1,0]])