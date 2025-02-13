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





#-------------------MORE TEST FEATURES AND OPTIONS ONLY-------------------

#--------------------OPTION ONE--------------------
#----------------------------
# We can use fixtures and @pytest.mark.parametrize to make your queue tests 
# more structured and scalable.

import pytest
# Uncomment if linear_search is needed
# from Data_structure_algo.linear_search import linear_search


# Step 1: Create a Fixture for Sample Arrays
@pytest.fixture
def sample_array():
    return [10, 30, 20, 50, 60]

def test_enqueue_peek(sample_array):
    q = Queue()
    q.enqueue(sample_array[0])  # Enqueue first element
    assert q.peek() == 10  # Check the first element

def test_enqueue_multiple(sample_array):
    q = Queue()
    arr = sample_array
    for i in range(len(arr)):  # Corrected iteration over the list
        q.enqueue(arr[i])  # Enqueue each element

    assert q.peek() == 10  # Ensure the first element is at the front




def test_is_empty2(sample_array):
    
    """  
    Test the is_empty method.
    Verify that is_empty correctly identifies whether the queue is empty or not.
    """
    q = Queue()
    assert q.is_empty() is True  # A new queue should initially be empty
    q.enqueue(sample_array[2])
    q.enqueue(sample_array[3])
    assert q.is_empty() is False  # Queue should not be empty after enqueueing an element
    q.dequeue()
    assert q.is_empty() is False  # Queue should be not be empty after dequeuing only one element



#--------------------OPTION TWO--------------------
# Step 3: Use @pytest.mark.parametrize for Multiple Cases
# Instead of testing one case, let's test multiple values with @pytest.mark.parametrize:
@pytest.mark.parametrize("value", [10, 30, 50, 99])

def test_enqueue3(value):
    q = Queue()
    q.enqueue(value)
    assert q.peek() == value  # Check if the first enqueued value is correct



#------------------OPTION THREE---------------
# USE BOTH FIXTURE AND PARAM

# Step 1: Create a Fixture for Sample Arrays
@pytest.fixture
def sample_array():
    return [10, 30, 20, 50, 60]

# Step 2: Use Parametrize with the Fixture
@pytest.mark.parametrize("value", [10, 30, 50, 99])

def test_enqueue(sample_array, value):
    q = Queue()
    for num in sample_array:  
        q.enqueue(num)  # Enqueue all fixture values
    
    q.enqueue(value)  # Enqueue the parameterized value
    assert q.peek() == sample_array[0]  # Ensure first enqueued value is still correct


# ✅ Add Parameterization to this Test Too!
@pytest.mark.parametrize("value", [10, 30, 50, 99])
# ✅ Each test that needs value must have its own @pytest.mark.parametrize.
# If you want both tests to share the same parameter values, put them inside a test class with a class-level @pytest.mark.parametrize:

def test_dequeue_the_parameterized_value(sample_array, value):
    q = Queue()

    # Enqueue all fixture values first
    for num in sample_array:
        q.enqueue(num)

    q.enqueue(value)  # Enqueue the parameterized value
    q.dequeue()  # Remove one element

    assert q.is_empty() is False  # Ensure queue is not empty yet