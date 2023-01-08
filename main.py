import database

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
