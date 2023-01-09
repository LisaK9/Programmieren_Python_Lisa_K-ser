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


""" Function drop_columns drops the columns ideal_function and Sum Abw from the dataframe  """


def drop_columns(df):
    df = df.drop(columns='ideal_function')  # drop column ideal_function
    df = df.drop(columns='Sum Abw')  # drop column Sum Abw
    return df


"""Function get_function takes as input a dataframe and returns the column name in place one, which ist the name
of the ideal function"""


def get_function(df):
    column_name = df.columns.tolist()
    return column_name[1]
