import math
import unittest
from C2_functions import *


class MyTestCase(unittest.TestCase):
    def test_find_one(self):
        self.assertEqual(1, find_one(1))  # add assertion here
        self.assertEqual(1, find_one(5))  # add assertion here
        self.assertEqual(2, find_one(10))  # add assertion here
        self.assertEqual(12, find_one(20))  # add assertion here
        self.assertEqual(689, find_one(1234))  # add assertion here
        self.assertEqual(2557, find_one(5123))  # add assertion here
        self.assertEqual(38000, find_one(70000))  # add assertion here
        self.assertEqual(93395, find_one(123321))  # add assertion here
        self.assertEqual(90051450678399649, find_one(int(math.pow(3,35))))  # add assertion here


if __name__ == '__main__':
    unittest.main()
