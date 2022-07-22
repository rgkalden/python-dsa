'''
Python program to demonstrate Queue data structure using lists

queue is a FIFO structure
enqueue() add item to queue
dequeue() remove item from queue
front() get item from front
rear() get item from rear
size() get length of queue
isEmpty() is empty
contains() returns true if contains

'''

class Queue():
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def front(self):
        return self.queue[-1]

    def rear(self):
        return self.queue[0]

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        self.queue.pop(0)

    def contains(self, item):
        if item in self.queue:
            for i in range(0, self.size()):
                if self.queue[i] == item:
                    return i
        else:
            return -1

    def __str__(self):
        return str(self.queue)

if __name__ == "__main__":

    queue = Queue()

    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    print("Initial queue")
    print(queue)

    print("queue size:", queue.size())

    print("Front item in queue: ", queue.front())
    print("Rear item in queue: ", queue.rear())

    checkItem = 'b'
    print(checkItem + " is at position " + str(queue.contains(checkItem)) + " in the queue")

    queue.dequeue()
    print("Current queue")
    print(queue)

    queue.dequeue()
    print("Current queue")
    print(queue)
    queue.dequeue()
    print("Current queue")
    print(queue)

    print("queue empty:", queue.isEmpty())
