import database
import pytest


"""test if Exception handling for train and ideal works correctly"""


@pytest.mark.parametrize('files',
                         ['test.csv', 'ideal.csv', 'train.csv', 'test_.csv', 'example.csv'])
def test_readCsv(files):
    csv = database.DatabaseOperations('table_name')
    try:
        csv.readCsv(files)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print('Error: ', e)
    else:
        print(csv.getHeader())


@pytest.mark.parametrize('csv, expected',
                         [('test.csv', ['x', 'y']), ('train.csv', ['x', 'y1', 'y2', 'y3', 'y4'])])
def test_getHeader(csv, expected):
    file = database.ReadCsv()
    file.readCsv(csv)
    assert file.getHeader() == expected

