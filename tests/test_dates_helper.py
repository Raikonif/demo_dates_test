from src.Assignment7_1 import get_dates_in_interval
from src.Assignment7_2 import get_default_date_data
import unittest


class TestDates(unittest.TestCase):
    # Assignments 7.1
    def test_one_date(self):
        start_date = '09/12/2022'
        end_date = '09/12/2022'

        dates = get_dates_in_interval(start_date, end_date)
        self.assertEqual('09/12/2022', dates)

    def test_between_two_dates(self):
        start_date = '9/12/2022'
        end_date = '9/15/2022'

        dates = get_dates_in_interval(start_date, end_date)
        self.assertEqual(['09/12/2022', '09/13/2022', '09/14/2022', '09/15/2022'], dates)

    def test_between_two_dates_start_bigger_than_end(self):
        start_date = '9/15/2022'
        end_date = '9/10/2022'

        dates = get_dates_in_interval(start_date, end_date)
        self.assertEqual(None, dates)

    def test_between_two_dates_none(self):
        start_date = None
        end_date = None

        dates = get_dates_in_interval(start_date, end_date)
        self.assertEqual(None, dates)

    # Assignments 7.2
    def test_start_date_and_end_date_equals_default_value_negative_number(self):
        start_date = '09/12/2022'
        end_date = '09/12/2022'
        default_value = -99999

        dates = get_default_date_data(start_date, end_date, default_value)
        self.assertEqual({'date': '09/12/2022', 'participants': -99999}, dates)

    def test_start_date_small_than_end_date_default_value_none(self):
        start_date = '09/12/2022'
        end_date = '09/15/2022'
        default_value = None

        dates = get_default_date_data(start_date, end_date, default_value)
        self.assertEqual(
            [{'date': '09/12/2022', 'participants': None},
             {'date': '09/13/2022', 'participants': None},
             {'date': '09/14/2022', 'participants': None},
             {'date': '09/15/2022', 'participants': None}],
            dates
        )

    def test_start_date_bigger_than_end_date_default_value_negative_nine(self):
        start_date = '09/15/2022'
        end_date = '09/12/2022'
        default_value = -99999

        dates = get_default_date_data(start_date, end_date, default_value)
        self.assertEqual(0, len(dates))

    def test_start_date_and_end_date_none_defaut_value_zerohours(self):
        start_date = None
        end_date = None
        default_value = '0h 0m'

        dates = get_default_date_data(start_date, end_date, default_value)
        self.assertEqual(
            [{'date': '09/12/2022', 'participants': '0h 0m'},
             {'date': '09/13/2022', 'participants': '0h 0m'},
             {'date': '09/14/2022', 'participants': '0h 0m'},
             {'date': '09/15/2022', 'participants': '0h 0m'}],
            dates
        )

    def test_start_date_small_than_end_date_default_value_negative_nine(self):
        start_date = '09/12/2022'
        end_date = '09/15/2022'
        default_value = -99999

        dates = get_default_date_data(start_date, end_date, default_value)
        self.assertEqual(
            [{'date': '09/12/2022', 'participants': -99999},
             {'date': '09/13/2022', 'participants': -99999},
             {'date': '09/14/2022', 'participants': -99999},
             {'date': '09/15/2022', 'participants': -99999}],
            dates
        )
