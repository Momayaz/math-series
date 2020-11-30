from math_series import __version__
from math_series.series import nums
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_version():
    actual = __version__
    expected = '0.1.0'
    assert actual == expected

def test_onen():
    actual = nums(1)
    expected = 0
    assert actual == expected

def test_multiply():
    actual = nums(5)
    expected = 40
    assert actual == expected


"""
Task Case:
-when user input 4 in fibonnacci function the result should be 3
-when user input 5 in lucas function the result should be 11

                
"""



def test_four():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


def test_five():
    actual = lucas(5)
    expected = 11
    assert actual == expected


def test_sum_fib():
    actual = sum_series(4,0,1)
    expected = 3
    assert actual == expected

def test_sum_luc():
    actual = sum_series(5,2,1)
    expected = 11
    assert actual == expected