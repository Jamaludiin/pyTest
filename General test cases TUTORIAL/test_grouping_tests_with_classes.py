
# pytest test_grouping_tests_with_classes.py
class TestMathOperations:
    def test_addition(self):
        assert 2 + 2 == 4

    def test_subtraction(self):
        assert 5 - 3 == 2

    def test_multipilication(self):
        assert 5 * 5 == 25 
 


class TestStringOperation:
   
    def test_capital(self):
        a = "jamal"
        print(a.capitalize())  # Call the method using ()
        assert a.capitalize() == "Jamal"  # Correct expected output

    def test_upercase(self):
        a = "Jamal"
        print(a.upper())  # Use upper() for all uppercase letters
        assert a.upper() == "JAMAL"


    def test_one_letter(self):
        a = "Jamal"
        assert a[0] == "J"

    def test_last_char(self):
        a = "Jamal"
        assert a[-1] == "l" 