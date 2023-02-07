"""
https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python
"""
import unittest
from functools import reduce


def range_extraction(args) -> str:
    if isinstance(args, int):
        return str(args)

    result = ''
    d = map(lambda x: '-', filter(lambda x, y: abs(x) - abs(y) == 0, reduce(lambda x, y: abs(abs(x) - abs(y)), args)))
    for i in range(len(args)):
        try:
            if abs(args[i] - args[i+1]) == 1 and abs(args[i+1] - args[i+2]) == 1:
                result += f"{args[i]}-"
            else:
                result += f"{args[i]},"
        except IndexError:
            return result

    return result


"""
best solutions:


"""


class RangeExtraction(unittest.TestCase):
    def test_range_extraction(self):
        # self.assertEqual('1', range_extraction(1))
        self.assertEqual('1,5,7', range_extraction([1, 5, 7]))
        self.assertEqual('-1-1', range_extraction([-1, 0, 1]))
        self.assertEqual('1,3-5,7', range_extraction([1, 3, 4, 5, 7]))
        self.assertEqual('-6,-3-1,3-5,7-11,14,15,17-20',
                         range_extraction([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
        self.assertEqual('-3--1,2,10,15,16,18-20', range_extraction([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]))
