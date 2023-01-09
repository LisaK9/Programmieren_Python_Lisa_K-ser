import database
import plot
import calc_functions
import pandas as pd
import numpy as np

# Read train.csv and ideal.csv, create table and write data into DB

# create new object and instance of class DatabaseOperations with table name train
data_train = database.DatabaseOperations('TRAIN')
# create new object and instance of class DatabaseOperations with table name ideal
data_ideal = database.DatabaseOperations('IDEAL')

# Exception Handling, try to open the csv file. If FileNotFoundError print this Error. For other Errors print Error.
# Else print Header of csv file and drop table, create table and insert the data into the table
try:
    data_train.readCsv('train.csv')  # open csv file
except FileNotFoundError as e:
    print("File not found: ", e)
except Exception as e:
    print('Error: ', e)
else:
    print("Header of CSV file: ", data_train.getHeader())  # get header of csv file
    data_train.dropTable()  # drop table train
    data_train.createTable()  # create table train
    data_train.insertTable()  # insert data into table train
    data_train = data_train.getQuery()  # return sql data from table train as a dataframe

# Read ideal csv, create table and write data into DB

try:
    data_ideal.readCsv('ideal.csv')  # open csv file
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error: ', e)
else:
    print("Header of CSV file: ", data_ideal.getHeader())  # get header of csv file
    data_ideal.dropTable()  # drop table ideal
    data_ideal.createTable()  # create table ideal
    data_ideal.insertTable()  # insert data into table ideal
    data_ideal = data_ideal.getQuery()  # return sql data from table train as dataframe

# for each training function create a dataframe with x- and y values
y1_data = data_train.filter(items=['x', 'y1'])
y2_data = data_train.filter(items=['x', 'y2'])
y3_data = data_train.filter(items=['x', 'y3'])
y4_data = data_train.filter(items=['x', 'y4'])
x_data = y1_data['x']

# plot trainings functions
plot.train_functions(y1_data['x'], y1_data['y1'], y2_data['y2'], y3_data['y3'], y4_data['y4'])

# drop x values from ideal functions
ideal_y = data_ideal.drop(columns='x')
ideal_y = ideal_y.T  # transpose data ideal

# find ideal function of training function 1:
abw = calc_functions.least_squared(y1_data['y1'], ideal_y)  # calculate least square of training function1
abw_t = abw.T  # transpose deviation
sum_abw = abw_t.sum()  # calculate sum of deviation
min_abw = sum_abw.min()  # calculate minimal sum

result = calc_functions.find_ideal(sum_abw, min_abw)  # find ideal function for training function 1
new_y1 = pd.DataFrame(abw)  # create new dataframe from the calculated deviations
new_y1['Sum Abw'] = sum_abw.tolist()  # add sum of deviation to dataframe
new_y1['ideal_function'] = result  # add result yes or no as column to the dataframe
new_y1 = new_y1.loc[(new_y1['ideal_function'] == "Yes")]  # filter by the ideal function (value equals yes)
new_y1 = calc_functions.drop_columns(new_y1)  # drop column ideal_function and Sum Abw
new_y1 = new_y1.T  # transpose dataframe to origin
new_y1 = y1_data.join(new_y1)  # join the two dataframes to get x-, y-train and y-abw of the ideal function
new_y1.set_index('x', inplace=True)  # set column x as index
print("function 1: ", new_y1)  # print dataframe of function 1

# find ideal function of training function 2:
abw = calc_functions.least_squared(y2_data['y2'], ideal_y)  # calculate least square of training function2
abw_t = abw.T  # transpose deviation
sum_abw = abw_t.sum()  # calculate sum of deviation
min_abw = sum_abw.min()  # calculate minimal sum
result = calc_functions.find_ideal(sum_abw, min_abw)  # find ideal function for training function 2
new_y2 = pd.DataFrame(abw)  # create new dataframe from the calculated deviations
new_y2['Sum Abw'] = sum_abw.tolist()  # add sum of deviation to dataframe
new_y2['ideal_function'] = result  # add result yes or no as column to the dataframe
new_y2 = new_y2.loc[(new_y2['ideal_function'] == "Yes")]  # filter by the ideal function (value equals yes)
new_y2 = calc_functions.drop_columns(new_y2)
new_y2 = new_y2.T  # transpose dataframe to origin
new_y2 = y2_data.join(new_y2)  # join the two dataframes to get x-, y-train and y-abw of the ideal function
new_y2.set_index('x', inplace=True)  # set column x as index
print("function 2: ", new_y2)  # print dataframe of function 2

# find ideal function of training function 3:
abw = calc_functions.least_squared(y3_data['y3'], ideal_y)  # calculate least square of training function3
abw_t = abw.T  # transpose deviation
sum_abw = abw_t.sum()  # calculate sum of deviation
min_abw = sum_abw.min()  # calculate minimal sum
result = calc_functions.find_ideal(sum_abw, min_abw)  # find ideal function for training function 3
new_y3 = pd.DataFrame(abw)  # create new dataframe from the calculated deviations
new_y3['Sum Abw'] = sum_abw.tolist()  # add sum of deviation to dataframe
new_y3['ideal_function'] = result  # add result yes or no as column to the dataframe
new_y3 = new_y3.loc[(new_y3['ideal_function'] == "Yes")]  # filter by the ideal function (value equals yes)
new_y3 = calc_functions.drop_columns(new_y3)
new_y3 = new_y3.T  # transpose dataframe to origin
new_y3 = y3_data.join(new_y3)  # join the two dataframes to get x-, y-train and y-abw of the ideal function
new_y3.set_index('x', inplace=True)  # set column x as index
print("function 3: ", new_y3)  # print dataframe of function 3

# find ideal function of training function 4:
abw = calc_functions.least_squared(y4_data['y4'], ideal_y)  # calculate least square of training function4
abw_t = abw.T  # transpose deviation
sum_abw = abw_t.sum()  # calculate sum of deviation
min_abw = sum_abw.min()  # calculate minimal sum
result = calc_functions.find_ideal(sum_abw, min_abw)  # find ideal function for training function 4
new_y4 = pd.DataFrame(abw)  # create new dataframe from the calculated deviations
new_y4['Sum Abw'] = sum_abw.tolist()  # add sum of deviation to dataframe
new_y4['ideal_function'] = result  # add result yes or no as column to the dataframe
new_y4 = new_y4.loc[(new_y4['ideal_function'] == "Yes")]  # filter by the ideal function (value equals yes)
new_y4 = calc_functions.drop_columns(new_y4)
new_y4 = new_y4.T  # transpose dataframe to origin
new_y4 = y4_data.join(new_y4)  # join the two dataframes to get x-, y-train and y-abw of the ideal function
new_y4.set_index('x', inplace=True)  # set column x as index
print("function 4: ", new_y4)  # print dataframe of function 4

# read test data from csv as dataframe:
data_test = pd.read_csv('test.csv')  # import data from test.csv as dataframe
data_test.set_index('x', inplace=True)  # set column x as index
print("Data of test.csv: ", data_test)  # print test_data


"""Compare train function 1 with test data"""
column_name = calc_functions.get_function(new_y1)  # get column name of ideal function 1
abw_train_max = np.max(new_y1[column_name])  # get max deviate from training data
ideal = data_ideal.filter(items=['x', column_name])  # filtering data_ideal to the ideal function
ideal['abw_train'] = new_y1[column_name].tolist()  # add abw_train to the dataframe ideal
ideal.set_index('x', inplace=True)  # set column x as index
data_function1 = data_test.join(ideal)  # join the test data with die data of the ideal function
print(data_function1)
abw_test = calc_functions.least_squared(data_function1['y'], data_function1[
    column_name])  # calculate least square between y_test and y_ideal
abw_train = data_function1['abw_train']  # get deviate from training data
abw_test_train = abw_test - abw_train  # calculate deviate between test and train deviate
