"""Functions that work with data regarding cities"""

def city_country(city, country, population):
    """Format a string as such: City, Country - Population: xxxxx"""
    return f"{city.title()}, {country.title()} - Population: {population}."
