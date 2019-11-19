import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.yellowpages.com/austin-tx/plumbers')

# with open('plumbers.html', 'wb') as output_file:
#     output_file.write(r.text.encode('utf-8'))

soup = BeautifulSoup(r.text, 'html5lib')


# print(soup.prettify())
# print(soup.contents[0])
# print(soup.find('div', {'class': 'phones phone primary'}))
# print(soup.find_all('div', {'class': 'phones phone primary'}))
# print(soup.title)
# print(soup.body)
# print(soup.body)
