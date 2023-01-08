import csv


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