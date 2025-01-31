

# pytest -v test_with_multiple_sets_of_parameters.py

# remeber we used to unback the Fixture with Parameters (Multiple Cases) 
# but this no need is easier

# Alternative Approach Using pytest.mark.parametrize
# If you want to run a test with multiple sets of parameters, a better way is:

import pytest

@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (1, 1, 2), (5, 5, 10)])
@pytest.mark.parametrize("x, y, expected_sum", [(10, 20, 30), (3, 7, 10), (4, 6, 10)])
def test_addition(a, b, expected, x, y, expected_sum):
    assert a + b == expected
    assert x + y == expected_sum


# Each combination of (a, b, expected) pairs with every (x, y, expected_sum), leading to:
# 3 × 3 = 9 total test cases.

"""
Where Are the 9 Test Cases?
Pytest generates a test case for each possible combination of a, b, expected with x, y, expected_sum, as shown below:

Test #	a	b	expected	x	y	expected_sum
    1	2	3	5	        10	20	30
    2	2	3	5	        3	7	10
    3	2	3	5	        4	6	10
    4	1	1	2	        10	20	30
    5	1	1	2	        3	7	10
    6	1	1	2	        4	6	10
    7	5	5	10	        10	20	30
    8	5	5	10	        3	7	10
    9	5	5	10	        4	6	10
"""