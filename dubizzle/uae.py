# Set of classes for interfacing with Dubizzle UAE
import re
import math
import multiprocessing
from time import time
from .helpers import parse_date, scrape, headers, dubizzle_request
from .regions import uae
from bs4 import BeautifulSoup

class SearchException(BaseException):
    pass

class Search(object):
    """
    Simple class that organizes search parameters into a dictionary and allows for a search request to be made.
    Works only with Dubizzle UAE.

    Arguments:

        A keyword (string) and any number of kwargs. Details of possible arguments are provided in the docs or in
        `regions.py`.

    Returns:

        A `Results` object.

    """
    def __init__(self, **kwargs):
        # General parameters
        keyword = kwargs.get('keyword', '')
        city = kwargs.get('city', 'all')
        section = kwargs.get('section', 'all')
        category = kwargs.get('category', 'all')
        min_price = kwargs.get('min_price', '')
        max_price = kwargs.get('max_price', '')
        added_days = kwargs.get('added_days', 30)

        # Motors only
        make = kwargs.get('make', 'all')
        min_year = kwargs.get('min_year', '')
        max_year = kwargs.get('max_year', '')
        min_kms = kwargs.get('min_kms', '')
        max_kms = kwargs.get('max_kms', '')
        seller = kwargs.get('seller', 'all')
        fuel = kwargs.get('fuel', 'all')
        cylinders = kwargs.get('cylinders', 'all')
        transmission = kwargs.get('transmission', 'all')

        self.params = {
            uae['cities']['code']: uae['cities']['options'][city],
            uae['sections']['code']: uae['sections']['options'][section],
            uae['categories']['code']: uae['categories']['options'][category],
            uae['makes']['code']: uae['makes']['options'][make],
            'keywords': keyword,
            'price__gte': min_price,
            'price__lte': max_price,
            'added__gte': added_days,
            'year__gte': min_year,
            'year__lte': max_year,
            'kilometers__gte': min_kms,
            'kilometers__lte': max_kms,
            'seller_type': uae['motors_options']['seller'][seller],
            'fuel_type': uae['motors_options']['fuel'][fuel],
            'no._of_cylinders': uae['motors_options']['cylinders'][cylinders],
            'transmission_type': uae['motors_options']['transmission'][transmission]
        }

        self.num_results = kwargs.get('num_results', 50)
        self.detailed = kwargs.get('detailed', False)

    def search(self):
        """Returns a Results object."""
        resp = dubizzle_request(uae['base_url'], headers, self.params)

        return Results(resp.text, self.num_results, resp.url, self.detailed)

class Results(object):
    """
    Given a base search page in HTML, this fetches (when `fetch` is invoked) required amount of pages in parallel
    and then parses the results from each page. The final results are stored in the `results` instance variable.

    Arguments:

        html (string), num_results (int), url (string)

    Returns:

        A list of results each in dictionary format.

    """
    def __init__(self, html, num_results, url, detailed):
        self.html = BeautifulSoup(html)
        self.num_results = num_results
        self.url = url
        self.detailed = detailed
        self.results = []

    def fetch(self):
        # Track time
        self.time = time()

        items = self.html.select('.listing-item')

        if not items:
            return []

        # Find total pages
        try:
            num_pages = int(re.match(r'^\?page=(\d+)', self.html.select('.paging_forward > #last_page')[0]['href']).group(1))
        except IndexError:
            num_pages = 1

        # Make sure num_results is less than total results
        total_results = len(items) * num_pages

        if self.num_results > total_results or self.num_results == 'all':
            self.num_results = total_results

        # Collect enough page urls to satisfy num_results
        needed_pages = int(math.ceil(self.num_results / float(len(items))))
        page_urls = [self.url]
        search_base = re.match(r'^(.+)\?', self.url).group(1)  # Use base provided by Dubizzle's redirect

        for el in self.html.select('.pages > .page-links')[1:needed_pages+1]:
            page_urls.append(search_base + el['href'])

        # Scrape pages in parallel
        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count()*2)
        raw_results = []

        # Iterate through fetched pages and render into BS objects
        for page in pool.map(scrape, page_urls):
            soup = BeautifulSoup(page)
            raw_results += soup.select('.listing-item')

        # Parse the raw results and store into self.results; return self.results
        return self.parse(raw_results)

    def parse(self, raw_results):
        for index, result in enumerate(raw_results):
            # Stop when requested result count is exceeded
            if index+1 > self.num_results:
                return self.results

            # Skip any featured listings that cause parsing errors
            try:
                # Don't try to understand the hacks below. I don't even... just hope they don't change the design :P
                parsed_result = {
                    u'title': result.select('.title')[0].text.strip(),
                    u'date': parse_date(result.select('.date')[0].text.strip()),
                    u'url': re.match(r'^(.+)\?back', result.select('.title > a')[0]['href']).group(1),
                    u'location': ' '.join(result.select('.location')[0].text.replace('\n', '').replace(u'\u202a', '')
                                    .split()).replace('Located : ', '').split(' > ')
                }

                # Get price
                try:
                    parsed_result[u'price'] = int(result.select('.price')[0].text.strip().split(' ')[1].replace(',', ''))
                except IndexError:
                    parsed_result[u'price'] = 0

                # Get the category
                try:
                    parsed_result[u'category'] = result.select('.description .breadcrumbs')[0].text.replace(u'\u202a', '') \
                                                       .lstrip().split('  >  ')
                except IndexError:
                    parsed_result[u'category'] = result.select('.descriptionindented .breadcrumbs')[0].text\
                                                      .replace(u'\u202a', '').lstrip().split('  >  ')

                # Get the image, if available
                image = result.select('.has_photo > .thumb > a > div')

                if result.select('.has_photo > .thumb > a > div'):
                    parsed_result[u'image'] = re.findall(r'\((.+)\)', image[0]['style'])[0]
                else:
                    parsed_result[u'image'] = ''

                # Get the features
                features = {}

                for feature in result.select('.features'):
                    data = feature.select('li')

                    if data:
                        for each in data:
                            pair = each.text.split(': ')
                            feature_name, feature_value = pair[0].lower(), pair[1].lower()

                            if feature_name in ['kilometers', 'year']:
                                if feature_value == 'none':
                                    feature_value = 0

                                feature_value = int(feature_value)
                            elif feature_name == 'doors':
                                feature_value = int(feature_value.split(' ')[0].rstrip('+'))

                            features[feature_name] = feature_value

                parsed_result[u'features'] = features

                # Add dict to results list
                self.results.append(parsed_result)
            except:
                continue

        return self.results

class Listing(object):
    """Represents a single Dubizzle UAE listing."""
    def __init__(self, url):
        self.url = url

    def fetch(self):
        # Listing dict
        listing = {}

        # Track time
        start = time()

        # Get listing html
        resp = dubizzle_request(self.url, headers)
        soup = BeautifulSoup(resp.text)

        # URL
        listing[u'url'] = self.url

        # Title
        listing[u'title'] = soup.select('.title')[0].text.strip()

        # Photos, if found
        photos = []

        if soup.select('#photo-count'):
            # Find photo count
            num_photos = int(soup.select('#photo-count')[0].text.strip().split(' Photo')[0])

            # Iterate through photo thumbs
            for i in range(1, num_photos+1):
                photo = soup.select('#thumb%d > a' % i)[0]
                photos.append(photo['href'])

        listing[u'photos'] = photos

        # Location; too experimental to explain
        raw_location = soup.select('.location')[0].text.replace('\n', '').replace('\t', '') \
                           .replace(u'\u202a', '').replace(u'\xa0', '').strip().split(';')

        location = [each.strip() for each in raw_location[0].split(' > ')]
        near_to = [raw_location[1].strip()] if raw_location[1] else []

        listing[u'location'] = location + near_to

        # Google Maps URL
        map_js = soup.select('.map-wrapper > script')[0].text
        coordinates = re.findall(r'\.setCenter\((\S+)\);', map_js)[0]

        listing[u'map'] = u'http://maps.google.com/?q=%s' % coordinates

        # Phone number
        listing[u'phone'] = soup.select('.phone-content')[0].text.strip().replace(u'\u202a', '')

        # Post date
        raw_date = soup.select('.listing-details-header > span')[0].text.split(': ')[1]
        listing[u'date'] = parse_date(raw_date)

        # Description
        listing[u'description'] = soup.select('.trans_toggle_box')[0].text.strip()

        # Details
        raw_details = soup.select('#listing-details-list li')
        parsed_details = {}

        for detail in raw_details:
            detail_text = detail.text.replace('\n', '').replace(u'\xa0', '').strip()

            # For multi-part information
            if ',' in detail_text:
                split_detail = detail_text.split(':')
                title, info = split_detail[0].lower(), [each.strip().lower() for each in split_detail[1].split(', ')]
            else:
                title, info = [each.strip().lower() for each in detail_text.split(':')]

            # Try to convert to integer
            try:
                info = int(info)
            except:
                pass

            # Store each detail
            parsed_details[title] = info

        listing[u'details'] = parsed_details

        listing[u'time'] = time() - start

        return listing
