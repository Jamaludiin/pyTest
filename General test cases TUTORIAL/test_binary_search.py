

from Data_structure_algo.binary_search import binary_search

# pytest binary_search.py::test_binary_search

# pytest -v test_binary_search.py

def test_binary_search():
    arr = [10, 40, 70, 20, 13, 11, 100]
    target = 100

    assert binary_search(arr, target) == 6