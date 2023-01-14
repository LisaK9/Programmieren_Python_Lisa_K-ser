import database
import pytest


"""test if Exception handling for train and ideal works correctly"""


@pytest.mark.parametrize('files, expected',
                         [('test.csv', "['x', 'y']\n"), ('example.csv',
                                                         "[Errno 2] No such file or directory: 'example.csv'\n")])
def test_readCsv(capsys, files, expected):
    csv = database.DatabaseOperations('table_name')
    try:
        csv.readCsv(files)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print('Error: ', e)
    else:
        print(csv.getHeader())
    captures = capsys.readouterr()
    assert captures.out == expected



@pytest.mark.parametrize('csv, expected',
                         [('test.csv', ['x', 'y']), ('train.csv', ['x', 'y1', 'y2', 'y3', 'y4'])])
def test_getHeader(csv, expected):
    file = database.ReadCsv()
    file.readCsv(csv)
    assert file.getHeader() == expected

