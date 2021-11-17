import unittest
from Offline import Offline
from ReadJson import ReadJson


class testOffline(unittest.TestCase):

    def test_offline(self):
        try:
            json_object = ReadJson("B2.json")
            building = json_object.building
            algo = Offline(building, "Calls_a.csv", "out.csv")
        except:
            self.assertEqual(1, 0)  # if it is not succeed

    def test_read_json(self):
        json_object = ReadJson("B2.json")
        self.assertNotEqual(json_object.building, None)
