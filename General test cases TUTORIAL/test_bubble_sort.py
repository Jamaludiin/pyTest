
from Data_structure_algo.bubble_sort import bubble_sort

# pytest test_math_operations.py::test_multipilication

# pytest -v test_bubble_sort.py

def test_bubble_sort():
    arr = [10, 30, 20, 50, 60]
    target = 30

    assert bubble_sort(arr) == [10, 20, 30, 50, 60]
