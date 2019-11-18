import datetime
import json
import sendgrid

API_KEY = ''  # https://app.sendgrid.com

sg = sendgrid.SendGridAPIClient(API_KEY)

def how_spammed(str_date):
    start_time = datetime.datetime.strptime(str_date, '%Y-%m-%d')
    end_time = start_time + datetime.timedelta(days=1)


    response = sg.client.suppression.spam_reports.get(query_params={
    'start_time': int(start_time.timestamp()),
    'end_time':int(end_time.timestamp())
    })

    data = json.loads(response.body)

    return len(data)


print('You had {} spam reports in 2016-01-01'.format(how_spammed('2016-01-01')))
