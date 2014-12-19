# Maps sites to their respective classes
from . import uae

mapper = {
    'uae': {
        'search': uae.Search,
        'results': uae.Results,
        'listing': uae.Listing,
    }
}
