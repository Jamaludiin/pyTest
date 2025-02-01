# test_math.py

def test_addition():
    assert 2 + 2 == 4  # Passes

def test_subtraction():
    assert 5 - 3 == 2  # Passes


def test_operations():
    assert 2 * 3 == 6          # Passes
    assert 10 / 2 == 5         # Passes
    assert 3 ** 2 == 9         # Passes
    assert 5 % 2 == 1          # Passes


def test_pass():
    a = 10
    b = 20
    c = a + b
    assert c == 30      # Passes


def test_fail():
    assert 2 + 2 == 5  # This will fail

