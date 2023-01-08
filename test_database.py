import database
import pytest

"""test if readCsv works correctly"""


def test_readCsv():
    csv = database.ReadCsv()
    csv.readCsv('test.csv')
    assert csv.getHeader() == ['x', 'y']


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
