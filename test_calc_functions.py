import calc_functions
import pytest

"""test if the function least_squared works correctly"""


@pytest.mark.parametrize('input1, input2, expected',
                         [(10, 5, 25), (-1, 7, 64), (-5, -4, 1), (10, 5.5, 20.25), (-1.75, 7.9, 93.1225),
                          (1.75, -7.9, 93.1225), (-5.111, -4.45, 0.43692099999999945)])
def test_least_squared(input1, input2, expected):
    assert calc_functions.least_squared(input1, input2) == expected


"""test if the function find_ideal works correctly"""


def test_find_ideal():
    sum_abw = [7, 2, 5, 4, 5, 1, 7, 8, 9]
    min_abw = 1
    result = calc_functions.find_ideal(sum_abw, min_abw)
    assert result[5] == "Yes"
    assert result[1] == "No"
    assert result[4] == "No"
    assert result[0] == "No"
