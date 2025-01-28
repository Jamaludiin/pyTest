
from Data_structure_algo.linear_search import linear_search

# pytest test_math_operations.py::test_multipilication

# pytest -v test_linear_search.py

def test_linear_search():
    arr = [10, 30, 20, 50, 60]
    target = 30

    assert linear_search(arr, target) == 1
