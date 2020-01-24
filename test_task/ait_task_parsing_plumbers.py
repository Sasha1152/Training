import requests
import json
from bs4 import BeautifulSoup

r = requests.get('https://www.yellowpages.com/austin-tx/plumbers')
soup = BeautifulSoup(r.text, 'html5lib')
companies = soup.body.find('div', {'class': 'search-results organic'}).find_all('div', {'class': 'info'})

# print(soup.prettify())
# print(soup.contents[0])
# print(soup.find('div', {'class': 'phones phone primary'}))
# print(soup.find_all('div', {'class': 'phones phone primary'}))
# print(soup.title)
# print(soup.body)
# print(soup.body)

def get_company_name(com):
    if com.find('a', {'class': 'track-map-it directions'}):
        return com.find('a', {'class': 'business-name'}).text
    else:
        return False


def get_address(com):
    try:
        street = com.find('div', {'class': 'street-address'}).text
    except AttributeError:
        street = ''

    try:
        locality = com.find('div', {'class': 'locality'}).text
    except AttributeError:
        locality = ''

    return street + locality


def get_phone(com):
    try:
        phone = com.find('div', {'class': 'phones phone primary'}).text
    except AttributeError:
        return None
    phone_pure = ''
    for symbol in phone:
        if symbol.isdigit():
            phone_pure += symbol
    return int(phone_pure)


plumbers = {}
for company in companies:
    company_name = get_company_name(company)
    if company_name:
        plumbers[company_name] = {}
        plumbers[company_name]['address'] = get_address(company)
        plumbers[company_name]['phone_number'] = get_phone(company)

plumbers_serialised = json.dumps(plumbers)

with open('plumbing.json', 'w') as plumbers_data_file:
    plumbers_data_file.write(plumbers_serialised)

print('The file "plumbing.json" successfully created!')
