import calc_functions
import pytest

"""test if the function least_squared works correctly"""


@pytest.mark.parametrize('input1, input2, expected',
                         [(10, 5, 25), (-1, 7, 64), (-5, -4, 1), (10, 5.5, 20.25), (-1.75, 7.9, 93.1225),
                          (1.75, -7.9, 93.1225), (-5.111, -4.45, 0.43692099999999945)])
def test_least_squared(input1, input2, expected):
    assert calc_functions.least_squared(input1, input2) == expected
