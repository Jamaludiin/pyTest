import pytest
from calculator import addition

def test_addition_positive_numbers():
    # Test with positive numbers
    assert addition(10, 20) == 30
    assert addition(5, 5) == 10
    
def test_addition_negative_numbers():
    # Test with negative numbers
    assert addition(-1, -1) == -2
    assert addition(-10, -20) == -30
    
def test_addition_zero():
    # Test with zero
    assert addition(0, 0) == 0
    assert addition(10, 0) == 10
    assert addition(0, 10) == 10
    
def test_addition_float_numbers():
    # Test with floating point numbers
    assert addition(1.5, 2.5) == 4.0
    assert addition(0.1, 0.2) == pytest.approx(0.3)  # Using approx for floating point comparison

def test_addition_mixed_numbers():
    # Test with mixed positive and negative numbers
    assert addition(-5, 10) == 5
    assert addition(10, -5) == 5