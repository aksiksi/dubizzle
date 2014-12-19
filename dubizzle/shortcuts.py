from .regionmapper import mapper

def search(country='uae', **kwargs):
    """Simpler way to run a search on implemented Dubizzle sites. Please check respective site for parameters."""
    # Retrieve classes needed; defaults to UAE
    Search, Results = mapper[country]['search'], mapper[country]['results']

    # Run search
    s = Search(**kwargs)
    raw = s.search()

    # Fetch results
    results = raw.fetch()

    return results

def listing(url, country='uae'):
    """Retrieves a single Dubizzle UAE listing via URL."""
    Listing = mapper[country]['listing']

    # Create and fetch listing
    l = Listing(url)
    result = l.fetch()

    return result
