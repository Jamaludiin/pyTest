
# pytest -v test_stack_setup_tear_down.py
import pytest
from Data_structure_algo.stack import Stack

# Create a pytest fixture for setup and teardown
@pytest.fixture
def stack():
    # Setup: Create a new Stack instance before each test
    s = Stack()
    yield s  # Provide the stack instance to the test function
    # Teardown: (optional cleanup can be done here, e.g., clearing the stack)
    del s

"""
EXPLANATION 

The stack fixture creates a new Stack instance before each test.
The yield keyword allows the fixture to provide the Stack instance to the test functions. 
After the test completes, the code following yield is executed (useful for cleanup).

"""
# Test cases
def test_peek(stack):
    """Test the peek method."""
    stack.push(10)
    stack.push(20)
    assert stack.peek() == 20  # Check the top element

def test_pop(stack):
    """Test the pop method."""
    stack.push(10)
    stack.push(20)
    assert stack.pop() == 20  # Ensure the top element is popped
    assert stack.pop() == 10  # Ensure the next element is popped
    assert stack.pop() == "Stack is empty"  # Ensure empty stack returns the correct message

def test_is_empty(stack):
    """Test the is_empty method."""
    assert stack.is_empty() is True  # New stack should be empty
    stack.push(100)
    assert stack.is_empty() is False  # Stack should not be empty after push
    stack.pop()
    assert stack.is_empty() is True  # Stack should be empty after popping the only element

def test_peek2(stack):
    """Test the peek method with different values."""
    stack.push(100)
    stack.push(200)
    assert stack.peek() == 200  # Ensure the top element is correct

def test_pop1(stack):
    """Test popping multiple elements."""
    stack.push(100)
    stack.push(200)
    assert stack.pop() == 200  # Ensure the top element is popped correctly
    assert stack.pop() == 100  # Ensure the next element is popped correctly
    assert stack.pop() == "Stack is empty"  # Ensure empty stack returns the correct message

def test_is_empty1(stack):
    """Test the is_empty method with a series of operations."""
    assert stack.is_empty() is True  # Check if the stack is empty initially
    stack.push(300)
    assert stack.is_empty() is False  # Check after pushing an element
    stack.pop()
    assert stack.is_empty() is True  # Check after popping the only element
