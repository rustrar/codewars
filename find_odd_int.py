"""
https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
"""
import unittest
from collections import Counter


def find_it(seq):
    return next(k for k, v in Counter(seq).items() if v % 2)


"""
best solutions:

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
            
            
def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]
"""


class FindOddInt(unittest.TestCase):
    def test_make_readable(self):
        self.assertEqual(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)
        self.assertEqual(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]), -1)
        self.assertEqual(find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]), 5)
        self.assertEqual(find_it([10]), 10)
        self.assertEqual(find_it([10, 10, 10]), 10)
        self.assertEqual(find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]), 10)
        self.assertEqual(find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]), 1)
