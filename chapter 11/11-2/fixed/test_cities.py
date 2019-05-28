import unittest

from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile.')

    def test_city_country_pop(self):
        santiago_chile_pop = city_country('santiago', 'chile', 500000)
        self.assertEqual(santiago_chile_pop, 'Santiago, Chile - '
                        'Population: 500000.')    

unittest.main()
