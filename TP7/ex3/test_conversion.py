import unittest
import os
import sys

# Add the root directory (TP7) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ex1.conversion import dollars_to_dirhams, meters_to_kilometers

class TestConversion(unittest.TestCase):

    def test_dollars_to_dirhams(self):
        self.assertAlmostEqual(dollars_to_dirhams(1), 10.05)
        self.assertAlmostEqual(dollars_to_dirhams(0), 0)
        self.assertAlmostEqual(dollars_to_dirhams(100), 1005)
        
    def test_meters_to_kilometers(self):
        self.assertAlmostEqual(meters_to_kilometers(1000), 1)
        self.assertAlmostEqual(meters_to_kilometers(0), 0)
        self.assertAlmostEqual(meters_to_kilometers(500), 0.5)
        

if __name__ == '__main__':
    unittest.main()