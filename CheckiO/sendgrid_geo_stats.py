import json
import sendgrid

API_KEY = ''  # https://app.sendgrid.com
sg = sendgrid.SendGridAPIClient(API_KEY)


def best_country(str_date):
    response = sg.client.geo.stats.get(query_params={
        'start_date': str_date,
        'end_date': str_date
    })

    data = json.loads(response.body)
    max_data = max(data[0]['stats'], key=lambda a: a['metrics']['unique_clicks'])
    return max_data['name']


print('Your best country in 2016-01-01 was ' + best_country('2016-01-01'))
