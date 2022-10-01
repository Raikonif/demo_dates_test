from datetime import datetime
from datetime import timedelta

# import numpy as np
DATE_FORMAT = "%d/%m/%Y"
DEFAULT_FORMAT = "%m/%d/%Y"


def convert_to_str(date):
    print(type(date.strftime(DEFAULT_FORMAT)))
    return date.strftime(DEFAULT_FORMAT)


def get_dates_in_interval(start_date, end_date):
    # Convert to datetime
    print(start_date, end_date)

    if start_date is None or end_date is None:
        return None
    elif start_date > end_date:
        return None

    start_date = datetime.strptime(start_date, DEFAULT_FORMAT)
    end_date = datetime.strptime(end_date, DEFAULT_FORMAT)
    print(start_date, end_date)

    # Generate a list of dates
    date_list = []
    if start_date < end_date:
        date_list = [convert_to_str((start_date + timedelta(days=i)))
                     for i in range((end_date - start_date).days + 1)]
    else:
        date_list = start_date.strftime(DEFAULT_FORMAT)

    print(date_list)
    return date_list


# if __name__ == "__main__":
#     start_date = '9/12/2022'
#     end_date = '9/12/2022'
#     get_dates_in_interval(start_date, end_date)
