
from Data_structure_algo.stack import Stack

# pytest -v test_stack.py

def test_peek():
   # push_value = 20
    #Stack.push(push_value)

    s = Stack()
    s.push(10)
    s.push(20)

    assert s.peek() == 20

def test_pop():
    s = Stack()
    s.push(10)
    s.push(20)
    assert s.pop() == 20

def test_is_empty():
    s = Stack()
    assert s.is_empty() == 1




def test_peek2():
    """Test the peek method."""
    s = Stack()
    s.push(100)
    s.push(200)

    assert s.peek() == 200  # Ensure the top element is correct after pushing

def test_pop1():
    """Test the pop method."""
    s = Stack()
    s.push(100)
    s.push(200)

    assert s.pop() == 200  # Ensure the top element is popped correctly
    assert s.pop() == 100  # Ensure the next element is popped correctly
    assert s.pop() == "Stack is empty"  # Ensure empty stack returns the correct message

def test_is_empty1():
    """Test the is_empty method."""
    s = Stack()

    assert s.is_empty() is True  # Check if a new stack is empty

    s.push(100)
    assert s.is_empty() is False  # Check after pushing an element

    s.pop() 
    assert s.is_empty() is True  # Check after popping the only element


"""s = Stack()
s.push(10)
s.push(20)
print("Top element:", s.peek())
print("Popped:", s.pop())"""

