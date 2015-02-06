# Helper functions
import re
import datetime
import requests

def dubizzle_request(url, headers, params={}):
    resp = requests.get(url, params=params, headers=headers)

    # Retry if there's an ad and use given cookie
    if 'interstitial' in resp.text:
        # Make sure it's really an ad...
        try:
            search_base = re.match(r'^(.+)\?', resp.url).group(1)
            resp = requests.get(search_base, params=params, headers=headers, cookies=resp.cookies)
        except AttributeError:
            pass

    return resp

def parse_date(date):
    months = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12
    }

    day, month, year = re.findall(r'(\d+) (\w+) (\w+)', date)[0]
    return datetime.date(year=int(year), month=months[month], day=int(day))

def scrape(url):
    resp = requests.get(url, headers=headers)
    return resp.text

headers = {
    'User-Agent': 'SkyNet Version 4.4 Revision 12',
    'Description': 'https://github.com/Cyph0n/dubizzle'
}
