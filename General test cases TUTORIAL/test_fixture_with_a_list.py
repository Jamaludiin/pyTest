# Fixture with a List (Multiple Data)
# A fixture returning a list of numbers.

# pytest test_fixture_with_a_list.py

# pytest -v test_fixture_with_a_list.py

import pytest

@pytest.fixture
def number_list():
    return [1, 2, 3, 4, 5]

def test_number_list(number_list):
    assert sum(number_list) == 15

def test_find_a_value_in_a_list(number_list):
    assert number_list[1] == 2

def test_two_items_added(number_list):
    total = number_list[1] + number_list[2] # 2+3 = 5
    assert total == 5