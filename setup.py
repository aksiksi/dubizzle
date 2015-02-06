from distutils.core import setup

# Load up README
with open('README.txt') as f:
	long_description = f.read()

setup(
	name='dubizzle',
	author='Assil Taoufik Ksiksi',
	author_email='cyph0nik@gmail.com',
	url='https://github.com/Cyph0n/dubizzle/',
	keywords=['dubizzle', 'scraping', 'API', 'search', 'classifieds'],
	version='0.1',
	description='A scraping-based API for Dubizzle.',
	long_description=long_description,
	packages=['dubizzle'],
	install_requires=['requests', 'beautifulsoup4'],
	classifiers=[
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
	],
)

