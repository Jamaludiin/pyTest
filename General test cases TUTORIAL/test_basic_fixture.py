# Fixtures are reusable pieces of setup code for tests. 
# For example, if all your tests need a database connection or a sample object, 
# you can use a fixture.
# A fixture that provides a simple string value for tests.

# pytest test_basic_fixture.py

# pytest -v test_basic_fixture.py

import pytest

@pytest.fixture
def sample_text():
    return "Hello, Pytest!"

def test_sample_text(sample_text):
    assert sample_text == "Hello, Pytest!"


def test_again(sample_text):
    assert sample_text # if you did not use the == this will be considered true 
    # # Passes, because a non-empty string is truthy

def test_again_true(sample_text):
    assert sample_text is True # whay this fail
    # fails because sample_text is a string, not the Boolean value True.

def test_again_with_bool(sample_text):
    assert bool(sample_text) is True  # Passes