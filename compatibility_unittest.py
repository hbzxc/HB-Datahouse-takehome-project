import unittest
import json
from Compatibility_predictor import is_valid_data, get_lowest_avg, get_result

# sample JSON data for testing
sample_data_json = '''
{
    "team": [
        {
            "name": "Monk",
            "attributes": {
                "intelligence": 5,
                "strength": 4,
                "endurance": 5,
                "spicyFoodTolerance" : 1
            }
        }
    ],
    "applicants": [
        {
            "name": "Jommy",
            "attributes": {
                "intelligence": 1,
                "strength": 1,
                "endurance": 1,
                "spicyFoodTolerance" : 10
            }
        },
        {
            "name": "Jokey",
            "attributes": {
                "intelligence": 9,
                "strength": 9,
                "endurance": 9,
                "spicyFoodTolerance" : 1
            }
        }
    ]
}
'''

class Compatibility_test(unittest.TestCase):

    def setUp(self):
        # Load the sample data into a dictionary
        self.sample_data = json.loads(sample_data_json)

    def test_is_valid_data(self):
        self.assertTrue(is_valid_data(self.sample_data))

        # Test with invalid data
        invalid_data = {"invalid_key": "value"}
        self.assertFalse(is_valid_data(invalid_data))

    def test_get_lowest_avg(self):
        # Test the get_lowest_avg function with the sample data
        lowest_single = {
            "intelligence": 5,
            "strength": 4,
            "endurance": 5,
            "spicyFoodTolerance": 1
        }
        lowest_attributes = get_lowest_avg(lowest_single)
        self.assertEqual(lowest_attributes, ["spicyFoodTolerance"])

        lowest_double = {
            "intelligence": 1,
            "strength": 4,
            "endurance": 5,
            "spicyFoodTolerance": 1
        }
        lowest_attributes = get_lowest_avg(lowest_double)
        self.assertEqual(lowest_attributes, ["intelligence","spicyFoodTolerance"])

    def test_get_result(self):
        # Test the get_result function
        result_test_1 = {
            "name": "Jokey",
            "attributes": {
                "intelligence": 9,
                "strength": 9,
                "endurance": 9,
                "spicyFoodTolerance" : 1
            }
        }
        # Test 1 desired attribute || 9/10 = 0.9
        lowest_attributes = ['strength']
        result = get_result(result_test_1, lowest_attributes)
        self.assertEqual(result, 0.9)

        # Test 2 desired attributes || 9+1 = 10 // 10/20 = 0.5
        lowest_attributes = ['strength', 'spicyFoodTolerance']
        result = get_result(result_test_1, lowest_attributes)
        self.assertEqual(result, 0.5)


if __name__ == '__main__':
    unittest.main()
