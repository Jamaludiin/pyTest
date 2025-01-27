# test_math_operations.py

import pytest

from Simple_Projects.math_operations import add, subtract, multipilication

# pytest test_math_operations.py::test_multipilication
def test_add():
    assert add(3, 2) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(5, 5) == 0


@pytest.mark.parametrize("x, y, result", [

    (2, 2, 4),
    (2, 3, 6),
    (2, 4, 8),
    ])

def test_multipilication(x, y, result):
    assert multipilication(x, y) == result