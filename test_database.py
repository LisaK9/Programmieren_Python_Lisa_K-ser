import database
import pytest


def test_readCsv():
    csv = database.ReadCsv()
    csv.readCsv('test.csv')
    assert csv.getHeader() == ['x', 'y']
