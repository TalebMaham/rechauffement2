import pytest 
from logic import add_numbers, multiply_numbers, is_even 
 
def test_add_numbers(): 
    assert add_numbers(2, 3) == 5 
    assert add_numbers(-1, 1) == 0 
    assert add_numbers(0, 0) == 0 
 
def test_multiply_numbers(): 
    assert multiply_numbers(2, 3) == 6 
    assert multiply_numbers(-1, 5) == -5 
    assert multiply_numbers(0, 10) == 0 
 
def test_is_even(): 
    assert is_even(2) is True 
    assert is_even(3) is False 
    assert is_even(0) is True 
