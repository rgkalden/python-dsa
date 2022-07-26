'''
Breadth First Search

Traverse a tree or graph data structure one level at a time

Use a queue to keep track of visited nodes

Breadth First:
Traverse level by level
Utilizes a queue
Better if destination is on average close to start
Siblings are visited before children

Depth first:
Traverse branch by branch
Utilizes a stack
Better if destination is on average far from the start
Children are visited before siblings
More popular for games/puzzles
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

    def breadthFirstSearch(self, src):

        # src is the starting point
        
        queue = []
        visited = [False for i in range(0, len(self.matrix))]

        queue.append(src)
        visited[src] = True

        while len(queue) != 0:
            src = queue.pop(0)
            print(self.nodes[src].data + " = visited")

            for i in range(0, len(self.matrix[src])):
                if self.matrix[src][i] == 1 and visited[i] == False:
                    queue.append(i)
                    visited[i] = True


if __name__ == "__main__":
    graph = Graph(5)

    graph.addNode(Node("A"))
    graph.addNode(Node("B"))
    graph.addNode(Node("C"))
    graph.addNode(Node("D"))
    graph.addNode(Node("E"))

    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(1, 4)
    graph.addEdge(2, 3)
    graph.addEdge(2, 4)
    graph.addEdge(4, 0)
    graph.addEdge(4, 2)

    graph.print()

    graph.breadthFirstSearch(4)