import unittest

from core.validators import normalize_date


class TestNormalizeDate(unittest.TestCase):

    def test_normalize_date(self):
        assert normalize_date('2023-01-01') == datetime.date(2023, 1, 1)
        assert normalize_date(datetime.date(2023, 1, 1)) == datetime.date(2023, 1, 1)
        assert normalize_date(datetime.datetime(2023, 1, 1)) == datetime.date(2023, 1, 1)
