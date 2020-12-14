from bs4 import BeautifulSoup
import requests

corona_source = requests.get('https://www.worldometers.info/coronavirus/country/india/').text
soup = BeautifulSoup(corona_source,'lxml')
new_cases = soup.find('li', class_ = 'news_li').strong.text
new_deaths =list(soup.find('li', class_ = 'news_li').strong.next_siblings)[1].text

print('\nCorona virus update for India\n')
print('new cases: {}\nnew deaths: {}'.format(new_cases.split()[0],new_deaths.split()[0]))