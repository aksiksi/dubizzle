from .regionmapper import mapper


def search(**kwargs):
    """Simpler way to run a search on implemented Dubizzle sites. Please check respective site for parameters."""
    # Retrieve classes needed; defaults to UAE
    Search, Results = mapper[kwargs.get('country', 'uae')].values()

    # Run search
    s = Search(**kwargs)
    raw = s.search()

    # Fetch results
    results = raw.fetch()

    return results


def listing(country, url):
    """Retrieve a single listing via URL."""
    pass