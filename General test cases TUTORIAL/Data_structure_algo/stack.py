
# Using a list to implement a stack with push, pop, and peek operations.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

# Example
s = Stack()
s.push(10)
s.push(20)
print("Top element:", s.peek())
print("Popped:", s.pop())
