'''
Python program to demonstrate a Singly Linked List

Linked list is a linear collection of nodes
Each node contains data and a reference to the next node in the list

Linked Lists vs Arrays:
Insertion/Deletion is more efficient with a linked list
Searching is less efficient with a linked list. No random access, so must traverse through list to search

'''

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, newData):
        # Allocate new node and add data
        newNode = Node(newData)
        # Make next of new node refer to the old head
        newNode.next = self.head
        # Move head of list to the new node
        self.head = newNode

    def insertAfter(self, previousNode, newData):
        if previousNode is None:
            print('Given node must be in the linked list')
            return
        # Allocate new node and add data
        newNode = Node(newData)
        # Make next of new node refer to the next of previous node
        newNode.next = previousNode.next
        # Make next of previous node as new node
        previousNode.next = newNode

    def append(self, newData):
        # Allocate new node and add data
        newNode = Node(newData)
        # if the linked list is empty, make the new node the head
        if self.head is None:
            self.head = newNode
            return
        # otherwise traverse list until last node
        last = self.head
        while last.next:
            last = last.next
        # Change the next of the last node
        last.next = newNode

    def deleteNodeByKey(self, key):
        temp = self.head
        # Check if head node contains key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        # Search for key, keep track of previous node
        while temp is not None:
            if temp.data == key:
                break
            previous = temp
            temp = temp.next
        # if key not found
        if temp == None:
            return
        # Unlink node to be deleted fromm linked list
        previous.next = temp.next
        temp = None

    def deleteNodeByPosition(self, position):
        if self.head is None:
            return

        index = 0
        current = self.head
        while current.next and index < position:
            previous = current
            current = current.next
            index += 1

        if index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next
            current = None

    def countNodes(self):
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next

        return count

    def search(self, target):
        temp = self.head
        while temp:
            if temp.data == target:
                return True
            temp = temp.next
        return False

    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def getNodeData(self, index):
        current = self.head
        count = 0
        while current is not None:
            if count == index:
                return current.data
            count += 1
            current = current.next

        return "No data at given index"


if __name__ == "__main__":

    
    llist = LinkedList()
    llist.append(6)
    llist.push(7)
    llist.push(1)
    llist.append(4)

    llist.insertAfter(llist.head.next, 8)

    print('Created linked list is: ')
    llist.printList()

    # Delete Node with value
    key = 8
    print('\nDelete node with key', key)
    llist.deleteNodeByKey(key)
    llist.printList()

    # Delete Node at position
    position = 2
    print('\nDelete node at position', position)
    llist.deleteNodeByPosition(position)
    llist.printList()

    # Get count of nodes
    print("Number of nodes:", llist.countNodes())

    # Search for node value
    target = 100
    print('\nLinked list contains ' + str(target) + "? " + str(llist.search(target)))

    # reverse the linked list
    print('\nReverse the list')
    llist.reverse()
    llist.printList()

    # Get data at node index
    index = 1
    print('\nLinked list data at index ' + str(index) + "? " + str(llist.getNodeData(index)))