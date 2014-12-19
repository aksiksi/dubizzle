# Contains region-specific attributes for Dubizzle sites
uae = {
    'base_url': 'http://uae.dubizzle.com/search',
    'cities': {
        'code': 'site',
        'options': {
            'all': '--',
            'dubai': '2',
            'abudhabi': '3',
            'ajman': '14',
            'alain': '39',
            'fujairah': '13',
            'rasalkhaimah': '11',
            'sharjah': '12',
            'ummalquwain': '15',
        },
    },

    'sections': {
        'code': 's',
        'options': {
            'all': '--',
            'motors': 'MT',
            'classifieds': 'CL',
            'propertyforsale': 'SP',
            'propertyforrent': 'RP',
            'jobs': 'JB',
            'jobseekers': 'JW',
            'community': 'CO',
        },
    },

    'categories': {
        'code': 'rc',
        'options': {
            'all': '--',

            # Motors
            'cars': '140',
            'parts': '141',
            'boats': '229',
            'motorcycles': '890',

            # Classifieds
            'baby': '182',
            'books': '250',
            'cameras': '299',
            'clothing': '360',
            'business': '1194',
            'collectibles': '426',
            'computers': '467',
            'movies': '520',
            'electronics': '570',
            'free': '645',
            'furniture': '665',
            'gaming': '723',
            'home': '766',
            'jewelry': '804',
            'lost': '836',
            'misc': '851',
            'mobiles': '852',
            'music': '900',
            'instruments': '971',
            'pets': '1016',
            'sports': '1045',
            'stuff-wanted': '1111',
            'tickets': '1135',
            'toys': '1143',

            # Property for Sale
            'res-sale': '1742',
            'com-sale': '32',
            'mul-sale': '33',
            'land-sale': '34',

            # Property for Rent
            'res-rent': '1743',
            'com-rent': '25',
            'room-rent': '26',
            'room-wanted': '27',
            'short-monthly': '28',
            'short-daily': '1930',
            'rent-wanted': '29',

            # TODO: Add more
        },
    },

    # For Motors only
    'makes': {
        'code': 'c1',
        'options': {
            'all': '--',

            'acura': '1167',
            'alfa romeo': '1173',
            'aston martin': '1180',
            'audi': '1185',
            'bentley': '1196',
            'bizzarrini': '1200',
            'bmw': '1202',
            'bufori': '1220',
            'bugatti': '1222',
            'buick': '1224',
            'cadillac': '1226',
            'chevrolet': '1235',
            'chrysler': '1255',
            'citroen': '1826',
            'cmc': '1802',
            'daewoo': '1264',
            'daihatsu': '1268',
            'delorean': '1274',
            'dodge': '1276',
            'ferrari': '1287',
            'fiat': '1289',
            'ford': '1294',
            'gac gonow': '2022',
            'gmc': '1315',
            'honda': '1324',
            'hummer': '1337',
            'hyundai': '1341',
            'infiniti': '1354',
            'isuzu': '1363',
            'jac': '2023',
            'jaguar': '1373',
            'jeep': '1386',
            'jinbei': '2021',
            'jmc': '2020',
            'kia': '1393',
            'lada': '1834',
            'lamborghini': '1403',
            'lancia': '1627',
            'land rover': '1408',
            'lexus': '1415',
            'lincoln': '1424',
            'lotus': '1430',
            'maserati': '1434',
            'maybach': '1439',
            'mazda': '1442',
            'mclaren': '1456',
            'mercedes-benz': '1459',
            'mercury': '1633',
            'mini': '1479',
            'mitsubishi': '1481',
            'nissan': '1495',
            'opel': '1513',
            'oullim': '1840',
            'peugeot': '1520',
            'pontiac': '1870',
            'porsche': '1530',
            'proton': '1825',
            'renault': '1537',
            'rolls royce': '1541',
            'rover': '1544',
            'saab': '1546',
            'seat': '1553',
            'shenlong/sunlong': '2024',
            'skoda': '1560',
            'smart': '1564',
            'speranza': '1836',
            'ssang yong': '1566',
            'subaru': '1568',
            'suzuki': '1575',
            'tata': '1580',
            'toyota': '1584',
            'volkswagen': '1604',
            'volvo': '1615',
            'wiesmann': '1939',
            'other': '1621'
        },
    },

    'motors_options': {
        'transmission': {
            'all': '',
            'manual': '378',
            'automatic': '377'
        },

        'cylinders': {
            'all': '',
            3: '365',
            4: '366',
            5: '367',
            6: '368',
            8: '369',
            10: '371',
            12: '746'
        },

        'seller': {
            'all': '',
            'owner': 'OW',
            'dealer': 'DL'
        },

        'fuel': {
            'all': '',
            'gasoline': '380',
            'diesel': '381',
            'hybrid': '382',
            'electric': '383'
        }
    },
}
