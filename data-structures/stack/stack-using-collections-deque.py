'''
Python program to demonstrate Stack data structure using 
deque from the collections library

Stack is a LIFO structure
empty() is empty
size() return size
peek() return top item from stack
push() add item to top of stack
pop() remove top item from stack
'''

from collections import deque

class Stack():
    def __init__(self):
        self.stack = deque()
    
    def empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def __str__(self):
        return str(self.stack)

if __name__ == "__main__":

    stack = Stack()

    stack.push('a')
    stack.push('b')
    stack.push('c')
    print("Initial Stack")
    print(stack)

    print("Stack size:", stack.size())

    print("Top item in stack: ", stack.peek())

    stack.pop()
    print("Current Stack")
    print(stack)

    stack.pop()
    stack.pop()
    print("Current Stack")
    print(stack)

    print("Stack empty:", stack.empty())
