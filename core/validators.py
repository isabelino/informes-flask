import datetime


def normalize_date(date: str | datetime.date | datetime.datetime) -> datetime.date:
    if isinstance(date, datetime.date):
        return date
    elif isinstance(date, datetime.datetime):
        return date.date()
    elif isinstance(date, str):
        # detect dd-mm-yyyy, transform to yyyy-mm-dd

        return datetime.strptime(date, '%Y-%m-%d').date()
    else:
        raise ValueError
