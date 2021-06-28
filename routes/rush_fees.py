
from flask import request
import time
import traceback
from datetime import datetime
from utility import date_utils

RUSH_DELAY = 3 ## Delay of 3 days, it can be configured for more/less days

def __calculate_rush_due_date(ts):
    day_of_week = date_utils.day_of_week(ts)

    if day_of_week < 2:
        return ts+(RUSH_DELAY*86400)

    elif 2 <= day_of_week <= 5:
        return ts+((RUSH_DELAY+2)*86400)

    return ts+((RUSH_DELAY+1)*86400)


def ___is_rushed(curr_time, due_date):

    curr_hour = date_utils.get_curr_hour(curr_time)
    if curr_hour >= 17:  # EDT 5:00 PM is 9:00 PM UTC
        curr_time = date_utils.get_end_of_day(curr_time)
    else:
        curr_time = date_utils.get_beginning_of_day(curr_time)

    rush_due_date = __calculate_rush_due_date(curr_time)

    due_date = date_utils.utc_converter(due_date)

    return due_date < rush_due_date


def __validate_date_string(due_date, curr_time):

    SATURAY_IDX = 5
    SUNDAY_IDX = 6

    try:
        due_date = date_utils.date_to_dateobj(due_date)
        utc_due_date = date_utils.utc_converter(due_date)
        utc_curr_time = date_utils.utc_converter(curr_time)

        if utc_due_date < utc_curr_time:
            return False, "Please select future due date"

        if due_date.weekday() in (SATURAY_IDX, SUNDAY_IDX):
            return False, "Due date has to be weekday"
        return True, "Success"
    except:
        traceback.print_exc()
        return False, "Invalid date - Please add date in YYYY-MM-DD"


def is_rushed_api():
    due_date = request.args.get('due')
    curr_time = date_utils.get_current_time()

    isValid, msg = __validate_date_string(due_date, curr_time)
    if not isValid:
        return {"error": msg}, 400

    due_date = date_utils.date_to_dateobj(due_date)
    return {"isRushed": ___is_rushed(curr_time, due_date)}
