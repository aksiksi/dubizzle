Introduction
============

`Dubizzle <http://www.dubizzle.com/>`_ is an online classifieds website. This project aims to become a simple and complete scraping-based API for Dubizzle.

Repo
----

https://github.com/Cyph0n/dubizzle

Prerequisites
=============

* `Requests <http://docs.python-requests.org/en/latest/index.html>`_
* `BeautifulSoup 4 <http://www.crummy.com/software/BeautifulSoup/>`_
* Python 2.6+

Quickstart
==========

::

  >> import dubizzle
  >> results = dubizzle.search(country='uae', city='dubai', section='motors', num_results=100)
  >> print results
  >>
  [
    {
      'url': 'test',
      'image': 'http://...',
      'price': 10000,
      'date': datetime.datetime(2013, 07, 20, 0, 0, 0),
      'features': {
        'Color': 'black',
        'Doors': 4,
        'Kilometers': 35000
      },
      ...
    },
    ...
  ]

Examples
========

::

  # Find average price of year 2007 and above Nissan Altimas in Dubai
  import dubizzle

  results = dubizzle.search(keyword='altima', country='uae', city='dubai', section='motors',
                category='cars', make='nissan', min_year=2007, num_results='all')

  total_price, result_count = 0, len(results)

  for result in results:
    total_price += result['price']

  print float(total_price) / result_count # Prints 39239.94

::

  # Use the above results to find distribution of post-2007 Altima colors
  from collections import Counter

  colors = [result['features']['color'] for result in results]
  distribution = Counter(colors)

  print distribution['white'] # Prints 52

::

  # Retrieve a single listing from Dubizzle UAE
  import dubizzle

  listing = dubizzle.listing('http://dubai.dubizzle.com/motors/used-cars/nissan/tiida/2013/9/25/easy-installment-new-and-used-cars-0563276-2/', country='uae')

  print listing

Search Parameters
=================

General
-------

* `country` - string; defaults to 'uae'
* `keyword` - string
* `city` - string
* `section` - string
* `min_price` and `max_price` - integers
* `category` - string
* `added_days` - choices are 0, 3, 7, 14, 30, 90, or 180
* `num_results` - integer; 'all' fetches all results available
* `detailed` (not implemented) - if set to `True`, fetches full listing data for each result; slower, obviously

Motors
------

* `make` - a long list can be found in `regions.py`
* `min_year` and `max_year` - integers
* `min_kms` and `max_kms` - integers
* `seller` - 'dealer' or 'owner'
* `fuel` - 'gasoline', 'hybrid', 'diesel', or 'electric'
* `cylinders` - 3, 4, 5, 6, 8, 10, or 12
* `transmission` - 'automatic' or 'manual'

Listing Parameters
------------------

* `url` - string, **required**
* `country` - string; defaults to 'uae'

Issues
------

Please use the `Issues <https://github.com/Cyph0n/dubizzle/issues>`_ page for that.
