import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   num = 7
   assert 7*7 == 49

def tesequality():
   assert 10 == 11

   """ 
   The test tesequality() will actually fail, not pass, because 10 is not equal to 11. 
   However, there's a typo in your test function name that might cause it to be skipped 
   by pytest. 
   
   Here's why:
   pytest looks for test functions that start with test_ or end with _test 
   """