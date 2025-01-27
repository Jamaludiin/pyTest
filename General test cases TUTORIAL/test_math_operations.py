# test_math_operations.py

from Simple_Projects.math_operations import add, subtract

def test_add():
    assert add(3, 2) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(5, 5) == 0
