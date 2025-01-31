
# Fixture with Parameters (Multiple Cases)
# Parametrize the fixture to test different values.

# pytest test_fixture_with_parameters.py
# pytest -v test_fixture_with_parameters.py

import pytest
# three test cases, each with three value 
#                       test 1:     test 2:     test 3:  
#                        a, b, exp, (a, b, ex)   etc
@pytest.fixture(params=[(2, 3, 5), (1, 1, 2), (5, 5, 10)])
def add_data(request):
    return request.param

def test_addition(add_data):
    a, b, expected = add_data # one example is 2+3 =5. 
                              # this is the shape of each test (a,b, expected)
    assert a + b == expected

"""
@pytest.fixture(params=[...]):
    This defines a fixture named add_data, which provides test data.
    The params argument contains a list of tuples, where each tuple represents 
    test cases in the form (a, b, expected).
    pytest automatically runs the test multiple times, once for each tuple in params.

request.param:
    This retrieves the current tuple from params and returns it when add_data is used 
    in a test.

The test function test_addition(add_data):
    It receives add_data, which will be one of the tuples (a, b, expected).
    The tuple is unpacked into three variables:
        a: First number
        b: Second number
        expected: Expected sum of a + b
    The assertion assert a + b == expected checks whether the sum is correct.

    
How Pytest Runs This:
Pytest will run the test three times, once for each tuple in params:

First run with (2, 3, 5) → assert 2 + 3 == 5 ✅ Passes
Second run with (1, 1, 2) → assert 1 + 1 == 2 ✅ Passes
Third run with (5, 5, 10) → assert 5 + 5 == 10 ✅ Passes
"""