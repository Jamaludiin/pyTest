# You can run the same test with multiple inputs using parametrize.

# pytest test_parametrizing_tests.py

# pytest -v test_parametrizing_tests.py
import pytest

@pytest.mark.parametrize("x, y, result", [
    (2, 3, 5),  # Test case 1
    (1, 1, 2),  # Test case 2
    (0, 0, 0),  # Test case 3
])


def test_add(x, y, result):
    assert x + y == result

@pytest.mark.parametrize("x, y, result", [

    (2, 2, 4),
    (2, 3, 6),
    (2, 4, 8),
    ])

def test_multiplication(x, y, result):
    assert x * y == result