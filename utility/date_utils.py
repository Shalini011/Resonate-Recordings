from datetime import timezone, datetime, timedelta, time
import datetime
from pytz import timezone

est = timezone('EST')

def get_curr_hour(ts):
    return int(str(ts.hour))

def get_end_of_day(ts):
    ts = get_beginning_of_day(ts)
    return ts+86400
    

def get_beginning_of_day(ts):
    today_beginning = datetime.datetime.combine(ts, time(), est)
    return utc_converter(today_beginning)
    

def utc_converter(dt):
    utc_time = dt.replace(tzinfo=est)
    utc_timestamp = utc_time.timestamp()
    return utc_timestamp


def date_to_dateobj(date_string):
    return datetime.datetime.fromisoformat(date_string)

def get_current_time():
    return datetime.datetime.now(est)

def day_of_week(dt):
    dt = int(dt)
    x = datetime.datetime.fromtimestamp(dt, est)
    return x.weekday()
    