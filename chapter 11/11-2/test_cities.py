import unittest

from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile_pop, 'Santiago, Chile.')

unittest.main()
