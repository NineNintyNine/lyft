import unittest

from tire.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        sensor_array = [0.8, 0.8, 0.8, 0.7]
        tires = OctoprimeTires(sensor_array)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        sensor_array = [0.1, 0.2, 0.4, 0.2]
        tires = OctoprimeTires(sensor_array)
        self.assertFalse(tires.needs_service())