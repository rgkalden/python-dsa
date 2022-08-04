'''
Binary Tree

Binary Search Tree = A tree data structure, where each node is greater than it's left child,
but less than it's right. Each node has no more than two children.

benefit: easy to locate a node when they are in this order						

time complexity: best case  O(log n)
                 worst case O(n)

space complexity: O(n)

'''


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, node):
        self.root = self.insertHelper(self.root, node)
        #print("inserted ", node.data)

    def insertHelper(self, root, node):
        data = node.data

        if root is None:
            root = node
            return root
        elif data < root.data:
            root.left = self.insertHelper(root.left, node)
        else:
            root.right = self.insertHelper(root.right, node)

        return root

    def display(self):
        self.displayHelper(self.root)

    def displayHelper(self, root):
        if root != None:
            # in order traversal. Swap left and right for decreasing
            self.displayHelper(root.left)
            print(root.data, end=' ')
            self.displayHelper(root.right)

    def search(self, data):
        return self.searchHelper(self.root, data)

    def searchHelper(self, root, data):
        if root is None:
            return False
        elif root.data == data:
            return True
        elif root.data > data:
            return self.searchHelper(root.left, data)
        else:
            return self.searchHelper(root.right, data)

    def remove(self, data):
        if self.search(data):
            self.removeHelper(self.root, data)
        else:
            print(str(data) + " could not be found")

    def removeHelper(self, root, data):
        if root is None:
            return root
        elif data < root.data:
            root.left = self.removeHelper(root.left, data)
        elif data > root.data:
            root.right = self.removeHelper(root.right, data)
        else:
            # node found
            if root.left is None and root.right is None:
                root = None
            elif root.right is not None:
                # find successor to replace node
                root.data = self.successor(root)
                root.right = self.removeHelper(root.right, root.data)
            else:
                # find predecessor to replace node
                root.data = self.predecessor(root)
                root.left = self.removeHelper(root.left, root.data)

        return root

    def successor(self, root):
        # find least value below right child of root node
        root = root.right
        while root.left is not None:
            root = root.left
        
        return root.data

    def predecessor(self, root):
        # find greatest value below left child of root node
        root = root.left
        while root.right is not None:
            root = root.right
        
        return root.data


if __name__ == "__main__":

    tree = BinarySearchTree()

    tree.insert(Node(5))
    tree.insert(Node(1))
    tree.insert(Node(9))
    tree.insert(Node(2))
    tree.insert(Node(7))
    tree.insert(Node(3))
    tree.insert(Node(6))
    tree.insert(Node(4))
    tree.insert(Node(8))

    tree.display()

    print('\n')
    print(tree.search(100))

    print('\n')
    tree.remove(0)
    tree.display()


    
