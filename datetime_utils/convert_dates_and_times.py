import datetime
from datetime import timezone

def datetime_to_timestamp(dt):
    """Converts a datetime object to a timestamp."""
    return int(dt.replace(tzinfo=datetime.timezone.utc).timestamp())

def timestamp_to_datetime(timestamp):
    """Converts a timestamp to a datetime object."""
    return datetime.datetime.utcfromtimestamp(timestamp)

def datetime_to_datestr(dt, format='%Y-%m-%d'):
    """Converts a datetime object to a string."""
    return dt.strftime(format)

def datestr_to_datetime(string, format='%Y-%m-%d'):
    """Converts a string to a datetime object."""
    return datetime.datetime.strptime(string, format)

def datetime_to_datetimestr(dt, format='%Y-%m-%d %H:%M:%S'):
    """Converts a datetime object to a string."""
    return dt.strftime(format)
