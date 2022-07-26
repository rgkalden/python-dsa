'''
Graphs with Adjacency List

Array of linked lists
Each linked list has a unique node at the head
All adjacent neighbors to a node are added to the nodes linked list

To check an edge: O(V)
space complexity: O(V + E)

'''


class Graph():

    def __init__(self) -> None:
        self.alist = []

    def addNode(self, node):
        currentList = []
        currentList.insert(0, node)
        self.alist.append(currentList)

    def addEdge(self, src, dst):
        currentList = self.alist[src]
        dstNode = self.alist[dst][0]
        currentList.append(dstNode)

    def checkEdge(self, src, dst):
        currentList = self.alist[src]
        dstNode = self.alist[dst][0]

        for node in currentList:
            if node == dstNode:
                return True

        return False

    def print(self):

        for currentList in self.alist:
            for item in currentList:
                print(item + " -> ", end="")
            print("\n")


if __name__ == "__main__":
    graph = Graph()

    graph.addNode("A")
    graph.addNode("B")
    graph.addNode("C")
    graph.addNode("D")
    graph.addNode("E")

    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(1, 4)
    graph.addEdge(2, 3)
    graph.addEdge(2, 4)
    graph.addEdge(4, 0)
    graph.addEdge(4, 2)

    graph.print()

    print(graph.checkEdge(3, 2))
