import unittest
from city_function import get_city_country

class CityCountryTest(unittest.TestCase):
    """Test for city_function.py """

    def test_city_country(self):
        formatted_city = get_city_country('corvallis', 'united states')
        self.assertEqual(formatted_city, 'Corvallis, United States')

    def test_city_country_population(self):
        formatted_city = get_city_country('corvallis', 'united states', 50000)
        self.assertEqual(formatted_city, 'Corvallis, United States - Population 50000')

if __name__ == '__main__':
    unittest.main()