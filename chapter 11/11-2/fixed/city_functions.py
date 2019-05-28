"""Functions that work with data regarding cities"""

def city_country(city, country, population=0):
    """Format a string as such: City, Country - Population: xxxxx"""
    if population:
        return f"{city.title()}, {country.title()} - Population: {population}."
    else:
        return f"{city.title()}, {country.title()}."
