import csv
import sqlite3
import pandas as pd

"""Class ReadCsv which defines the variable csvfile, dialect, contents and header. Also it includes 
the functions readeCsv, getHeader and getContents"""


class ReadCsv:
    def __init__(self):
        self.csvfile = None
        self.dialect = None
        self.contents = None
        self.header = None

    """ the function readCSV is reading a CSV file. Input is the csv file"""

    def readCsv(self, csv_file):
        self.csvfile = open(csv_file)
        self.dialect = csv.Sniffer().sniff(self.csvfile.read())
        self.csvfile.seek(0)  # set on first record
        self.contents = csv.reader(self.csvfile, self.dialect)  # read csv
        self.header = next(self.contents)  # get first row
        self.header = [''.join(e for e in string if e.isalnum()) for string in self.header]

    """the function getHeader returns the header from the reading csv file"""

    def getHeader(self):
        return self.header

    """the function getContents returns the contents from the reading csv file"""

    def getContents(self):
        return self.contents


"""the class DatabaseOperations inherits from the class ReadCsv and extends these by the variable sql and the functions 
dropTable, createTable, insertTable, getQuery and close."""


class DatabaseOperations(ReadCsv):
    def __init__(self, table_name):
        ReadCsv.__init__(self)  # inherit from Database class
        self.sql = None
        self.connection = sqlite3.connect('PythonDB.db')  # connection to database
        self.cursor = self.connection.cursor()  # cursor for database
        self.table_name = table_name

    """the function dropTable deletes a table if it exists."""

    def dropTable(self):
        self.sql = 'DROP TABLE IF EXISTS {0}'.format(self.table_name)  # delete table if exists
        print(self.sql)
        self.cursor.execute(self.sql)

    """the function createTable creates a table if not exists with the columns of the csv file """

    def createTable(self):
        self.sql = 'CREATE TABLE IF NOT EXISTS {0} ('.format(self.table_name)  # create table
        for column in self.header:
            self.sql += column + ', '
        self.sql = self.sql[:-2] + ')'
        print(self.sql)
        self.cursor.execute(self.sql)

    """the function insertTable insert the data from the cvs file into a database table. """

    def insertTable(self):
        self.sql = 'INSERT INTO {0} ('.format(self.table_name)  # insert all rows from csv
        for column in self.header:
            self.sql += column + ', '
        self.sql = self.sql[:-2] + ') VALUES('
        self.sql += '?, ' * len(self.header)
        self.sql = self.sql[:-2] + ')'
        self.cursor.executemany(self.sql, self.contents)
        self.connection.commit()
        self.csvfile.close()

    """the function query returns the rows from the database table as a dataframe """

    def getQuery(self):  # get rows from sql
        self.sql = 'SELECT * FROM {0}'.format(self.table_name)
        query = pd.read_sql(self.sql, self.connection)
        print(query)
        return query

    """the function close is closing the connection to the database"""

    def close(self):
        self.connection.close()


"""the class WriteDataframeIntoDB inherits from the class DatabaseOperations and override the function insertTable
to write the data of a dataframe into a database table"""


class WriteDataframeIntoDB(DatabaseOperations):

    def __init__(self, table_name, df):
        super().__init__(table_name)
        self.header = df.columns.tolist()
        self.contents = df.values
        self.table_name = table_name

    def insertTable(self):
        self.sql = 'INSERT INTO {0} ('.format(self.table_name)  # insert all rows from csv
        for column in self.header:
            self.sql += column + ', '
        self.sql = self.sql[:-2] + ') VALUES('
        self.sql += '?, ' * len(self.header)
        self.sql = self.sql[:-2] + ')'
        self.cursor.executemany(self.sql, self.contents)
        self.connection.commit()
        self.close()



