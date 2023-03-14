"""
https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python
"""
import operator
import unittest
from functools import reduce


def persistence(n):
    lst = [int(s) for s in str(n)]
    cnt = 0
    while len(lst) > 1:
        lst = [int(s) for s in str(reduce(lambda x, y: x*y, lst))]
        cnt += 1
    return cnt


class PersistentBugger(unittest.TestCase):
    def test_persistence(self):
        self.assertEqual(3, persistence(39))
        self.assertEqual(0, persistence(4))
        self.assertEqual(2, persistence(25))
        self.assertEqual(4, persistence(999))


# Best solution
# def persistence1(n):
#     i = 0
#     while n >= 10:
#         n = reduce(operator.mul, [int(x) for x in str(n)], 1)
#         i += 1
#     return i
