# Helper functions

import re
import datetime


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

    day, month, year = re.findall(r'(\d+)\w+ (\w+) (\w+)', date)[0]
    return datetime.date(year=int(year), month=months[month], day=int(day))