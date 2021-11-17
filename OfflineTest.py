import unittest
import Offline
import ReadJson
from unittest import TestCase


class OfflineTest(unittest.TestCase):

    # def test_allocate(self):
    #     var = Offline.allo

    def test_read_json(self):
        json_file = "B2.json"
        json_object = ReadJson(json_file)
        building = json_object.building
        self.assertEquals(1,1)

    if __name__ == '__main__':
        unittest.main()
