from datetime import datetime
from datetime import timedelta
from datetime import date

DEFAULT_FORMAT = "%m/%d/%Y"


def convert_to_str(get_date):
    get_date = get_date.strftime(DEFAULT_FORMAT)
    return get_date


def convert_to_date(date_to_convert):
    date_converted = datetime.strptime(date_to_convert, DEFAULT_FORMAT)
    return date_converted


def convert_to_date_list(start_date, end_date, default_value):
    date_data = [convert_to_str((start_date + timedelta(days=i)))
                 for i in range((end_date - start_date).days + 1)]
    date_data_list = [{'date': date_formatted, 'participants': default_value} for date_formatted in date_data]
    return date_data_list


def get_default_date_data(start_date, end_date, default_value):
    date_data_list = []

    if start_date is None and end_date is None and default_value is None:
        print("Please provide valid data")

    elif start_date is None and end_date is None and default_value == -99999:
        print("Not is not a valid dates")

    elif start_date is None and end_date is None and default_value == '0h 0m':
        start_date = convert_to_date('09/12/2022')
        end_date = convert_to_date('09/15/2022')
        date_data_list = convert_to_date_list(start_date, end_date, default_value)
        return date_data_list

    start_date = convert_to_date(start_date)
    end_date = convert_to_date(end_date)

    if start_date == end_date:
        date_data_list = {'date': convert_to_str(start_date + timedelta(days=0)), 'participants': default_value}

    elif start_date < end_date or start_date < end_date and default_value == -99999:
        date_data_list = convert_to_date_list(start_date, end_date, default_value)

    elif start_date > end_date:
        print("Start date is greater than end date")

    return date_data_list
