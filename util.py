from datetime import datetime, timedelta

def convert_datetime_to_millisec(self, date_time):
    return (date_time - datetime(1970, 1, 1)) // timedelta(milliseconds=1)

def generate_millisec_range_of_one_day(self, date_str):
    utc_time_day_start = convert_datetime_to_millisec(self,
        datetime(date_str[:4], date_str[5:7], date_str[8:10], 0, 0))
    utc_time_day_end = convert_datetime_to_millisec(self,
        datetime(date_str[:4], date_str[5:7], date_str[8:10], 23, 59, 59))
    return [utc_time_day_start, utc_time_day_end]