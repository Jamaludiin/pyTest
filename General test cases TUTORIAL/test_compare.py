
# pytest test_compare.py::

# pytest -v test_compare.py
# pytest test_compare.py -v


# Substring Matching of Test Names
# fromat:    pytest -k <substring> -v
def test_greater():
   num = 100
   assert num > 10

def test_greater_equal():
   num = 100
   assert num >= 100

def test_less():
   num = 100
   assert num < 200


"""
This lesson explains how to use the -k option in pytest to selectively run 
tests based on a substring in their names. Let me break this down with clear examples.

What is -k?
The -k option allows you to run only the tests whose names contain a specific substring.
This is useful when you have many tests but want to focus on specific ones 
without running the entire test suite.


pytest -k <substring> -v
<substring>: The substring you want to search for in test names.
-v: Verbose mode for detailed output.

pytest -k great -v
 two test case match this 
    test_greater():
    test_greater_equal():

pytest -k less -v
    It will run only tests with the substring less in their names.
    In this case:
    Only test_less matches.

"""