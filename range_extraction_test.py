"""
https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python
"""
import unittest
from itertools import groupby


def group_consecutives(lst):
    for _, g in groupby(enumerate(lst), lambda i_x: i_x[0] - i_x[1]):
        r = [x for _, x in g]
        if len(r) > 2:
            yield f"{r[0]}-{r[-1]}"
        else:
            yield from map(str, r)


def range_extraction(args) -> str:
    return ','.join(group_consecutives(args))


"""
best solutions:

def solution(arr):
    ranges = []
    a = b = arr[0]
    for n in arr[1:] + [None]:
        if n != b+1:
            ranges.append(str(a) if a == b else "{}{}{}".format(a, "," if a+1 == b else "-", b))
            a = n
        b = n
    return ",".join(ranges)
"""


class RangeExtraction(unittest.TestCase):
    def test_range_extraction(self):
        # self.assertEqual('1', range_extraction(1))
        self.assertEqual('1,5,7', range_extraction([1, 5, 7]))
        self.assertEqual('-1-1', range_extraction([-1, 0, 1]))
        self.assertEqual('1,3-5,7', range_extraction([1, 3, 4, 5, 7]))
        self.assertEqual('-6,-3-1,3-5,7-11,14,15,17-20',
                         range_extraction([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
        self.assertEqual('-3--1,2,10,15,16,18-20',
                         range_extraction([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]))
