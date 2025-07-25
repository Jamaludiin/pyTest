# test_inc.py
# Where tests are written


# this should get the testinputs from generate_input_value2
#from generate_input_value2 import get_pass_input, get_fail_input

# pytest test_inc.py
import pytest
#from targets.inc import inc, dec

from inc import inc, dec, add, sub, mul, div, mod, pow, sqrt, log, exp, sin, cos, tan, cot, log10, log2, factorial, fibonacci, is_even, is_odd, is_prime, is_palindrome


def test_inc_functionality():
    assert inc(4) == 5


def test_inc_none_input_fails():
    assert inc(None) == 2


def test_dec_positive():
    assert dec(4) == 3


def test_dec_negative():
    assert dec(1) == 3


def test_add_function_with_positive_input():
    assert add(4, 5) == 9
    assert add(4, 0) == 4
    assert add(4, -1) == 3


def test_add_function_fails_with_correct_result():
    assert add(4, 5) != 9


def test_sub_with_positive_numbers():
    assert sub(4, 2) == 2
    assert sub(4, 0) == 4
    assert sub(4, -2) == 6


def test_sub_negative():
    assert sub(4, 2) == 7


def test_mul_positive():
    assert mul(4, 0) == 0
    assert mul(4, 1) == 4
    assert mul(4, 2) == 8
    assert mul(4, 3) == 12
    assert mul(4, 4) == 16


def test_mul_returns_incorrect_result():
    assert mul(4, 2) == 11


def test_div_positive():
    assert div(4, 2) == 2
    assert div(4, 1) == 4
    assert div(4, 4) == 1


#test_div_zero_division_error
def test_div_zero_division_error():
    assert div(0, 0) == 1


def test_mod_function_with_positive_input():
    assert mod(4, 2) == 0
    assert mod(4, 3) == 1
    assert mod(4, 4) == 0
    assert mod(4, 5) == 4


def test_mod_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        mod(0, 0)


def test_pow_with_positive_base_and_exponent():
    assert pow(2, 2) == 4
    assert pow(2, 3) == 8
    assert pow(2, 4) == 16

def test_pow_with_positive_base_and_zero_exponent():
    assert pow(2, 0) == 1

def test_pow_with_positive_base_and_negative_exponent():
    assert pow(2, -1) == 0.5
    assert pow(2, -2) == 0.25
    assert pow(2, -3) == 0.125


def test_pow_zero_base_fails_with_nonzero_result():
    assert pow(0, 2) == 1


def test_sqrt_positive_value():
    assert sqrt(4) == 2.0


def test_sqrt_negative_input_fails():
    with pytest.raises(ValueError):
        sqrt(-4)


def test_log_positive_input():
    import math
    assert round(log(4), 4) == round(math.log(4), 4)


def test_log_negative_input_zero():
    import math
    try:
        log(0)
        assert False, "Expected ValueError to be raised"
    except ValueError as e:
        assert str(e) != "math domain error"


def test_exp_zero():
    import math
    assert round(math.exp(0), 10) == round(exp(0), 10)


def test_exp_overflow():
    import math
    assert math.exp(1000) == 0


def test_sin_zero():
    assert round(sin(0), 10) == 0


def test_sin_function_returns_incorrect_value():
    import math
    assert math.sin(4) == 0


def test_cos_zero():
    import math
    assert math.cos(0) == cos(0)
    assert round(cos(0), 10) == 1.0


def test_cos_function_returns_incorrect_value():
    import math
    assert math.cos(4) == 2


def test_tan_zero():
    import math
    assert math.tan(0) == 0.0


def test_tan_returns_incorrect_value():
    import math
    assert math.tan(4) == 0


def test_cot_function_with_positive_value():
    import math
    assert round(1 / math.tan(4), 4) == round(cot(4), 4)


def test_cot_at_zero_division_error():
    import math
    try:
        assert cot(0) == 1 / math.tan(0)
    except ZeroDivisionError:
        assert False


def test_log10_positive_value():
    import math
    assert round(log10(10000), 2) == round(math.log10(10000), 2)


def test_log10_negative_value_zero():
    import math
    assert math.log10(0) == 0


def test_log2_positive_value():
    import math
    assert log2(4) == 2


def test_log2_zero_input_fails():
    import math
    try:
        log2(0)
        assert False
    except ValueError:
        assert True


def test_factorial_positive_input():
    import math
    assert factorial(4) == math.factorial(4)


def test_factorial_negative_input_fails():
    import math
    try:
        math.factorial(-4)
        assert False
    except ValueError:
        assert True


def test_fibonacci_with_positive_integer():
    assert fibonacci(4) == 3


def test_fibonacci_incorrect_result():
    assert fibonacci(4) != 3


def test_is_even_returns_true_for_even_number():
    assert is_even(4) == True


def test_is_even_returns_true_for_odd_number():
    assert is_even(3) == True


def test_is_odd_positive_number():
    assert is_odd(3) == True


def test_is_odd_returns_true_for_even_number():
    assert is_odd(4) == True


def test_is_prime_returns_true_for_prime_number_two():
    assert is_prime(2) == True


def test_is_prime_returns_true_for_composite_number():
    assert is_prime(4) == True


def test_is_palindrome_with_single_digit_number():
    assert is_palindrome(4) == True


def test_is_palindrome_returns_false_for_non_palindrome():
    assert is_palindrome(4) == True


def test_is_even_returns_true_for_even_number():
    assert is_even(4) == True


def test_is_even_fails_with_odd_number():
    assert is_even(3) == True


def test_is_odd_returns_true_for_odd_number():
    assert is_odd(1) == True


def test_is_odd_returns_true_for_even_number():
    assert is_odd(4) == True


def test_is_prime_returns_false_for_composite_numbers():
    assert is_prime(4) == False


def test_is_prime_returns_true_for_composite_number():
    assert is_prime(4) == True


# 54 tests
