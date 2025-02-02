
from Data_structure_algo.linear_search import linear_search

# pytest test_math_operations.py::test_multipilication

# pytest -v test_linear_search.py
#--------------------OPTION ZER0--------------------

def test_linear_search():
    arr = [10, 30, 20, 50, 60]
    target = 30

    assert linear_search(arr, target) == 1


#--------------------OPTION ONE--------------------
#----------------------------
# We can use fixtures and @pytest.mark.parametrize to make your linear search tests 
# more structured and scalable.

import pytest
#from Data_structure_algo.linear_search import linear_search

# Step 1: Create a Fixture for Sample Arrays
@pytest.fixture
def sample_array():
    return [10, 30, 20, 50, 60]

#--------------------OPTION TWO--------------------

# Step 2: Use Fixture in the Test Function
# Modify the test function to use sample_array:
def test_linear_search_using_fixture(sample_array):
    target = 30
    assert linear_search(sample_array, target) == 1


#--------------------OPTION THREE--------------------
# Step 3: Use @pytest.mark.parametrize for Multiple Cases
# Instead of testing one case, let's test multiple values with @pytest.mark.parametrize:
@pytest.mark.parametrize("target, expected_index", [
    (10, 0),  # First element
    (30, 1),  # Middle element
    (50, 3),  # Last element
    (99, -1)  # Not found case
])

def test_linear_search_param(sample_array, target, expected_index):
    assert linear_search(sample_array, target) == expected_index


#--------------------OPTION FOUR--------------------

# Step 4: Using a Factory for Custom Arrays
# If you want dynamic test data, use a factory fixture:

@pytest.fixture
def array_factory():
    def create_array(*values):
        return list(values)
    return create_array

@pytest.mark.parametrize("arr, target, expected_index", [
    ([5, 15, 25, 35], 15, 1), # Test 1: 15 found at index 1
    ([1, 2, 3, 4, 5], 4, 3), # Test 2: 4 found at index 3
    ([100, 200, 300], 500, -1) # Test 3: 500 NOT found, should return -1
])
def test_linear_search_with_factory(array_factory, arr, target, expected_index):
    array = array_factory(*arr)  # Dynamically create arrays
    assert linear_search(array, target) == expected_index
