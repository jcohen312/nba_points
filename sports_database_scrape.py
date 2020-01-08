from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
import pandas as pd

url = 'https://sportsdatabase.com/nba/query?output=default&sdql=date%2C+team%2C+site%2C+o%3Ateam%2C+line%2C+total+%40season%3D2018&submit=++S+D+Q+L+%21++'

req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

page_soup = BeautifulSoup(webpage, "html.parser")

headers = page_soup.find_all('th')
headers[1].get_text()

insert_dict = {}
for item in headers[1:]:
    insert_dict[item.get_text(strip=True)] = []

len(insert_dict)

data = page_soup.find_all('td')[6:-2]

zipped = list(zip(data[::6], data[1::6], data[2::6], data[3::6], data[4::6], data[5::6]))
zipped[0][0].get_text()

insert_dict['date'].append(zipped[0][0].get_text())
insert_dict['date']
insert_dict['date'] = []
insert_dict['date']
headers[1:]

for row in zipped[1:]:
    insert_dict['date'].append(row[0].get_text(strip=True))
    insert_dict['team'].append(row[1].get_text(strip=True))
    insert_dict['site'].append(row[2].get_text(strip=True))
    insert_dict['o:team'].append(row[3].get_text(strip=True))
    insert_dict['line'].append(row[4].get_text(strip=True))
    insert_dict['total'].append(row[5].get_text(strip=True))

pd.DataFrame(insert_dict)


def pull_nba_lines(season):
### Function to pull over/under and pointspread from NBA games by season from sportsdatabase.com
    url = 'https://sportsdatabase.com/nba/query?output=default&sdql=date%2C+team%2C+site%2C+o%3Ateam%2C+line%2C+total+%40season%3D{}&submit=++S+D+Q+L+%21++'.format(season)
### Must request the html using the masked header below because the site protects itself against calls from sources other than web browsers
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    webpage = urlopen(req).read()

    page_soup = BeautifulSoup(webpage, "html.parser")
### Find headers for columns and data in the table of the webpage
    headers = page_soup.find_all('th')
    data = page_soup.find_all('td')[6:-2]
### Create a dictionary with the headers as keys
    insert_dict = {}
    for item in headers[1:]:
        insert_dict[item.get_text(strip=True)] = []
### Create tuples of each row of data from the table for upload into the dictionary
    zipped = list(zip(data[::6], data[1::6], data[2::6], data[3::6], data[4::6], data[5::6]))
### For each tuple, insert each datapoint into the dictionary under its proper header
    for row in zipped:
        insert_dict['date'].append(row[0].get_text(strip=True))
        insert_dict['team'].append(row[1].get_text(strip=True))
        insert_dict['site'].append(row[2].get_text(strip=True))
        insert_dict['o:team'].append(row[3].get_text(strip=True))
        insert_dict['line'].append(row[4].get_text(strip=True))
        insert_dict['total'].append(row[5].get_text(strip=True))
### Generate a dataframe from the dictionary
    return pd.DataFrame(insert_dict)


pull_nba_lines('2018')
lines =[]
for year in ['2017', '2018', '2019']:
    lines.append(pull_nba_lines(year))

lines[1]
all_lines = pd.concat(lines)
all_lines.reset_index(drop=True, inplace=True)
all_lines.to_csv('vegas_info.csv')
