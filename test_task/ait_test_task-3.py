import json
import pytz
import requests
from datetime import datetime


"""
The JSON string contains the next data structure (US/Eastern local time):
json_str = '{"dt": ["2019-03-28 13:27", "2019-05-15 23:14", "2020-01-15 12:29"]}'
Task: you need to build the Python list of dates/times as UTC Timezone
and POST it as 'VALS' paramether to http://some_example.com/controller/get_data
"""

def send_datetime_list(json_est_time, url):
    data = json.loads(json_est_time)
    date_format = '%Y-%m-%d %H:%M'
    est_timezone = pytz.timezone('US/Eastern')
    est_time_list = [est_timezone.localize(datetime.strptime(est_date, date_format)) for est_date in data['dt']]
    utc_time_list = [date_obj.astimezone(pytz.utc).strftime(date_format) for date_obj in est_time_list]
    payload = json.dumps({'VALS': utc_time_list})

    try:
        requests.post(url, payload)
    except requests.exceptions.ConnectionError:
        print("Resource server IP address could not be found")
    else:
        print('Data was sent successfully')



if __name__ == '__main__':
    json_str = '{"dt": ["2019-03-28 13:27", "2019-05-15 23:14", "2020-01-15 12:29"]}'
    resource = 'http://some_example.com/controller/get_data'
    send_datetime_list(json_str, resource)
