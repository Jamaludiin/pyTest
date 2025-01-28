
# Using a list to implement a queue with enqueue and dequeue operations.

"""
A queue is a data structure that follows the FIFO (First In, First Out) principle. 
This means that the first item added to the queue is the first one to be removed. 
Think of it like a line of people waiting for a ticket: the person who arrives 
first gets served first.
"""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value): # Adding to the Queue: enqueue()
        self.queue.append(value) # Adds the value to the end of the queue.

    def dequeue(self): # Removing from the Queue: dequeue()
        if not self.is_empty(): # Checks if the queue is not empty using the is_empty() method.
            return self.queue.pop(0) # Uses pop(0) to remove the first item in the list (position 0).
        return "Queue is empty" # If the queue is empty, it returns "Queue is empty".

    def is_empty(self):
        return len(self.queue) == 0
    
    def peek(self): # (view the front element)
        if not self.is_empty():
            return self.queue[0]  # Return the front element without removing it
        return "Queue is empty"


# Example
q = Queue()
q.enqueue(1)
q.enqueue(2)
print("Dequeued:", q.dequeue())
print("Dequeued:", q.dequeue())


q.enqueue(1)
q.enqueue(2)
print("Peek one: ", q.peek())