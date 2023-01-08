

""" Function to calculate the least squared y deviation.
  Input: y, y_ideal
  Output: least squared y deviation"""


def least_squared(y, y_ideal):
    return (y - y_ideal) ** 2


""" Function for finding the ideal function, which has the minimal sum
     Input: sum deviation, min deviation
     Output: list with yes if value is equal to min deviation, else no  """


def find_ideal(sum_abw, min_abw):
    result = []
    for value in sum_abw:
        if value == min_abw:
            result.append("Yes")
        else:
            result.append("No")
    return result
