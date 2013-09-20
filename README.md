# Introduction

[Dubizzle](http://www.dubizzle.com/) is an online classifieds website. This project aims to 
become a simple and complete scraping-based API for Dubizzle.

# Notice

This is still a work in progress. There is much left to do until this becomes what it should be. I will however make sure that the `master` branch functions as expected. Any help would be greatly appreciated, obviously.

Another thing to point out is that the main focus for the time being is on Motors search within Dubizzle.

# Prerequisites

* [Requests](http://docs.python-requests.org/en/latest/index.html)
* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)
* Python 2.6+

# Quickstart

```python
>> import dubizzle
>> results = dubizzle.search(country='uae', city='dubai', section='motors', num_results=100)
>> print results
>>
[
	{
		'url': 'test',
		'image': 'http://...',
		'price': 10000,
		'date': datetime.datetime(2013, 07, 20, 0, 0, 0)
		'features': {
			'Color': 'black',
			'Doors': 4,
			'Kilometers': 35000
		}
	},
	...
]
```

# Search Parameters

## General

* `country` - **required**
* `keyword`
* `city`
* `section`
* `min_price` and `max_price`
* `category`
* `added_days` - choices are 0, 3, 7, 14, 30, 90, or 180

## Motors

* `make` - a long list can be found in `regions.py`
* `min_year` and `max_year`
* `min_kms` and `max_kms`
* `seller` - dealer or owner
* `fuel` - gasoline, hybrid, diesel, or electric
* `cylinders` - 3, 4, 5, 6, 8, 10, or 12
* `transmission` - automatic or manual

# Issues

Please use the [Issues](https://github.com/Cyph0n/dubizzle/issues) page for that.
