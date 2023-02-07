"""
https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
"""

import unittest
from collections import Counter


def move_zeros(lst):
    zeros = [0 for _ in range(Counter(lst)[0])]
    lst = [x for x in lst if x != 0]
    lst.extend(zeros)
    return lst


"""
best solution:
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
"""


class MovingZerosToTheEnd(unittest.TestCase):
    def test_move_zeros(self):
        self.assertEqual([1, 2, 1, 1, 3, 1, 0, 0, 0, 0],
                         move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
        self.assertEqual([9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
        self.assertEqual([0, 0], move_zeros([0, 0]))
        self.assertEqual([0], move_zeros([0]))
        self.assertEqual([], move_zeros([]))
