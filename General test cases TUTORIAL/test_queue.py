# pytest -v test_queue.py
import pytest
from Data_structure_algo.queue import Queue

# Create a pytest fixture for setup and teardown
@pytest.fixture
def queue():
    """
    Fixture to create a new Queue instance for each test.
    Setup: Initialize a Queue instance before each test.
    Teardown: Perform cleanup after the test (if necessary).
    """
    q = Queue()
    yield q  # Provide the Queue instance to the test function
    del q  # Optional cleanup (if additional teardown is required)


# Test cases
def test_peek(queue):
    """
    Test the peek method.
    Verify that peek returns the front element of the queue without removing it.
    """
    queue.enqueue(10)
    queue.enqueue(20)
    assert queue.peek() == 10  # The first element in the queue should be 10


def test_dequeue(queue):
    """
    Test the dequeue method.
    Ensure elements are removed in FIFO (First-In-First-Out) order and handle empty queue cases.
    """
    queue.enqueue(10)
    queue.enqueue(20)
    assert queue.dequeue() == 10  # The first element dequeued should be 10
    assert queue.dequeue() == 20  # The second element dequeued should be 20
    assert queue.dequeue() == "Queue is empty"  # Dequeuing from an empty queue should return the correct message


def test_is_empty(queue):
    """
    Test the is_empty method.
    Verify that is_empty correctly identifies whether the queue is empty or not.
    """
    assert queue.is_empty() is True  # A new queue should initially be empty
    queue.enqueue(10)
    assert queue.is_empty() is False  # Queue should not be empty after enqueueing an element
    queue.dequeue()
    assert queue.is_empty() is True  # Queue should be empty after dequeuing the only element
