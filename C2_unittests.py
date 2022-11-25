import math
import unittest
from C2_functions import *


class MyTestCase(unittest.TestCase):
    def test_find_one(self):
        self.assertEqual(find_one_naiive(1), find_one_complete(1))  # add assertion here
        self.assertEqual(find_one_naiive(5), find_one_complete(5))  # add assertion here
        self.assertEqual(find_one_naiive(10), find_one_complete(10))  # add assertion here
        self.assertEqual(find_one_naiive(20), find_one_complete(20))  # add assertion here
        self.assertEqual(find_one_naiive(100), find_one_complete(100))  # add assertion here
        self.assertEqual(find_one_naiive(152), find_one_complete(152))  # add assertion here
        self.assertEqual(find_one_naiive(184), find_one_complete(184))  # add assertion here
        self.assertEqual(find_one_naiive(199), find_one_complete(199))  # add assertion here
        self.assertEqual(find_one_naiive(280), find_one_complete(280))  # add assertion here
        self.assertEqual(find_one_naiive(1000), find_one_complete(1000))  # add assertion here
        self.assertEqual(find_one_naiive(1152), find_one_complete(1152))  # add assertion here
        self.assertEqual(find_one_naiive(1280), find_one_complete(1280))  # add assertion here
        self.assertEqual(find_one_naiive(2000), find_one_complete(2000))  # add assertion here
        self.assertEqual(find_one_naiive(2152), find_one_complete(2152))  # add assertion here
        # self.assertEqual(90051450678399649, find_one(int(math.pow(3,35))))  # add assertion here


if __name__ == '__main__':
    unittest.main()
