from .regionmapper import mapper


def search(country, **kwargs):
    """Simpler way to run a search on implemented Dubizzle sites. Please check respective site for parameters."""
    # Retrieve classes needed
    Search, Results = mapper[country].values()

    # Run search
    s = Search(**kwargs)
    raw = s.search()

    # Fetch results
    results = raw.fetch()

    return results


def listing(country, url):
    """Retrieve a single listing via URL."""
    pass