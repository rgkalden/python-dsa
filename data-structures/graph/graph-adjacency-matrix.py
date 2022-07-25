'''
Graphs with Adjacency Matrix

2D array to store 1/0 to represent presence of an edge between notes

square array, # rows = # unique nodes

To check an edge: O(1)
space compelixity: O(V^2)

'''

class Node():
    def __init__(self, data) -> None:
        self.data = data

class Graph():
    
    def __init__(self, size) -> None:
        self.nodes = []
        self.size = size
        self.matrix = [[0 for i in range(size)] for j in range(size)] # matrix is 2D list
    
    def addNode(self, node):
        self.nodes.append(node)

    def addEdge(self, src, dst):
        self.matrix[src][dst] = 1

    def checkEdge(self, src, dst):
        if self.matrix[src][dst] == 1:
            return True
        else:
            return False

    def print(self):
        print("  ", end=" ")
        for node in self.nodes:
            print(str(node.data) + " ", end=" ")
        print("\n")
        for i in range(0, self.size):
            print(str(self.nodes[i].data) + " ", end=" ")
            for j in range(0, self.size):
                print(str(self.matrix[i][j]) + " ", end=" ")
            print("\n")


if __name__ == "__main__":
    graph = Graph(5)

    graph.addNode(Node("A"))
    graph.addNode(Node("B"))
    graph.addNode(Node("C"))
    graph.addNode(Node("D"))
    graph.addNode(Node("E"))

    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(2, 4)
    graph.addEdge(4, 0)
    graph.addEdge(4, 2)

    graph.print()

    print(graph.checkEdge(3, 2))
